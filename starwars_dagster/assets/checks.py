"""
Data Quality: Asset Checks
==========================
Key Dagster concept — Asset Checks:
  An @asset_check attaches a data-quality assertion to an asset. It runs
  when the asset materializes and its pass/fail state shows up right on the
  lineage graph in the Dagster UI.

  Severity discipline used here:
    ERROR (blocking=True) — structural breakage that would corrupt everything
      downstream: empty tables, missing keys, wrong film count. Stop the run.
    WARN — value drift: SWAPI is someone else's dataset; if they add person
      #83 tomorrow that's news, not a bug. Warn and keep going.

  Tests vs. checks: pytest guards the CODE at dev time (offline, fixtures);
  these checks guard the DATA at run time (live SWAPI pull). You need both,
  because SWAPI can change under you without a single line of code changing.
"""

import duckdb
import pandas as pd
from dagster import (
    AssetCheckResult,
    AssetCheckSeverity,
    asset_check,
)

from starwars_dagster.assets.ingestion import raw_people
from starwars_dagster.assets.transforms import (
    characters_enriched,
    film_character_counts,
    star_wars_db,
    starship_stats,
)
from starwars_dagster.known_facts import (
    EXPECTED_DB_TABLES,
    EXPECTED_EPISODE_IDS,
    EXPECTED_FILM_COUNT,
    EXPECTED_PEOPLE_COUNT,
    EXPECTED_UNKNOWN_MASS_COUNT,
    REQUIRED_PEOPLE_KEYS,
)


# ── Structural checks (ERROR, blocking) ──────────────────────────────────────

@asset_check(
    asset=raw_people,
    blocking=True,
    description="Every people record must be non-empty and carry the keys "
    "downstream transforms join and cast on (name, homeworld, films, mass, gender).",
)
def raw_people_has_required_shape(raw_people: list[dict]) -> AssetCheckResult:
    if not raw_people:
        return AssetCheckResult(passed=False, metadata={"reason": "empty response"})
    missing = [
        (rec.get("name", f"record #{i}"), sorted(REQUIRED_PEOPLE_KEYS - rec.keys()))
        for i, rec in enumerate(raw_people)
        if not REQUIRED_PEOPLE_KEYS <= rec.keys()
    ]
    return AssetCheckResult(
        passed=not missing,
        metadata={"records": len(raw_people), "records_missing_keys": missing[:10]},
    )


@asset_check(
    asset=star_wars_db,
    blocking=True,
    description="All five SWAPI tables must exist in DuckDB with at least one row — "
    "an empty table means an ingestion asset silently returned nothing.",
)
def star_wars_db_tables_populated(star_wars_db: str) -> AssetCheckResult:
    con = duckdb.connect(star_wars_db, read_only=True)
    try:
        existing = {row[0] for row in con.execute("SHOW TABLES").fetchall()}
        counts = {
            t: con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
            for t in EXPECTED_DB_TABLES & existing
        }
    finally:
        con.close()
    missing = sorted(EXPECTED_DB_TABLES - existing)
    empty = sorted(t for t, n in counts.items() if n == 0)
    return AssetCheckResult(
        passed=not missing and not empty,
        metadata={"row_counts": counts, "missing_tables": missing, "empty_tables": empty},
    )


@asset_check(
    asset=film_character_counts,
    blocking=True,
    description="The saga is episodes 1-6, exactly once each. Anything else means "
    "the films table is corrupt or SWAPI changed its dataset out from under us.",
)
def films_are_exactly_the_six_episodes(film_character_counts: pd.DataFrame) -> AssetCheckResult:
    episodes = set(film_character_counts["episode_id"].astype(int))
    return AssetCheckResult(
        passed=len(film_character_counts) == EXPECTED_FILM_COUNT
        and episodes == EXPECTED_EPISODE_IDS,
        metadata={"rows": len(film_character_counts), "episode_ids": sorted(episodes)},
    )


@asset_check(
    asset=characters_enriched,
    blocking=True,
    description="character_name is the join key for everything downstream; "
    "a null name means the people table itself is malformed.",
)
def characters_enriched_has_no_null_names(characters_enriched: pd.DataFrame) -> AssetCheckResult:
    nulls = int(characters_enriched["character_name"].isna().sum())
    return AssetCheckResult(passed=nulls == 0, metadata={"null_names": nulls})


# ── Drift checks (WARN — upstream data is not ours to freeze) ────────────────

@asset_check(
    asset=raw_people,
    description=f"swapi.info returned {EXPECTED_PEOPLE_COUNT} people when this "
    "pipeline was verified. A different count isn't a bug — it's upstream drift "
    "that every published number (report and site) depends on. Investigate, then "
    "update known_facts.py.",
)
def raw_people_count_matches_verified_snapshot(raw_people: list[dict]) -> AssetCheckResult:
    return AssetCheckResult(
        passed=len(raw_people) == EXPECTED_PEOPLE_COUNT,
        severity=AssetCheckSeverity.WARN,
        metadata={"count": len(raw_people), "expected": EXPECTED_PEOPLE_COUNT},
    )


@asset_check(
    asset=characters_enriched,
    description="The people→planets LEFT JOIN keeps characters with no matching "
    "homeworld but nulls their planet columns silently. This check makes the "
    "loss visible: it warns if the join misses more than the verified baseline.",
)
def characters_enriched_join_coverage(characters_enriched: pd.DataFrame) -> AssetCheckResult:
    total = len(characters_enriched)
    null_homeworld = int(characters_enriched["homeworld"].isna().sum())
    return AssetCheckResult(
        passed=null_homeworld == 0,
        severity=AssetCheckSeverity.WARN,
        metadata={
            "characters": total,
            "null_homeworld": null_homeworld,
            "join_coverage_pct": round(100 * (total - null_homeworld) / total, 1) if total else 0,
        },
    )


@asset_check(
    asset=characters_enriched,
    description=f"{EXPECTED_UNKNOWN_MASS_COUNT} of {EXPECTED_PEOPLE_COUNT} people "
    "have mass='unknown' in the verified snapshot. The report's mass-based claims "
    "depend on this denominator, so drift here should be noticed, not silent.",
)
def characters_enriched_unknown_mass_baseline(characters_enriched: pd.DataFrame) -> AssetCheckResult:
    mass = characters_enriched["mass"]
    unknown = int(((mass == "unknown") | mass.isna()).sum())
    return AssetCheckResult(
        passed=unknown == EXPECTED_UNKNOWN_MASS_COUNT,
        severity=AssetCheckSeverity.WARN,
        metadata={"unknown_mass": unknown, "expected": EXPECTED_UNKNOWN_MASS_COUNT},
    )


@asset_check(
    asset=starship_stats,
    description="TRY_CAST turns unparseable strings ('unknown', '30-165', '5,000') "
    "into NULL silently. This check publishes the per-column loss rate and warns "
    "on impossible values, so nobody mistakes 'castable' for 'complete'.",
)
def starship_stats_cast_sanity(starship_stats: pd.DataFrame) -> AssetCheckResult:
    cast_columns = ["hyperdrive_rating", "max_speed", "crew_size", "passenger_capacity", "length_m"]
    total = len(starship_stats)
    null_rates = {
        col: f"{int(starship_stats[col].isna().sum())}/{total}" for col in cast_columns
    }
    negatives = {
        col: int((starship_stats[col] < 0).sum())
        for col in cast_columns
        if (starship_stats[col] < 0).any()
    }
    return AssetCheckResult(
        passed=not negatives,
        severity=AssetCheckSeverity.WARN,
        metadata={"null_rates_after_cast": null_rates, "negative_values": negatives},
    )
