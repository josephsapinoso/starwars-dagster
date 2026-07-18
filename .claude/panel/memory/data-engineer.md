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
