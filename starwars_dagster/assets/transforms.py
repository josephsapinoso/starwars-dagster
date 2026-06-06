"""
Layer 2 & 3: Storage + Transform Assets
========================================
These assets load raw JSON into DuckDB and run SQL transformations.

Key Dagster concept — asset dependencies:
  By listing `raw_films`, `raw_people`, etc. as function parameters,
  Dagster knows to run ingestion first and pass the results here automatically.

Why DuckDB?
  - Embedded (no server to install or run)
  - Speaks SQL natively on JSON, CSV, and Parquet
  - Blazing fast for analytical queries on laptop-scale data
  - Perfect for learning and local development

Asset lineage here:
  raw_films ──┐
  raw_people ─┤
  raw_planets ┼──► star_wars_db ──► characters_enriched
  raw_ships ──┤                 ──► film_character_counts
  raw_species ┘                 ──► starship_pilot_stats
"""

import json
import pathlib
import duckdb
import pandas as pd
from dagster import asset, AssetExecutionContext

_GROUP = "02_transformed"
DB_PATH = pathlib.Path("data/star_wars.duckdb")


def _extract_id_from_url(url: str) -> int | None:
    """SWAPI URLs end with /id/ — extract the integer ID."""
    try:
        return int(url.rstrip("/").rsplit("/", 1)[-1])
    except (ValueError, AttributeError):
        return None


# ── Load raw JSON into DuckDB ────────────────────────────────────────────────

@asset(
    group_name=_GROUP,
    description="Loads all raw SWAPI data into a local DuckDB database",
)
def star_wars_db(
    context: AssetExecutionContext,
    raw_films: list[dict],
    raw_people: list[dict],
    raw_planets: list[dict],
    raw_starships: list[dict],
    raw_species: list[dict],
) -> str:
    """
    Takes the five raw ingestion assets and loads them into DuckDB tables.

    Returns the database file path as a string so downstream assets can connect.
    """
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(DB_PATH))

    # Helper: flatten a list of dicts into a DuckDB table
    # We convert list-valued fields (like film.characters) to JSON strings
    # so they fit cleanly into a relational table.
    def load_table(name: str, records: list[dict]) -> int:
        if not records:
            return 0
        # Stringify any fields that are lists or dicts
        cleaned = []
        for row in records:
            cleaned.append(
                {k: (json.dumps(v) if isinstance(v, (list, dict)) else v) for k, v in row.items()}
            )
        df = pd.DataFrame(cleaned)
        con.execute(f"DROP TABLE IF EXISTS {name}")
        con.execute(f"CREATE TABLE {name} AS SELECT * FROM df")
        return len(df)

    counts = {
        "films": load_table("films", raw_films),
        "people": load_table("people", raw_people),
        "planets": load_table("planets", raw_planets),
        "starships": load_table("starships", raw_starships),
        "species": load_table("species", raw_species),
    }

    context.add_output_metadata({"table_row_counts": counts, "db_path": str(DB_PATH)})
    con.close()
    return str(DB_PATH)


# ── Transform: Characters with their homeworld ───────────────────────────────

@asset(
    group_name=_GROUP,
    description="Characters joined with their homeworld planet name and climate",
)
def characters_enriched(context: AssetExecutionContext, star_wars_db: str) -> pd.DataFrame:
    """
    Join people → planets on homeworld URL to add planet name + climate.

    This is the kind of enrichment you'd do in a real data warehouse:
    resolve foreign keys (URLs here) into human-readable attributes.
    """
    con = duckdb.connect(star_wars_db)

    df = con.execute("""
        SELECT
            p.name                              AS character_name,
            p.gender,
            p.birth_year,
            p.height,
            p.mass,
            p.eye_color,
            p.hair_color,
            pl.name                             AS homeworld,
            pl.climate                          AS homeworld_climate,
            pl.terrain                          AS homeworld_terrain,
            pl.population                       AS homeworld_population
        FROM people p
        LEFT JOIN planets pl
            ON p.homeworld = pl.url
        ORDER BY p.name
    """).df()

    con.close()

    df.to_csv("data/output/characters_enriched.csv", index=False)
    context.add_output_metadata({"row_count": len(df), "columns": list(df.columns)})
    return df


# ── Transform: Characters per film ───────────────────────────────────────────

@asset(
    group_name=_GROUP,
    description="Number of named characters appearing in each film, sorted by episode",
)
def film_character_counts(context: AssetExecutionContext, star_wars_db: str) -> pd.DataFrame:
    """
    Count characters per film.

    SWAPI stores characters as a JSON array of URLs inside films.characters.
    We use DuckDB's json_array_length() to count them without unnesting.
    """
    con = duckdb.connect(star_wars_db)

    df = con.execute("""
        SELECT
            episode_id,
            title,
            director,
            release_date,
            json_array_length(characters)  AS character_count,
            json_array_length(planets)     AS planet_count,
            json_array_length(starships)   AS starship_count
        FROM films
        ORDER BY CAST(episode_id AS INTEGER)
    """).df()

    con.close()

    df.to_csv("data/output/film_character_counts.csv", index=False)
    context.add_output_metadata({"films": df[["title", "character_count"]].to_dict("records")})
    return df


# ── Transform: Starship stats ─────────────────────────────────────────────────

@asset(
    group_name=_GROUP,
    description="Starship performance stats — hyperdrive rating, crew, passengers",
)
def starship_stats(context: AssetExecutionContext, star_wars_db: str) -> pd.DataFrame:
    """
    Clean and type-cast starship fields for analysis.

    Raw SWAPI data has numeric fields as strings (e.g. "1.0", "unknown").
    We use TRY_CAST to convert, treating 'unknown' as NULL.
    """
    con = duckdb.connect(star_wars_db)

    df = con.execute("""
        SELECT
            name,
            model,
            starship_class,
            manufacturer,
            TRY_CAST(hyperdrive_rating AS DOUBLE)  AS hyperdrive_rating,
            TRY_CAST(max_atmosphering_speed AS INTEGER) AS max_speed,
            TRY_CAST(crew AS INTEGER)              AS crew_size,
            TRY_CAST(passengers AS INTEGER)        AS passenger_capacity,
            TRY_CAST(length AS DOUBLE)             AS length_m,
            json_array_length(pilots)              AS known_pilots
        FROM starships
        ORDER BY hyperdrive_rating NULLS LAST
    """).df()

    con.close()

    df.to_csv("data/output/starship_stats.csv", index=False)
    context.add_output_metadata(
        {
            "total_starships": len(df),
            "best_hyperdrive": df.dropna(subset=["hyperdrive_rating"])
            .nsmallest(1, "hyperdrive_rating")[["name", "hyperdrive_rating"]]
            .to_dict("records"),
        }
    )
    return df
