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
  design is out; label the derivation honestly instead. A per-character-grain transform
  remains an open candidate on its own analytical merits only. (Pipeline-reveal panel.)

## Working knowledge

- Lineage: `SWAPIResource → raw_{films,people,planets,starships,species}
  (assets/ingestion.py) → star_wars_db (transforms.py, DuckDB at data/star_wars.duckdb)
  → {characters_enriched, film_character_counts, starship_stats} → galaxy_report
  (analytics.py)`. Ten assets in three groups.
- The site's `const DATA` literal (site/index.html:378) is hand-authored, one-line
  strict JSON — no asset writes the HTML. The pipeline↔site contract is enforced at
  runtime (drift detector) and, where possible, by offline tests, not by generation.
- DuckDB is not a Dagster resource; assets connect directly to the path string threaded
  through `star_wars_db`. List/dict fields are JSON-stringified into DuckDB columns.
- Eight asset checks in `assets/checks.py`: four blocking ERROR (people shape, tables
  populated, exactly six episodes, no null names) and four WARN drift (82-count, join
  coverage, 23-unknown-mass baseline, TRY_CAST sanity).

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
- Open candidates I co-own: per-character-grain transform (real analytics merits only;
  would upgrade beats 4–6 to DIRECT), SQL-string migration into a verified home.
