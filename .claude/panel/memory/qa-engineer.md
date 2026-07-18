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

## Working knowledge

- The 8 checks in `assets/checks.py`: blocking — `raw_people_has_required_shape`,
  `star_wars_db_tables_populated`, `films_are_exactly_the_six_episodes`,
  `characters_enriched_has_no_null_names`; WARN —
  `raw_people_count_matches_verified_snapshot`,
  `characters_enriched_join_coverage`,
  `characters_enriched_unknown_mass_baseline`, `starship_stats_cast_sanity`.
- Failure modes with named detectors today: SWAPI shape change (shape check), count
  drift (count/mass baselines), join rot (coverage check), cast rot (TRY_CAST
  sanity), copy drift on the site (runtime detector). New site claims must extend one
  of these, not bypass them.
- A feature and its guard land in the same commit; "verified" means an automated
  detector exists and has been seen to fail when the guarded thing breaks.
