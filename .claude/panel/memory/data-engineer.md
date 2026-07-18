# Data Engineer — Panel Memory

## Settled (do not relitigate)

- Single HTML file for the site: no CDNs, no webfonts, no build step. Anything that
  needs a compile/bundle step is out — honesty must be architectural. (First design
  panel, PR #1.)
- Every number on the site must be derivable from the inline pipeline JSON; a runtime
  drift detector in `site/index.html` warns when data and copy diverge. (First design
  panel.)
- `starwars_dagster/known_facts.py` is the single source of verified baselines,
  imported by both pytest and asset checks. No duplicated constants. (Testing panel,
  PR #3.)
- Severity discipline: structural breakage = ERROR/blocking asset checks; upstream
  drift = WARN — SWAPI is not ours to freeze. (Testing panel, PR #3.)
- `scripts/snapshot_fixtures.py` (and the `snapshot.yml` workflow) refresh the frozen
  fixture snapshot; the workflow exists because remote dev containers may not reach
  swapi.info while GitHub runners can. CI (`ci.yml`) is offline-only. (Testing panel,
  PR #3.)
- No second data-quality framework (no Great Expectations/Pandera). Dagster-native
  checks + one green workflow carry the signal. (Testing panel, PR #3.)
- ONE `DATA.provenance` object is the sole source of every provenance/severity string
  on the site: `assets` keyed by id (`deps`, `checks[{name,label,blocking,why}]`, `why`
  verbatim from checks.py `description=`) + `claims[]` for beats 1–6 (`chain`, `hot`,
  `relation: direct|derived`, `guard: {kind: check|pytest|none, ref}`). Badge severity
  derives from `blocking` — never a hand-typed severity string. (Pipeline-reveal panel.)
- Guard honesty: a check badge may only appear where the check asserts the displayed
  number (or its denominator/structure, labeled as such); derived/unguarded claims say
  so in plain words. No fabricated or implied live status. (Pipeline-reveal panel.)
- `tests/test_site_provenance.py` cross-checks the site provenance blob against
  `defs.resolve_asset_graph()` + `check_specs` offline: real assets/edges, check
  ownership, blocking flags, verbatim rationales, exact 1–6 coverage, honest guard
  typing. Feature and guard land in the same commit. (Pipeline-reveal panel.)
- The one-line strict-JSON format of `const DATA` is load-bearing — tests parse it by
  extraction; changing the format must fail loudly. (Pipeline-reveal panel.)
- No assets added primarily to make a diagram truthful — presentation-driven pipeline
  design is out; label the derivation honestly instead. The per-character-grain
  transform cleared this bar on analytical merits and landed as `character_stats`
  (commit 082d9c9) — the principle stands for future candidates. (Pipeline-reveal panel.)
- Exact-value baselines (42 one-film, the six-film trio, 19 pilots, max flown 5) are
  WARN drift checks — never blocking; `known_facts.py` already held all four, zero new
  constants. Provenance-map membership is claim-driven: an asset no claim cites
  (raw_starships, post-082d9c9) leaves the map rather than lingering as decoration.
  (Per-character-transform landing.)
- Displayed SQL is executed SQL: any SQL text shown on the site lives in `DATA.sql`
  (one entry per card; the site renders disclosures from DATA only) and is executed
  against the fixture-built warehouse by the offline suite — execute layer ungated,
  compare layer (SQL rows == the rows the charts derive from DATA) snapshot-gated.
  No hand-verified SQL copy anywhere. (Post-landing cleanup.)
- Check strings are site copy: descriptions state the invariant and its stakes; run
  metadata carries the particulars; `known_facts.py` is the only roster/number home;
  no check string quotes another beat's caption or payoff. A standing spoiler pin
  derives payoff term sets (names AND numbers) from known_facts and asserts no check
  string renders on a beat earlier than its claim's reveal; new checks pass it before
  landing, and the pin must be seen-to-fail before merge. (Post-landing cleanup.)
- `DATA.provenance` carries no narrative fields — everything in it must stay derivable
  from / verifiable against the real Dagster definitions plus known_facts; a
  hand-authored `beat` index is unverifiable surface and is out. The rail is uniform:
  every beat renders the same rule (all checks of its chain assets); spoiler safety
  lives in the strings, not the renderer. (Post-landing cleanup.)
- Write-backs pass the merit test on warehouse grounds only: `characters_enriched`'s
  `CREATE OR REPLACE TABLE` landed because the enriched grain belonged in the DB
  (CSV-only was the anomaly) — never "to make the site's SQL true". Conditions: same-df
  parity assertion, `EXPECTED_DB_TABLES` frozen at five, `tables_populated` does NOT
  grow (it guards `star_wars_db`, which materializes before the write-back — growing
  it would be an ordering lie). (Post-landing cleanup.)

## Working knowledge

- Lineage: `SWAPIResource → raw_{films,people,planets,starships,species}
  (assets/ingestion.py) → star_wars_db (transforms.py, DuckDB at data/star_wars.duckdb)
  → {characters_enriched, film_character_counts, starship_stats, character_stats} →
  galaxy_report (analytics.py)`. ELEVEN assets in three groups (was ten; corrected
  2026-07-18 after commit 082d9c9). Site totals: 11 assets / 4 transforms / 13 checks.
- `characters_enriched` writes itself back to the warehouse
  (`CREATE OR REPLACE TABLE characters_enriched AS SELECT * FROM df`,
  transforms.py:131) on the same df it returns; parity-tested in test_pipeline.py.
  The DB file ends a full run with six tables, but `EXPECTED_DB_TABLES` stays five and
  `tables_populated` checks only the raw layer (ordering).
- The site's `const DATA` literal (site/index.html:378) is hand-authored, one-line
  strict JSON — no asset writes the HTML. The pipeline↔site contract is enforced at
  runtime (drift detector) and, where possible, by offline tests, not by generation.
- DuckDB is not a Dagster resource; assets connect directly to the path string threaded
  through `star_wars_db`. List/dict fields are JSON-stringified into DuckDB columns.
- Thirteen asset checks in `assets/checks.py`: four blocking ERROR (people shape,
  tables populated, exactly six episodes, no null names) and nine WARN drift (82-count,
  join coverage, 23-unknown-mass baseline, unknown-height baseline, TRY_CAST sanity,
  plus four `character_stats` baselines: one_film=42, six-film trio, pilot_count=19,
  max_flown=5). Descriptions follow the style rule — invariant + stakes, no rosters.
- The five dashboard SQL strings live in `DATA.sql`; chart 1 uses
  `json_array_length()`, chart 2's droid recode and charts 4/5's tiebreaks are inside
  the SQL so executed output equals rendered rows. `tests/test_site_sql.py` runs both
  layers (execute ungated; five per-chart compares snapshot-gated, riding full_run's
  pipeline-built DB read-only); the drift detector asserts every SQL disclosure
  resolves a nonempty DATA entry. Suite is 41 tests, all green post-landing.
- `character_stats` (02_transformed): `star_wars_db` → per-person `film_count` /
  `starships_flown` via `json_array_length()` on the JSON-stringified URL arrays — no
  unnesting needed; CSV side-effect `character_stats.csv`; feeds `galaxy_report`, which
  now consumes it for the screen-persistence figures instead of page-authoring math.

## Prep notes: pipeline-reveal (2026-07-17, compacted post-decision)

- Dagster 1.13.14: `AssetCheckSpec` exposes `blocking`/`name`/`asset_key`/`description`;
  WARN severity is runtime-only on `AssetCheckResult` — hence provenance encodes
  `blocking` and badges derive from it (Settled). `defs.resolve_asset_graph()` +
  `check_specs` give offline pytest everything it needs.
- Drift detector does copy-vs-data plus internal consistency only; truth vs the
  Dagster graph is pytest's job — the browser can't see Python.
- Still unverified offline: how the Dagster UI renders check badges (screenshot
  retake remains open).

## Banked: pipeline-reveal (2026-07-18)

- **Won:** the single asset-keyed provenance object inside `DATA` (adjudication
  adopted my schema nearly verbatim, incl. `relation: direct|derived` and
  `guard: {kind: check|pytest|none}`); badges derived from `blocking` because severity
  is runtime-only; honest "derived at authoring time" labeling over the analyst's
  presentation-driven transform (hiring-manager co-signed: hasty checks are coverage
  theater); ship-only-if-honest framing; drift-detector split (internal consistency in
  browser, graph truth in pytest); same-commit test file.
- **Lost/adjusted:** my "mini-SVG renderer via `el()`" technology guess — HTML `.chip`
  elements won (better CSS reuse, native text accessibility, no SVG text-measurement
  hazards at ≤260px). Lesson: propose the data contract firmly, hold the rendering
  technology loosely. My stretch goal (migrating the five SQL strings into provenance)
  was deferred for lack of a verification story for SQL text — a fair standard; next
  time bring the verification story or don't bring the stretch.
- **Learned:** the brief's beat→asset map was partly false and the analyst caught it,
  not me. Next prep: trace each displayed number to its producing query, not just each
  beat to a plausible asset; verify a brief's factual claims against the actual data
  before designing the contract that encodes them.
- Both open candidates from this round have since landed: per-character transform
  (082d9c9) and SQL-string migration (c0b97e0).

## Banked: per-character transform landed (2026-07-18, commit 082d9c9)

- Execution note, not a debate: `.claude/panel/decisions/2026-07-18-per-character-transform-landed.md`.
  Built straight from the banked acceptance criteria — the bank worked as a spec.
- What landed: one asset `character_stats` (details promoted to Working knowledge);
  four WARN drift checks; beats 4–6 flipped to `relation:"direct"` with
  `guard.kind:"check"` on the `raw_people → star_wars_db → character_stats` chain.
  `known_facts.py` needed zero changes — the single-source-of-baselines law paid off
  exactly as designed.
- Contract discipline held: the provenance subtree was edited surgically and the
  one-line strict-JSON `DATA` literal round-tripped byte-identical for every other
  subtree. `raw_starships` dropped from the provenance map because no claim cites it
  anymore — claims drive membership, not diagram completeness (now Settled).
- Same-commit guard law honored: provenance pin
  (`test_beats_four_through_six_are_direct_and_check_guarded`), grain/zero-count tests,
  snapshot-gated test that the four WARN checks pass, plus a performed negative check
  (perturbing EXPECTED_ONE_FILM_COUNT failed both guards).
- Latent-bug lesson: the beat-7 number-word array stopped at "nine" — 12 checks would
  have rendered "undefined checks" — and beat-7 prose hardcoded "three transforms".
  Word-lists and spelled-out counts are hidden duplicate facts; the drift detector now
  warns on word-list overflow. Next prep: grep for prose-encoded numerals whenever a
  count changes.
- Prep differently: my Working-knowledge asset count went stale (said ten after eleven
  shipped) — after any pipeline-shape commit, refresh the lineage bullet in the same
  banking pass.

## Prep notes: post-landing cleanup (2026-07-18, compacted post-decision)

- Audited the five dashboard SQL strings by executing them against the actual fixture
  DB: three of five were live lies (charts 2/4 queried `characters_enriched`, which
  was never a DuckDB table; chart 1's `len()` on a JSON-stringified VARCHAR returned
  string length — 1222 "characters" for Episode I). The orchestrator's execution run
  confirmed all three. Technique banked in the provenance-contract skill: execute
  displayed SQL, never eyeball it. Outcomes are now Settled law above.

## Banked: post-landing cleanup (2026-07-18, commits c0b97e0 + 2aa845e)

- **Won — Q2 landed in exactly my shape, unanimous:** characters_enriched write-back
  on the same df it returns; all five strings into DATA.sql rendered only from DATA;
  chart 1 on `json_array_length`; recode/tiebreaks moved into the SQL; execute
  (ungated) + compare (snapshot-gated) layers in tests/test_site_sql.py; drift-detector
  claim; README:92 corrected. The 3-of-5 prep audit was the decisive evidence —
  executing the artifact under test beats arguing about it.
- **Won — Q1 (5-3-1):** re-authoring beat lore's "never rewrite checks.py"; my framing
  held (label/description are ours to author — the verbatim law binds only the
  projection, and runtime metadata keeps operators whole). My uniform-rail stance beat
  both per-beat filtering and the designer's guard-only rail (coverage understatement:
  character_stats has zero blocking checks). Credit where due: the decisive argument
  was technical-writer's — the trio prose was a THIRD home for a roster whose single
  source is known_facts, a drift bug independent of spoilers. One-home is the stronger
  frame than spoiler-hygiene; lead with it next time.
- **Won — Q3:** (a) unknown-height WARN check landed with my WORDS-overflow caveat
  honored (list extended through "thirteen" in the same commit; beat-1 guard flipped
  pytest→check); (b) disclose-only, per my coverage-theater call.
- **Lost/adjusted:** QA supplied conditions I should have specified myself — the
  same-df parity assertion and the ordering argument for why `tables_populated` must
  not grow. Hiring-manager's framing veto corrected a drift in my own prep: I
  half-justified the write-back as "keeps the displayed table name aligned with the
  provenance chip" — that is presentation-driven reasoning; the honest merit is the
  warehouse gap (enriched grain queryable). And I missed the Exercise-8 collision on
  Q3(b): a galaxy_report check would pre-solve a WORKSHOP exercise — QA and
  technical-writer caught it, not me.
- **Prep differently:** when proposing a write-back or a new check, state its
  check/materialization ordering implications explicitly, and grep WORKSHOP for
  exercise collisions before recommending coverage anywhere near the teaching modules.
- Closes my long-open SQL-string migration item. Still open: README screenshot retake,
  now targeting 13 green checks (desktop UI).
