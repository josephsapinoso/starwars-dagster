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
  guards never render a check badge as asserting the number.
- **Per-character grain is materialized (2026-07-18, commit 082d9c9):** `character_stats`
  (02_transformed, `star_wars_db` → per-person `film_count`, `starships_flown`) computes
  the 42/trio/19/maxFlown-5 numbers in-pipeline; WARN drift checks assert them from
  known_facts constants. Beats 4–6 are `relation:"direct"` with check guards on
  `raw_people → star_wars_db → character_stats`. Do not re-derive these by hand.
- **Displayed SQL is executed SQL (2026-07-18, post-landing cleanup, commit c0b97e0):**
  any SQL text shown on the site lives in `DATA.sql` (single source; the page renders
  only from DATA) and is executed against the fixture-built warehouse by the offline
  suite — ungated EXECUTE layer plus snapshot-gated COMPARE layer asserting each
  query's result set equals the rows the chart derives from DATA
  (tests/test_site_sql.py). Recodes (gender→droid) and LIMIT-10 name tiebreaks live IN
  the SQL, mirrored in the JS sorts; numeric comments inside displayed SQL are a
  banned, pytest-pinned class. `characters_enriched` is written back to the warehouse
  (same df it returns, full_run parity; EXPECTED_DB_TABLES stays five) so
  `FROM characters_enriched` is true — framed as closing a warehouse gap, never as
  "making the site's SQL true."
- **Spoiler pin law (2026-07-18, commit 2aa845e):** a standing offline test
  (`test_no_payoff_leaks_before_reveal_beat`) derives payoff term sets — numbers AND
  names — from known_facts and asserts no check string renders on a beat earlier than
  its claim's reveal beat. Every new check passes the spoiler audit before landing.
- **Description style rule (2026-07-18):** check descriptions state the invariant and
  its stakes; run metadata carries the particulars; `known_facts.py` is the ONLY
  roster/number home; no check string quotes another beat's caption or payoff.
- **DATA.provenance carries no narrative fields (2026-07-18):** everything in it stays
  derivable from / verifiable against the real Dagster definitions plus known_facts —
  no hand-authored `beat` attribution pytest cannot check.
- **The rail is uniform (2026-07-18):** every beat renders the same rule — all checks
  of its chain assets. Spoiler safety lives in the strings, not the renderer; no
  per-beat filtering that would make disclosed coverage beat-dependent.
- **13 checks (4 blocking / 9 WARN) as of 2aa845e:**
  `characters_enriched_unknown_height_baseline` (WARN, from
  EXPECTED_UNKNOWN_HEIGHT_COUNT) guards beat 1's "1 unmeasured"; beat 1's guard
  flipped pytest→check. `galaxy_report` stays check-free BY DESIGN (WORKSHOP
  Exercise-8 collision + coverage-theater law) — a deliberate, disclosed gap, not an
  open one. Stop flagging it.

## Working knowledge

- Nulls are the story, not noise: the mass beeswarm's 23 missing values and the
  homeworld join's misses are disclosed in captions — this pattern must extend to any
  new claim.
- The drift detector (site/index.html) recomputes {total, noMass, oneFilm, naboo,
  tatooine, pilots, maxFlown} from `DATA.people` and compares against expectations,
  plus the six-film-trio exact-set check, provenance internal consistency (claims
  cover beats 1–6, chain ids resolve, badges derive from `blocking`, beat-7 callback
  counts, number-word list overflow), and — since c0b97e0 — that every SQL disclosure
  resolves a nonempty DATA entry.
- Chart honesty conventions in force: log scale flagged in captions; excluded rows
  named; Chart/Table toggle exposes rows per card; chart 5's subtitle computes
  "Top 10 of the ${rated} starships with a rated hyperdrive" from DATA — denominators
  computed, never typed.
- **Check→claim relevance map** (re-verified 2026-07-18 after 2aa845e):
  - Beat 0 (82): `raw_people_count_matches_verified_snapshot` WARN +
    `raw_people_has_required_shape` ERROR — direct; best-guarded number on the site;
    raw_people heads every chain so the story appears in all six reveals.
  - Beat 1 (heights): `characters_enriched_unknown_height_baseline` WARN — direct
    (gap closed 2aa845e).
  - Beat 2 (23/82): `characters_enriched_unknown_mass_baseline` WARN — direct.
  - Beat 3 (homeworlds): `characters_enriched_join_coverage` WARN — direct.
  - Beats 4–5 (42 one-film, all-six set): `character_stats_one_film_baseline` +
    `character_stats_six_film_trio` WARN — direct; `films_are_exactly_the_six_episodes`
    ERROR guards the frame.
  - Beat 6 (19 flew; max 5): `character_stats_pilot_count_baseline` +
    `character_stats_max_flown_baseline` WARN — direct, per-PERSON grain.
    `starship_stats` is per-SHIP and irrelevant to pilots claims.
- WARN severity is runtime-only in Dagster; `spec.blocking` is the static field —
  provenance encodes `blocking` and derives badge wording from it.
- Storage lies about types: load_table json.dumps's list fields into VARCHAR, so
  `len()` on them is string length; `json_array_length` is the honest count. Full
  displayed-SQL audit technique: `.claude/skills/panel-data-analyst-sql-display-audit/`.
- SNAPSHOT.json is a real dated snapshot (2026-07-17: 82 people / 6 films /
  36 starships / 60 planets / 37 species) — snapshot-gated compare tests are
  meaningful, not synthetic.
- Hardcoded number-words and counts in prose/aria labels are a drift surface; audit
  them whenever totals change (the beat-7 "undefined checks" overflow bug class).
- README screenshot open item now targets **13** green checks; land any future check
  count changes BEFORE retaking screenshots.

## Prep notes: improvement survey (2026-07-18)

Unused DATA fields verified by grep against the live `const DATA` line (line 390):
`birthYear` null for **39 of 82** (43 dated — biggest untold null story);
`people.species` null for **0 of 82** (fully populated, unused beyond scatter
table/tooltip); starship `cost` null for **10 of 36** (26 priced); `length`,
`speed`, `crew`, per-ship `films`/`pilots` all unused; planets payload
(climate/terrain/population/diameter/residents/films) and species payload
(classification/language/lifespan/members) unused beyond KPI counts. Redundant
grains now in DATA enable cross-foot checks: planets.residents vs
people.homeworld counts; species.members vs people.species counts;
starships.pilots edges vs people.starshipsFlown edges. Proposed top-3: (1)
cross-foot drift checks, S; (2) birthYear age census beat/card, M (needs
character_stats column for `direct`); (3) starship price board with cost
denominators, M (extend starship_stats).

## Banked: pipeline-reveal (2026-07-18) — compacted

Won: my false-beat-map prep finding drove the spec; check-badge honesty and the deep
pytest cross-check (topology, check ownership, blocking, verbatim rationales, exact
coverage set, honest guard typing) became law; the drift detector grew provenance
consistency checks. Lost: option (a) per-character grain lost on cost, then landed
later on merit (082d9c9) — lessons: lead with grain-correctness, not the diagram, and
keep a losing option's acceptance criteria specified to landing precision (that is
exactly what let it ship later with zero new debate; my assertion set shipped
verbatim, WARN-not-blocking per my severity law; the `derived` vocabulary made the
upgrade a clean testable flip to `direct`). Prep-differently residue: check
`spec.blocking` semantics myself; pre-rank either/or proposals and cost them; verify
rendering-tech assumptions in briefs early. All three open items from this round
(unverified SQL strings, beat-1 height gap, galaxy_report) were closed or resolved by
the post-landing cleanup — see below.

## Banked: post-landing cleanup (2026-07-18, commits c0b97e0 + 2aa845e)

**Won broadly (Q1 5–3–1 with my labels; Q2/Q3 unanimous):**
- Q1: re-authoring won and my number-free labels shipped almost verbatim ("all-six
  set", "pilot census", "flight record", "mass baseline"). The remedy exceeded my
  guard candidate: the spoiler pin covers numbers AND names, derived from known_facts,
  across all beats — not just my beat-4 assertion. Note WHY it won, though: the
  writer's one-home law (trio roster hand-listed in a check description = drift bug
  that could make the Dagster UI lie) and QA's unverifiable-`beat`-field point carried
  the room. My spoiler framing was correct but the DRIFT framing was decisive — frame
  string bugs as data-integrity bugs first.
- Q2: my compare-layer demand is law — tests/test_site_sql.py asserts each string's
  result set equals the DATA-derived chart rows, not merely that it executes. The
  droid recode moved INTO the gender SQL; both LIMIT-10 boards got name tiebreaks
  mirrored in the JS sorts; the dead `-- 59 of 82` comment died and
  `test_displayed_sql_carries_no_unverified_count_comments` pins the whole class;
  chart 5's card discloses its denominator, computed from DATA (my law in its best
  form — dynamic, not typed).
- Q3(a): the height-null WARN check landed exactly as I specced (mirror of the mass
  baseline, constant already in known_facts); beat 1 flipped pytest→check; all
  13-check ripples (WORDS through "thirteen", provenance totals, README/CLAUDE.md)
  rode the same commit. My checks-before-screenshots sequencing held.

**Lost / adjusted:**
- galaxy_report: I had carried "zero checks" as an open coverage gap; it is now
  DELIBERATE disclosed design (Exercise-8 collision + coverage-theater law). My own
  skill already said "design for the zero-check terminal asset rather than invent
  coverage" — I should have promoted that to a firm verdict instead of a hedge; QA
  got credit for the retraction I should have led.
- Data-engineer's write-back shape beat my implicit fix-the-strings-only scope:
  making `FROM characters_enriched` TRUE (same-df parity, table count frozen) is
  stronger than rewriting queries around a missing table. Lesson: when displayed SQL
  names a table that doesn't exist, first ask whether the table SHOULD exist.
- I opposed rail filtering and won on the coverage-understatement objection — but the
  designer's uniform-filter variant lost narrowly; the argument that saved my position
  was "character_stats has zero blocking checks, so final beats would understate
  forever." Keep that concrete counterexample style; abstractions about "disclosed
  coverage" alone would not have carried.

**Prep differently next time:** my execution-level audit (two provably wrong strings)
was the highest-value artifact in the debate — but the orchestrator still had to run
the queries live to clinch it (1222 "characters" for Episode I, two
CatalogExceptions). Where a read-only DuckDB run against the fixture is possible in
prep, do it and quote the outputs; "cannot verify offline" cost me the final 10% of
the argument I had already won on paper.
