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

- Inventory (post-082d9c9): 11 assets, 4 transforms, 12 checks in `assets/checks.py`.
  Blocking (4) — `raw_people_has_required_shape`, `star_wars_db_tables_populated`,
  `films_are_exactly_the_six_episodes`, `characters_enriched_has_no_null_names`.
  WARN (8) — `raw_people_count_matches_verified_snapshot`,
  `characters_enriched_join_coverage`, `characters_enriched_unknown_mass_baseline`,
  `starship_stats_cast_sanity`, plus four `character_stats` drift baselines:
  `character_stats_one_film_baseline` (42), `character_stats_six_film_trio`
  (C-3PO/R2-D2/Obi-Wan), `character_stats_pilot_count_baseline` (19),
  `character_stats_max_flown_baseline` (5).
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
  would have been coverage theater. My condition if it landed: checks asserting
  42-of-82, the trio, 19-of-82, maxFlown 5, with beats 4–6 flipping to DIRECT and
  test updates in the same commit. [SATISFIED — see Banked: per-character-transform
  landed, below.]

Prep-differently next time: my prep verified mechanics but took the brief's
beat→asset map on faith until the analyst falsified parts of it. For any brief that
asserts a data→claim mapping, spot-check the mapping itself against the raw data
during PREP, not just the machinery. Also: when I want scope (SQL migration), arrive
with the verification design in hand — objections without a detector design get
deferred.

## Banked: per-character-transform landed (2026-07-18, commit 082d9c9)

Execution note: `.claude/panel/decisions/2026-07-18-per-character-transform-landed.md`.
No new debate — the open item shipped directly against my banked acceptance criteria,
and I verified in-repo that every condition was honored:

- New `character_stats` asset (`star_wars_db` → per-person `film_count`,
  `starships_flown`, feeds `galaxy_report`); four WARN drift checks assert exactly
  42-of-82, the trio, 19-of-82, maxFlown 5. Correct severity call: exact-value
  baselines are drift, never blocking. `known_facts.py` unchanged — baselines were
  already banked there; single-home law held.
- Same-commit condition honored in full: beats 4–6 flipped to `relation:"direct"` +
  `guard.kind:"check"` alongside the provenance pin
  `test_beats_four_through_six_are_direct_and_check_guarded`, grain/zero-count
  behavior tests via `InlineSWAPIResource` (tests/test_transforms.py), and a
  snapshot-gated test asserting the four WARN evaluations PASS
  (`test_character_stats_drift_checks_pass_on_the_real_snapshot`) — necessary
  because WARN cannot fail a materialize, so green must be asserted explicitly.
- Negative check performed and reported: perturbing `EXPECTED_ONE_FILM_COUNT` made
  both the check-passing test and the banked-facts pytest fail, then was reverted.
  "Seen to fail" standard met.
- Bonus catches vindicating the drift detector: beat-7 number-word array stopped at
  "nine" (12 checks would have rendered "undefined checks"; detector now warns on
  word-list overflow), and stale "three transforms" copy fixed in prose + aria label.
  Lesson: any count rendered through a lookup table needs an overflow guard.
- `raw_starships` dropped from the provenance map because no claim cites it anymore —
  correct under guard-honesty law: provenance lists what claims cite, not the whole DAG.

Still OPEN (unchanged): the five hand-written dashboard SQL strings in `makeCard`
remain unverified copy — keep resisting any new hand-written pipeline copy, and next
time I raise migration I bring a concrete verification design. README screenshot
retake also still open (needs 12 green checks, desktop UI).

## Prep notes: post-landing cleanup — trio leak / SQL verification / coverage gaps (2026-07-18)

Verified in-repo (not taken on faith this time):

- **Data-engineer's SQL audit is TRUE.** transforms.py `star_wars_db` creates ONLY
  `films/people/planets/starships/species`; list fields are `json.dumps`-stringified.
  So chart 2 (index.html:1047) and chart 4 (:1184) `FROM characters_enriched` fail —
  no such table. Chart 1 (:985) `len(f.characters)` = string length of stringified
  JSON, not array length (transform correctly uses `json_array_length`). Charts 3
  (:1102) and 5 (:1224) hit real tables and use DuckDB lateral-alias-in-WHERE
  (supported); plausibly correct — only execution proves it. 3 of 5 displayed SQL
  strings are wrong TODAY. This is the exact failure my open item predicted.
- **Q2 spec (mine, full design in skill panel-qa-engineer-sql-verification):** SQL
  strings move into `DATA.sql` (map chart-id → string; `\n` fine in strict JSON);
  site renders only from DATA. New pytest reuses the existing `full_run` fixture
  (materialize all assets via FakeSWAPIResource in isolated_cwd), then connects
  read_only to the `data/star_wars.duckdb` the pipeline itself wrote — never a
  bespoke DB or test-created views (that would verify SQL against a warehouse that
  doesn't exist). Two layers: ungated EXECUTE (catches charts 2/4 class), and
  snapshot-gated compare of results vs DATA-derived expectations (catches chart 1
  class). SNAPSHOT.json IS present, so gated tests run locally. Inline SQL comments
  citing counts (`-- 59 of 82 rows`, :1105) must equal the executed row count.
  Runtime detector grows one internal-consistency claim only: rendered sql
  disclosures ↔ DATA.sql keys, 1:1, non-empty. It cannot execute SQL (no DuckDB-wasm
  under one-file/no-CDN law) — don't pretend otherwise.
- **Charts 2/4 fix is data-engineer's choice, my test is fix-agnostic:** either
  re-author SQL against real tables, or persist transform outputs back into DuckDB
  and keep `FROM characters_enriched`. Both pass the same execute-and-compare test.
- **Q1:** verbatim-projection law binds site strings to checks.py `description=`,
  not the wording — both label and description are ours to re-author (option a).
  Names appear in check runtime metadata regardless (Dagster UI, ops-facing, fine).
  Rendering-rule filter (option b) forks rail truth from Dagster truth — veto lens.
  Pin for (a): existing test_site_provenance forces same-commit site sync; add a
  spoiler pin — for every claim with beat < 5, union of its assets' check
  labels+whys in DATA.provenance contains no member of `SIX_FILM_CHARACTERS` (import
  from known_facts — single source) and no "trio"/count-of-three phrasing. Purely
  offline, mechanical. Note: description :218 also names the "'Ben counts' beat" —
  re-author that too.
- **Q3(a)** height baseline WARN on characters_enriched guards a DISPLAYED number
  (beat 1 "1 unmeasured"), mirrors the mass baseline exactly, baseline already at
  known_facts.py:26 → earns its place. Same-commit costs: beat-1 guard flips
  pytest→check in DATA.provenance, totals.checks 12→13, and WORDS (:798) ends at
  "twelve" — 13 overflows; extend WORDS or beat 7 warns. **Q3(b)** galaxy_report has
  a REAL unnamed failure mode: live data yielding an empty section writes a
  half-empty report while everything shows green (pytest report tests are
  fixture-only). A thin BLOCKING structural check (file written, expected section
  headers present, tables non-empty) is a guard, not decoration — but it guards the
  report artifact, not a site number; no site claim cites galaxy_report, so no
  provenance change. Weak-yes; won't spend a veto on it.
- Cannot verify offline: whether charts 3/5 results match DATA exactly (needs the
  execute-and-compare test to exist) and actual rendered spoiler surface on a real
  phone hover (title-attr hover is desktop-only; label is the mobile leak).
