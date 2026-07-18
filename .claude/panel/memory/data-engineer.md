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

## Working knowledge

- Lineage: `SWAPIResource → raw_{films,people,planets,starships,species}
  (assets/ingestion.py) → star_wars_db (transforms.py, DuckDB at data/star_wars.duckdb)
  → {characters_enriched, film_character_counts, starship_stats, character_stats} →
  galaxy_report (analytics.py)`. ELEVEN assets in three groups (was ten; corrected
  2026-07-18 after commit 082d9c9). Site totals: 11 assets / 4 transforms / 12 checks.
- The site's `const DATA` literal (site/index.html:378) is hand-authored, one-line
  strict JSON — no asset writes the HTML. The pipeline↔site contract is enforced at
  runtime (drift detector) and, where possible, by offline tests, not by generation.
- DuckDB is not a Dagster resource; assets connect directly to the path string threaded
  through `star_wars_db`. List/dict fields are JSON-stringified into DuckDB columns.
- Twelve asset checks in `assets/checks.py`: four blocking ERROR (people shape, tables
  populated, exactly six episodes, no null names) and eight WARN drift (82-count, join
  coverage, 23-unknown-mass baseline, TRY_CAST sanity, plus four `character_stats`
  baselines: one_film=42, six-film trio, pilot_count=19, max_flown=5).
- `character_stats` (02_transformed): `star_wars_db` → per-person `film_count` /
  `starships_flown` via `json_array_length()` on the JSON-stringified URL arrays — no
  unnesting needed; CSV side-effect `character_stats.csv`; feeds `galaxy_report`, which
  now consumes it for the screen-persistence figures instead of page-authoring math.

## Prep notes: pipeline-reveal (2026-07-17, compacted post-decision)

- Dagster 1.13.14: `AssetCheckSpec` exposes `blocking`/`name`/`asset_key`/`description`;
  WARN severity is runtime-only on `AssetCheckResult`. Hence provenance encodes
  `blocking` and badges derive from it (now Settled). `defs` builds via
  `load_assets_from_modules` / `load_asset_checks_from_modules` in
  `starwars_dagster/__init__.py`; `defs.resolve_asset_graph()` + `check_specs` give
  offline pytest everything it needs.
- Pre-decision the site carried three hand-authored pipeline representations (lineage
  strip ~index.html:311-340, five makeCard SQL strings ~848-854, footer line); the
  single-provenance-object rule prevents a fourth. SQL-string migration deferred (open).
- Drift detector (index.html:481-497) does copy-vs-data; provenance extension is
  internal-consistency only (ids resolve, coverage exactly 1–6, badge derivation,
  callback counts) — truth vs the Dagster graph is pytest's job; browser can't see
  Python.
- Still unverified offline: how the Dagster UI renders check badges (screenshot retake
  remains a separate open item).

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
- **Learned from other roles' prep I'd missed:** the brief's beat→asset map was partly
  false (beats 4–5 are per-character numbers no asset computes; beat 6's pilot counts
  aren't in `starship_stats`; `galaxy_report` has zero checks) — the analyst caught
  this, not me. Next prep: trace each displayed number to its producing query, not
  just each beat to a plausible asset. Also: desktop steps are center-anchored flex,
  so disclosure growth placement is a real layout constraint (ux).
- **Prep differently:** verify the brief's factual claims against the actual data
  before designing the contract that encodes them; check README integrity (it was
  truncated mid-word — hiring-manager found it).
- Open candidates I co-own: per-character-grain transform (LANDED 082d9c9 — see below),
  SQL-string migration into a verified home (still OPEN).

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
- My SQL-string migration stretch remains OPEN, still blocked on a verification story
  for SQL text; the README screenshot retake now needs 12 green checks (desktop UI).
- Prep differently: my Working-knowledge asset count went stale (said ten after eleven
  shipped) — after any pipeline-shape commit, refresh the lineage bullet in the same
  banking pass.
