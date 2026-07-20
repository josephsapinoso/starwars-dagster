---
name: panel-qa-engineer-second-source-guards
description: Guard slate for integrating a SECOND upstream data source (new resource + raw asset + join transform) into the two-layer pytest/asset-check system without weakening existing pins. Use when reviewing the akabab integration or any future extra-source proposal (vehicles exercise excepted).
---

# Guarding a second upstream source (designed for akabab, 2026-07-20)

Principle: a second source doubles the drift surface but must not double the
framework. Same two layers — pytest proves the CODE offline, asset checks judge
the DATA — extended, never forked.

## 1. Independent snapshot markers, dual gating

Each source gets its OWN fixture dir and its OWN `SNAPSHOT.json` marker written
by `scripts/snapshot_fixtures.py`. Never merge markers: the sources refresh
independently, and `tests/test_site_data.py` substring-matches the swapi
marker's shape (do not touch it). Gating rule:
- facts about source B alone → gated on B's marker;
- facts about the JOIN (match count, deceased count) → gated on BOTH markers.
Plumbing checklist (all verified gaps in this repo): snapshot script fetches the
new endpoint; `snapshot.yml` `git add` gains the new fixture dir (it currently
adds only `tests/fixtures/swapi`); the workflow's full-suite step then IS the CI
for a refreshed pair.

## 2. Baselines are computed at freeze, never transcribed

Survey/brief numbers (record counts, field sparsity) are hearsay until the
fixture is frozen — my two WebFetch passes on akabab returned conflicting
sparsity counts. Every `EXPECTED_*` constant for the new source is COMPUTED from
the committed fixture in the freeze commit (script or one-off, results into
known_facts.py), then guarded by the WARN drift checks. Hand-copying a brief
number into known_facts is the seed of a lying badge.

## 3. Join guards: grain is blocking, coverage is WARN, aliases are proven

- BLOCKING grain check on the join asset: rows == left-source count AND join key
  unique. This is what stops silent LEFT-JOIN fan-out when the right source
  gains a duplicate normalized name. Seen-to-fail via an Inline resource pair
  with duplicate names.
- WARN coverage check: unmatched names BOTH directions in metadata — misses are
  drift, not breakage.
- Curated alias map (no fuzzy matching, ever) lives in known_facts and gets an
  UNGATED pytest invariant: aliasing+normalization must stay injective — no two
  right-source records may map to one left-source name. Real trap that motivates
  it: akabab and SWAPI both carry "Darth Vader" and "Anakin Skywalker" as
  SEPARATE records; a careless Vader→Anakin alias would merge them.

## 4. Ripples with existing guards (know which are automatic)

- Site totals triple: `test_totals_match_the_real_definitions` introspects real
  defs — automatic same-commit enforcement, no new pin needed.
- Listed-provenance pin: each LISTED asset's check set is pinned exactly → new
  checks attach only to UNLISTED assets until a site-surfacing panel.
- New warehouse writer (`CREATE OR REPLACE TABLE`) → add to the writers list in
  `test_warehouse_access_policy_is_encoded_in_code`; EXPECTED_DB_TABLES does NOT
  grow and `star_wars_db_tables_populated` does NOT assert downstream tables.
- Spoiler pin scans only claim-chain checks — unsurfaced assets' strings don't
  render, but write them spoiler-safe now (numbers only via known_facts
  interpolation) so surfacing later is a rail change, not a rewrite.
- README/WORKSHOP counts: NO automated pin exists — human checklist, same commit.

## 5. SURFACING a second source on the site (which pins break)

When the pipeline already carries the source and the question is putting it on
`site/index.html`, the cost is a function of PLACEMENT (verified 2026-07-20):

- **Dashboard card (mirror `#card-registry` / `registryChart`):** cheapest. Card
  numbers compute from inline DATA at render, disclose via `DATA.sql.<key>`, and
  are guarded by the census drift detector + the SQL execute/compare layer. NO
  provenance-claim, NO live check badge. Touches nothing in the beat/kicker/
  claims machinery. This is the birth-registry precedent — reach for it first.
- **New scroll beat:** reopens settled 8-step geometry and breaks, in one commit,
  ALL of: `test_story_has_a_real_heading_outline` (`== 8` kickers),
  `test_claims_cover_exactly_beats_one_through_six`, the runtime
  `beats !== "1,2,3,4,5,6"` string, and any hand-typed "six of its numbers"
  handoff literal (make it `WORDS[P.claims.length]`, self-verifying). Append the
  beat; inserting before beat 4 shifts `test_beats_four_through_six...`.

Extensions required for EITHER placement if a number renders:
- Every displayed number derivable from inline JSON → add per-record flags to
  DATA (not just an aggregate) and extend a drift detector to recompute it.
- New SQL chart → key into `SQL_KEYS` AND `DATA.sql`, AND the module `warehouse`
  fixture must materialize the new source's assets + inject its Fake resource,
  or the UNGATED execute test fails on a missing table (expected, per §2/§4 of
  the sql skill). Compare test recomputes from DATA arrays; signed-unit display
  gets a `> 0`-style pin.
- Provenance-listing the new assets triggers the assets/edges/checks-are-real
  test: deps exact, ALL checks listed, blocking + `why`-verbatim.
- Add a `payoff_terms[N]` spoiler entry from known_facts so the new source's
  numbers can't appear on earlier rails (hard break only if the join asset is in
  a CLAIM chain; belt-and-suspenders otherwise).

Watch for UNGUARDED hand-copy: a hardcoded DAG-strip / aria-label / static prose
count is NOT pinned by any test and drifts from `totals` silently. Surfacing is
the moment to render it from `DATA.provenance` or add a strip-vs-provenance pin —
that pin is the guard that lands with the feature.

## 6. Unit traps

Cross-source fields sharing a concept but not a unit (akabab meters/kg vs SWAPI
cm/kg-string) are excluded from the join output unless a unit pin ships with
them (positive-BBY style compare-test assertion). Presence-derived counts (has
`died` key) are NOT parses — one WARN baseline suffices; the two-guard
failure-mode-separation law applies only when a field is parsed into a displayed
number.
