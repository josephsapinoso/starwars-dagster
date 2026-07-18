"""
The site's provenance claims must match the real Dagster definitions.

site/index.html renders per-beat "paper trail" reveals from DATA.provenance.
This file is the honesty guard: every asset, dependency edge, check name,
blocking flag, and rationale string in that object is verified against
starwars_dagster's actual Definitions — offline, no network, no new deps.

The one-line strict-JSON format of the `const DATA = {...};` literal is
load-bearing: these tests parse it with a regex and must fail loudly if
the formatting ever changes.
"""

import json
import re
from pathlib import Path

import pytest

from starwars_dagster import defs
from starwars_dagster.known_facts import (
    EXPECTED_MAX_STARSHIPS_FLOWN,
    EXPECTED_PEOPLE_COUNT,
    EXPECTED_PILOT_COUNT,
    EXPECTED_UNKNOWN_MASS_COUNT,
    SIX_FILM_CHARACTERS,
)

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site" / "index.html"
TESTS_DIR = REPO / "tests"

VALID_RELATIONS = {"direct", "derived"}
VALID_GUARD_KINDS = {"check", "pytest", "none"}


@pytest.fixture(scope="module")
def prov():
    html = SITE.read_text(encoding="utf-8")
    m = re.search(r"^const DATA = (\{.*\});$", html, re.M)
    assert m, (
        "site/index.html no longer contains a one-line `const DATA = {...};` "
        "literal. That formatting is load-bearing — these tests parse it. "
        "Restore the single-line strict-JSON form."
    )
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as exc:  # pragma: no cover - message matters
        pytest.fail(f"const DATA is no longer strict JSON: {exc}")
    assert "provenance" in data, "DATA.provenance is missing from the site"
    return data["provenance"]


@pytest.fixture(scope="module")
def real():
    graph = defs.resolve_asset_graph()
    keys = {k.to_user_string() for k in graph.get_all_asset_keys()}
    parents = {
        k.to_user_string(): {p.to_user_string() for p in graph.get(k).parent_keys}
        for k in graph.get_all_asset_keys()
    }
    groups = {
        k.to_user_string(): graph.get(k).group_name
        for k in graph.get_all_asset_keys()
    }
    checks = {}
    for checks_def in defs.asset_checks:
        for spec in checks_def.check_specs:
            checks[(spec.asset_key.to_user_string(), spec.name)] = spec
    return {"keys": keys, "parents": parents, "groups": groups, "checks": checks}


def test_provenance_assets_edges_and_checks_are_real(prov, real):
    for aid, entry in prov["assets"].items():
        assert aid in real["keys"], f"provenance names unknown asset {aid!r}"
        assert set(entry["deps"]) == real["parents"][aid], (
            f"provenance deps for {aid} diverge from the real graph: "
            f"{sorted(entry['deps'])} vs {sorted(real['parents'][aid])}"
        )
        real_names = {n for (a, n) in real["checks"] if a == aid}
        listed = {c["name"] for c in entry["checks"]}
        assert listed == real_names, (
            f"checks listed for {aid} diverge from the real definitions: "
            f"{sorted(listed)} vs {sorted(real_names)}"
        )
        for c in entry["checks"]:
            spec = real["checks"][(aid, c["name"])]
            assert c["blocking"] == bool(spec.blocking), (
                f"{c['name']}: provenance says blocking={c['blocking']} but the "
                f"real spec says {spec.blocking} — severity derives from this flag"
            )
            assert c["why"] == spec.description, (
                f"{c['name']}: provenance 'why' is not a verbatim projection of "
                f"the check's description= in checks.py"
            )
            assert c["label"], f"{c['name']}: display label must be non-empty"
            assert len(c["label"]) <= 20, f"{c['name']}: display label too long"


def test_claims_cover_exactly_beats_one_through_six(prov):
    assert sorted(c["beat"] for c in prov["claims"]) == [1, 2, 3, 4, 5, 6]


def test_claims_are_honest(prov, real):
    test_source = "\n".join(
        p.read_text(encoding="utf-8") for p in TESTS_DIR.glob("test_*.py")
    )
    for c in prov["claims"]:
        beat = c["beat"]
        assert c["relation"] in VALID_RELATIONS, f"beat {beat}: bad relation"
        assert c["guard"]["kind"] in VALID_GUARD_KINDS, f"beat {beat}: bad guard kind"
        for aid in c["assets"]:
            assert aid in prov["assets"], f"beat {beat}: chain names unlisted asset {aid}"
        assert c["hot"] in c["assets"], f"beat {beat}: hot asset not in its own chain"

        if c["relation"] == "direct":
            # a direct chain must be a true dependency path in the Dagster graph
            for up, down in zip(c["assets"], c["assets"][1:]):
                assert up in real["parents"][down], (
                    f"beat {beat}: {up} → {down} is not a real dependency edge"
                )
        else:
            # a derived claim must never wear a check badge as its guard —
            # no asset computes the number, so no check can assert it
            assert c["guard"]["kind"] != "check", (
                f"beat {beat}: derived claims cannot be guarded by an asset check"
            )

        if c["guard"]["kind"] == "check":
            ref = c["guard"]["ref"]
            assert any((aid, ref) in real["checks"] for aid in c["assets"]), (
                f"beat {beat}: guard check {ref!r} is not attached to any asset "
                f"in this claim's chain"
            )
        elif c["guard"]["kind"] == "pytest":
            ref = c["guard"]["ref"]
            assert re.search(rf"^def {re.escape(ref)}\(", test_source, re.M), (
                f"beat {beat}: guard cites pytest {ref!r} but no such test exists"
            )


def test_beats_four_through_six_are_direct_and_check_guarded(prov):
    # Banked acceptance criteria for the per-character transform (decision log
    # 2026-07-18): once character_stats lands, beats 4-6 stop being derived
    # page-authoring math. Pin the upgrade so it can't silently regress.
    expected_guards = {
        4: "character_stats_one_film_baseline",
        5: "character_stats_six_film_trio",
        6: "character_stats_pilot_count_baseline",
    }
    claims = {c["beat"]: c for c in prov["claims"]}
    for beat, guard_ref in expected_guards.items():
        c = claims[beat]
        assert c["relation"] == "direct", f"beat {beat} regressed to derived"
        assert c["guard"] == {"kind": "check", "ref": guard_ref}
        assert c["hot"] == "character_stats"
        assert "character_stats" in c["assets"]


def test_no_payoff_leaks_before_reveal_beat(prov):
    # The spoiler pin (panel decision 2026-07-18-post-landing-cleanup): every
    # beat's rail renders ALL checks of its chain assets, so a check string
    # naming a later beat's payoff pre-tells the story. Term sets are DERIVED
    # from known_facts — never hand-listed — so they survive cast changes.
    payoff_terms = {
        # beat 2's payoff: the unweighed count
        2: {
            f"{EXPECTED_UNKNOWN_MASS_COUNT} unweighed",
            f"{EXPECTED_UNKNOWN_MASS_COUNT} of {EXPECTED_PEOPLE_COUNT}",
        },
        # beat 5's payoff: who (and how many) appear in all six films
        5: {name.lower() for name in SIX_FILM_CHARACTERS} | {"trio", "ben counts"},
        # beat 6's payoff: the pilot count and the max-flown record holder
        6: {
            f"{EXPECTED_PILOT_COUNT} pilot",
            f"max flown = {EXPECTED_MAX_STARSHIPS_FLOWN}",
            f"flown {EXPECTED_MAX_STARSHIPS_FLOWN}",
            "obi-wan",
        },
    }
    for claim in prov["claims"]:
        beat = claim["beat"]
        visible = " • ".join(
            f'{c["label"]} {c["why"]}'
            for aid in claim["assets"]
            for c in prov["assets"][aid]["checks"]
        ).lower()
        for reveal_beat, terms in payoff_terms.items():
            if reveal_beat <= beat:
                continue
            for term in terms:
                assert term.lower() not in visible, (
                    f"beat {beat} rail pre-tells beat {reveal_beat}'s payoff: "
                    f"{term!r} appears in a check label/why rendered there"
                )


def test_totals_match_the_real_definitions(prov, real):
    totals = prov["totals"]
    assert totals["assets"] == len(real["keys"])
    transforms = [
        a for a, g in real["groups"].items()
        if g == "02_transformed" and a != "star_wars_db"
    ]
    assert totals["transforms"] == len(transforms)
    assert totals["checks"] == len(real["checks"])
    chain_checks = sum(len(e["checks"]) for e in prov["assets"].values())
    assert chain_checks <= totals["checks"]
