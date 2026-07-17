"""
Transform-layer tests: the two places data is lost on purpose.

TRY_CAST and the homeworld LEFT JOIN both swallow bad values silently by
design — these tests pin down exactly what "silently" means so a future
change can't widen the loss unnoticed.
"""

import pandas as pd
import pytest
from dagster import materialize

from starwars_dagster.assets import (
    raw_films,
    raw_people,
    raw_planets,
    raw_species,
    raw_starships,
    star_wars_db,
    starship_stats,
)

UPSTREAM = [raw_films, raw_people, raw_planets, raw_starships, raw_species, star_wars_db]


@pytest.fixture
def starship_df(isolated_cwd, fake_swapi):
    result = materialize(UPSTREAM + [starship_stats], resources={"swapi": fake_swapi})
    assert result.success
    return result.output_for_node("starship_stats")


def test_unknown_hyperdrive_rating_becomes_null_not_zero(starship_df):
    jedi = starship_df[starship_df["name"] == "Jedi starfighter"].iloc[0]
    assert pd.isna(jedi["hyperdrive_rating"])


def test_range_and_comma_crew_strings_become_null_not_a_guess(starship_df):
    by_name = starship_df.set_index("name")
    # "30-165" is a range, "342,953" has a separator — TRY_CAST must refuse both
    assert pd.isna(by_name.loc["CR90 corvette", "crew_size"])
    assert pd.isna(by_name.loc["Death Star", "crew_size"])
    # while plain integers survive the cast
    assert by_name.loc["Millennium Falcon", "crew_size"] == 4


def test_parseable_numeric_strings_are_cast_faithfully(starship_df):
    falcon = starship_df[starship_df["name"] == "Millennium Falcon"].iloc[0]
    assert falcon["hyperdrive_rating"] == 0.5
    assert falcon["length_m"] == pytest.approx(34.37)
