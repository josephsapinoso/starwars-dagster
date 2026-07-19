"""
Displayed SQL is executed SQL.

The dashboard's "Show the DuckDB SQL" disclosures render strings from
DATA.sql in site/index.html. This file is the guard the 2026-07-18
post-landing-cleanup decision demanded: every one of those strings is
EXECUTED against a warehouse built by the real pipeline (ungated — a string
that cannot run is broken no matter what the data says), and its result rows
are COMPARED to the rows the charts derive from the inline DATA (snapshot-
gated, because only the real fixture snapshot matches the page's numbers).

History: before this guard existed, three of the five displayed strings were
wrong — two queried a table that didn't exist in the warehouse and one
measured the string length of a JSON array. Hand verification is how that
happened; execution is how it stops happening.
"""

import json
import re
from pathlib import Path

import duckdb
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
)
from tests.conftest import SNAPSHOT_MARKER, FakeSWAPIResource

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site" / "index.html"

SQL_KEYS = ["films", "gender", "scatter", "homeworlds", "hyper", "ages"]

requires_real_snapshot = pytest.mark.skipif(
    not SNAPSHOT_MARKER.exists(),
    reason="fixtures are synthetic; run scripts/snapshot_fixtures.py to enable",
)


@pytest.fixture(scope="module")
def data():
    html = SITE.read_text(encoding="utf-8")
    m = re.search(r"^const DATA = (\{.*\});$", html, re.M)
    assert m, "one-line `const DATA = {...};` literal missing (load-bearing format)"
    return json.loads(m.group(1))


@pytest.fixture(scope="module")
def warehouse(tmp_path_factory, monkeypatch_module):
    """The real pipeline builds the DuckDB the strings run against."""
    cwd = tmp_path_factory.mktemp("site_sql_run")
    monkeypatch_module.chdir(cwd)
    result = materialize(
        [raw_films, raw_people, raw_planets, raw_starships, raw_species,
         star_wars_db, characters_enriched, character_stats],
        resources={"swapi": FakeSWAPIResource()},
    )
    assert result.success
    return cwd / "data" / "star_wars.duckdb"


@pytest.fixture(scope="module")
def monkeypatch_module():
    from _pytest.monkeypatch import MonkeyPatch

    mp = MonkeyPatch()
    yield mp
    mp.undo()


def run_sql(warehouse, sql: str):
    con = duckdb.connect(str(warehouse), read_only=True)
    try:
        return con.execute(sql).fetchall()
    finally:
        con.close()


# ── Layer 1: EXECUTE (ungated — broken SQL is broken on any data) ───────────

def test_data_sql_has_exactly_the_chart_entries(data):
    assert "sql" in data, "DATA.sql missing — the site would render empty disclosures"
    assert sorted(data["sql"]) == sorted(SQL_KEYS)
    for k in SQL_KEYS:
        assert data["sql"][k].strip(), f"DATA.sql.{k} is empty"


def test_no_inline_sql_strings_remain_in_the_page():
    # single-source law: the only home for displayed SQL is DATA.sql
    html = SITE.read_text(encoding="utf-8")
    assert "const sql = `" not in html, (
        "an inline SQL template literal crept back into a chart IIFE — "
        "displayed SQL must live in DATA.sql where tests execute it"
    )


@pytest.mark.parametrize("key", SQL_KEYS)
def test_every_displayed_string_executes_against_the_warehouse(data, warehouse, key):
    rows = run_sql(warehouse, data["sql"][key])
    assert rows, f"DATA.sql.{key} executed but returned no rows"


def test_displayed_sql_carries_no_unverified_count_comments(data):
    # the old `-- 59 of 82 rows` comment drifted silently; counts belong in
    # query results or on-card copy derived from DATA, never in SQL comments
    for k in SQL_KEYS:
        assert not re.search(r"--.*\d", data["sql"][k]), (
            f"DATA.sql.{k} contains a numeric comment — an unexecutable claim"
        )


# ── Layer 2: COMPARE (snapshot-gated — results must equal the chart rows) ───

@requires_real_snapshot
def test_films_sql_reproduces_the_films_chart(data, warehouse):
    rows = run_sql(warehouse, data["sql"]["films"])
    expected = [
        (f["title"], f["episode"], f["characters"], f["starships"])
        for f in data["films"]
    ]
    assert [(r[0], int(r[1]), r[2], r[3]) for r in rows] == expected


@requires_real_snapshot
def test_gender_sql_reproduces_the_gender_chart(data, warehouse):
    counts = {}
    for p in data["people"]:
        counts[p["gender"]] = counts.get(p["gender"], 0) + 1
    expected = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    assert [(r[0], r[1]) for r in run_sql(warehouse, data["sql"]["gender"])] == expected


@requires_real_snapshot
def test_scatter_sql_reproduces_the_scatter_points(data, warehouse):
    rows = run_sql(warehouse, data["sql"]["scatter"])
    expected = {
        (p["name"], p["height"], float(p["mass"]))
        for p in data["people"]
        if p["height"] and p["mass"]
    }
    assert {(r[0], r[1], float(r[2])) for r in rows} == expected


@requires_real_snapshot
def test_homeworlds_sql_reproduces_the_top_ten(data, warehouse):
    counts = {}
    for p in data["people"]:
        if p["homeworld"]:
            counts[p["homeworld"]] = counts.get(p["homeworld"], 0) + 1
    expected = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:10]
    assert [(r[0], r[1]) for r in run_sql(warehouse, data["sql"]["homeworlds"])] == expected


@requires_real_snapshot
def test_ages_sql_reproduces_the_birth_registry(data, warehouse):
    # positive-BBY form is pinned here: a signed year in the result set would
    # falsify the unit on display (decision 2026-07-19)
    rows = run_sql(warehouse, data["sql"]["ages"])
    expected = sorted(
        (
            (p["name"], float(p["birthYear"][:-3]))
            for p in data["people"]
            if p["birthYear"]
        ),
        key=lambda r: (-r[1], r[0]),
    )
    assert [(r[0], float(r[1])) for r in rows] == expected
    assert all(r[1] > 0 for r in rows)


@requires_real_snapshot
def test_hyper_sql_reproduces_the_leaderboard(data, warehouse):
    ships = [s for s in data["starships"] if s["hyperdrive"] is not None]
    ships.sort(key=lambda s: (s["hyperdrive"], -(s["mglt"] or 0), s["name"]))
    expected = [(s["name"], float(s["hyperdrive"])) for s in ships[:10]]
    rows = run_sql(warehouse, data["sql"]["hyper"])
    assert [(r[0], float(r[3])) for r in rows] == expected
