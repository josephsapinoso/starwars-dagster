"""
Second-source join tests: how profiles attach to the census, and how they miss.

The character_biographies LEFT JOIN tolerates exactly two kinds of name
variance — case/whitespace normalization and the curated alias map in
known_facts.py. Everything else must stay unmatched and countable. These
tests pin that contract on crafted records (Inline resources), plus the
seen-to-fail proofs for the two blocking checks and the alias-map governance
rules (injectivity, load-bearing entries).
"""

import json

import pandas as pd
import pytest
from dagster import materialize

from starwars_dagster.assets import (
    character_biographies,
    raw_character_profiles,
    raw_films,
    raw_people,
    raw_planets,
    raw_species,
    raw_starships,
    star_wars_db,
)
from starwars_dagster.assets import checks as checks_module
from starwars_dagster.assets.transforms import _normalize_name
from starwars_dagster.known_facts import PROFILE_NAME_ALIASES
from tests.conftest import (
    AKABAB_SNAPSHOT_MARKER,
    SNAPSHOT_MARKER,
    InlineAkababResource,
    InlineSWAPIResource,
    load_fixture,
)

RAW_ASSETS = [raw_films, raw_people, raw_planets, raw_starships, raw_species]
JOIN_ASSETS = RAW_ASSETS + [star_wars_db, raw_character_profiles, character_biographies]


def _person(name: str) -> dict:
    return {
        "name": name,
        "homeworld": "https://swapi.info/api/planets/1/",
        "films": [],
        "starships": [],
        "mass": "unknown",
        "gender": "n/a",
        "birth_year": "unknown",
        "height": "unknown",
        "eye_color": "n/a",
        "hair_color": "n/a",
        "url": f"https://swapi.info/api/people/{name}/",
    }


def _profile(pid: int, name: str, **overrides) -> dict:
    record = {"id": pid, "name": name}
    record.update(overrides)
    return record


def _run_join(people: list[dict], profiles: list[dict], **kwargs):
    swapi = InlineSWAPIResource(data={"people": people})
    akabab = InlineAkababResource(data={"all": profiles})
    return materialize(
        JOIN_ASSETS + list(kwargs.pop("checks", [])),
        resources={"swapi": swapi, "akabab": akabab},
        **kwargs,
    )


@pytest.fixture
def joined(isolated_cwd):
    result = _run_join(
        [_person("Luke Skywalker"), _person("Beru Whitesun lars"), _person("Greedo")],
        [
            _profile(
                1,
                "Luke Skywalker",
                affiliations=["Jedi Order", "Red Squadron"],
                masters=["Obi-Wan Kenobi", "Yoda"],
                died=34,
                diedLocation="ahch-to",
                wiki="http://example.invalid/luke",
            ),
            # case variance only — normalization must bridge it
            _profile(2, "Beru Whitesun Lars", affiliations=[]),
            # no counterpart in the census — must not invent a row
            _profile(9, "Rey", masters=["Luke Skywalker"]),
        ],
    )
    assert result.success
    return result.output_for_node("character_biographies").set_index("character_name")


def test_left_join_keeps_every_census_character(joined):
    assert sorted(joined.index) == ["Beru Whitesun lars", "Greedo", "Luke Skywalker"]


def test_unmatched_character_gets_null_profile_columns_not_dropped(joined):
    greedo = joined.loc["Greedo"]
    assert pd.isna(greedo["profile_id"])
    assert pd.isna(greedo["died_year_aby"])
    assert pd.isna(greedo["affiliation_count"])


def test_case_and_whitespace_variance_is_bridged_by_normalization(joined):
    beru = joined.loc["Beru Whitesun lars"]
    assert beru["profile_name"] == "Beru Whitesun Lars"  # source spelling preserved
    assert beru["affiliation_count"] == 0  # present-but-empty list counts as 0


def test_matched_profile_carries_lineage_strings_and_death_on_file(joined):
    luke = joined.loc["Luke Skywalker"]
    assert json.loads(luke["masters"]) == ["Obi-Wan Kenobi", "Yoda"]
    assert luke["master_count"] == 2
    assert luke["died_year_aby"] == 34.0
    assert luke["died_location"] == "ahch-to"


def test_missing_optional_fields_stay_null_never_zero(joined):
    # Luke's record has no apprentices key at all: absent field ≠ empty list
    luke = joined.loc["Luke Skywalker"]
    assert pd.isna(luke["apprentices"])
    assert pd.isna(luke["apprentice_count"])


def test_akabab_only_profiles_never_create_rows(joined):
    assert "Rey" not in joined.index
    assert not joined["profile_name"].eq("Rey").any()


def test_alias_bridges_the_join_but_never_mutates_the_census_spelling(isolated_cwd):
    # the real alias pair from known_facts: akabab holds canon "Ratts Tyerell",
    # SWAPI's as-filed record is "Ratts Tyerel"
    result = _run_join(
        [_person("Ratts Tyerel")],
        [_profile(7, "Ratts Tyerell", died=-32)],
    )
    assert result.success
    df = result.output_for_node("character_biographies")
    row = df.set_index("character_name").loc["Ratts Tyerel"]
    assert row["profile_name"] == "Ratts Tyerell"
    assert row["died_year_aby"] == -32.0


# ── Seen-to-fail: the blocking checks trip on the failures they claim to ─────


def test_duplicate_profile_names_fan_out_and_fail_the_grain_check(isolated_cwd):
    result = _run_join(
        [_person("Luke Skywalker"), _person("Greedo")],
        [_profile(1, "Luke Skywalker"), _profile(2, "luke  SKYWALKER")],
        checks=[checks_module.character_biographies_grain_is_one_row_per_character],
        raise_on_error=False,
    )
    outcomes = {e.check_name: e for e in result.get_asset_check_evaluations()}
    grain = outcomes["character_biographies_grain_is_one_row_per_character"]
    assert not grain.passed


def test_profile_record_missing_its_name_fails_the_shape_check(isolated_cwd):
    swapi = InlineSWAPIResource(data={})
    akabab = InlineAkababResource(data={"all": [{"id": 1}]})
    result = materialize(
        [raw_character_profiles, checks_module.raw_character_profiles_has_required_shape],
        resources={"swapi": swapi, "akabab": akabab},
        raise_on_error=False,
    )
    outcomes = {e.check_name: e for e in result.get_asset_check_evaluations()}
    assert not outcomes["raw_character_profiles_has_required_shape"].passed


def test_join_coverage_check_names_the_misses_on_both_sides(isolated_cwd):
    result = _run_join(
        [_person("Luke Skywalker"), _person("Greedo")],
        [_profile(1, "Luke Skywalker"), _profile(9, "Rey")],
        checks=[checks_module.character_biographies_join_coverage],
        raise_on_error=False,
    )
    outcomes = {e.check_name: e for e in result.get_asset_check_evaluations()}
    coverage = outcomes["character_biographies_join_coverage"]
    metadata = {k: v.value for k, v in coverage.metadata.items()}
    assert metadata["unmatched_characters"] == ["Greedo"]
    assert metadata["unmatched_profiles"] == ["Rey"]


# ── Alias-map governance (ungated: structural rules of the map itself) ───────


def test_alias_map_is_injective_after_normalization():
    # no two profile names may collapse onto one census record —
    # Vader and Anakin are separate records in BOTH sources and must stay so
    targets = [_normalize_name(v) for v in PROFILE_NAME_ALIASES.values()]
    assert len(targets) == len(set(targets)), "two aliases map to one census name"


def test_every_alias_is_load_bearing():
    # an alias whose key normalizes to its value is dead weight the
    # normalization step already handles — it must be removed, not kept
    for source, target in PROFILE_NAME_ALIASES.items():
        assert _normalize_name(source) != _normalize_name(target), (
            f"alias {source!r} -> {target!r} is redundant with normalization"
        )


# ── Alias resolution (gated: needs the real fixture on the relevant side) ────


@pytest.mark.skipif(
    not SNAPSHOT_MARKER.exists(),
    reason="alias targets resolve against the real census fixture",
)
def test_every_alias_target_is_a_real_census_name():
    census = {p["name"] for p in load_fixture("people")}
    for target in PROFILE_NAME_ALIASES.values():
        assert target in census, f"alias target {target!r} not in the census"


@pytest.mark.skipif(
    not AKABAB_SNAPSHOT_MARKER.exists(),
    reason="alias keys resolve against the real profile fixture",
)
def test_every_alias_key_is_a_real_profile_name():
    from tests.conftest import AKABAB_FIXTURE_DIR

    profiles = json.loads((AKABAB_FIXTURE_DIR / "all.json").read_text())
    names = {p["name"] for p in profiles}
    for source in PROFILE_NAME_ALIASES:
        assert source in names, f"alias key {source!r} not in the profile source"
