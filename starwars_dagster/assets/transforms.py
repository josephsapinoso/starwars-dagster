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
  raw_species ┘                 ──► starship_stats
                                ──► character_stats
  raw_character_profiles ─┐
  star_wars_db ───────────┴──► character_biographies
"""

import json
import pathlib
import duckdb
import pandas as pd
from dagster import asset, AssetExecutionContext

from starwars_dagster.known_facts import PROFILE_NAME_ALIASES

_GROUP = "02_transformed"

# Warehouse access is hand-managed with raw `duckdb.connect(...)` ON PURPOSE — not via
# dagster-duckdb's DuckDBResource. The framework resource can't express this pipeline's
# per-asset safety contract: DuckDBResource.get_connection() hardcodes read_only=False,
# so pure-read transforms could not open read_only and DuckDB's single-writer file lock
# would go unenforced. Raw connect() lets each asset declare read_only itself — a lock
# DuckDB enforces, source-tested in tests/test_pipeline.py. Full rationale + the tradeoff
# both ways live in WORKSHOP.md Module 10 ("Why NOT dagster-duckdb's DuckDBResource?").
DB_PATH = pathlib.Path("data/star_wars.duckdb")
OUTPUT_DIR = pathlib.Path("data/output")


def _write_csv(df: pd.DataFrame, name: str) -> None:
    """Write a transform output CSV, creating data/output/ if needed."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_DIR / name, index=False)


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

    # Persist the enriched grain back into the warehouse so downstream SQL can
    # query it — including the dashboard's displayed strings, which pytest
    # executes against this table (tests/test_site_sql.py).
    con.execute("CREATE OR REPLACE TABLE characters_enriched AS SELECT * FROM df")

    con.close()

    _write_csv(df, "characters_enriched.csv")
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
    # read_only: DuckDB allows many readers OR one writer per file, so every
    # pure-read transform must say which it is (tests/test_pipeline.py pins this)
    con = duckdb.connect(star_wars_db, read_only=True)

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

    _write_csv(df, "film_character_counts.csv")
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
    con = duckdb.connect(star_wars_db, read_only=True)

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

    _write_csv(df, "starship_stats.csv")
    context.add_output_metadata(
        {
            "total_starships": len(df),
            "best_hyperdrive": df.dropna(subset=["hyperdrive_rating"])
            .nsmallest(1, "hyperdrive_rating")[["name", "hyperdrive_rating"]]
            .to_dict("records"),
        }
    )
    return df


# ── Transform: Per-character screen persistence ──────────────────────────────

@asset(
    group_name=_GROUP,
    description="Per-character grain — films appeared in and starships flown, one row per person",
)
def character_stats(context: AssetExecutionContext, star_wars_db: str) -> pd.DataFrame:
    """
    Count each character's film appearances and starships flown.

    SWAPI stores both as JSON arrays of URLs on the person record, so
    json_array_length() gives the counts without unnesting. This is the asset
    that computes the story's screen-persistence figures (one-film cameos,
    the six-film trio, the pilots) instead of leaving them page-authoring math.
    """
    con = duckdb.connect(star_wars_db)

    df = con.execute("""
        SELECT
            p.name                          AS character_name,
            json_array_length(p.films)      AS film_count,
            json_array_length(p.starships)  AS starships_flown,
            -- BBY positive, ABY negative (none in the current snapshot),
            -- 'unknown' and anything unparseable become NULL
            TRY_CAST(regexp_extract(p.birth_year, '^([0-9.]+)(BBY|ABY)$', 1) AS DOUBLE)
                * CASE WHEN p.birth_year LIKE '%ABY' THEN -1 ELSE 1 END
                                            AS birth_year_bby
        FROM people p
        ORDER BY p.name
    """).df()

    # Same write-back contract as characters_enriched: the per-character grain
    # is queryable, so the dashboard's displayed SQL (DATA.sql.ages) runs
    # against the real table (tests/test_site_sql.py executes it).
    con.execute("CREATE OR REPLACE TABLE character_stats AS SELECT * FROM df")

    con.close()

    _write_csv(df, "character_stats.csv")
    context.add_output_metadata(
        {
            "row_count": len(df),
            "one_film_characters": int((df["film_count"] == 1).sum()),
            "pilots": int((df["starships_flown"] > 0).sum()),
            "max_starships_flown": int(df["starships_flown"].max()) if len(df) else 0,
        }
    )
    return df


# ── Transform: Second-source profile enrichment ──────────────────────────────

def _normalize_name(name: str) -> str:
    """Case-fold and collapse whitespace. The ONLY tolerated variance —
    anything beyond this is a curated alias in known_facts, never fuzzy."""
    return " ".join(name.lower().split())


# The profile fields the join carries. A field missing on a record stays NULL
# (the schema is polymorphic by kind); an empty list is a present field with
# count 0 — the distinction feeds the report's field-present denominators.
_PROFILE_COLUMNS = [
    "join_key", "profile_id", "profile_name",
    "affiliations", "affiliation_count",
    "masters", "master_count",
    "apprentices", "apprentice_count",
    "died_year_aby", "died_location", "wiki",
]


@asset(
    group_name=_GROUP,
    description="Akabab character profiles joined onto the census grain by exact name",
)
def character_biographies(
    context: AssetExecutionContext,
    star_wars_db: str,
    raw_character_profiles: list[dict],
) -> pd.DataFrame:
    """
    LEFT JOIN from people onto the akabab profiles: one row per census
    character, always. The join key is the normalized name plus the curated
    alias map — misses stay visible as NULL profile columns and are counted
    by the join-coverage check, never dropped or fuzzily matched.

    Lineage strings (masters/apprentices) are stored as JSON strings with
    counts: display-only, never join keys — the source mixes prose into them.
    """

    def _list_field(rec: dict, key: str) -> tuple[str | None, float | None]:
        if key not in rec:
            return None, None
        values = rec[key]
        return json.dumps(values), float(len(values))

    rows = []
    for rec in raw_character_profiles:
        affiliations, affiliation_count = _list_field(rec, "affiliations")
        masters, master_count = _list_field(rec, "masters")
        apprentices, apprentice_count = _list_field(rec, "apprentices")
        rows.append({
            # aliases bridge the join only; character_name below stays SWAPI's
            "join_key": _normalize_name(
                PROFILE_NAME_ALIASES.get(rec["name"], rec["name"])
            ),
            "profile_id": rec["id"],
            "profile_name": rec["name"],
            "affiliations": affiliations,
            "affiliation_count": affiliation_count,
            "masters": masters,
            "master_count": master_count,
            "apprentices": apprentices,
            "apprentice_count": apprentice_count,
            # akabab years are ABY-positive — the OPPOSITE sign convention to
            # character_stats.birth_year_bby. The unit lives in the name.
            "died_year_aby": float(rec["died"]) if "died" in rec else None,
            "died_location": rec.get("diedLocation"),
            "wiki": rec.get("wiki"),
        })
    profiles = pd.DataFrame(rows, columns=_PROFILE_COLUMNS)

    con = duckdb.connect(star_wars_db)

    people = con.execute("SELECT name AS character_name FROM people ORDER BY name").df()
    people["join_key"] = people["character_name"].map(_normalize_name)

    # merge keeps duplicate profile names as extra rows on purpose: a fan-out
    # must trip the blocking grain check, not vanish inside a dict
    df = people.merge(profiles, on="join_key", how="left").drop(columns=["join_key"])

    # Write-back law: the enriched grain is queryable in the warehouse
    con.execute("CREATE OR REPLACE TABLE character_biographies AS SELECT * FROM df")

    con.close()

    _write_csv(df, "character_biographies.csv")

    matched = df[df["profile_id"].notna()]
    matched_keys = {_normalize_name(n) for n in matched["character_name"]}
    unmatched_profiles = sorted(
        rec["name"]
        for rec in raw_character_profiles
        if _normalize_name(PROFILE_NAME_ALIASES.get(rec["name"], rec["name"]))
        not in matched_keys
    )
    context.add_output_metadata(
        {
            "row_count": len(df),
            "matched": len(matched),
            "unmatched_characters": sorted(
                df.loc[df["profile_id"].isna(), "character_name"]
            )[:10],
            "unmatched_profiles": unmatched_profiles[:10],
            "deaths_on_file": int(matched["died_year_aby"].notna().sum()),
        }
    )
    return df
