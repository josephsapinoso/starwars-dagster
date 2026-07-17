"""
Refresh tests/fixtures/swapi/ with a real, dated snapshot of swapi.info.

Run this once from a machine with network access:

    python scripts/snapshot_fixtures.py

It overwrites the synthetic fixture files with the live API responses and
writes SNAPSHOT.json (source, timestamp, record counts). The presence of
SNAPSHOT.json activates the banked-facts tests in tests/test_pipeline.py —
so after running this, `pytest` also verifies the real-world numbers
(82 people, 3 six-film characters, 23 unknown masses, Naboo 11/Tatooine 10).

Commit the refreshed fixtures: they are the frozen dataset every exact
assertion refers to, and their date is the provenance of every published number.
"""

import datetime
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from starwars_dagster.resources.swapi_resource import SWAPIResource

ENDPOINTS = ["films", "people", "planets", "starships", "species"]
FIXTURE_DIR = pathlib.Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "swapi"


def main() -> None:
    swapi = SWAPIResource()
    counts = {}
    for endpoint in ENDPOINTS:
        records = swapi.fetch(endpoint)
        (FIXTURE_DIR / f"{endpoint}.json").write_text(json.dumps(records, indent=2))
        counts[endpoint] = len(records)
        print(f"  {endpoint}: {len(records)} records")

    marker = {
        "source": swapi.base_url,
        "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "record_counts": counts,
    }
    (FIXTURE_DIR / "SNAPSHOT.json").write_text(json.dumps(marker, indent=2))
    print(f"Wrote {FIXTURE_DIR / 'SNAPSHOT.json'} — banked-facts tests are now active.")


if __name__ == "__main__":
    main()
