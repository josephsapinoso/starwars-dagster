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
- **Guard honesty (2026-07-18, pipeline-reveal):** a check badge may appear ONLY where
  the check asserts the displayed number (or its denominator/structure, labeled as
  such); derived/unguarded claims say so in plain words. No fabricated or implied live
  status, ever.
- **Provenance strings are data, not copy (2026-07-18):** every provenance/severity
  string on the site derives from `DATA.provenance`, pytest-verified against real
  Dagster definitions; badge severity derives from `spec.blocking`; check rationales
  are verbatim projections of checks.py `description=`.
- **Reveal coverage (2026-07-18):** provenance reveals on beats 1–6 only; beat 0 stays
  a clean hook; beat 7 carries the provenance-computed callback line. One disclosure
  style shared with details.sql.
- **The one-line strict-JSON format of `const DATA` is load-bearing** — tests parse it
  by extraction; format changes must fail loudly. (2026-07-18.)
- **`relation: direct|derived` is the honesty vocabulary (2026-07-18):** claims not
  computed by any asset render as derived — never as asset-attributed. Derived/none
  guards never render a check badge as asserting the number. (Since commit 082d9c9 no
  claim currently uses `derived`, but the vocabulary and its structural pytest guard
  remain law for any future claim.)
- **Per-character grain is materialized (2026-07-18, commit 082d9c9):** `character_stats`
  (02_transformed, `star_wars_db` → per-person `film_count`, `starships_flown`) computes
  the 42/trio/19/maxFlown-5 numbers in-pipeline; four WARN drift checks assert them from
  known_facts constants. Beats 4–6 are `relation:"direct"` with check guards on
  `raw_people → star_wars_db → character_stats`. Totals: 11 assets / 4 transforms /
  12 checks; character_stats feeds galaxy_report. Do not re-derive these by hand.

## Working knowledge

- Nulls are the story, not noise: the mass beeswarm's 23 missing values and the
  homeworld join's misses are disclosed in captions — this pattern must extend to any
  new claim.
- The drift detector (site/index.html ~481–497) recomputes
  {total, noMass, oneFilm, naboo, tatooine, pilots, maxFlown} from `DATA.people` and
  compares against hardcoded expectations, plus an exact-set check on the six-film
  trio. Post pipeline-reveal it also asserts provenance internal consistency: claims
  cover exactly beats 1–6, every chain id resolves in `provenance.assets`, badge
  values derive from `blocking`, beat-7 callback counts match the object.
- Chart honesty conventions in force: log scale flagged in mass/scatter captions;
  excluded rows named; Chart/Table toggle exposes underlying rows per dashboard card.
- **Check→claim relevance map** (durable reference; re-verified 2026-07-18 against
  checks.py/transforms.py after commit 082d9c9):
  - Beat 0 (82): `raw_people_count_matches_verified_snapshot` WARN +
    `raw_people_has_required_shape` ERROR — direct; best-guarded number on the site.
    `raw_people` is the first node of every chain, so this story appears in all six
    reveals without a beat-0 reveal.
  - Beat 1 (heights, 1 unmeasured): no check covers height nulls. Coverage gap (open).
  - Beat 2 (23/82): `characters_enriched_unknown_mass_baseline` WARN — direct.
  - Beat 3 (homeworlds): `characters_enriched_join_coverage` WARN — direct.
  - Beats 4–5 (42 one-film, six-film trio): `character_stats_one_film_baseline` +
    `character_stats_six_film_trio` WARN — direct. `SIX_FILM_CHARACTERS` is now
    imported by checks.py; the trio is guarded both in-pipeline and by pytest.
    `films_are_exactly_the_six_episodes` ERROR still guards the six-film frame.
  - Beat 6 (19 of 82 flew; Obi-Wan 5): `character_stats_pilot_count_baseline` +
    `character_stats_max_flown_baseline` WARN — direct, at the correct per-PERSON
    grain. `starship_stats` remains per-SHIP and irrelevant to the pilots claims;
    `raw_starships` no longer appears in any claim chain.
  - `galaxy_report` still has zero attached checks (open gap; note it now consumes
    character_stats and carries a Screen Persistence section).
- WARN severity is runtime-only in Dagster; `spec.blocking` is the static field —
  provenance must encode `blocking` and derive badge wording from it (data-engineer/
  qa-engineer finding I should have caught in prep).

## Banked: pipeline-reveal (2026-07-18)

**Won:**
- My central prep finding — the brief's beat→asset map was partly false — drove the
  spec: it is the first line of "prep-pass findings that changed the spec," and beats
  4–6 now ship with honest `relation: "derived"` attribution instead of fabricated
  lineage. Option (b) of my proposal is what shipped.
- Check-badge honesty ("badge only where the check asserts the displayed number") is
  now banked law verbatim, and the pytest suite asserts it structurally
  (derived/none guards can never render an asserting badge).
- My demand that the pytest cross-check validate more than asset existence landed:
  `tests/test_site_provenance.py` asserts topology, check ownership, blocking, verbatim
  rationales, exact coverage set, and honest guard typing.
- Drift-detector growth: the detector gains provenance internal-consistency checks,
  extending my standing "grows with every new claim" constraint.

**Lost (and why):**
- Option (a), the per-character-grain transform, lost to data-engineer +
  hiring-manager: adding an asset primarily so a diagram can point at it is
  presentation-driven pipeline design. Fair adjudication at the time; it survived as
  an open candidate on analytics merits and later landed (see Banked section below).
  Lesson stands: lead with grain-correctness/analytics value, not the diagram.
- Hiring-manager's beat-0 reveal (which would have showcased the best-guarded number)
  lost to the clean-hook coalition; I was neutral, and the structural compensation —
  raw_people heading every chain — preserves the census guard story anyway.

**Prep differently next time:**
- Check `spec.blocking` vs runtime severity semantics myself — a data-honesty question
  (what does a WARN badge legally mean?) that I left to the engineers.
- When I propose "either A or B," pre-rank them and cost them: the panel will pick the
  cheaper honest option, so B (honest labeling) deserved the fuller spec in my prep.
- Verify the rendering-tech assumption in briefs ("inline SVG") early; the HTML-chip
  decision changed what "denominators on-chart" means for reveal text (plain text,
  trivially drift-checkable — good for me, but I didn't argue it).

**Open items I track:** the five hand-written dashboard SQL strings still have no
verified home; beat-1 height-null check gap and galaxy_report's zero checks remain
undisclosed coverage gaps worth raising when check coverage next comes up.

## Banked: per-character transform landed (2026-07-18, commit 082d9c9)

Execution close-out, not a debate — the pipeline-reveal open item shipped at the
user's direction, implemented from the banked acceptance criteria. I verified the
code, not just the note: `character_stats` in transforms.py (star_wars_db →
per-person film_count, starships_flown, feeds galaxy_report); four WARN drift checks
in checks.py built from known_facts constants (42, trio, 19, maxFlown 5) with
known_facts.py unchanged; provenance pin
`test_beats_four_through_six_are_direct_and_check_guarded` at
tests/test_site_provenance.py:135; grain/zero-count and snapshot-gated tests rode
the same commit, plus a negative check (perturbed baseline fails both guards).

**Won (delayed):** the exact assertion set I specified in the pipeline-reveal debate
shipped verbatim, and severity followed my law — exact-value baselines are WARN
drift, never blocking. The relation vocabulary proved its worth: `derived` labels
made the upgrade a clean, testable flip to `direct` instead of a copy rewrite.
**Bonus wins for my constraints:** the beat-7 number-word overflow bug ("undefined
checks" at 12) was caught and the drift detector now warns on word-list overflow;
hardcoded "three transforms" copy was fixed — both are exactly the data-vs-copy
drift class my standing constraint exists for. Hardcoded number-words and counts in
prose/aria labels are a drift surface I should audit whenever totals change.

**Prep differently:** when an option loses on cost grounds, keep its acceptance
criteria specified to landing precision anyway — that is what let this ship later
with zero new debate.
