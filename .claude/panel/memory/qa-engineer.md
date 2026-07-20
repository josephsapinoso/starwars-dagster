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

## Working knowledge

- Inventory (post-f170379): 11 assets, 4 transforms, 15 checks — 4 blocking, 11 WARN
  (people count, join coverage, unknown-mass/height, cast sanity, four
  character_stats drift baselines, birth-year baseline + UNGATED-principle
  parse-honesty via `additional_ins`, read_only connect). After akabab lands:
  13 assets, 5 transforms, 20 checks (6 blocking) — the totals pin at
  test_site_provenance.py:242 introspects real defs, so the site triple ripples
  same-commit automatically. Grep trap: docstrings mention `@asset_check` /
  `blocking=True` — always introspect check_specs, never grep counts.
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

## Banked: akabab second source (2026-07-20)

Decision log: `.claude/panel/decisions/2026-07-20-akabab-second-source.md`.

Won nearly the whole slate: five-checks ceiling HELD against the analyst's per-field
baselines (she conceded the mechanism, kept nested denominators as report-copy
convention — the right trade); my seen-to-fail acceptance matrix adopted verbatim as
plan item 5; the WORDS-overflow carve-out won jointly with technical-writer (it is
totals-pin ripple, not surfacing); ungated alias-injectivity + load-bearing pytest
ratified with engineer's better framing (aliases bridge the join, never repair
records); no-prose-grep-pins held (README counts stay a human checklist); Q3 ruling
adopted exactly (key-presence ≠ parse, one WARN guard, two-guard law dormant).

Lost, correctly: my constant name `EXPECTED_DECEASED_COUNT` fell to lore's
`EXPECTED_DEATHS_ON_FILE` package. The lesson generalizes: identifier names (checks,
constants, columns) are CLAIM SURFACE — "deceased" overclaims canon-completeness the
same way a wrong badge overclaims verification. Same force renamed `died` →
`died_year_aby`. Vocabulary honesty is part of my definition of verified now.

Vindicated condition: baselines computed-not-transcribed became plan item 6 after
three independent surveys of the same live JSON disagreed (my WebFetch summarizer
said died=30; brief said 47; a third said 28). A number nobody can transcribe twice
identically is a number only a script may bank.

Prep differently next time: (1) summarizer-derived counts from live fetches are
unreliable evidence — don't burn prep verifying a brief's exact counts; instead
verify the SHAPE and make computed-at-freeze a condition from the start. (2) Run my
proposed check/constant/column NAMES past the vocabulary roles' likely objections
during prep, so my slate survives adjudication intact. (3) The pre-veto tripwire
(Yoda derivation) is a new guard genre — a written constraint for a FUTURE panel;
cheap, and it moves spoiler/testimony law forward in time. Use it again.
