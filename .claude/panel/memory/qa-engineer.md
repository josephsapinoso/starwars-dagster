# QA / Data Quality Engineer — Panel Memory

## Settled (do not relitigate)

- Two-layer guard: pytest proves the CODE offline against committed fixtures; Dagster
  `@asset_check`s judge the DATA at materialization. Structural breakage = ERROR /
  `blocking=True`; upstream drift = WARN — SWAPI is not ours to freeze. (Testing
  panel, PR #3.)
- Verified baselines live once in `starwars_dagster/known_facts.py`, imported by both
  tests and checks. (Testing panel, PR #3.)
- Behavior tests craft their own records via `InlineSWAPIResource`
  (tests/conftest.py) and must NEVER depend on shared fixture content; only the
  banked-facts tests read the frozen snapshot, gated on `SNAPSHOT.json` being present.
  (Testing panel, PR #3.)
- `scripts/snapshot_fixtures.py` refreshes the snapshot (also via the `snapshot.yml`
  workflow — remote dev containers may not reach swapi.info; GitHub runners can).
  CI (`ci.yml`) is offline-only. (Testing panel, PR #3.)
- No second data-quality framework (no Great Expectations/Pandera), no coverage
  gates, no CI matrix. Dagster-native checks + one green workflow carry the signal.
  (Testing panel, PR #3.)
- Every number on the site is guarded by the runtime drift detector; data-vs-copy
  divergence must warn, not silently ship. (First design panel.)

## Working knowledge

- The 8 checks in `assets/checks.py`: blocking — `raw_people_has_required_shape`,
  `star_wars_db_tables_populated`, `films_are_exactly_the_six_episodes`,
  `characters_enriched_has_no_null_names`; WARN —
  `raw_people_count_matches_verified_snapshot`,
  `characters_enriched_join_coverage`,
  `characters_enriched_unknown_mass_baseline`, `starship_stats_cast_sanity`.
- Failure modes with named detectors today: SWAPI shape change (shape check), count
  drift (count/mass baselines), join rot (coverage check), cast rot (TRY_CAST
  sanity), copy drift on the site (runtime detector). New site claims must extend one
  of these, not bypass them.
- A feature and its guard land in the same commit; "verified" means an automated
  detector exists and has been seen to fail when the guarded thing breaks.

## Prep notes: pipeline-reveal (2026-07-17)

Verified myself, in-repo (Dagster 1.13.14):

- Offline graph introspection WORKS: `from starwars_dagster import defs` is
  network-free (SWAPIResource is constructed, never called).
  `defs.resolve_asset_graph()` → `graph.get(key).parent_keys` yields the true
  edge list; `defs.asset_checks[*].check_specs` yields `(asset_key, name,
  blocking)`. Confirmed output matches the brief's DAG and the 4/4
  blocking/non-blocking split. This is the ground truth the provenance
  cross-check test must compare against — never a hand-copied edge list.
- CRITICAL nuance: WARN severity is a *runtime* `AssetCheckResult(severity=...)`
  argument and is NOT statically introspectable. `spec.blocking` IS. In this repo
  blocking ⇔ ERROR and non-blocking ⇔ WARN by discipline, so provenance badges
  must be derived from `spec.blocking`, and the pytest cross-check asserts
  badge-severity == f(blocking). Hand-typed severity labels are banned.
- `const DATA = {...};` at site/index.html:378 is one-line strict JSON —
  extractable with a regex + `json.loads`. NO test currently reads
  site/index.html (grepped tests/: zero matches), so the promised cross-check
  test is precedent-free new surface; it must fail with a clear message if the
  literal stops being one-line strict JSON (that formatting is now load-bearing).
- Bad precedent to not repeat: the five dashboard SQL reveals are hand-written
  strings in `makeCard` (~848–854) — unverified copy. Provenance must be data
  rendered from `DATA.provenance`, one schema for beats AND any dashboard
  parity; no second hand-drawn diagram path.
- Runtime drift detector (481–497) checks 8 stats + the trio; it can only check
  *internal* consistency (beats ↔ provenance entries ↔ badge enum), not truth
  vs. Dagster — truth is pytest's job offline. Split the duty exactly there.
- What I cannot verify mechanically: the *semantic* beat→asset attribution
  (beat 2 ← characters_enriched etc.) is a human claim — analyst/owner review;
  pytest can only prove cited assets/edges/checks are real and correctly typed.
- New failure modes needing named detectors: (a) refactor changes real DAG,
  provenance stale → pytest cross-check; (b) DATA extraction regex rots →
  same test, loud message; (c) blocking flag flipped in checks.py without site
  update → same test; (d) beat added without provenance → runtime detector warn
  + pytest coverage-set assertion.
- Skill written: `.claude/skills/panel-qa-engineer-provenance-verification/SKILL.md`
  (introspection recipes + DATA extraction snippet).
