"""
Refresh tests/fixtures/ with real, dated snapshots of BOTH sources.

Run this once from a machine with network access:

    python scripts/snapshot_fixtures.py

It overwrites the synthetic fixture files with the live responses and writes a
SNAPSHOT.json marker per source (source, timestamp, record counts). The two
sources refresh in one run on purpose: the cross-source baselines (join
coverage, deaths on file) are only meaningful against a coherent pair.

Marker effects:
  tests/fixtures/swapi/SNAPSHOT.json  — activates the SWAPI banked-facts tests
  tests/fixtures/akabab/SNAPSHOT.json — activates the akabab banked-facts tests;
                                        cross-source tests need BOTH markers

The script also computes the second-source baselines against the fixtures it
just froze and prints them next to the values currently in known_facts.py —
baselines are frozen from this computation, never transcribed from a survey.
The dual-gated pytest layer re-verifies whatever lands in known_facts.py
against these same fixtures, so a stale paste fails the suite, not the reader.

Commit the refreshed fixtures: they are the frozen dataset every exact
assertion refers to, and their date is the provenance of every published number.
"""

import datetime
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from starwars_dagster import known_facts
from starwars_dagster.assets.transforms import _normalize_name
from starwars_dagster.known_facts import PROFILE_NAME_ALIASES
from starwars_dagster.resources.akabab_resource import AkababResource
from starwars_dagster.resources.swapi_resource import SWAPIResource

ENDPOINTS = ["films", "people", "planets", "starships", "species"]
AKABAB_ENDPOINTS = ["all"]
FIXTURES = pathlib.Path(__file__).resolve().parents[1] / "tests" / "fixtures"
FIXTURE_DIR = FIXTURES / "swapi"
AKABAB_FIXTURE_DIR = FIXTURES / "akabab"


def _write_marker(directory: pathlib.Path, source: str, counts: dict) -> None:
    marker = {
        "source": source,
        "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "record_counts": counts,
    }
    (directory / "SNAPSHOT.json").write_text(json.dumps(marker, indent=2))
    print(f"Wrote {directory / 'SNAPSHOT.json'}")


def _report_baseline(name: str, computed: int) -> None:
    current = getattr(known_facts, name)
    tag = "OK" if computed == current else f"UPDATE known_facts.py (currently {current})"
    print(f"  {name} = {computed}  [{tag}]")


def main() -> None:
    swapi = SWAPIResource()
    counts = {}
    for endpoint in ENDPOINTS:
        records = swapi.fetch(endpoint)
        (FIXTURE_DIR / f"{endpoint}.json").write_text(json.dumps(records, indent=2))
        counts[endpoint] = len(records)
        print(f"  swapi/{endpoint}: {len(records)} records")
    _write_marker(FIXTURE_DIR, swapi.base_url, counts)

    akabab = AkababResource()
    akabab_counts = {}
    AKABAB_FIXTURE_DIR.mkdir(parents=True, exist_ok=True)
    for endpoint in AKABAB_ENDPOINTS:
        records = akabab.fetch(endpoint)
        (AKABAB_FIXTURE_DIR / f"{endpoint}.json").write_text(json.dumps(records, indent=2))
        akabab_counts[endpoint] = len(records)
        print(f"  akabab/{endpoint}: {len(records)} records")
    _write_marker(AKABAB_FIXTURE_DIR, akabab.base_url, akabab_counts)

    # ── Second-source baselines, computed from the pair just frozen ──────────
    people = json.loads((FIXTURE_DIR / "people.json").read_text())
    profiles = json.loads((AKABAB_FIXTURE_DIR / "all.json").read_text())
    census = {_normalize_name(p["name"]) for p in people}
    matched = [
        rec
        for rec in profiles
        if _normalize_name(PROFILE_NAME_ALIASES.get(rec["name"], rec["name"])) in census
    ]
    unmatched_profiles = sorted(
        r["name"]
        for r in profiles
        if _normalize_name(PROFILE_NAME_ALIASES.get(r["name"], r["name"])) not in census
    )
    matched_keys = {
        _normalize_name(PROFILE_NAME_ALIASES.get(r["name"], r["name"])) for r in matched
    }
    unmatched_census = sorted(
        p["name"] for p in people if _normalize_name(p["name"]) not in matched_keys
    )

    print("\nSecond-source baselines (computed from the frozen pair):")
    _report_baseline("EXPECTED_PROFILE_COUNT", len(profiles))
    _report_baseline("EXPECTED_PROFILE_MATCH_COUNT", len(people) - len(unmatched_census))
    _report_baseline("EXPECTED_DEATHS_ON_FILE", sum(1 for r in matched if "died" in r))
    if unmatched_census:
        print(f"  census names with no profile: {unmatched_census}")
        print("  (candidates for PROFILE_NAME_ALIASES — curate, never fuzzy-match)")
    if unmatched_profiles:
        print(f"  profiles with no census row: {unmatched_profiles}")

    print("Banked-facts tests are now active for both sources.")


if __name__ == "__main__":
    main()
