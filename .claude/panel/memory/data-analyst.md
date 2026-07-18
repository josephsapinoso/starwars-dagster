# Data Analyst — Panel Memory

## Settled (do not relitigate)

- Every number on the site must be derivable from the inline pipeline JSON; disclose
  denominators and nulls on-chart, not in footnotes. The runtime drift detector warns
  on any mismatch between data and copy. (First design panel, PR #1/#2.)
- Verified baselines: **82** people; **23** lack mass (of 82 — always with the
  denominator); Naboo **11**, Tatooine **10**; exactly **three** characters in all six
  films (C-3PO, R2-D2, Obi-Wan Kenobi); **42** of 82 appear in exactly one film;
  **19** of 82 flew at least one starship; max starships flown is **5** (Obi-Wan).
  (First design panel; frozen in `known_facts.py`, PR #3.)
- Height extremes: Yoda 66cm to Yarael Poof 264cm, with 1 person unmeasured. (Site
  beat 1, verified against snapshot.)

## Working knowledge

- Nulls are the story, not noise: the mass beeswarm's 23 missing values and the
  homeworld join's misses are disclosed in captions — this pattern must extend to any
  new claim.
- The drift detector (site/index.html ~481–497) recomputes
  {total, noMass, oneFilm, naboo, tatooine, pilots, maxFlown} from `DATA.people` and
  compares against hardcoded expectations, plus an exact-set check on the six-film
  trio. Any new on-site claim should be added there.
- Chart honesty conventions already in force: log scale flagged in the mass/scatter
  captions; excluded rows named (e.g. unmeasured/unweighed counts); the Chart/Table
  toggle exposes underlying rows for every dashboard card.

## Prep notes: pipeline-reveal (2026-07-17)

**Central finding: the brief's beat→asset map is partly false, and the reveal must not
ship it as-is.** Verified against `starwars_dagster/assets/transforms.py`:

- Beats 0–3 ← `characters_enriched`: TRUE. The transform (transforms.py:108–125)
  carries height, mass, and the people→planets LEFT JOIN; 82 rows.
- Beats 4–5 ← `film_character_counts`: FALSE. That asset (transforms.py:149–160) is
  6 rows of characters-per-FILM (`json_array_length(films.characters)`). The
  42-of-82-one-film and six-film-trio numbers are films-per-CHARACTER — computed by
  NO asset. They were hand-derived from raw `people[].films` array lengths when the
  site JSON was authored.
- Beat 6 ← `starship_stats`: FALSE for the beat's claims. It's per-SHIP
  (`known_pilots` per starship, transforms.py:195); "19 of 82 flew" and "Obi-Wan
  flew 5" are per-PERSON, computed by no asset.
- Beat 7 ← `galaxy_report`: the asset exists but has ZERO asset checks attached
  (checks.py covers raw_people, star_wars_db, characters_enriched,
  film_character_counts, starship_stats only).

**Check→claim relevance map** (checks.py; badge only where the check guards the number):
- Beat 0 (82): `raw_people_count_matches_verified_snapshot` WARN +
  `raw_people_has_required_shape` ERROR — direct. Best-guarded number on the site.
- Beat 1 (heights, 1 unmeasured): NO check covers height nulls. Gap.
- Beat 2 (23/82 unweighed): `characters_enriched_unknown_mass_baseline` WARN —
  direct, asserts the exact 23-of-82 denominator.
- Beat 3 (homeworlds): `characters_enriched_join_coverage` WARN — direct.
- Beats 4–5: `films_are_exactly_the_six_episodes` ERROR guards the six-film FRAME
  only; nothing asserts the trio or the 42. `SIX_FILM_CHARACTERS` lives in
  known_facts.py:20 but checks.py never imports it — trio is pytest-guarded only.
- Beat 6: `starship_stats_cast_sanity` WARN is about ship numeric columns —
  irrelevant to the pilots claims. Gap.

Consequences I will argue: (a) per-beat provenance labels are only honest where
lineage is real — beats 4–6 need either an honest attribution (derived from
raw_people arrays at site-authoring time) or a real transform that computes
films-per-character / ships-per-person before the diagram may claim them; (b) check
badges appear ONLY where the check asserts the displayed number, else it is
verification theater; (c) the promised pytest cross-check must validate not just
that the named asset exists but that it computes the claimed column/quantity.

Cannot verify offline: live materialization state; whether data/star_wars.duckdb on
disk matches the snapshot (CI is offline-only by design).
