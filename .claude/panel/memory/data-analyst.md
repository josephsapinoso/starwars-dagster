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
- **Token hygiene law (2026-07-19, a30a5bc):** *Whisper clause* — every sanctioned
  style exception is an exact (selector, value, reason) pin in
  `test_site_style_hygiene.py`, failing loudly on change in EITHER direction.
  *Scenery is not ink* — decorative paints (aria-hidden canvas `#cdd8ef`) may stay
  literals with a required sanction comment; data ink is tokenized; no runtime
  bridges for decoration. *Ink adapts to its ground* — on-mark labels pick ink per
  computed ground from the SAME array that drives the ground; every rendered pair
  ≥4.5:1, verified computationally; never a new hex. *The registry is the test* —
  the sanctioned type scale's one machine-readable home is the structural pytest;
  no font-size tokens. *Raise-only grants permission, not obligation* — the 11.5
  data-ink stratum (.axis-t/.val-t/.anno-t/.seg-pct with its `w > 46` gate, plus
  the .prov-check badge) stands still without evidence; MOVING it needs
  collision/clipping/gate evidence. Gold literal exactly once, in :root,
  `var(--gold)` free.

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

Won: number-free labels, spoiler pin (numbers AND names, from known_facts), the
compare layer (test_site_sql.py: result sets equal DATA-derived chart rows),
recodes/tiebreaks INTO the SQL, count-comments banned class. Lessons: frame string
bugs as data-integrity bugs first (writer's DRIFT framing carried my correct
point); when displayed SQL names a missing table, ask whether the table SHOULD
exist (engineer's write-back beat my fix-the-strings scope); wins ride concrete
counterexamples, not abstractions; run read-only DuckDB against the fixture in prep
and quote outputs — "cannot verify offline" costs the last 10% of a won argument.

## Banked: birth registry + polish (2026-07-19, 1f3cf9e…f170379) — compacted

Won: card shape shipped nearly verbatim (39-of-82 headline, 43-of-82 dated, zero
numeric literals — all counts from DATA); drift detector grew undated/oldestBby;
Vader ruling, coda digit-pin (absence half), number-free Q4 all held. Lost 7–1 on
one-check economy, and the loss IS the lesson: "39 undated" and "39 unparsed" are
different claims wearing the same digits — parse-honesty is data-independent and
separates "data moved" from "parser broke." Economy arguments only beat redundancy
arguments when the two guards would fail for the SAME reason. Before defending any
single-guard position, enumerate the derivation path's distinct failure modes
(source drift / parse breakage / join loss / render drift) and check each fires a
guard alone; say "parsed display number" out loud — it triggers the two-guard law.

## Banked: token hygiene (2026-07-19, decision log + commit a30a5bc)

**Won, and why:**
- **Hard veto CARRIED — the guard scans JS** (`test_no_style_literals_outside_the_style_block`);
  the four JS residues gone or pinned. What carried it: prep enumerated the residues
  with line numbers and showed a `<style>`-only scraper misses ALL of them —
  "coverage theater" with a concrete inventory beats it as an abstraction.
- **11.5 data-ink-stratum hold WON (3–2);** `w > 46` gate untouched because
  `.seg-pct` stays 11.5, and the pin's reason string NAMES the gate — my dependency
  argument, verbatim. Winning frame was evidence-burden, not taste: the designer's
  integer collapse died on unfunded verification cost.
- **Starfield allow-list + required comment shipped verbatim**
  (`test_sanctioned_literals_are_pinned_and_commented`; line-491 comment cites the
  decision); init-order-risk-for-zero-data-payoff beat the bridge. But the
  storyteller's (selector, value, reason) triple is the DURABLE form of my
  allow-list — the fails-in-both-directions pin is what kills rot. Default shape now.
- **No font-size tokens (5–1)** — executable test beats prose ledgers AND beats
  minting variables to feed a test. **Gold exactly once** landed as byte-pattern
  pins with `var(--gold)` explicitly free (line-693 ceremony safe).

**Where the room beat me — gender label:** I said "tokenize the #fff"; ux showed it
fails AA (~3.6:1) and the orchestrator's contrast math proved NO single ink passes
both labeled segments. Landed: per-rank ink from the ladder index that drives the
segment color (`--void` rank 1, `--ink` tinted ranks), every rendered pair verified
≥4.5:1 computationally, pre-authorized fallback = drop in-segment % (legend + table
carry the data). Labels stayed; no false-claim risk. Lesson: I audited the label as
data ink but never checked its contrast — an unreadable denominator is an
undisclosed denominator. Legibility of data ink is inside my remit.

**Prep differently:** run the contrast math myself on any ink I touch (same rigor as
running DuckDB on the fixture); when proposing an exemption, spec it as a
both-directions pin from the start, not a comment; when I hold a position on a
dependency (the 46px gate), get the dependency named IN the pin's reason string —
that is what makes the hold self-enforcing after I leave the room.
