"""
Akabab Resource — wraps the akabab/starwars-api character dataset.

A second, independent data source next to SWAPIResource: fan-curated character
profiles served as static JSON from GitHub Pages (MIT licensed). Same resource
pattern, different endpoint shape — akabab serves files (`/all.json`), not
trailing-slash API routes, which is why this is its own class and not a
SWAPIResource subclass.
"""

import requests
from dagster import ConfigurableResource, get_dagster_logger


class AkababResource(ConfigurableResource):
    """
    A Dagster resource for akabab/starwars-api
    (https://akabab.github.io/starwars-api/api).

    The dataset is static and effectively frozen — the practical failure mode
    is the host disappearing, not data drift. Committed fixtures plus the
    blocking shape check on raw_character_profiles cover that.
    """

    base_url: str = "https://akabab.github.io/starwars-api/api"
    timeout_seconds: int = 30

    def fetch(self, endpoint: str) -> list[dict]:
        """
        Fetch a list endpoint, e.g. fetch("all") -> GET {base_url}/all.json.

        Akabab list endpoints return a plain JSON array. Anything else is a
        contract break and raises rather than being silently coerced.
        """
        log = get_dagster_logger()
        url = f"{self.base_url}/{endpoint}.json"
        log.info(f"Fetching {url}")

        response = requests.get(url, timeout=self.timeout_seconds)
        response.raise_for_status()

        data = response.json()
        if not isinstance(data, list):
            raise ValueError(
                f"Expected a JSON array from /{endpoint}.json, "
                f"got {type(data).__name__}"
            )

        log.info(f"Got {len(data)} records from /{endpoint}.json")
        return data
