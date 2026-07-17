"""
Shared test plumbing.

Two ideas carry the whole suite:

1. FakeSWAPIResource — Dagster resources are injected, so swapping the real
   HTTP client for one that reads committed fixture JSON gives us the entire
   pipeline offline. No test in this suite ever touches the network.

2. isolated_cwd — the pipeline writes data/ relative to the working directory,
   so each test runs in its own tmp_path and can never clobber real artifacts.
"""

import json
import pathlib

import pytest

from starwars_dagster.resources.swapi_resource import SWAPIResource

FIXTURE_DIR = pathlib.Path(__file__).parent / "fixtures" / "swapi"

# Written by scripts/snapshot_fixtures.py when the fixtures are a real, dated
# SWAPI snapshot rather than the synthetic defaults. Gates the banked-facts tests.
SNAPSHOT_MARKER = FIXTURE_DIR / "SNAPSHOT.json"


class FakeSWAPIResource(SWAPIResource):
    """Reads tests/fixtures/swapi/<endpoint>.json instead of calling the API."""

    fixture_dir: str = str(FIXTURE_DIR)

    def fetch(self, endpoint: str) -> list[dict]:
        path = pathlib.Path(self.fixture_dir) / f"{endpoint}.json"
        return json.loads(path.read_text())


@pytest.fixture
def fake_swapi() -> FakeSWAPIResource:
    return FakeSWAPIResource()


@pytest.fixture
def isolated_cwd(tmp_path, monkeypatch) -> pathlib.Path:
    monkeypatch.chdir(tmp_path)
    return tmp_path


def load_fixture(endpoint: str) -> list[dict]:
    return json.loads((FIXTURE_DIR / f"{endpoint}.json").read_text())
