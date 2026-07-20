"""
Internal consistency of the site's inline DATA payload.

DATA ships the same fact at two grains in two places (a planet's resident
count and the people who name it home; a starship's pilot-edge count and each
person's starshipsFlown). Redundant grains can silently disagree with zero
warning — these tests and the runtime cross-foot detector are the guard.

Also pins the freshness line: DATA.meta must match the committed fixture
snapshot's identity, so the site can never claim a vintage it wasn't
verified against.
"""

import json
import re
from collections import Counter
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site" / "index.html"
SNAPSHOT = REPO / "tests" / "fixtures" / "swapi" / "SNAPSHOT.json"


@pytest.fixture(scope="module")
def data():
    html = SITE.read_text(encoding="utf-8")
    m = re.search(r"^const DATA = (\{.*\});$", html, re.M)
    assert m, "one-line `const DATA = {...};` literal missing (load-bearing format)"
    return json.loads(m.group(1))


def test_planet_residents_cross_foot_with_people(data):
    homeworlds = Counter(p["homeworld"] for p in data["people"] if p["homeworld"])
    for planet in data["planets"]:
        assert planet["residents"] == homeworlds.get(planet["name"], 0), (
            f"{planet['name']} lists {planet['residents']} residents but "
            f"{homeworlds.get(planet['name'], 0)} people call it home"
        )


def test_pilot_edges_cross_foot_with_starships_flown(data):
    edges = sum(s["pilots"] for s in data["starships"])
    flown = sum(p["starshipsFlown"] for p in data["people"])
    assert edges == flown


def test_species_members_divergence_is_the_known_swapi_quirk(data):
    # species[].members counts raw SWAPI species->people links; people[].species
    # was inferred at authoring for the 32 people whose raw species list is
    # empty (SWAPI under-links Human: 4 raw links vs 36 inferred). The two
    # grains measure different things, so they must NOT be pinned equal —
    # but the divergence must stay exactly this one, or something new drifted.
    members = {s["name"]: s["members"] for s in data["species"]}
    derived = Counter(p["species"] for p in data["people"] if p.get("species"))
    diverged = sorted(
        name
        for name in set(members) | set(derived)
        if members.get(name, 0) != derived.get(name, 0)
    )
    assert diverged == ["Human"], (
        f"species/people divergence changed: {diverged} — the only sanctioned "
        "mismatch is Human (raw SWAPI under-linking)"
    )


def test_meta_matches_the_committed_snapshot(data):
    snap = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    assert data["meta"]["snapshot"] == snap["fetched_at"][:10]
    assert data["meta"]["source"] in snap["source"]


def test_words_renderer_covers_every_spelled_count(data):
    # The provenance closer spells pipeline counts as words (WORDS[n]). A count
    # that outgrows the lookup table renders "undefined checks" with only a
    # console.warn to show for it — so the table must cover every count DATA
    # can ask it to spell. Caught nearly happening when checks went 15 → 20.
    html = SITE.read_text(encoding="utf-8")
    m = re.search(r"const WORDS = \[([^\]]*)\];", html)
    assert m, "WORDS lookup table missing from the provenance renderer"
    words = [w.strip().strip('"') for w in m.group(1).split(",")]
    totals = data["provenance"]["totals"]
    for key in ("assets", "transforms", "checks"):
        assert totals[key] < len(words), (
            f"WORDS stops at {words[-1]!r} but totals.{key}={totals[key]} — "
            "grow the array in the same commit as the count"
        )
