"""
SWAPI Resource — wraps the Star Wars API (swapi.info).

In Dagster, a "resource" is a shared, configurable connection to an external system.
Think of it like a database connection or API client you inject into your assets.
"""

import requests
from dagster import ConfigurableResource, get_dagster_logger


class SWAPIResource(ConfigurableResource):
    """
    A Dagster resource for the Star Wars API (https://swapi.info/api).

    Using a resource instead of raw requests.get() calls means:
    - One place to change the base URL or auth headers
    - Easy to swap for a mock in tests
    - Dagster tracks it as a dependency
    """

    base_url: str = "https://swapi.info/api"
    timeout_seconds: int = 30

    def fetch(self, endpoint: str) -> list[dict]:
        """
        Fetch all records from a SWAPI endpoint.

        swapi.info returns a plain JSON array (no pagination needed),
        so this is a single GET call.

        Args:
            endpoint: e.g. "films", "people", "planets"

        Returns:
            List of record dicts
        """
        log = get_dagster_logger()
        url = f"{self.base_url}/{endpoint}/"
        log.info(f"Fetching {url}")

        response = requests.get(url, timeout=self.timeout_seconds)
        response.raise_for_status()

        data = response.json()

        # swapi.info returns a list directly; guard in case it ever wraps in {"results": [...]}
        if isinstance(data, list):
            records = data
        else:
            records = data.get("results", data)

        log.info(f"Got {len(records)} records from /{endpoint}/")
        return records
