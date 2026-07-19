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
- **15 checks (4 blocking / 11 WARN) as of 1f3cf9e:** birth registry added
  `character_stats_birth_year_baseline` + `character_stats_birth_year_parse_honesty`
  (both WARN). `galaxy_report` stays check-free BY DESIGN (WORKSHOP Exercise-8
  collision + coverage-theater law) — deliberate, disclosed. Stop flagging it.
- **Birth registry baselines (2026-07-19, commit 1f3cf9e):** **39 of 82** have no
  birth year on file; **43** dated; oldest on file **896 BBY (Yoda)**; all 43 dated
  values are BBY, zero ABY. Frozen in known_facts (EXPECTED_UNDATED_BIRTH_COUNT,
  EXPECTED_DATED_BIRTH_COUNT, OLDEST_BIRTH_BBY, OLDEST_DATED_CHARACTER); parsed
  in-pipeline as `character_stats.birth_year_bby` (sign-safe: ABY parses negative,
  tested on synthetics). Registry card computes every count from DATA in JS — zero
  numeric literals.
- **Failure-mode separation law (2026-07-19, 7–1 — I was the 1):** any displayed
  number derived through a parse gets TWO guards — a drift baseline AND a
  data-independent parse-honesty invariant — because "the data moved" and "the
  parser broke" must fail differently. Without parse-honesty, "39 undated" can
  silently mean "39 unparsed" while the badge glows green.
- **Gold ring means "extreme" (2026-07-19):** persistent gold emphasis asserts
  superlatives only; named non-extremes (Vader) get labels, never rings.
- **Quoted-testimony rule (2026-07-19):** external claims (dialogue, canon — e.g.
  Yoda's "900 years") may be audited in copy but never rendered as site-derived
  data; derived numbers come only from DATA.
- **Absence pins are legitimate guards (2026-07-19):** an element exempted from a
  detector by a property (number-free coda) gets a pin asserting that property;
  pinning wording is theater. The coda digit-pin is an absence assertion.
- **Gender legend conversion (2026-07-19):** segment names + counts summing to 82
  stay visible via the CONVERTED legend (opacity ladder via color-mix; bar/legend/
  tooltips carry identical colors). Legend counts are part of the denominator law.
- **WORKSHOP.md is on the count-ripple checklist;** teaching prose states counts
  count-free unless the count is the lesson. Q4 "Limits, by design" bullets are
  number-free by law.

## Working knowledge

- Nulls are the story, not noise: the mass beeswarm's 23 missing values and the
  homeworld join's misses are disclosed in captions — this pattern must extend to any
  new claim.
- The drift detector (site/index.html) recomputes {total, noMass, noHeight, oneFilm,
  naboo, tatooine, pilots, maxFlown, undatedBirth, oldestBby} from `DATA.people` and
  compares against expectations, plus the six-film-trio exact-set check, provenance
  internal consistency (claims cover beats 1–6, chain ids resolve, badges derive from
  `blocking`, beat-7 callback counts, number-word list overflow), that every SQL
  disclosure resolves a nonempty DATA entry (list now includes "ages"), and the coda
  digit-pin.
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
  - Registry card (39/43/896): `character_stats_birth_year_baseline` +
    `character_stats_birth_year_parse_honesty` WARN — direct via
    `character_stats.birth_year_bby`; DATA.sql.ages executed + compared with the
    positive-BBY pin.
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
  Screenshots retaken at **15** green checks (f170379); checks-before-screenshots
  sequencing held again.
- Improvement-survey residue (2026-07-18, still unbuilt): starship `cost` null for
  10 of 36 (26 priced — price-board candidate with denominators); planets/species
  payloads unused beyond KPI counts; redundant grains enable cross-foot drift checks
  (planets.residents vs people.homeworld; species.members vs people.species;
  starships.pilots vs people.starshipsFlown). birthYear item shipped 2026-07-19.

## Banked: pipeline-reveal (2026-07-18) — compacted

Won: false-beat-map prep drove the spec; check-badge honesty and the deep pytest
cross-check became law. Lost: per-character grain lost on cost, then landed later on
merit (082d9c9) — lessons: lead with grain-correctness, not the diagram; keep a
losing option's acceptance criteria specified to landing precision (that let it ship
later with zero new debate; the `derived` vocabulary made the upgrade a clean flip
to `direct`). Prep residue: check `spec.blocking` semantics myself; pre-rank
either/or proposals and cost them; verify rendering-tech assumptions early. All
three open items from this round were closed by the post-landing cleanup.

## Banked: post-landing cleanup (2026-07-18, c0b97e0 + 2aa845e) — compacted

Won: number-free check labels shipped verbatim; the spoiler pin exceeded my guard
candidate (numbers AND names, derived from known_facts, all beats); my compare-layer
demand became law (test_site_sql.py asserts result sets equal DATA-derived chart
rows); recodes/tiebreaks moved INTO the SQL; unverified count-comments are a pinned
banned class; the height-null WARN check landed as specced with all count ripples in
one commit. Decisive lesson: my spoiler framing was correct but the writer's DRIFT
framing carried the room — frame string bugs as data-integrity bugs first.
Lost/adjusted: galaxy_report zero-checks is deliberate design (I hedged where my own
skill had the firm answer — promote skill guidance to verdicts); the engineer's
write-back (make `FROM characters_enriched` TRUE) beat my fix-the-strings scope —
when displayed SQL names a missing table, ask whether the table SHOULD exist; my
anti-rail-filtering win rode a concrete counterexample ("character_stats has zero
blocking checks, so final beats would understate forever"), not abstractions.
Prep-differently: run read-only DuckDB against the fixture in prep and quote outputs;
"cannot verify offline" cost the final 10% of an argument already won on paper.

## Banked: birth registry + polish (2026-07-19, commits 1f3cf9e/4d92cb7/7d96df5/f170379)

**Won:** card shape shipped nearly verbatim — "39 of 82" headline, "43 of 82 dated"
denominators, youngest-dated Wicket line, every count computed from DATA in JS with
zero numeric literals; drift detector gained undated=39 / oldestBby=896;
DATA.sql.ages executed + compared with the positive-BBY pin; the Vader ruling is law
(labeled, unringed — held against annotation creep); gender legend kept name+count
summing to 82 riding the designer's opacity ladder; coda digit-pin won as I framed
its half (absence assertion; wording-pin rightly dropped per QA); Q4 bullets shipped
number-free as demanded.

**Lost — and the loss is the lesson:** one-check economy, 7–1. I argued a single
baseline check was sufficient; the room's failure-mode argument was better ON MY OWN
TERMS: the baseline compares a count against a constant, but if the source format
changes, the parser nulls everything, "undated" swells to absorb the breakage, and —
because 39 could still match by coincidence during partial breakage, or the failure
reads as drift when it's a bug — the badge asserts a number whose MEANING changed.
Parse-honesty (each null traces to a literal 'unknown' raw string) is data-
independent and separates "the data moved" from "the parser broke." That IS
denominator honesty: "39 undated" and "39 unparsed" are different claims wearing the
same digits. I optimized check count (economy) over failure semantics; my own
coverage-theater instinct misfired against a check that carries real information.
Rule of thumb banked: economy arguments only beat redundancy arguments when the two
guards would fail for the SAME reason.

## Prep notes: token hygiene + raise-only small type (2026-07-19)

- **11.5px is the data-ink stratum.** The whole cluster carries quantitative claims:
  `.axis-t` (denominator endcaps — "82 characters", "youngest dated · Wicket, 8 BBY"),
  `.val-t` (bar value labels at `x(d.n)+7`, right of bars — raise risks right-edge
  clipping), `.anno-t` (registry "Name · N BBY" annos, line 1359), the JS gender
  %-label (line 1131–1132: `fill:"#fff"`, `"font-size":"11.5"` as unitless SVG attr),
  and `.prov-check` (settled badge-only exception). Any raise here needs 360/390px
  re-verification of: val-t clipping, anno staggering, densest prov rail wrap.
- **Gender %-label has a hardcoded fit gate:** renders only when `w > 46` px
  (line 1130). The 46 was tuned for 11.5px; a raise-only merge to 12 must re-derive
  or re-verify that constant, else a wider label overflows the segment it certifies.
  The label is data ink (rounded %, tooltip carries the .1f exact) — its `#fff`
  belongs in the token system; the starfield `#cdd8ef` (line 489, aria-hidden
  decorative canvas) does not — sanctioned literal + comment + guard allow-list
  beats a getComputedStyle bridge that adds init-order risk for zero data payoff.
- **JS-side literal habitats a `<style>`-only scraper would miss** — all four current
  residues live in JS, not CSS: canvas `fillStyle` (489), anno small-label attr
  `font-size = 11` (747), gender label attrs (1131–32), registry caption inline
  `cssText` `font-size:13px` (1374). A hygiene guard scanning only `<style>` is
  coverage theater. Preferred fix: convert SVG attr font-sizes to CSS classes (a
  `.seg-t` for the gender label; reuse existing classes elsewhere) so the guard can
  assert "no font-size/fill literals in JS outside an explicit allow-list."
  Scraper must handle unitless SVG attrs AND `px` forms, and must exclude the
  one-line `const DATA` literal (load-bearing; never regex-mangle it).
- **Guard home:** this is structural, not data-vs-copy — it belongs in the offline
  pytest suite (doctype/lang precedent), NOT the runtime drift detector, which
  grows with claims only. One test, existing suite, no second lint framework;
  lands in the same commit as the consolidation.
- Line 1374 caption is a model citizen: computes `dated.length` from DATA and gates
  the literal "896 BBY" behind `oldest.name==="Yoda" && oldest.bby===896`.
- Raising `.prov-check` 11.5→12 is technically raise-only and would dissolve the
  settled exception — acceptable to me ONLY with densest-rail 360px re-wrap proof;
  otherwise keep the exception as-is (settled: never propagate, never shrink).
- No numbers change in this brief; drift detector untouched. My stale-note check:
  none of my notes reference the four already-tokenized hexes — memory clean.

**Prep differently:** before defending a single-guard position, enumerate the
distinct failure modes of the value's derivation path (source drift / parse
breakage / join loss / render drift) and check each has a guard that fires alone.
Had I run that enumeration in prep, I'd have proposed the second check myself —
qa-engineer and hiring-manager took the point that was natively mine (badge-glows-
while-lying is MY guard-honesty law). Also: when a number passes through a parse,
say "parsed display number" in my verdict explicitly — that phrase triggers the
two-guard law now settled above.
