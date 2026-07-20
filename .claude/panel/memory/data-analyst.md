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
  (Akabab lands 15→20 checks, assets 11→13, transforms 4→5 — totals pin ripple.)
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
  parser broke" must fail differently. (Scope boundary, 2026-07-20: key-PRESENCE
  counts are not parses — one guard suffices; the law triggers on parsing.)
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
  separately, verbatim, in the log. (My Q2 evidence gate, now law.)
- **Anchoring restoration is not scroll-jacking (2026-07-19):** a synchronous,
  activation-triggered, measured-delta scroll correction that no-ops where the
  browser already anchors is the sanctioned shape for disclosure-growth compensation
  (capture summary top on click, `scrollBy` the measured delta, instant). Animated or
  assumed-delta variants stay banned. Verified render-only-style: recorded proxy
  evidence re-run on landed code — never a fakeable mechanical pin.
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
- **Akabab warehouse shape is Option C (2026-07-20, unanimous):** `star_wars_db`
  stays byte-identical; `EXPECTED_DB_TABLES` stays 5; `character_biographies` is a
  transform-join (02_transformed); coverage misses surface via check metadata.
  Revisit raw-akabab-in-warehouse ONLY if a surfacing panel needs it in displayed
  SQL (my evidence condition, recorded in the log).
- **Nested denominators on enrichment joins (2026-07-20):** every number off a
  second source reads "N of field-present of 81 matched of 82" — report-copy
  discipline COMPUTED from the data, not per-field checks (qa's five-check ceiling
  won the mechanism; the convention is mine and stands). No superlatives from
  sparse lineage fields (masters ~15/87); affiliations rank only with n disclosed.
- **"On file" vocabulary (2026-07-20):** akabab death data is "deaths on file"
  everywhere — never "deceased", never saga-scoped or canon-complete. "Absence is
  not survival." Constant `EXPECTED_DEATHS_ON_FILE`; check
  `character_biographies_deaths_on_file_baseline` (WARN, ships with the report
  number under my symmetry rule: report prints it → drift guard same commit).
- **Signed-year columns name their convention (2026-07-20):** `_bby`/`_aby` suffix
  required; no bare year columns in the warehouse (`died` → `died_year_aby`).
- **Cross-source derived figures are quoted-testimony territory (2026-07-20):**
  SWAPI-birth × akabab-death arithmetic (the Yoda 896+4=900 derivation) is
  pre-vetoed off all surfaces until a surfacing panel rules.
- **Alias governance (2026-07-20):** curated dict in known_facts with a
  canon-direction comment per entry; aliases BRIDGE the join, never mutate as-filed
  records (`character_name` keeps SWAPI's spelling); ungated pytest for injectivity
  + every-alias-load-bearing; resolution-vs-fixture assertions dual-snapshot-gated;
  no fuzzy matching, ever.
- **Baselines are computed, never transcribed (2026-07-20):** enrichment baselines
  (EXPECTED_PROFILE_COUNT / _MATCH_COUNT / _DEATHS_ON_FILE, final aliases) are
  frozen by script from the real fixture at the freeze-reality commit. Three
  independent surveys disagreed (87 vs 88 records; died 47 vs 28) — survey numbers
  never become displayed numbers or baselines.
- **The WORDS number-renderer is a guard surface (2026-07-20):** it grows (with its
  pytest pin — `len(WORDS)` exceeds every DATA-rendered count) in the same commit
  as any count it must spell.

## Working knowledge

- Nulls are the story, not noise: the mass beeswarm's 23 missing values and the
  homeworld join's misses are disclosed in captions — extend to every new claim.
- The drift detector (site/index.html) recomputes {total, noMass, noHeight, oneFilm,
  naboo, tatooine, pilots, maxFlown, undatedBirth, oldestBby} from `DATA.people` and
  compares against expectations, plus the six-film-trio exact-set check, provenance
  internal consistency, that every SQL disclosure resolves a nonempty DATA entry,
  and the coda digit-pin.
- Chart honesty conventions in force: log scale flagged in captions; excluded rows
  named; Chart/Table toggle exposes rows per card; denominators computed, never
  typed (e.g. chart 5's "Top 10 of the ${rated}" subtitle).
- **Check→claim relevance map** (re-verified 2026-07-18 after 2aa845e):
  - Beat 0 (82): `raw_people_count_matches_verified_snapshot` WARN +
    `raw_people_has_required_shape` ERROR — direct; best-guarded number on the site.
  - Beat 1 (heights): `characters_enriched_unknown_height_baseline` WARN — direct.
  - Beat 2 (23/82): `characters_enriched_unknown_mass_baseline` WARN — direct.
  - Beat 3 (homeworlds): `characters_enriched_join_coverage` WARN — direct.
  - Beats 4–5 (42 one-film, all-six set): `character_stats_one_film_baseline` +
    `character_stats_six_film_trio` WARN; `films_are_exactly_the_six_episodes`
    ERROR guards the frame.
  - Beat 6 (19 flew; max 5): `character_stats_pilot_count_baseline` +
    `character_stats_max_flown_baseline` WARN — per-PERSON grain
    (`starship_stats` is per-SHIP, irrelevant to pilot claims).
  - Registry card (39/43/896): the two birth-year checks WARN — direct via
    `character_stats.birth_year_bby`; DATA.sql.ages executed + compared.
- Akabab guards landing (per plan): blocking shape contract exactly `{id,name}`;
  blocking grain check (rows == people count AND character_name unique) fires ALONE
  on fan-out — join inflation is loss's twin; coverage WARN emits unmatched names
  both directions; masters/apprentices stored as JSON strings + counts, display-only,
  never join keys. QA's seen-to-fail matrix runs before merge.
- WARN severity is runtime-only in Dagster; `spec.blocking` is the static field —
  provenance encodes `blocking` and derives badge wording from it.
- Storage lies about types: load_table json.dumps's list fields into VARCHAR, so
  `len()` is string length; `json_array_length` is the honest count. Full audit
  technique: `.claude/skills/panel-data-analyst-sql-display-audit/`.
- SNAPSHOT.json is a real dated snapshot (2026-07-17: 82 people / 6 films /
  36 starships / 60 planets / 37 species); akabab gets its own SNAPSHOT marker with
  fixture provenance labeled (synthetic period declared, transition commit named).
- Hardcoded number-words and counts in prose/aria labels are a drift surface; audit
  on any totals change. Screenshots retaken at 15 green checks (f170379);
  hiring-manager's retake reflex applies when visuals show check/asset counts.
- Stage-type mover hazards (watchlist log): the hygiene font-size scanner misses
  @media-block declarations, so pinned selectors can move in-scale SILENTLY inside
  media queries; `.anno-name` 12px is in-scale, unpinned; `.axis-t`/`.anno-t`
  shared with measured-px dashboards; beat 5 has an ~8px effective ceiling @360.
- Improvement residue (unbuilt): starship `cost` null for 10 of 36 (26 priced);
  planets/species payloads unused beyond KPI counts; redundant grains enable
  cross-foot drift checks (planets.residents vs people.homeworld, etc.). Stage anno
  literals ("not weighed · 23", "Obi-Wan · 5", …) could be derived from the adjacent
  computed collections — offer as a rider whenever the stage is touched.
- Surfacing-panel tripwires on record (akabab log): Yoda 896+4=900 pre-vetoed; if
  `character_biographies` joins a beat chain, spoiler-pin term sets extend in that
  landing; `DATA.meta` dual-source format, provenance entries, image field, and
  signed-year display all deferred — do not build ahead of the panel.

## Banked lessons: 2026-07-18/19 rounds — compacted

- Lead with grain-correctness, not diagrams; keep losing options specified to
  landing precision (per-character grain later shipped debate-free).
- Frame string bugs as data-integrity bugs; when displayed SQL names a missing
  table, ask whether the table SHOULD exist; run read-only DuckDB against fixtures
  in prep and quote outputs — "cannot verify offline" costs the last 10%.
- Birth registry: won the zero-numeric-literals card shape; lost 7–1 on one-check
  economy — that loss IS the failure-mode-separation law. Enumerate a derivation
  path's distinct failure modes (source drift / parse breakage / join loss / render
  drift) before defending any single-guard position.
- Token hygiene: enumerated residues with line numbers beat abstractions; lost the
  single-ink gender label to ux's contrast math — run contrast math myself on any
  ink I touch; spec exemptions as both-directions pins from the start.
- Watchlist: a well-specified evidence gate (branch matrix + expected values) gets
  EXECUTED, not just cited — write them as run-books. Redundancy is defined at the
  grain of the CLAIM, not the value: I audited numeric twins and missed that the
  stage tooltip was the only identity channel — ask what claim dies if a channel
  dies. Put "bonus, not justification" separations in writing before synthesis.

## Banked: akabab second source (2026-07-20)

**Won, and why:**
- **Option C ratified unanimously** — my verdict, including my recorded evidence
  condition for ever revisiting Option A (displayed-SQL need only).
- **Nested-denominator convention adopted** and embedded verbatim in storyteller's
  drafted report copy, including the closing "absence is not survival" line; my
  sparse-field superlative trap landed as law (no lineage superlatives; rank only
  with n disclosed).
- **Symmetry rule decided Q3:** the report prints the deaths-on-file number, so its
  drift guard lands in the same commit — my conditional ("ship the check only if
  the number surfaces this round") resolved TRUE and became the adjudication's
  stated warrant.
- **Frozen-fixture baselines won and were immediately vindicated:** my prep's
  distrust of fast-model JSON counts (my fetch said 88/died-28 vs the brief's
  87/died-47) became final-plan item 6 — three disagreeing surveys cited as proof
  that transcription is not a baseline method. Flagging my OWN evidence as
  unreliable bought credibility and won the mechanism.
- **Grain-fires-alone** made qa's seen-to-fail acceptance matrix (duplicate-name
  fan-out demo before merge).

**Lost / conceded, and why:**
- **Per-field baseline checks lost to qa's five-check ceiling.** Right call: the
  denominators are copy discipline computed from data at render time; a check per
  sparse field is guard-for-guard's-sake. I conceded the mechanism, kept the
  convention — the concession is what got the convention adopted unanimously.
- **Two-guard law scope narrowed (correctly):** deaths-on-file is key-presence,
  not a parse — one guard suffices. Banked as a scope boundary on the law itself.
- **"Deceased" → "deaths on file":** lore caught that akabab deaths are
  sequel-inclusive AND canon-incomplete, so "deceased" overclaims in BOTH
  directions. I policed denominators but not the noun — vocabulary is part of the
  claim's honesty surface.

**Prep differently next time:**
- Draft my denominator lines as ready-to-ship copy, not conventions — storyteller's
  verbatim drafted copy won the section-title tiebreak on as-filed grounds; drafted
  artifacts beat described intentions.
- For any new source: put the freeze-by-script step and the survey-distrust
  statement in my first prep note, with my own count listed as one more unreliable
  survey.
- Audit nouns and vocabulary alongside numbers: ask what a count-word claims about
  completeness ("deceased" vs "on file"), not just whether the count is right.
