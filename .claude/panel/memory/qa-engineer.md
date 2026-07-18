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

## Working knowledge

- Inventory (post-2aa845e): 11 assets, 4 transforms, 13 checks in `assets/checks.py`;
  41 pytest tests green. Blocking (4) — `raw_people_has_required_shape`,
  `star_wars_db_tables_populated`, `films_are_exactly_the_six_episodes`,
  `characters_enriched_has_no_null_names`. WARN (9) —
  `raw_people_count_matches_verified_snapshot`, `characters_enriched_join_coverage`,
  `characters_enriched_unknown_mass_baseline`,
  `characters_enriched_unknown_height_baseline` (guards beat 1's "1 unmeasured"),
  `starship_stats_cast_sanity`, plus four `character_stats` drift baselines:
  one-film (42), six-film trio, pilot count (19), max flown (5).
- SQL guard file map (tests/test_site_sql.py): ungated layer —
  `test_data_sql_has_exactly_the_five_chart_entries`,
  `test_no_inline_sql_strings_remain_in_the_page` (pins `const sql = \`` out of
  chart IIFEs), `test_every_displayed_string_executes_against_the_warehouse`
  (parametrized over films/gender/scatter/homeworlds/hyper),
  `test_displayed_sql_carries_no_unverified_count_comments`; snapshot-gated layer —
  five `test_*_sql_reproduces_the_*` compare tests asserting executed rows == the
  rows the charts derive from DATA. Warehouse = module-scoped fixture materializing
  raw_* → star_wars_db → characters_enriched with FakeSWAPIResource, then
  read_only duckdb.connect on the pipeline-written file.
- Failure modes with named detectors: SWAPI shape change (shape check), count drift
  (count/mass/height baselines), join rot (coverage check), cast rot (TRY_CAST
  sanity), copy drift on site (runtime detector), SQL rot (execute layer), SQL
  computing the wrong thing or DATA edited without SQL (compare layer), spoiler
  regression in check strings (spoiler pin). New site claims must extend one of
  these, not bypass them.
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

Won (nearly the whole slate), and why it held:

- Both write-back conditions are now law verbatim (one code path with same-df parity
  assertion; EXPECTED_DB_TABLES stays five — the ordering-lie argument is in the log
  word for word). Verified in-repo: transforms.py:131 writes the same df it returns;
  parity test exists in test_pipeline.py.
- My execute-and-compare spec shipped as tests/test_site_sql.py, both layers plus
  the no-inline-SQL and no-numeric-comments pins. Unanimous adoption — direct payoff
  of last panel's lesson: I arrived with the full detector design (skill) instead of
  the smell, and the 18-month open item closed in one debate.
- Q1 re-authoring won 5–3–1 on MY framing: the one-home law (trio roster hand-listed
  in a description = drift bug) plus "a `beat` field is hand-authored attribution
  pytest cannot verify" sealed it. That second argument is now the settled
  "provenance carries no narrative fields" law.
- My galaxy_report retraction held: disclose-only, unanimous. Retracting a weak-yes
  when the Exercise-8 collision surfaced cost nothing and bought credibility.

Amended / deviations I accept:

- Spoiler pin: I leaned names-only; storyteller's amendment added payoff NUMBERS to
  the derived term sets. Correct — "42", "19", "5" leak the punchline as surely as
  the trio's names. Seen-to-fail verified by reinserting "trio" into a beat-4 label.
- Implementation deviation from my spec: test_site_sql.py builds its own
  module-scoped warehouse fixture (raw_* through characters_enriched) instead of
  reusing test_pipeline's full_run. Same principle honored — pipeline-built DB, no
  bespoke tables, read_only connect — and module scoping avoids cross-file fixture
  coupling. Fine; skill updated to match reality.

Prep-differently next time: verifying the data-engineer's SQL audit in-repo during
PREP (instead of taking it on faith) made my debate position unassailable — keep
doing that. And when a guard's severity is WARN, always ask "what asserts green?" —
the snapshot-gated pass-assertion pattern is now standard for every new WARN check.

Still OPEN: README screenshot retake, now targeting 13 green checks (desktop UI).
