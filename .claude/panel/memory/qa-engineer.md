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
- Write-back one-code-path: every declared writer persists via
  `CREATE OR REPLACE TABLE ... AS SELECT * FROM df` on the SAME df the asset returns,
  guarded by the write-back parity test looping ALL writers. `EXPECTED_DB_TABLES`
  stays five and `star_wars_db_tables_populated` must NOT grow — asserting a
  downstream asset's table from an upstream check is an ordering lie. (2026-07-18.)
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
  assets; spoiler safety lives in the STRINGS, not the renderer. Descriptions state
  the invariant and stakes; run metadata carries particulars; known_facts.py is the
  only roster/number home; no check string quotes another beat's caption or payoff.
  (Post-landing cleanup, 2026-07-18.)
- galaxy_report stays check-free BY DESIGN: a check there pre-solves WORKSHOP
  Exercise 8 and duplicates pytest coverage. The gap is deliberately disclosed, not
  an oversight — don't re-propose it. (Post-landing cleanup, 2026-07-18.)
- Failure-mode separation law: a displayed number derived through a parse gets TWO
  guards — a drift baseline (WARN, snapshot-gated green assertion) and a
  data-independent parse-honesty invariant asserted UNGATED (must hold on synthetic
  fixtures too). "The data moved" and "the parser broke" must fail differently.
  (Birth-registry panel, 2026-07-19, 7–1.)
- Absence pins are legitimate guards: an element exempted from a detector by a
  property (number-free, spoiler-free) gets a pin asserting that PROPERTY
  (test_the_coda_stays_number_free); pinning wording is theater. (2026-07-19, 5–3.)
- Warehouse access policy is encoded in code: pure-read transforms open
  `read_only=True`, every writer is declared, the executor is pinned in-process —
  test_pipeline.py::test_warehouse_access_policy_is_encoded_in_code. (2026-07-19.)
- The `read_only` per-asset single-writer lock is enforced+source-tested law and
  `DuckDBResource` CANNOT express it: `get_connection()` hardcodes `read_only=False`
  with no per-connection override (stable Dagster 1.7–1.13). We keep raw
  `duckdb.connect()` deliberately; `dagster-duckdb` is NOT a dependency. Do not
  "modernize" without a panel. (Dagster-duckdb non-migration, 2026-07-21.)
- A deliberate technology NON-adoption is a guardable artifact, not just prose: pin
  a stable rationale marker in the source next to the invariant it protects (here
  `"DuckDBResource"`+`"read_only=False"` asserted present in transforms.py source by
  test_warehouse_access_policy_is_encoded_in_code), so a future refactor trips BOTH
  the invariant pin and the marker and must re-read the decision. Rationale home is
  WORKSHOP Module 10 (beside the "Why NOT Great Expectations" why-not). Kin to the
  absence-pin law: guard the PROPERTY/choice, not the wording. (2026-07-21.)
- Quoted-testimony rule: external claims (dialogue, canon) may be audited in copy
  but never rendered as site-derived data; derived numbers come only from DATA.
  WORKSHOP.md is on the count-ripple checklist; teaching prose stays count-free
  unless the count is the lesson. (2026-07-19.)
- Akabab second source lands as Option C (2026-07-20, unanimous): transform-join
  `character_biographies`; `star_wars_db` byte-identical, EXPECTED_DB_TABLES stays
  five, tables_populated does not grow; join misses surface via coverage-check
  metadata. Five checks (2 blocking: grain, shape; 3 WARN: coverage, count,
  deaths-on-file) is the CEILING for this feature.
- Enrichment-join numbers carry nested denominators (matched AND field-present) —
  report-copy discipline COMPUTED from the data, not new per-field checks.
  (2026-07-20.)
- Akabab death data is "deaths on file" vocabulary everywhere: check
  `character_biographies_deaths_on_file_baseline`, constant
  `EXPECTED_DEATHS_ON_FILE`; never "deceased". Key-presence is not a parse — one
  WARN guard suffices; the two-guard law wakes only if born/died get parsed for
  display. (2026-07-20.)
- Signed-year warehouse columns name their convention in the column name
  (`_bby`/`_aby`, e.g. `died_year_aby`); no bare year columns; no sign-convention
  asset check — naming + pytest suffice. (2026-07-20.)
- Alias governance: curated `PROFILE_NAME_ALIASES` in known_facts with a
  canon-direction comment per entry; ungated pytest asserts injectivity (Vader/
  Anakin stay distinct) AND every alias load-bearing (key ≠ value post-
  normalization); resolution-vs-fixture assertions dual-snapshot-gated; no fuzzy
  matching, ever. Aliases bridge joins; they never mutate as-filed records.
  (2026-07-20.)
- Cross-source derived figures (SWAPI birth × akabab death arithmetic, e.g. Yoda
  896+4=900) are quoted-testimony territory: pre-vetoed off all surfaces until a
  surfacing panel rules. (2026-07-20.)
- akabab surfaces as a `#card-biographies` dashboard card, NEVER a story beat: the
  census spine stays 8 steps / "n/8" (BUILDERS.length=8 untouched); the second source
  is a second READING, a dashboard act. Card carries NO check badge (a badge needs a
  claim entry; beats 1–6 machinery). Totals stay 13/5/20. (Surfacing panel, 2026-07-20.)
- akabab card numbers render from per-row `DATA.people[].bio` (nested object or null),
  never an aggregate blob; `bio` carries `diedOnFile` boolean — no signed year value
  ever enters the page. matched (82/82) & deaths-on-file (47/82) are drift-recomputable
  from `bio` AND pinned to known_facts by pytest; 75/14/12 are render-computed copy
  whose ONLY guard is the drift detector, explicitly labeled uncheckable, no badge.
  (Surfacing panel, 2026-07-20.)
- A ranked affiliations/faction chart is BANNED on the six-film site: `affiliations` is
  canon-wide/sequel-inclusive, so a ranked bar is a ranking claim the site can't
  honestly make. Only saga-safe coverage COUNTS surface. (Surfacing panel, 2026-07-20.)
- A displayed akabab SQL string returns coverage COUNTS only, never `died_year_aby`
  VALUES (dodges ABY-sign display + the pre-vetoed derivation). (Surfacing, 2026-07-20.)
- The DAG-strip chip set is a GUARDED surface: a new pytest pins the chip set to the
  real Dagster asset keys (chips stay HTML, ruled PIN not full render — same guarantee,
  less churn), so it can never silently contradict totals again. (Surfacing, 2026-07-20.)
- The site WORDS number-renderer is a guard surface: it grows (through "twenty")
  with a pytest pin (`len(WORDS)` exceeds every DATA-rendered count) in the same
  commit as any count it must spell. (2026-07-20.)
- Baselines for external-source facts are COMPUTED by script from the frozen fixture
  at the freeze commit — three independent surveys of akabab disagreed (87/88
  records; died 47/28); transcription is not a baseline method. (2026-07-20.)
- Seen-to-fail acceptance matrix before merge (akabab): grain check fails on an
  inline duplicate-name pair; shape check fails on a missing-`name` record; coverage
  WARN emits unmatched names both directions. README/WORKSHOP counts stay a human
  same-commit checklist — no prose grep pins. (2026-07-20.)
- Provenance-pin ripple law (governs ANY asset/check addition): site provenance
  totals (test_site_provenance.py L261-269) and the DAG-strip chip set (L242-258) are
  EQUALITY pins against introspected real defs; the per-asset check blob (L76-101) is
  a SUBSET pin. So ANY new asset KEY or `@asset_check` ripples the site's totals +
  DAG strip in the SAME commit by law — a pipeline change is NOT "site-free" unless it
  adds zero asset keys and zero checks. A new UNLISTED asset carrying checks passes the
  subset blob but STILL trips the two equality pins. (Production-pattern panel,
  2026-07-21.)
- No production-pattern-for-show: a partition / incremental / SCD / backfill asset is
  NOT added merely to signal scale. On a static, small, heterogeneous source lacking
  the pattern's dimension, the documented "Limits, by design" why-not is the stronger
  senior signal (extends the dagster-duckdb why-not principle from framework idioms to
  architectural patterns). Docs must not claim a capability the code lacks (schedules.py
  is a full refresh on a static source and says so). Revisit only if the source gains a
  real time axis or grows past re-pull scale. (Production-pattern panel, 2026-07-21.)

## Working knowledge

- Inventory (post-f170379): 11 assets, 4 transforms, 15 checks — 4 blocking, 11 WARN
  (people count, join coverage, unknown-mass/height, cast sanity, four
  character_stats drift baselines, birth-year baseline + UNGATED-principle
  parse-honesty via `additional_ins`, read_only connect). After akabab lands:
  13 assets, 5 transforms, 20 checks (6 blocking) — the equality pins (totals
  L261-269, DAG-strip L242-258; see provenance-pin ripple law in Settled) introspect
  real defs, so the site ripples same-commit automatically on any asset/check add.
  Grep trap: docstrings mention `@asset_check` / `blocking=True` — always introspect
  check_specs, never grep counts.
- Provenance pins (test_site_provenance.py:76-101) pin each LISTED asset's check set
  exactly → new checks must attach only to UNLISTED assets (raw_character_profiles,
  character_biographies comply). Spoiler pin scans only claim-chain assets; unlisted
  assets' strings never render until surfacing — write them spoiler-safe anyway.
- SQL guard file map (tests/test_site_sql.py): SQL_KEYS is six (films/gender/
  scatter/homeworlds/hyper/ages). Ungated layer — key-set pin, no-inline-SQL pin,
  execute test, no-numeric-comments pin; snapshot-gated layer — six compare tests;
  ages also pins positive-BBY. Warehouse = module-scoped pipeline-built fixture.
- Failure modes with named detectors: SWAPI shape change (shape check), count drift
  (baselines), parse breakage (parse-honesty, ungated), join rot (coverage), cast
  rot (TRY_CAST sanity), site copy drift (runtime detector), SQL rot (execute
  layer), wrong SQL / edited DATA (compare layer), spoiler regression (spoiler pin),
  coda numbers (absence pin), writer/reader race (access-policy test). New claims
  extend one of these, never bypass.
- A feature and its guard land in the same commit; "verified" means an automated
  detector exists and has been SEEN TO FAIL when the guarded thing breaks.
- `from starwars_dagster import defs` is network-free — safe ground truth offline.
  Never hand-copy an edge list. Semantic beat→asset attribution is a human claim;
  spot-check data→claim mappings against raw data during PREP.
- Akabab facts (verified live 2026-07-20): 87 records = ids 1–88 with id 17 absent
  (mirrors SWAPI's skip); sequel five are ids 84–88; Vader (4) and Anakin (11) are
  separate records in BOTH sources; sole alias "Ratts Tyerell"→"Ratts Tyerel";
  akabab height/mass are meters/kg vs SWAPI cm — any future numeric inclusion needs
  a unit pin (positive-BBY style). Snapshot plumbing must grow: snapshot.yml adds
  the akabab dir; snapshot_fixtures.py fetches it; akabab gets its OWN
  tests/fixtures/akabab/SNAPSHOT.json marker; character_biographies joins the
  declared-writers list (THIRD writer) same commit.

## Banked: production-pattern (STAND PAT) (2026-07-21)

Log: `.claude/panel/decisions/2026-07-21-production-pattern.md`. Outcome: no
partitioned/incremental/SCD asset shipped; change was copy-only (fix schedules.py
over-claim, sharpen "Limits, by design"). My endpoint-partition VOTE did not carry.

Won (durable, now Settled): my site-ripple READING was decisive and is banked as the
provenance-pin ripple law — totals + DAG-strip are EQUALITY pins, per-asset blob is
SUBSET, so any new asset key OR asset_check ripples the site same-commit. This governs
ALL future asset additions, not just this one.

Moot: my full production-pattern guard slate (partition roster/single-slice/backfill-
parity; SCD merge-correctness/idempotency/no-phantom-change/static-source-honesty;
two-guard separation for mechanism-vs-static). No asset shipped → no guard slate needed.
Kept as a DORMANT playbook only if a real time axis ever arrives — captured in skill
panel-qa-engineer-production-pattern-guards, not re-inlined here.

Lost correctly: endpoint partition was falsified by CODE SHAPE — the raw layer is FIVE
separate SDAs, so an "endpoint partition" collapses 5→1 (asset count 13→9, rewrites the
WORKSHOP Layer-1 lesson, changes star_wars_db's signature) and DOES ripple the site —
contradicting the "site-free" premise the partition majority (incl. me) rested on. On a
dimensionless snapshot every pattern is contrived.

Prep differently (the lesson): VERIFY THE TARGET ASSET'S GRAPH SHAPE before ruling any
change "site-free" or "contained." I reasoned about a hypothetical single partitioned
asset without confirming the raw layer was 5 assets; the containment premise was false.
Read the actual asset topology, not the mental model, before scoping ripple. Reinforces
the standing habit: introspect real defs, never a mental inventory.

## Banked: dagster-duckdb non-migration (2026-07-21)

Log: `.claude/panel/decisions/2026-07-21-dagster-duckdb-decision.md`. Outcome (A):
do NOT migrate. My position largely won.

Won: the `read_only` source-introspection pin stays UNCHANGED (Q3 — the contract is
LOST not relocated under `DuckDBResource`, which hardcodes `read_only=False`). My
prep-verified fact (no per-connection read_only override, stable 1.7–1.13) was the
external fact that decided the panel: IO-manager unanimously OUT (5 raw tables can't
map one-asset→one-table without reshaping the provenance graph), (C) subclass
unanimously vetoed (re-hand-rolls the deleted line for zero added enforcement). My
"a deliberate omission CAN be guarded" idea SHIPPED as the marker-pin: the access-
policy test now also asserts `"DuckDBResource"`+`"read_only=False"` present in
transforms.py source, so a future "modernize" trips both pins. Both now Settled above.

Moot / not needed: my behavioral "write raises" bar for allowing (B) never triggered —
(B) was rejected (its reader/writer split would move from a DuckDB-enforced source-
tested lock into Definitions wiring, best-case invisible, worst-case theater; hiring-
manager's guard-honesty veto). Good: I held the line that a migration must not delete a
guard to satisfy an idiom checklist, AND I named the acceptable non-detector resolution
(document the why-not) — that policy alternative is what shipped.

Prep validated: introspection-based provenance tests ripple automatically (deps=
populates parent_keys), so lineage can't silently break — I confirmed the detector
already exists rather than proposing a new one. Prep differently: I checked dagster
MASTER for the API, not this repo's pinned version — flagged it as unverified and it
happened not to matter (dagster-duckdb isn't even a dep), but pin the ACTUAL installed
version's source next time before ruling on upstream behavior. Lesson reinforced (3rd
time): whenever I spec a detector, name the lower-churn policy variant in the same
breath — here "document the why-not + marker pin" beat "migrate + rewrite the pin."

## Banked: earlier panels (2026-07-18/19, compacted)

Pipeline-reveal + character_stats: provenance/SQL/spoiler laws above shipped as
specced; lesson — objections without a detector design get deferred; arrive with the
verification design in hand (execute-and-compare won unanimously because it did).
Birth registry: my rulings were the adjudication (two-checks 7–1, coda pin 5–3,
guard slate item-for-item); the lock-race item resolved by POLICY (encode + pin)
instead of my detector — when I spec a detector, also spec the acceptable policy
alternative and its conditions. Ledger closure: snapshot.yml runs the FULL suite
before the bot commit; DATA.meta freshness pinned; re-verify open items AT BANK TIME
before writing "OPEN".

## Banked: akabab second source (2026-07-20, compacted)

Log: `.claude/panel/decisions/2026-07-20-akabab-second-source.md`. Won the slate:
five-checks ceiling held vs per-field baselines; seen-to-fail matrix = plan item 5;
WORDS-overflow carve-out; ungated alias-injectivity/load-bearing pytest; no-prose-grep;
Q3 (key-presence ≠ parse, one WARN, two-guard law dormant). Lost correctly:
`EXPECTED_DECEASED_COUNT` → lore's `EXPECTED_DEATHS_ON_FILE` — identifier names
(checks/constants/columns) are CLAIM SURFACE; vocabulary honesty is now part of my
definition of verified. Vindicated: computed-not-transcribed baselines (three surveys
of the same JSON disagreed). Lessons: verify SHAPE not exact counts from live fetches;
run my proposed NAMES past vocabulary roles in prep; the pre-veto tripwire (Yoda
derivation) is a reusable guard genre.

## Banked: akabab site surfacing (2026-07-20, compacted)

Log: `.claude/panel/decisions/2026-07-20-akabab-site-surfacing.md`. Durable law is in
Settled (card-not-beat; checked-vs-uncheckable honesty split; no per-card badge; no
ranked-affiliations chart; bios SQL returns counts; DAG-strip PIN). Whole slate shipped
as specced; my prep break-map WAS the adjudication skeleton. Refined on my side: shape
is boolean `diedOnFile` (no signed ABY value on the page). Overruled cheaper in my
favor: DAG strip PINned, not full-rendered. Lessons (both now standing habits): arrive
with the exact guard-by-guard ripple map (which pins a card vs a beat touches); whenever
I spec a detector, name the lower-churn policy variant + its equivalent-guarantee
condition in the same breath. The captured skill: panel-qa-engineer-second-source-guards.
