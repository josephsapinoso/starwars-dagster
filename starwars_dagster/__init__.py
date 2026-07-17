"""
Star Wars Dagster Pipeline
==========================
The Definitions object is the single entry point Dagster reads.
It wires together assets, resources, schedules, and jobs.
"""

from dagster import (
    Definitions,
    load_asset_checks_from_modules,
    load_assets_from_modules,
)

from starwars_dagster import assets as assets_module
from starwars_dagster.assets import checks as checks_module
from starwars_dagster.resources import SWAPIResource
from starwars_dagster.schedules import (
    daily_refresh_schedule,
    analytics_only_job,
    full_pipeline_job,
)

# Automatically discover all @asset-decorated functions in the assets package
all_assets = load_assets_from_modules([assets_module])

# ... and every @asset_check in checks.py (they render on the lineage graph)
all_checks = load_asset_checks_from_modules([checks_module])

defs = Definitions(
    assets=all_assets,
    asset_checks=all_checks,
    resources={
        # The key "swapi" matches the parameter name in assets that need it
        "swapi": SWAPIResource(),
    },
    schedules=[daily_refresh_schedule],
    jobs=[full_pipeline_job, analytics_only_job],
)
