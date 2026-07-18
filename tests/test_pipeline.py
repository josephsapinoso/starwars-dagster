"""
Integration test: the full asset graph, offline.

One dagster.materialize() run of all 10 assets (plus every asset check)
against fixture JSON, in an isolated working directory. This is the test
that proves the pipeline runs from a clean clone.
"""

import json

import pytest
from dagster import materialize

from starwars_dagster.assets import (
    characters_enriched,
    film_character_counts,
    galaxy_report,
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
from tests.conftest import SNAPSHOT_MARKER, load_fixture

ALL_ASSETS = [
    raw_films,
    raw_people,
    raw_planets,
    raw_starships,
    raw_species,
    star_wars_db,
    characters_enriched,
    film_character_counts,
    starship_stats,
    galaxy_report,
]

ALL_CHECKS = [
    checks_module.raw_people_has_required_shape,
    checks_module.star_wars_db_tables_populated,
    checks_module.films_are_exactly_the_six_episodes,
    checks_module.characters_enriched_has_no_null_names,
    checks_module.raw_people_count_matches_verified_snapshot,
    checks_module.characters_enriched_join_coverage,
    checks_module.characters_enriched_unknown_mass_baseline,
    checks_module.starship_stats_cast_sanity,
]


@pytest.fixture
def full_run(isolated_cwd, fake_swapi):
    result = materialize(
        ALL_ASSETS + ALL_CHECKS,
        resources={"swapi": fake_swapi},
    )
    return result, isolated_cwd


def test_all_ten_assets_materialize_from_a_clean_directory(full_run):
    result, cwd = full_run
    assert result.success
    # the CSV side effects prove data/output/ gets created before first use
    assert (cwd / "data" / "output" / "characters_enriched.csv").exists()
    assert (cwd / "data" / "output" / "galaxy_report.md").exists()
    assert (cwd / "data" / "star_wars.duckdb").exists()


def test_structural_asset_checks_pass_on_well_formed_data(full_run):
    result, _ = full_run
    blocking = {
        "raw_people_has_required_shape",
        "star_wars_db_tables_populated",
        "films_are_exactly_the_six_episodes",
        "characters_enriched_has_no_null_names",
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


# The three facts below back the site's per-beat provenance reveals: the
# reveal copy names these tests as the offline guard for figures no asset
# computes (site/index.html DATA.provenance, tests/test_site_provenance.py).


@requires_real_snapshot
def test_exactly_one_character_has_unknown_height():
    unmeasured = [p["name"] for p in load_fixture("people") if p["height"] == "unknown"]
    assert len(unmeasured) == EXPECTED_UNKNOWN_HEIGHT_COUNT


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
