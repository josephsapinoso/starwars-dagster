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

  Description style rule (panel-settled, 2026-07-18): a description states
  the INVARIANT and its STAKES; run metadata carries the particulars; the
  rosters and numbers themselves live only in known_facts.py. Check strings
  render on the site's story rails, so they must never pre-tell a later
  beat's payoff — tests/test_site_provenance.py pins this.
"""

import duckdb
import pandas as pd
from dagster import (
    AssetCheckResult,
    AssetCheckSeverity,
    AssetIn,
    asset_check,
)

from starwars_dagster.assets.ingestion import raw_character_profiles, raw_people
from starwars_dagster.assets.transforms import (
    character_biographies,
    character_stats,
    characters_enriched,
    film_character_counts,
    star_wars_db,
    starship_stats,
)
from starwars_dagster.known_facts import (
    EXPECTED_DB_TABLES,
    EXPECTED_DEATHS_ON_FILE,
    EXPECTED_EPISODE_IDS,
    EXPECTED_FILM_COUNT,
    EXPECTED_MAX_STARSHIPS_FLOWN,
    EXPECTED_OLDEST_BIRTH_BBY,
    EXPECTED_ONE_FILM_COUNT,
    EXPECTED_PEOPLE_COUNT,
    EXPECTED_PILOT_COUNT,
    EXPECTED_PROFILE_COUNT,
    EXPECTED_PROFILE_MATCH_COUNT,
    EXPECTED_UNDATED_BIRTH_COUNT,
    EXPECTED_UNKNOWN_HEIGHT_COUNT,
    EXPECTED_UNKNOWN_MASS_COUNT,
    REQUIRED_PEOPLE_KEYS,
    REQUIRED_PROFILE_KEYS,
    SIX_FILM_CHARACTERS,
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


@asset_check(
    asset=raw_character_profiles,
    blocking=True,
    description="Every character profile must be non-empty and carry the id and "
    "name keys the census join anchors on — the profile schema is polymorphic "
    "by kind, but the anchor is non-negotiable.",
)
def raw_character_profiles_has_required_shape(
    raw_character_profiles: list[dict],
) -> AssetCheckResult:
    if not raw_character_profiles:
        return AssetCheckResult(passed=False, metadata={"reason": "empty response"})
    missing = [
        (rec.get("name", f"record #{i}"), sorted(REQUIRED_PROFILE_KEYS - rec.keys()))
        for i, rec in enumerate(raw_character_profiles)
        if not REQUIRED_PROFILE_KEYS <= rec.keys()
    ]
    return AssetCheckResult(
        passed=not missing,
        metadata={
            "records": len(raw_character_profiles),
            "records_missing_keys": missing[:10],
        },
    )


@asset_check(
    asset=character_biographies,
    blocking=True,
    additional_ins={"star_wars_db": AssetIn("star_wars_db")},
    description="Exactly one row per census character, with unique names — "
    "a fan-out in the profile join would silently inflate every downstream count.",
)
def character_biographies_grain_is_one_row_per_character(
    character_biographies: pd.DataFrame, star_wars_db: str
) -> AssetCheckResult:
    con = duckdb.connect(star_wars_db, read_only=True)
    try:
        people_count = con.execute("SELECT COUNT(*) FROM people").fetchone()[0]
    finally:
        con.close()
    duplicates = (
        character_biographies["character_name"]
        .value_counts()
        .loc[lambda s: s > 1]
        .index.tolist()
    )
    return AssetCheckResult(
        passed=len(character_biographies) == people_count and not duplicates,
        metadata={
            "rows": len(character_biographies),
            "census_characters": people_count,
            "duplicated_names": duplicates[:10],
        },
    )


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
    description="The count of people with mass='unknown' matches the verified "
    "baseline in known_facts.py. The report's mass-based claims depend on this "
    "denominator, so drift here should be noticed, not silent.",
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
    asset=characters_enriched,
    description="The count of people with height='unknown' matches the verified "
    "baseline in known_facts.py. The census's opening range claim and the "
    "report's height stats depend on it.",
)
def characters_enriched_unknown_height_baseline(characters_enriched: pd.DataFrame) -> AssetCheckResult:
    height = characters_enriched["height"]
    unknown = int(((height == "unknown") | height.isna()).sum())
    return AssetCheckResult(
        passed=unknown == EXPECTED_UNKNOWN_HEIGHT_COUNT,
        severity=AssetCheckSeverity.WARN,
        metadata={"unknown_height": unknown, "expected": EXPECTED_UNKNOWN_HEIGHT_COUNT},
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


@asset_check(
    asset=character_stats,
    description=f"{EXPECTED_ONE_FILM_COUNT} of {EXPECTED_PEOPLE_COUNT} characters "
    "appear in exactly one film in the verified snapshot. The story's one-scene-"
    "wonders beat displays this number, so drift here changes the page.",
)
def character_stats_one_film_baseline(character_stats: pd.DataFrame) -> AssetCheckResult:
    one_film = int((character_stats["film_count"] == 1).sum())
    return AssetCheckResult(
        passed=one_film == EXPECTED_ONE_FILM_COUNT,
        severity=AssetCheckSeverity.WARN,
        metadata={"one_film_characters": one_film, "expected": EXPECTED_ONE_FILM_COUNT},
    )


@asset_check(
    asset=character_stats,
    description="The set of characters appearing in all six films matches the "
    "verified snapshot in known_facts.py. The story's late payoff leans on this "
    "exact set — if it shifts, that beat is wrong, not just stale.",
)
def character_stats_six_film_trio(character_stats: pd.DataFrame) -> AssetCheckResult:
    six_film = set(character_stats.loc[character_stats["film_count"] == 6, "character_name"])
    return AssetCheckResult(
        passed=six_film == SIX_FILM_CHARACTERS,
        severity=AssetCheckSeverity.WARN,
        metadata={"six_film_characters": sorted(six_film), "expected": sorted(SIX_FILM_CHARACTERS)},
    )


@asset_check(
    asset=character_stats,
    description="The count of characters listed at the controls of at least one "
    "starship matches the verified baseline in known_facts.py — the denominator "
    "behind the census's flight records.",
)
def character_stats_pilot_count_baseline(character_stats: pd.DataFrame) -> AssetCheckResult:
    pilots = int((character_stats["starships_flown"] > 0).sum())
    return AssetCheckResult(
        passed=pilots == EXPECTED_PILOT_COUNT,
        severity=AssetCheckSeverity.WARN,
        metadata={"pilots": pilots, "expected": EXPECTED_PILOT_COUNT},
    )


@asset_check(
    asset=character_stats,
    description="No character has flown more starships than the verified maximum "
    "in known_facts.py. The census's most-flown record depends on this cap — "
    "drift means the leaderboard changed.",
)
def character_stats_max_flown_baseline(character_stats: pd.DataFrame) -> AssetCheckResult:
    max_flown = int(character_stats["starships_flown"].max()) if len(character_stats) else 0
    return AssetCheckResult(
        passed=max_flown == EXPECTED_MAX_STARSHIPS_FLOWN,
        severity=AssetCheckSeverity.WARN,
        metadata={"max_starships_flown": max_flown, "expected": EXPECTED_MAX_STARSHIPS_FLOWN},
    )


@asset_check(
    asset=character_stats,
    description="The undated count and the oldest dated record in the birth "
    "registry match the verified baselines in known_facts.py. The registry "
    "card's headline and its oldest-on-file claim depend on them.",
)
def character_stats_birth_year_baseline(character_stats: pd.DataFrame) -> AssetCheckResult:
    undated = int(character_stats["birth_year_bby"].isna().sum())
    oldest = float(character_stats["birth_year_bby"].max()) if undated < len(character_stats) else None
    return AssetCheckResult(
        passed=undated == EXPECTED_UNDATED_BIRTH_COUNT and oldest == EXPECTED_OLDEST_BIRTH_BBY,
        severity=AssetCheckSeverity.WARN,
        metadata={
            "undated": undated,
            "expected_undated": EXPECTED_UNDATED_BIRTH_COUNT,
            "oldest_bby": oldest,
            "expected_oldest_bby": EXPECTED_OLDEST_BIRTH_BBY,
        },
    )


@asset_check(
    asset=character_stats,
    additional_ins={"star_wars_db": AssetIn("star_wars_db")},
    description="Every null in the parsed birth-year column corresponds to a "
    "record whose raw field is the literal string 'unknown' — a source format "
    "change degrades loudly here instead of silently swelling the undated count.",
)
def character_stats_birth_year_parse_honesty(
    character_stats: pd.DataFrame, star_wars_db: str
) -> AssetCheckResult:
    parsed_nulls = int(character_stats["birth_year_bby"].isna().sum())
    con = duckdb.connect(star_wars_db, read_only=True)
    try:
        raw_unknowns = con.execute(
            "SELECT COUNT(*) FROM people WHERE birth_year = 'unknown'"
        ).fetchone()[0]
    finally:
        con.close()
    return AssetCheckResult(
        passed=parsed_nulls == raw_unknowns,
        severity=AssetCheckSeverity.WARN,
        metadata={"parsed_nulls": parsed_nulls, "raw_unknowns": raw_unknowns},
    )


@asset_check(
    asset=raw_character_profiles,
    description=f"The profile source returned {EXPECTED_PROFILE_COUNT} records "
    "when this pipeline was verified. A different count isn't a bug — it's "
    "drift in a dataset we don't own. Investigate, then update known_facts.py.",
)
def raw_character_profiles_count_matches_verified_snapshot(
    raw_character_profiles: list[dict],
) -> AssetCheckResult:
    return AssetCheckResult(
        passed=len(raw_character_profiles) == EXPECTED_PROFILE_COUNT,
        severity=AssetCheckSeverity.WARN,
        metadata={
            "count": len(raw_character_profiles),
            "expected": EXPECTED_PROFILE_COUNT,
        },
    )


@asset_check(
    asset=character_biographies,
    additional_ins={"raw_character_profiles": AssetIn("raw_character_profiles")},
    description="The census→profile name join keeps every character and nulls "
    "the misses silently. This check publishes the losses on both sides — "
    "unmatched census names and unmatched profiles — so coverage drift is "
    "news, not noise.",
)
def character_biographies_join_coverage(
    character_biographies: pd.DataFrame, raw_character_profiles: list[dict]
) -> AssetCheckResult:
    matched = int(character_biographies["profile_id"].notna().sum())
    unmatched_characters = sorted(
        character_biographies.loc[
            character_biographies["profile_id"].isna(), "character_name"
        ]
    )
    matched_profile_names = set(
        character_biographies["profile_name"].dropna()
    )
    unmatched_profiles = sorted(
        rec["name"]
        for rec in raw_character_profiles
        if rec["name"] not in matched_profile_names
    )
    return AssetCheckResult(
        passed=matched == EXPECTED_PROFILE_MATCH_COUNT,
        severity=AssetCheckSeverity.WARN,
        metadata={
            "matched": matched,
            "expected": EXPECTED_PROFILE_MATCH_COUNT,
            "unmatched_characters": unmatched_characters[:10],
            "unmatched_profiles": unmatched_profiles[:10],
            "coverage_pct": round(
                100 * matched / len(character_biographies), 1
            ) if len(character_biographies) else 0,
        },
    )


@asset_check(
    asset=character_biographies,
    description="Profiles with a death on file match the verified baseline in "
    "known_facts.py — the denominator behind the report's deaths-on-file "
    "figure. Drift signals upstream edits, not casualties.",
)
def character_biographies_deaths_on_file_baseline(
    character_biographies: pd.DataFrame,
) -> AssetCheckResult:
    matched = character_biographies[character_biographies["profile_id"].notna()]
    deaths = int(matched["died_year_aby"].notna().sum())
    return AssetCheckResult(
        passed=deaths == EXPECTED_DEATHS_ON_FILE,
        severity=AssetCheckSeverity.WARN,
        metadata={"deaths_on_file": deaths, "expected": EXPECTED_DEATHS_ON_FILE},
    )
