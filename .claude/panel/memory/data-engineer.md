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

## Prep notes: pipeline-reveal (2026-07-17)

- Verified against installed Dagster 1.13.14: `AssetCheckSpec` exposes `blocking`,
  `name`, `asset_key`, `description` — so an offline pytest CAN enumerate
  `starwars_dagster.defs` (built in `starwars_dagster/__init__.py` via
  `load_assets_from_modules` / `load_asset_checks_from_modules`) and cross-check a
  site `provenance` blob for: asset names, dependency edges, check names per asset,
  and blocking flags. **Severity (WARN) is NOT on the spec** — it is chosen at
  runtime on `AssetCheckResult`. In this repo blocking↔ERROR maps 1:1, so the
  provenance schema must encode `blocking: true/false` (statically verifiable), and
  the site derives its ERROR/WARN badge from that — never a hand-typed "severity"
  string that nothing can verify.
- The site already carries THREE hand-authored representations of the pipeline:
  the static lineage strip (index.html:311-340, HTML chips), five hand-written SQL
  strings passed to `makeCard` (opts.sql, rendered at 848-854), and the footer line.
  Adding per-beat mini-DAGs naively would make it four+. My line: ONE `provenance`
  object inside `DATA`, keyed by asset id (nodes, deps, checks w/ blocking + one-line
  rationale), with beats AND dashboard cards referencing asset ids; the mini-SVG
  renderer draws from that single object via the existing `el()` factory (~383).
- Beat→asset mapping from the brief (0-3 characters_enriched, 4-5
  film_character_counts, 6 starship_stats, 7 galaxy_report) means only 4 distinct
  sub-DAGs exist; per-beat data should be a reference (asset id + highlighted checks),
  not 8 duplicated diagrams.
- Runtime drift detector (index.html:481-497) is copy-vs-data; extending it to
  provenance means internal-consistency checks only (every referenced asset id
  resolves, check counts sum to 8, badge derivation matches blocking flags). Truth
  against the actual Dagster graph is the pytest's job — browser can't see Python.
- Cannot verify offline: swapi.info reachability (irrelevant here) and how the
  Dagster UI renders check badges (README screenshots are a separate open item).
