"""
Integration test: the full asset graph, offline.

One dagster.materialize() run of all 13 assets (plus every asset check)
against fixture JSON, in an isolated working directory. This is the test
that proves the pipeline runs from a clean clone.
"""

import json

import pytest
from dagster import materialize

from starwars_dagster.assets import (
    character_biographies,
    character_stats,
    characters_enriched,
    film_character_counts,
    galaxy_report,
    raw_character_profiles,
    raw_films,
    raw_people,
    raw_planets,
    raw_species,
    raw_starships,
    star_wars_db,
    starship_stats,
)
from starwars_dagster.assets import checks as checks_module
from starwars_dagster.known_facts import (
    EXPECTED_MAX_STARSHIPS_FLOWN,
    EXPECTED_NABOO_CHARACTERS,
    EXPECTED_ONE_FILM_COUNT,
    EXPECTED_PEOPLE_COUNT,
    EXPECTED_PILOT_COUNT,
    EXPECTED_TATOOINE_CHARACTERS,
    EXPECTED_UNKNOWN_HEIGHT_COUNT,
    EXPECTED_UNKNOWN_MASS_COUNT,
    SIX_FILM_CHARACTERS,
)
from starwars_dagster.known_facts import EXPECTED_PROFILE_COUNT
from tests.conftest import (
    AKABAB_FIXTURE_DIR,
    AKABAB_SNAPSHOT_MARKER,
    SNAPSHOT_MARKER,
    load_fixture,
)

ALL_ASSETS = [
    raw_films,
    raw_people,
    raw_planets,
    raw_starships,
    raw_species,
    raw_character_profiles,
    star_wars_db,
    characters_enriched,
    film_character_counts,
    starship_stats,
    character_stats,
    character_biographies,
    galaxy_report,
]

ALL_CHECKS = [
    checks_module.raw_people_has_required_shape,
    checks_module.star_wars_db_tables_populated,
    checks_module.films_are_exactly_the_six_episodes,
    checks_module.characters_enriched_has_no_null_names,
    checks_module.raw_character_profiles_has_required_shape,
    checks_module.character_biographies_grain_is_one_row_per_character,
    checks_module.raw_people_count_matches_verified_snapshot,
    checks_module.characters_enriched_join_coverage,
    checks_module.characters_enriched_unknown_mass_baseline,
    checks_module.characters_enriched_unknown_height_baseline,
    checks_module.starship_stats_cast_sanity,
    checks_module.character_stats_one_film_baseline,
    checks_module.character_stats_six_film_trio,
    checks_module.character_stats_pilot_count_baseline,
    checks_module.character_stats_max_flown_baseline,
    checks_module.character_stats_birth_year_baseline,
    checks_module.character_stats_birth_year_parse_honesty,
    checks_module.raw_character_profiles_count_matches_verified_snapshot,
    checks_module.character_biographies_join_coverage,
    checks_module.character_biographies_deaths_on_file_baseline,
]


@pytest.fixture
def full_run(isolated_cwd, fake_swapi, fake_akabab):
    result = materialize(
        ALL_ASSETS + ALL_CHECKS,
        resources={"swapi": fake_swapi, "akabab": fake_akabab},
    )
    return result, isolated_cwd


def test_all_thirteen_assets_materialize_from_a_clean_directory(full_run):
    result, cwd = full_run
    assert result.success
    # the CSV side effects prove data/output/ gets created before first use
    assert (cwd / "data" / "output" / "characters_enriched.csv").exists()
    assert (cwd / "data" / "output" / "character_stats.csv").exists()
    assert (cwd / "data" / "output" / "character_biographies.csv").exists()
    assert (cwd / "data" / "output" / "galaxy_report.md").exists()
    assert (cwd / "data" / "star_wars.duckdb").exists()


def test_written_back_tables_match_the_returned_frames(full_run):
    # a write-back must be the SAME data the asset returns — one code path,
    # so each asset's checks extend to its warehouse table by construction
    import duckdb
    import pandas as pd

    result, cwd = full_run
    con = duckdb.connect(str(cwd / "data" / "star_wars.duckdb"), read_only=True)
    try:
        for node in ["characters_enriched", "character_stats", "character_biographies"]:
            df = result.output_for_node(node)
            table = con.execute(
                f"SELECT * FROM {node} ORDER BY character_name"
            ).df()
            pd.testing.assert_frame_equal(
                table.reset_index(drop=True),
                df.sort_values("character_name").reset_index(drop=True),
                check_dtype=False,
            )
    finally:
        con.close()


def test_structural_asset_checks_pass_on_well_formed_data(full_run):
    result, _ = full_run
    blocking = {
        "raw_people_has_required_shape",
        "star_wars_db_tables_populated",
        "films_are_exactly_the_six_episodes",
        "characters_enriched_has_no_null_names",
        "raw_character_profiles_has_required_shape",
        "character_biographies_grain_is_one_row_per_character",
    }
    outcomes = {
        e.check_name: e.passed for e in result.get_asset_check_evaluations()
    }
    failed = [name for name in blocking if not outcomes[name]]
    assert not failed, f"blocking checks failed: {failed}"


def test_gender_table_keeps_its_labels_on_modern_pandas(full_run):
    _, cwd = full_run
    report = (cwd / "data" / "output" / "galaxy_report.md").read_text()
    assert "| gender | count |" in report
    assert "| male |" in report


def test_climate_lines_count_characters_and_disclose_the_denominator(full_run):
    _, cwd = full_run
    report = (cwd / "data" / "output" / "galaxy_report.md").read_text()
    assert "characters" in report.split("Homeworld Climate Distribution")[1]
    assert "homeworlds**" not in report  # the old mislabeled bullet format
    assert "have a known homeworld" in report


def test_affiliations_section_discloses_nested_denominators(full_run):
    # the second-source section renders with BOTH denominators (matched and
    # field-present) on-page and speaks "on file", never "deceased" —
    # panel-settled vocabulary (decision log 2026-07-20)
    _, cwd = full_run
    report = (cwd / "data" / "output" / "galaxy_report.md").read_text()
    assert "## 🤝 Affiliations & Apprenticeships" in report
    section = report.split("Affiliations & Apprenticeships")[1].split("## 🚀")[0]
    assert "matched to a curated profile" in section
    assert "carry an affiliations list" in section
    assert "master on file" in section
    assert "record a death" in section
    assert "absence is not survival" in section
    assert "deceased" not in section.lower()


def test_birth_year_parse_honesty_holds_on_any_fixture(full_run):
    # data-independent invariant: parsed NULLs == raw 'unknown' strings.
    # Ungated by design — it must hold on synthetic fixtures too, which is
    # exactly what makes it a parse guard rather than a drift baseline.
    result, _ = full_run
    outcomes = {e.check_name: e.passed for e in result.get_asset_check_evaluations()}
    assert outcomes["character_stats_birth_year_parse_honesty"]


def test_warehouse_access_policy_is_encoded_in_code():
    # DuckDB allows many readers OR one writer per file. The multiprocess
    # executor raced transforms on that lock (observed 2026-07-18), so the
    # policy lives in code and this test keeps it there: every pure-read
    # transform opens read_only, every writer is declared below (write-back
    # law), and the repo's default executor is in-process (sequential).
    import inspect

    from dagster import in_process_executor

    from starwars_dagster import defs
    from starwars_dagster.assets import transforms

    readers = [
        transforms.film_character_counts,
        transforms.starship_stats,
    ]
    for asset_def in readers:
        src = inspect.getsource(asset_def.op.compute_fn.decorated_fn)
        assert "read_only=True" in src, f"{asset_def.key} must open the warehouse read_only"
    # the three writers persist their grain back into the warehouse (write-back
    # law: displayed table names must exist); sequential execution serializes them
    for writer in [
        transforms.characters_enriched,
        transforms.character_stats,
        transforms.character_biographies,
    ]:
        src = inspect.getsource(writer.op.compute_fn.decorated_fn)
        assert "read_only" not in src, f"{writer.key} is a declared writer"
        assert "CREATE OR REPLACE TABLE" in src, f"{writer.key} must write its grain back"
    assert defs.executor is in_process_executor


# ── Banked facts — real dataset only ─────────────────────────────────────────
# These assert exact values verified against swapi.info, so they only run when
# the fixtures are a real dated snapshot (scripts/snapshot_fixtures.py), not
# the synthetic defaults.

requires_real_snapshot = pytest.mark.skipif(
    not SNAPSHOT_MARKER.exists(),
    reason="fixtures are synthetic; run scripts/snapshot_fixtures.py to enable",
)


@requires_real_snapshot
def test_people_count_is_82():
    assert len(load_fixture("people")) == EXPECTED_PEOPLE_COUNT


@requires_real_snapshot
def test_exactly_three_characters_appear_in_all_six_films():
    six_film = {p["name"] for p in load_fixture("people") if len(p["films"]) == 6}
    assert six_film == SIX_FILM_CHARACTERS


@requires_real_snapshot
def test_23_characters_have_unknown_mass():
    unknown = [p["name"] for p in load_fixture("people") if p["mass"] == "unknown"]
    assert len(unknown) == EXPECTED_UNKNOWN_MASS_COUNT


@requires_real_snapshot
def test_naboo_has_11_characters_and_tatooine_10():
    planet_names = {p["url"]: p["name"] for p in load_fixture("planets")}
    homeworlds = [planet_names.get(p["homeworld"]) for p in load_fixture("people")]
    assert homeworlds.count("Naboo") == EXPECTED_NABOO_CHARACTERS
    assert homeworlds.count("Tatooine") == EXPECTED_TATOOINE_CHARACTERS


# The height fact below still backs the site's beat-1 provenance reveal as
# its named pytest guard (site/index.html DATA.provenance). The one-film and
# pilot facts are now also computed by the character_stats asset and asserted
# by its checks — beats 4-6 cite those checks; these tests stay as the
# known_facts.py guards behind the same numbers.


@requires_real_snapshot
def test_exactly_one_character_has_unknown_height():
    unmeasured = [p["name"] for p in load_fixture("people") if p["height"] == "unknown"]
    assert len(unmeasured) == EXPECTED_UNKNOWN_HEIGHT_COUNT


@requires_real_snapshot
def test_the_unmeasured_pilot_flew_the_a_wing():
    # beat 1's aside names Arvel Crynyd as an A-wing pilot; pin the craft to
    # the data so the copy can never misattribute it again (it shipped as
    # "X-wing" once — survey catch, 2026-07-19)
    people = {p["url"]: p["name"] for p in load_fixture("people")}
    a_wing = next(s for s in load_fixture("starships") if s["name"] == "A-wing")
    assert [people[u] for u in a_wing["pilots"]] == ["Arvel Crynyd"]
    unmeasured = [p["name"] for p in load_fixture("people") if p["height"] == "unknown"]
    assert unmeasured == ["Arvel Crynyd"]


@requires_real_snapshot
def test_42_of_82_appear_in_exactly_one_film():
    one_film = [p for p in load_fixture("people") if len(p["films"]) == 1]
    assert len(one_film) == EXPECTED_ONE_FILM_COUNT


@requires_real_snapshot
def test_19_pilots_and_obi_wan_leads_with_five():
    flown = {p["name"]: len(p["starships"]) for p in load_fixture("people")}
    assert sum(1 for c in flown.values() if c > 0) == EXPECTED_PILOT_COUNT
    assert max(flown.values()) == EXPECTED_MAX_STARSHIPS_FLOWN
    assert flown["Obi-Wan Kenobi"] == EXPECTED_MAX_STARSHIPS_FLOWN


# ── Banked facts, second source — gated on the akabab snapshot marker ────────
# Baselines are COMPUTED against the frozen fixture by snapshot_fixtures.py,
# never transcribed from a survey. Cross-source facts (join coverage, deaths
# on file) additionally need the swapi snapshot, so they gate on BOTH markers.

requires_real_akabab_snapshot = pytest.mark.skipif(
    not AKABAB_SNAPSHOT_MARKER.exists(),
    reason="akabab fixtures are synthetic; run scripts/snapshot_fixtures.py to enable",
)

requires_both_snapshots = pytest.mark.skipif(
    not (SNAPSHOT_MARKER.exists() and AKABAB_SNAPSHOT_MARKER.exists()),
    reason="cross-source baselines need real snapshots of BOTH sources",
)


@requires_real_akabab_snapshot
def test_profile_count_matches_the_verified_snapshot():
    profiles = json.loads((AKABAB_FIXTURE_DIR / "all.json").read_text())
    assert len(profiles) == EXPECTED_PROFILE_COUNT


@requires_both_snapshots
def test_second_source_drift_checks_pass_on_the_real_snapshots(full_run):
    # WARN checks can fail without failing materialize, so the second-source
    # baselines must be asserted green explicitly once both fixtures are real.
    result, _ = full_run
    outcomes = {e.check_name: e.passed for e in result.get_asset_check_evaluations()}
    baseline_checks = {
        "raw_character_profiles_count_matches_verified_snapshot",
        "character_biographies_join_coverage",
        "character_biographies_deaths_on_file_baseline",
    }
    failed = [name for name in baseline_checks if not outcomes[name]]
    assert not failed, f"second-source drift checks failed: {failed}"


@requires_real_snapshot
def test_character_stats_drift_checks_pass_on_the_real_snapshot(full_run):
    # WARN checks can fail without failing materialize, so the story-beat badge
    # checks must be asserted green explicitly. Snapshot-gated: synthetic
    # fixtures would legitimately miss these exact values.
    result, _ = full_run
    badge_checks = {
        "character_stats_one_film_baseline",
        "character_stats_six_film_trio",
        "character_stats_pilot_count_baseline",
        "character_stats_max_flown_baseline",
        "characters_enriched_unknown_height_baseline",
        "character_stats_birth_year_baseline",
    }
    outcomes = {
        e.check_name: e.passed for e in result.get_asset_check_evaluations()
    }
    failed = [name for name in badge_checks if not outcomes[name]]
    assert not failed, f"character_stats drift checks failed: {failed}"
