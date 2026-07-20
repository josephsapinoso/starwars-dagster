"""
Layer 1: Ingestion Assets
=========================
These assets pull raw data from the sources and save it as JSON files.

Key Dagster concept — "Software-Defined Assets" (SDAs):
  An asset is a piece of data your pipeline produces and tracks.
  You define WHAT the data is, not just the steps to make it.
  Dagster builds the execution graph automatically from dependencies.

Asset lineage here:
  SWAPIResource ───► raw_films
                ───► raw_people
                ───► raw_planets
                ───► raw_starships
                ───► raw_species
  AkababResource ──► raw_character_profiles
"""

import json
import pathlib
from dagster import asset, AssetExecutionContext

from starwars_dagster.resources.akabab_resource import AkababResource
from starwars_dagster.resources.swapi_resource import SWAPIResource

# Where to store raw JSON dumps
RAW_DIR = pathlib.Path("data/raw")


def _save_json(name: str, data: list[dict]) -> pathlib.Path:
    """Save a list of records to data/raw/<name>.json and return the path."""
    # mkdir at write time, not import time — the path is cwd-relative, so an
    # import-time mkdir would pin the directory to whatever cwd loaded the module
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DIR / f"{name}.json"
    path.write_text(json.dumps(data, indent=2))
    return path


# ── Asset group keeps these together in the Dagster UI ──────────────────────
_GROUP = "01_raw"


@asset(group_name=_GROUP, description="All Star Wars films from SWAPI")
def raw_films(context: AssetExecutionContext, swapi: SWAPIResource) -> list[dict]:
    """
    Fetch every Star Wars film from the API.

    The `swapi` parameter is automatically injected by Dagster from resources.
    `context` gives us logging and metadata helpers.
    """
    films = swapi.fetch("films")

    # Log a metadata preview in the Dagster UI
    context.add_output_metadata({"record_count": len(films), "titles": [f["title"] for f in films]})

    _save_json("films", films)
    return films


@asset(group_name=_GROUP, description="All Star Wars characters from SWAPI")
def raw_people(context: AssetExecutionContext, swapi: SWAPIResource) -> list[dict]:
    people = swapi.fetch("people")
    context.add_output_metadata({"record_count": len(people)})
    _save_json("people", people)
    return people


@asset(group_name=_GROUP, description="All Star Wars planets from SWAPI")
def raw_planets(context: AssetExecutionContext, swapi: SWAPIResource) -> list[dict]:
    planets = swapi.fetch("planets")
    context.add_output_metadata({"record_count": len(planets)})
    _save_json("planets", planets)
    return planets


@asset(group_name=_GROUP, description="All Star Wars starships from SWAPI")
def raw_starships(context: AssetExecutionContext, swapi: SWAPIResource) -> list[dict]:
    starships = swapi.fetch("starships")
    context.add_output_metadata({"record_count": len(starships)})
    _save_json("starships", starships)
    return starships


@asset(group_name=_GROUP, description="All Star Wars species from SWAPI")
def raw_species(context: AssetExecutionContext, swapi: SWAPIResource) -> list[dict]:
    species = swapi.fetch("species")
    context.add_output_metadata({"record_count": len(species)})
    _save_json("species", species)
    return species


@asset(
    group_name=_GROUP,
    description="Character profiles from the akabab dataset (second source)",
)
def raw_character_profiles(
    context: AssetExecutionContext, akabab: AkababResource
) -> list[dict]:
    """
    Fetch the full akabab character-profile dump — same pattern as the five
    SWAPI pulls, different resource. The profiles enrich the SWAPI census
    (affiliations, apprenticeships, deaths on file) via a name join in
    the character_biographies transform.
    """
    profiles = akabab.fetch("all")
    context.add_output_metadata({"record_count": len(profiles)})
    _save_json("character_profiles", profiles)
    return profiles
