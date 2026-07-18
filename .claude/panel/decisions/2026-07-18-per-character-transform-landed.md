# Note: per-character transform landed (open item from 2026-07-18-pipeline-reveal)

Date: 2026-07-18 · Scope: execution note, not a new debate · Orchestrator: Claude

The first open item of the pipeline-reveal decision — "per-character-grain transform
(films-per-character, starships-flown-per-person) with checks asserting 42-of-82, the
trio, 19-of-82, maxFlown 5" — landed in commit `082d9c9`, implemented directly from the
banked acceptance criteria at the user's direction (no fresh debate; this BANK note and
panelist memory updates are the closing step).

What shipped, against the banked criteria:

- One asset, `character_stats` (02_transformed, `star_wars_db` → per-person `film_count`
  and `starships_flown`), feeding `galaxy_report` so the DAG strip's "which feed the
  galaxy_report" copy stays true.
- Four WARN drift checks on it — `character_stats_one_film_baseline` (42),
  `character_stats_six_film_trio` (C-3PO, R2-D2, Obi-Wan), `character_stats_pilot_count_baseline`
  (19), `character_stats_max_flown_baseline` (5) — severity per the known_facts law:
  exact-value baselines are drift, never blocking. `known_facts.py` needed zero changes.
- Beats 4–6 flipped to `relation:"direct"` with `guard.kind:"check"` on the
  `raw_people → star_wars_db → character_stats` chain; `raw_starships` left the provenance
  map (no claim cites it anymore). Totals are now 11 assets / 4 transforms / 12 checks.
- QA's same-commit condition honored: the flip, a provenance pin
  (`test_beats_four_through_six_are_direct_and_check_guarded`), grain/zero-count behavior
  tests, and a snapshot-gated test that the four WARN checks pass all rode the feature
  commit. Negative check performed (perturbed EXPECTED_ONE_FILM_COUNT → both guards fail).
- Latent bugs fixed en route: the beat-7 number-word array stopped at "nine" (12 checks
  would have rendered "undefined checks" — the drift detector now warns on word-list
  overflow), and the hardcoded "three transforms" copy in beat-7 prose and the DAG-strip
  aria label.

Still open from the parent decision: the five dashboard SQL strings (blocked on a
verification story) and the README screenshot retake (now needs 12 green checks, desktop
UI required).
