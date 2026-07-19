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
- **Displayed SQL is executed SQL (2026-07-18, commit c0b97e0):** any SQL text shown
  on the site lives in `DATA.sql` (single source; the page renders only from DATA) and
  is executed against the fixture-built warehouse by the offline suite — ungated
  EXECUTE layer plus snapshot-gated COMPARE layer asserting each query's result set
  equals the rows the chart derives from DATA (tests/test_site_sql.py). Recodes
  (gender→droid) and LIMIT-10 name tiebreaks live IN the SQL, mirrored in the JS
  sorts; numeric comments inside displayed SQL are a banned, pytest-pinned class.
  `characters_enriched` is written back to the warehouse (same df it returns, full_run
  parity; EXPECTED_DB_TABLES stays five) so `FROM characters_enriched` is true —
  framed as closing a warehouse gap, never as "making the site's SQL true."
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
  parser broke" must fail differently.
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
- **Measured-vs-inferred labeling (2026-07-19, watchlist):** any decision resting on
  unreachable hardware/browser states records its MEASURED facts and its INFERENCES
  separately, verbatim, in the log. (My Q2 evidence gate, now law — the orchestrator
  ran the two-branch protocol before adjudicating.)
- **Anchoring restoration is not scroll-jacking (2026-07-19):** a synchronous,
  activation-triggered, measured-delta scroll correction that no-ops where the
  browser already anchors is the sanctioned shape for disclosure-growth compensation
  (capture summary top on click, `scrollBy` the measured delta, instant). Animated or
  assumed-delta variants stay banned. Verified render-only-style: recorded proxy
  evidence (anchoring-on 0px / anchoring-off −180px / fix restores 0px / no
  double-compensation), re-run on landed code — never a fakeable mechanical pin.
- **Acceptance is a decision with a tripwire (2026-07-19):** an accepted limitation
  enters the log with its reopening trigger written down. Q1 (hover-only whys):
  reopen if any why gains load-bearing content with no non-hover home, or legend line
  911 stops being true. Q4 (5px stage type): reopen if any anno carries content
  absent from copy/caption; any viewBox rework arrives with the 8-state
  anchor-geometry re-verification costed.
- **The census conceit is load-bearing (2026-07-19):** the stage tooltip is the ONLY
  surface naming most of the 82 individuals; no input modality may be cut off from
  it. Dashboard tables are a different grain — "the number exists elsewhere" is not
  redundancy when the identity channel doesn't.
- **Exposure changes reach, not content (2026-07-19):** widening a verified string's
  audience renders the same string verbatim from its one home; if it doesn't fit the
  vessel, change the vessel.

## Working knowledge

- Nulls are the story, not noise: the mass beeswarm's 23 missing values and the
  homeworld join's misses are disclosed in captions — this pattern must extend to any
  new claim.
- The drift detector (site/index.html) recomputes {total, noMass, noHeight, oneFilm,
  naboo, tatooine, pilots, maxFlown, undatedBirth, oldestBby} from `DATA.people` and
  compares against expectations, plus the six-film-trio exact-set check, provenance
  internal consistency, that every SQL disclosure resolves a nonempty DATA entry
  (includes "ages"), and the coda digit-pin.
- Chart honesty conventions in force: log scale flagged in captions; excluded rows
  named; Chart/Table toggle exposes rows per card; denominators computed, never typed
  (e.g. chart 5's "Top 10 of the ${rated}" subtitle).
- **Check→claim relevance map** (re-verified 2026-07-18 after 2aa845e):
  - Beat 0 (82): `raw_people_count_matches_verified_snapshot` WARN +
    `raw_people_has_required_shape` ERROR — direct; best-guarded number on the site;
    raw_people heads every chain so the story appears in all six reveals.
  - Beat 1 (heights): `characters_enriched_unknown_height_baseline` WARN — direct.
  - Beat 2 (23/82): `characters_enriched_unknown_mass_baseline` WARN — direct.
  - Beat 3 (homeworlds): `characters_enriched_join_coverage` WARN — direct.
  - Beats 4–5 (42 one-film, all-six set): `character_stats_one_film_baseline` +
    `character_stats_six_film_trio` WARN — direct; `films_are_exactly_the_six_episodes`
    ERROR guards the frame.
  - Beat 6 (19 flew; max 5): `character_stats_pilot_count_baseline` +
    `character_stats_max_flown_baseline` WARN — direct, per-PERSON grain
    (`starship_stats` is per-SHIP, irrelevant to pilot claims).
  - Registry card (39/43/896): the two birth-year checks WARN — direct via
    `character_stats.birth_year_bby`; DATA.sql.ages executed + compared.
- WARN severity is runtime-only in Dagster; `spec.blocking` is the static field —
  provenance encodes `blocking` and derives badge wording from it.
- Storage lies about types: load_table json.dumps's list fields into VARCHAR, so
  `len()` is string length; `json_array_length` is the honest count. Full audit
  technique: `.claude/skills/panel-data-analyst-sql-display-audit/`.
- SNAPSHOT.json is a real dated snapshot (2026-07-17: 82 people / 6 films /
  36 starships / 60 planets / 37 species) — snapshot-gated compares are meaningful.
- Hardcoded number-words and counts in prose/aria labels are a drift surface; audit
  them whenever totals change. Screenshots retaken at **15** green checks (f170379).
- **Stage-type mover hazards (recorded in watchlist log):** the hygiene font-size
  scanner attributes @media-block declarations to the `@media` selector string, so
  pins never match inside media queries — an in-scale bump of a pinned selector
  passes SILENTLY; `.anno-name` is 12px, in-scale, unpinned. `.axis-t`/`.anno-t` are
  shared with the measured-px dashboards. Any future raise inherits all of this plus
  beat 5's 20-viewBox-unit witness-name stack (~8px effective ceiling @360).
- Improvement residue (unbuilt): starship `cost` null for 10 of 36 (26 priced —
  price-board candidate with denominators); planets/species payloads unused beyond
  KPI counts; redundant grains enable cross-foot drift checks (planets.residents vs
  people.homeworld; species.members vs people.species; starships.pilots vs
  people.starshipsFlown). Stage anno literals ("not weighed · 23", "Naboo · 11",
  "everywhere else · 61", "Obi-Wan · 5", …) sit next to locally computed collections;
  deriving the strings would upgrade warned copy to computed numbers — offer as a
  rider whenever the stage is touched, not a demand.

## Banked: earlier rounds (2026-07-18) — lessons only

- Pipeline-reveal: lead with grain-correctness, not the diagram; keep a losing
  option's acceptance criteria specified to landing precision (per-character grain
  later shipped with zero new debate — `derived`→`direct` was a clean flip); verify
  `spec.blocking`-style semantics and rendering assumptions myself in prep.
- Post-landing cleanup (c0b97e0 + 2aa845e): frame string bugs as data-integrity bugs;
  when displayed SQL names a missing table, ask whether the table SHOULD exist; wins
  ride concrete counterexamples; run read-only DuckDB against the fixture in prep and
  quote outputs — "cannot verify offline" costs the last 10% of a won argument.

## Banked: birth registry + polish (2026-07-19, 1f3cf9e…f170379) — compacted

Won the card shape nearly verbatim (zero numeric literals; all counts from DATA);
lost 7–1 on one-check economy — that loss IS the failure-mode-separation law above.
Before defending any single-guard position, enumerate the derivation path's distinct
failure modes (source drift / parse breakage / join loss / render drift) and check
each fires a guard alone; "parsed display number" triggers the two-guard law.

## Banked: token hygiene (2026-07-19, a30a5bc) — compacted

Won: JS-scanning hard veto (residues enumerated with line numbers beat
coverage-theater as an abstraction); 11.5 stratum hold 3–2 with the `w > 46` gate
named in the pin's reason string; (selector, value, reason) both-directions pins are
now the default exemption shape; no font-size tokens; gold-once byte pins. Lost the
gender-label #fff: ux's contrast math showed no single ink passes both segments —
landed per-rank ink from the same ladder array, every pair ≥4.5:1 verified. Lessons:
run the contrast math myself on any ink I touch (an unreadable denominator is an
undisclosed denominator); spec exemptions as both-directions pins from the start;
name a held position's dependency inside the pin's reason string.

## Banked: watchlist round (2026-07-19, decision log + commit fdd3178)

**Won, and why:**
- **Q2 EVIDENCE GATE was the round's pivot.** The orchestrator executed my exact
  two-branch protocol BEFORE adjudication: anchoring-on 0px; anchoring-off −180px
  (Safari condition reproduced); fix restores 0px in both states — no
  double-compensation. "Measured-vs-inferred labeling" is now Settled, verbatim my
  must-have. Landed shape confirmed in fdd3178: revealAnchor capture + measured-delta
  instant `scrollBy` (index.html:476–484). What carried it: I specified the gate to
  run-book precision (branch matrix + expected values), which converted a debate into
  a measurement. A well-specified protocol gets EXECUTED, not just cited.
- **Q4 accepted unanimously on my redundancy-alone warrant** — the
  channel-redundancy-audit skill was cited as the acceptance's warrant, and my
  condition is quoted in the log: the pinned tooltip is "a bonus, NOT the
  justification." Never let a new feature retroactively become the load-bearing
  excuse for an acceptance argued on other grounds.
- **Q1 accept won 4–2** (my verdict): whys are rationale, not gated data; the visible
  label + severity is the complete claim; tripwire recorded.

**Lost, and why — Q3 framing.** Tap-to-pin (my first rank) shipped 5–1, but my
"convenience, not access" framing lost to the census-conceit veto: I audited whether
the VALUES were reachable elsewhere (dashboard tables) and missed that the tables are
a different GRAIN — the stage tooltip is the only surface naming most of the 82
individuals. Redundancy is defined at the grain of the claim, not the value: a number
with no identity channel is not redundant coverage. Extend the channel-redundancy
audit to check name/identity reach per modality, not just numeric twins.

**Prep differently:** when running a redundancy audit, state each channel's grain
explicitly and ask what claim DIES if the channel dies (lore saw the census conceit;
my orphan scan didn't); write evidence gates as executable run-books — matrix,
expected values, pass/fail — since the orchestrator will run them; when an acceptance
and a new feature land together, put the "bonus, not justification" separation in
writing before synthesis, as I did here — it held.
