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
- Displayed SQL is executed SQL: any SQL text shown on the site lives in `DATA.sql`
  and is executed against the fixture-built warehouse by the offline suite
  (tests/test_site_sql.py); no hand-verified SQL copy anywhere; SQL comments carry no
  numbers (an unexecutable claim). (Post-landing cleanup, 2026-07-18.)
- Write-back one-code-path: `characters_enriched` persists via
  `CREATE OR REPLACE TABLE ... AS SELECT * FROM df` on the SAME df the asset returns,
  guarded by test_pipeline.py::test_characters_enriched_table_matches_the_returned_frame
  (assert_frame_equal). `EXPECTED_DB_TABLES` stays five and
  `star_wars_db_tables_populated` must NOT grow — asserting a downstream asset's
  table from an upstream check is an ordering lie. (Post-landing cleanup, 2026-07-18.)
- Spoiler pin law: a standing offline test
  (test_site_provenance.py::test_no_payoff_leaks_before_reveal_beat) derives payoff
  term sets from known_facts — names AND payoff numbers, phrase-anchored — and
  asserts no check string renders on a beat earlier than its claim's reveal; new
  checks pass the spoiler audit before landing; seen-to-fail before merge.
  (Post-landing cleanup, 2026-07-18.)
- Provenance carries no narrative fields: everything in `DATA.provenance` stays
  derivable from / verifiable against the real Dagster definitions plus known_facts.
  Hand-authored beat indices and story metadata are unverifiable surface — vetoed.
  (Post-landing cleanup, 2026-07-18.)
- The rail is uniform: every beat renders the same rule — all checks of its chain
  assets; spoiler safety lives in the STRINGS, not the renderer. Description style
  rule (technical-writer's): descriptions state the invariant and stakes; run
  metadata carries particulars; known_facts.py is the only roster/number home; no
  check string quotes another beat's caption or payoff. (Post-landing cleanup,
  2026-07-18.)
- galaxy_report stays check-free BY DESIGN: a check there pre-solves WORKSHOP
  Exercise 8 and duplicates pytest coverage. The gap is deliberately disclosed, not
  an oversight — don't re-propose it. (Post-landing cleanup, 2026-07-18.)
- Failure-mode separation law: a displayed number derived through a parse gets TWO
  guards — a drift baseline (WARN, snapshot-gated green assertion) and a
  data-independent parse-honesty invariant asserted UNGATED (must hold on synthetic
  fixtures too). "The data moved" and "the parser broke" must fail differently;
  one check conflating them lets the headline lie under a glowing badge.
  (Birth-registry panel, 2026-07-19, 7–1.)
- Absence pins are legitimate guards: an element exempted from a detector by a
  property (number-free, spoiler-free) gets a pin asserting that PROPERTY
  (test_the_coda_stays_number_free); pinning wording is theater. (2026-07-19, 5–3.)
- Warehouse access policy is encoded in code: pure-read transforms open
  `read_only=True`, every writer is declared, the executor is pinned in-process —
  test_pipeline.py::test_warehouse_access_policy_is_encoded_in_code. character_stats
  is ratified as the SECOND declared writer; EXPECTED_DB_TABLES stays five,
  `star_wars_db_tables_populated` did not grow, the write-back parity test loops
  BOTH writers. (2026-07-19.)
- Quoted-testimony rule: external claims (dialogue, canon) may be audited in copy
  but never rendered as site-derived data; derived numbers come only from DATA.
  WORKSHOP.md is on the count-ripple checklist; teaching prose stays count-free
  unless the count is the lesson. (2026-07-19.)

## Working knowledge

- Inventory (post-f170379, 2026-07-19): 11 assets, 4 transforms, 15 checks —
  4 blocking (`raw_people_has_required_shape`, `star_wars_db_tables_populated`,
  `films_are_exactly_the_six_episodes`, `characters_enriched_has_no_null_names`),
  11 WARN: people count, join coverage, unknown-mass, unknown-height (beat 1's
  "1 unmeasured"), cast sanity, four character_stats drift baselines (one-film 42,
  six-film trio, pilots 19, max flown 5), plus `character_stats_birth_year_baseline`
  (undated + oldest vs known_facts) and `character_stats_birth_year_parse_honesty`
  (parsed NULLs == raw `'unknown'` strings, via `additional_ins` on star_wars_db,
  read_only connect). Grep trap: checks.py's docstring mentions `@asset_check` and
  `blocking=True`, so grep counts read 16/5 — always introspect check_specs.
- SQL guard file map (tests/test_site_sql.py): `SQL_KEYS` is six —
  films/gender/scatter/homeworlds/hyper/ages. Ungated layer —
  `test_data_sql_has_exactly_the_chart_entries` (renamed count-free; asserts
  key set == SQL_KEYS), the no-inline-SQL pin, the execute test (parametrized over
  SQL_KEYS), the no-numeric-comments pin; snapshot-gated layer — six
  `test_*_sql_reproduces_the_*` compare tests; the ages one also pins positive-BBY
  (`all(r[1] > 0)` — a signed year would falsify the displayed unit). Warehouse =
  module-scoped fixture, pipeline-built, read_only connect.
- Failure modes with named detectors: SWAPI shape change (shape check), count drift
  (count/mass/height/birth baselines), parse breakage (parse-honesty, ungated),
  join rot (coverage check), cast rot (TRY_CAST sanity), copy drift on site
  (runtime detector), SQL rot (execute layer), SQL computing the wrong thing or
  DATA edited without SQL (compare layer), spoiler regression in check strings
  (spoiler pin), coda regressing into numbers (digits absence pin), writer/reader
  lock race (access-policy test + in-process executor pin). New site claims must
  extend one of these, not bypass them.
- A feature and its guard land in the same commit; "verified" means an automated
  detector exists and has been seen to fail when the guarded thing breaks.
- `from starwars_dagster import defs` is network-free (SWAPIResource constructed,
  never called) — safe ground truth for offline tests. Never hand-copy an edge list.
- Semantic beat→asset attribution is a human claim; pytest proves only that cited
  assets/edges/checks are real and correctly typed. Spot-check asserted data→claim
  mappings against raw data during PREP.
- Any count rendered through a lookup table (e.g. the WORDS number-word list) needs
  an overflow guard; check-count ripples touch WORDS, beat-7 callback, README,
  CLAUDE.md, provenance totals — all same commit.

## Banked: pipeline-reveal + per-character-transform (2026-07-18, compacted)

test_site_provenance.py adopted as specced (topology vs resolve_asset_graph, badge =
f(blocking), verbatim descriptions, exact coverage set, honest guard typing).
character_stats landed against my banked acceptance criteria in full: four WARN
baselines, beats 4–6 flipped direct+check same commit, snapshot-gated
green-assertion test (WARN can't fail a materialize, so green must be asserted),
negative check performed. Lesson kept: objections without a detector design get
deferred — bring the verification design in hand.

## Banked: post-landing cleanup (2026-07-18, commits c0b97e0 + 2aa845e)

Decision log: `.claude/panel/decisions/2026-07-18-post-landing-cleanup.md`.

Won nearly the whole slate: write-back one-code-path + EXPECTED_DB_TABLES-stays-five
became law verbatim; execute-and-compare shipped as test_site_sql.py (unanimous —
arrived with the full detector design as a skill, not a smell); Q1 re-authoring won
on the one-home law + "a `beat` field is unverifiable attribution" (now the
no-narrative-fields law); galaxy_report retraction bought credibility. Amendments
accepted: spoiler pin covers payoff NUMBERS too (seen-to-fail via "trio" reinsert);
test_site_sql builds its own module-scoped warehouse instead of reusing full_run
(same principle, less coupling). Lessons kept: verify other roles' audits in-repo
during PREP; every new WARN check needs a "what asserts green?" answer.

## Banked: birth registry + polish (2026-07-19)

Decision log: `.claude/panel/decisions/2026-07-19-birth-registry-and-polish.md`.
Commits: 1f3cf9e (registry) · 4d92cb7 (coda + hues) · 7d96df5 (limits) · f170379
(screenshots at 15 green — the open item from last bank is CLOSED).

My rulings WERE the adjudication: two-checks won 7–1 (failure-mode separation now
law); the coda digits-pin stood 5–3 as an absence assertion; the guard slate shipped
nearly item-for-item (known_facts constants, subject-only descriptions, gated green
assertion for the baseline, UNGATED parse-honesty assertion, synthetic parse pytest
for ABY/fractional/garbage/unknown, DATA.sql.ages through both layers with the
positive-BBY pin, drift-detector claims, spoiler terms extended and seen-to-fail via
a "Yoda" label leak + baseline bump).

Deviation ratified: the execute layer caught character_stats' displayed table
missing mid-implementation, forcing it to become the SECOND declared writer. My
condition held — EXPECTED_DB_TABLES stays five, tables_populated did not grow, the
parity test loops both writers. This also resolved my prep item 2 (lock race) by a
DIFFERENT design than I specced: instead of an execute_job-under-multiprocess
detector, the policy itself is encoded (readers read_only, writers declared,
executor pinned in_process via test_warehouse_access_policy_is_encoded_in_code).
Accepted: pinning the executor makes the racy mode unreachable, and any future
executor swap fails the test first — cheaper than my detector and equally named.
The stale "one writer" comment nit was fixed same day.

BANK-pass verification habit that paid off: grep said 16 checks / 5 blocking; truth
is 15/4 (docstring mentions). Introspect check_specs, never grep counts.

Prep-differently: when I spec a detector, also spec the acceptable POLICY
alternative (make the failure mode unreachable + pin the policy) — the panel may
land there, and pre-approving its conditions keeps my ruling intact.

## Ledger closure (2026-07-19, compacted)

Both open items CLOSED same-day: snapshot.yml now runs the FULL suite before the
bot commit (ea840fb, that step IS the CI for a refreshed snapshot); DATA.meta
freshness line pinned by test_site_data.py::test_meta_matches_the_committed_snapshot
(2e47baa). Lesson kept: an open-items ledger is a claim about the tree — re-verify
AT BANK TIME before writing "OPEN".

## Prep notes: second source — akabab (2026-07-20)

Verified the brief's repo claims myself; all held:
- Provenance pins: test_site_provenance.py:76-101 pins each LISTED asset's check
  set exactly (listed = raw_people, star_wars_db, characters_enriched,
  character_stats) → new checks MUST attach only to unlisted assets; the brief's
  slate (raw_character_profiles, character_biographies) complies. Totals pin
  (:242) introspects real defs, so the site totals triple 11/4/15 → 13/5/20 is
  FORCED same-commit by an existing guard — no new pin needed there.
- Spoiler pin scans only checks of assets in claim CHAINS; unlisted assets'
  strings never render until site surfacing. Write them spoiler-safe anyway;
  f-string interpolation FROM known_facts is the sanctioned number pattern.
- Access policy (test_pipeline.py:155-181): character_biographies (CREATE OR
  REPLACE TABLE) becomes the THIRD declared writer — must join the writers list
  same commit; EXPECTED_DB_TABLES stays five; tables_populated must not grow.
- Snapshot plumbing gaps confirmed: snapshot.yml:39 `git add tests/fixtures/swapi`
  only (must add akabab dir); snapshot_fixtures.py fetches swapi only; akabab
  needs its OWN marker (tests/fixtures/akabab/SNAPSHOT.json). test_site_data.py:23
  points SNAPSHOT at the swapi dir only — its substring shape is untouched.
- README/WORKSHOP counts have NO automated pin (grep tests/ for README: none) —
  count ripple there stays a human checklist item, same commit.

External verification (WebFetch, live all.json, 2026-07-20):
- 87 records = ids 1–88 with id 17 ABSENT — akabab ids mirror SWAPI's famous
  id-17 skip; sequel five are ids 84–88. Consistent with brief.
- Darth Vader (id 4) and Anakin Skywalker (id 11) are SEPARATE records in BOTH
  sources — exact-name join keeps them distinct. Alias-map guard must therefore
  assert injectivity: after normalize+alias, akabab names stay unique AND no
  alias maps two akabab records onto one SWAPI name (ungated pytest, synthetic-
  safe). Sole alias: "Ratts Tyerell"(akabab 47) → "Ratts Tyerel" (confirmed in
  our people.json fixture).
- Brief's sparsity figures (masters 15/87, died 47/87, mass 64/87) NOT
  confirmable — summarizer counted 17/30/80. Design-irrelevant IF all baselines
  (EXPECTED_PROFILE_COUNT, _MATCH_COUNT, _DECEASED_COUNT) are COMPUTED from the
  frozen fixture at the freeze commit, never hand-copied from the brief. I will
  make that a condition.
- Units confirmed: akabab height/mass are meters/kg (Luke 1.72/73) vs SWAPI cm —
  exclusion is right; any future inclusion needs a unit pin (positive-BBY style).

Debate ammunition:
- Every new check answers "what asserts green?" + seen-to-fail before merge:
  grain (blocking) → Inline duplicate-name akabab pair must FAIL it; shape
  (blocking) → record missing `name`; coverage WARN → unmatchable name metadata;
  count/deceased baselines → dual-marker-gated green assertions.
- Q3 lean: deceased-count via key PRESENCE is not a parse — one WARN drift
  baseline suffices; the two-guard failure-mode-separation law triggers only if
  born/died get PARSED into displayed ages later.
- Q4 lean: accept curated PROFILE_NAME_ALIASES in known_facts WITH the
  injectivity pytest; fuzzy matching stays vetoed.
- Fixture law extension: synthetic akabab fixture may reference real SWAPI NAMES
  (join must hit offline), but fixture-based tests assert structure/grain only;
  match-count exactness is gated on BOTH markers (brief's dual gate — correct).
