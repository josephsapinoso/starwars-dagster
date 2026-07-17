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
