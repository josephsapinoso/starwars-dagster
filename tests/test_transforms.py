"""
Transform-layer tests: the two places data is lost on purpose.

TRY_CAST and the homeworld LEFT JOIN both swallow bad values silently by
design — these tests pin down exactly what "silently" means so a future
change can't widen the loss unnoticed.

Every test here crafts its own minimal records (InlineSWAPIResource) instead
of using the shared fixture snapshot: fixtures describe what the API returns
today, but these tests describe how the code must behave on any input.
"""

import pandas as pd
import pytest
from dagster import materialize

from starwars_dagster.assets import (
    character_stats,
    characters_enriched,
    raw_films,
    raw_people,
    raw_planets,
    raw_species,
    raw_starships,
    star_wars_db,
    starship_stats,
)
from tests.conftest import InlineSWAPIResource

RAW_ASSETS = [raw_films, raw_people, raw_planets, raw_starships, raw_species]


def _starship(name: str, **overrides) -> dict:
    record = {
        "name": name,
        "model": "test model",
        "starship_class": "test class",
        "manufacturer": "test yard",
        "hyperdrive_rating": "1.0",
        "max_atmosphering_speed": "1000",
        "crew": "1",
        "passengers": "0",
        "length": "10",
        "pilots": [],
        "url": f"https://swapi.info/api/starships/{name}",
    }
    record.update(overrides)
    return record


@pytest.fixture
def starship_df(isolated_cwd):
    swapi = InlineSWAPIResource(
        data={
            "starships": [
                _starship("Unknown Drive", hyperdrive_rating="unknown"),
                _starship("Range Crew", crew="30-165"),
                _starship("Comma Crew", crew="342,953"),
                _starship("Plain Numbers", hyperdrive_rating="0.5", crew="4", length="34.37"),
            ]
        }
    )
    result = materialize(RAW_ASSETS + [star_wars_db, starship_stats], resources={"swapi": swapi})
    assert result.success
    return result.output_for_node("starship_stats").set_index("name")


def test_unknown_hyperdrive_rating_becomes_null_not_zero(starship_df):
    assert pd.isna(starship_df.loc["Unknown Drive", "hyperdrive_rating"])


def test_range_and_comma_crew_strings_become_null_not_a_guess(starship_df):
    # "30-165" is a range, "342,953" has a separator — TRY_CAST must refuse both
    assert pd.isna(starship_df.loc["Range Crew", "crew_size"])
    assert pd.isna(starship_df.loc["Comma Crew", "crew_size"])
    # while plain integers survive the cast
    assert starship_df.loc["Plain Numbers", "crew_size"] == 4


def test_parseable_numeric_strings_are_cast_faithfully(starship_df):
    plain = starship_df.loc["Plain Numbers"]
    assert plain["hyperdrive_rating"] == 0.5
    assert plain["length_m"] == pytest.approx(34.37)


def _person(name: str, homeworld: str) -> dict:
    return {
        "name": name,
        "height": "180",
        "mass": "80",
        "hair_color": "brown",
        "eye_color": "brown",
        "birth_year": "unknown",
        "gender": "male",
        "homeworld": homeworld,
        "films": [],
        "url": f"https://swapi.info/api/people/{name}",
    }


def test_left_join_keeps_characters_whose_homeworld_is_unmatched(isolated_cwd):
    swapi = InlineSWAPIResource(
        data={
            "people": [
                _person("Matched", "https://swapi.info/api/planets/1"),
                _person("Orphan", "https://swapi.info/api/planets/999"),
            ],
            "planets": [
                {
                    "name": "Tatooine",
                    "climate": "arid",
                    "terrain": "desert",
                    "population": "200000",
                    "url": "https://swapi.info/api/planets/1",
                }
            ],
        }
    )
    result = materialize(RAW_ASSETS + [star_wars_db, characters_enriched], resources={"swapi": swapi})
    assert result.success

    df = result.output_for_node("characters_enriched").set_index("character_name")
    assert df.loc["Matched", "homeworld"] == "Tatooine"
    # the orphan's row survives with NULL planet columns — dropped rows would
    # silently shrink every downstream denominator
    assert "Orphan" in df.index
    assert pd.isna(df.loc["Orphan", "homeworld"])


def _flyer(name: str, films: list, starships: list, birth_year: str = "unknown") -> dict:
    record = _person(name, "https://swapi.info/api/planets/1")
    record["films"] = films
    record["starships"] = starships
    record["birth_year"] = birth_year
    return record


def test_character_stats_counts_arrays_and_keeps_person_grain(isolated_cwd):
    film_urls = [f"https://swapi.info/api/films/{i}" for i in range(1, 7)]
    ship = "https://swapi.info/api/starships/1"
    swapi = InlineSWAPIResource(
        data={
            "people": [
                _flyer("Grounded", films=[], starships=[]),
                _flyer("Cameo", films=film_urls[:1], starships=[ship]),
                _flyer("Ever-Present", films=film_urls, starships=[]),
            ]
        }
    )
    result = materialize(RAW_ASSETS + [star_wars_db, character_stats], resources={"swapi": swapi})
    assert result.success

    df = result.output_for_node("character_stats")
    # one row per person, no matter how many films or ships they touch
    assert list(df["character_name"]) == sorted(df["character_name"])
    assert len(df) == 3

    indexed = df.set_index("character_name")
    # empty arrays must count as 0, not NULL — a zero-film extra is still a row
    assert indexed.loc["Grounded", "film_count"] == 0
    assert indexed.loc["Grounded", "starships_flown"] == 0
    assert indexed.loc["Cameo", "film_count"] == 1
    assert indexed.loc["Cameo", "starships_flown"] == 1
    assert indexed.loc["Ever-Present", "film_count"] == 6
    assert indexed.loc["Ever-Present", "starships_flown"] == 0


def test_birth_year_parse_covers_every_format_branch(isolated_cwd):
    # the snapshot contains zero ABY records, so without this synthetic test
    # the sign branch is dead code (decision 2026-07-19)
    swapi = InlineSWAPIResource(
        data={
            "people": [
                _flyer("Plain", [], [], birth_year="19BBY"),
                _flyer("Fractional", [], [], birth_year="41.9BBY"),
                _flyer("PostYavin", [], [], birth_year="5ABY"),
                _flyer("Undated", [], [], birth_year="unknown"),
                _flyer("Garbage", [], [], birth_year="a long time ago"),
            ]
        }
    )
    result = materialize(RAW_ASSETS + [star_wars_db, character_stats], resources={"swapi": swapi})
    assert result.success

    df = result.output_for_node("character_stats").set_index("character_name")
    assert df.loc["Plain", "birth_year_bby"] == 19.0
    assert df.loc["Fractional", "birth_year_bby"] == pytest.approx(41.9)
    # ABY records sit after Yavin: negative in BBY terms, never displayed signed
    assert df.loc["PostYavin", "birth_year_bby"] == -5.0
    # 'unknown' and unparseable strings become NULL, never zero
    assert pd.isna(df.loc["Undated", "birth_year_bby"])
    assert pd.isna(df.loc["Garbage", "birth_year_bby"])
