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
- `DATA.provenance` is the single source for every provenance/severity string on the
  site; badge severity derives from `spec.blocking` (never hand-typed — WARN is
  runtime-only in Dagster); check rationales are verbatim projections of checks.py
  `description=`. Verified by `tests/test_site_provenance.py` against
  `defs.resolve_asset_graph()` + `check_specs`, same commit as the feature.
  (Pipeline-reveal panel, 2026-07-18.)
- Guard honesty: a check badge may only appear where the check asserts the displayed
  number (or its denominator/structure, labeled as such); derived/unguarded claims
  say so in plain words (`relation: direct|derived`, `guard.kind: check|pytest|none`;
  `guard.kind=pytest` refs must name real tests). No fabricated or implied live
  status, ever. (Pipeline-reveal panel, 2026-07-18.)
- Reveals exist on beats 1–6 only; beat 0 clean; beat 7 = provenance-computed callback
  whose counts must match the object. Coverage set asserted exactly by pytest AND the
  runtime detector's internal-consistency pass. (Pipeline-reveal panel, 2026-07-18.)
- The one-line strict-JSON format of `const DATA` in site/index.html is load-bearing:
  tests parse it and must fail LOUDLY if the format changes. (Pipeline-reveal panel,
  2026-07-18.)
- Duty split: pytest proves provenance TRUTH offline (real assets/edges/checks,
  blocking flags, verbatim descriptions); the runtime detector proves only INTERNAL
  consistency (beats ↔ claims ↔ badge enum ↔ callback counts). Neither does the
  other's job. (Pipeline-reveal panel, 2026-07-18.)

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

## Prep notes: pipeline-reveal (2026-07-17, compacted after banking)

Durable residue not yet promoted to Settled (most of the original notes are now law
above; introspection recipes + DATA extraction snippet live in the skill
`.claude/skills/panel-qa-engineer-provenance-verification/SKILL.md`):

- `from starwars_dagster import defs` is network-free (SWAPIResource constructed,
  never called) — safe ground truth for offline tests. Never hand-copy an edge list.
- Limit of mechanical verification: the *semantic* beat→asset attribution is a human
  claim (analyst/owner review); pytest can only prove cited assets/edges/checks are
  real and correctly typed. This limit surfaced the false beat map in prep — worth
  stating explicitly in any future provenance-style brief.
- Bad precedent still live: the five dashboard SQL reveals in `makeCard` (~848–854)
  are hand-written unverified strings. Migration into a verified home is an OPEN item
  (decision log) — resist any new hand-written pipeline copy meanwhile.

## Banked: pipeline-reveal (2026-07-18)

What won (essentially my whole debate slate):

- `tests/test_site_provenance.py` adopted as specced: one test file asserting
  topology vs `resolve_asset_graph()`, check ownership, blocking-derived badges,
  verbatim `description=` projection, exact 1–6 coverage set, honest guard typing
  (derived/none never render an asserting check badge), real pytest refs. Same
  commit as the feature — the standing law held without a fight.
- My WARN-is-runtime-only finding drove adjudication item 2's phrasing and killed
  hand-typed severity labels; badges derive from `spec.blocking` (now Settled).
- One-line strict-JSON DATA format declared load-bearing with loud-failure
  requirement — exactly my prep framing.
- The pytest-truth / runtime-internal-consistency duty split adopted verbatim.
- No second diagram path: HTML `.chip` reuse rendered from `DATA.provenance`
  (item 4) also serves my "data, not hand-drawn copy" objection.

What lost / was overruled, and why I accept it:

- I did not get dashboard-SQL migration into scope: deferred (item 6) as surface
  growth "without a verification story for SQL text" — fair; it stays an open item
  and I should bring a concrete verification story next time, not just the smell.
- Hiring-manager's beat-0 reveal lost to structure I can verify: `raw_people` heads
  every chain, so the census guards appear in all six reveals. Testable claim; fine.
- Analyst's per-character transform deferred on merits, not laziness — the honest
  `derived` labeling is the correct QA outcome; a transform added as diagram fuel
  would have been coverage theater. If the open item lands, its checks must assert
  42-of-82, the trio, 19-of-82, maxFlown 5 — and beats 4–6 flip to DIRECT with test
  updates in the same commit.

Prep-differently next time: my prep verified mechanics but took the brief's
beat→asset map on faith until the analyst falsified parts of it. For any brief that
asserts a data→claim mapping, spot-check the mapping itself against the raw data
during PREP, not just the machinery. Also: when I want scope (SQL migration), arrive
with the verification design in hand — objections without a detector design get
deferred.
