# Decision: akabab character API as the second data source

Date: 2026-07-20 · Scope: pipeline (+ minimal site ripple) · Panelists: data-engineer,
data-analyst, qa-engineer, hiring-manager, technical-writer, lore-fanatic, storyteller
(graphic-designer and ux-designer excused: no visual/UI surface changes).
Orchestrator/final decision: Claude (main session).

## Brief

Full brief preserved below (§Appendix). Summary: user-confirmed addition of
akabab/starwars-api (static MIT JSON, ~87 character records, GitHub Pages) as a second
source enriching the same cast SWAPI covers (affiliations, masters/apprentices,
born/died signed years, died locations, cybernetics). 81/82 SWAPI people match by exact
name. Site surfacing deferred; site touched only where the totals pin forces it.
Questions: Q1 warehouse shape (transform-join "Option C" vs sixth star_wars_db table
"Option A"), Q2 names, Q3 death-baseline check, Q4 alias governance, Q5 report
register/spoilers, Q6 deferrals.

## Per-role verdicts (one line each)

- **data-engineer**: Ratify C; veto bare `died` column (ABY/BBY sign trap → `died_year_aby`); blocking contract exactly `{id,name}`; alias bridges the join, never repairs SWAPI's as-filed records.
- **data-analyst**: Ratify C; nested-denominator convention (N of field-present of 81 matched of 82) on every enrichment number; grain check fires alone on fan-out; baselines computed from frozen fixture, never transcribed.
- **qa-engineer**: Ratify C; five checks is the ceiling; every guard seen-to-fail before merge; ungated alias-injectivity pytest + WORDS-overflow pytest pin; README counts stay a human checklist, no prose grep pins.
- **hiring-manager**: Ratify C (answers a new interview question); alias-honesty trio as one pytest; full docs ripple + screenshot retake in the feature commit; no sign-convention *check* — naming plus pytest suffices.
- **technical-writer**: Ratify C (keeps WORKSHOP:338 and "5 tables loaded" literally true); WORDS array at index.html:863 stops at "fifteen" → must grow same commit with a pytest pin; veto "Lineage" in the section title (pipeline-vocabulary collision).
- **lore-fanatic**: Ratify C; "deaths on file" vocabulary package (akabab deaths are sequel-inclusive AND canon-incomplete — "deceased" would overclaim); canon-direction comments on aliases (akabab "Ratts Tyerell" is canon, SWAPI holds the typo); akabab attributed as fan-curated + SWAPI-derived, never canon authority.
- **storyteller**: Ratify C; analyst register with drafted final copy; check strings number/name/payoff-free at birth; pre-veto on shipping the Yoda 896+4=900 derivation (quoted-testimony clause c) — written tripwire for the surfacing panel.

## Adjudication

- **Q1 — Option C, unanimous.** `star_wars_db` stays byte-identical; `EXPECTED_DB_TABLES`
  stays 5; misses surface via coverage-check metadata. Revisit only if a future surfacing
  panel needs raw akabab in displayed SQL (analyst's evidence condition).
- **Q2 — names.** `AkababResource` (separate class — the `.json` URL shape makes
  subclassing a lie), key `"akabab"`, `raw_character_profiles`, `character_biographies`
  all ratified. Amendments won: death column is **`died_year_aby`** (engineer's veto,
  seconded twice); check is **`character_biographies_deaths_on_file_baseline`** and
  constant **`EXPECTED_DEATHS_ON_FILE`** (lore's package, unopposed). Section title:
  technical-writer and lore proposed "Allegiances & Apprenticeships", storyteller's
  drafted copy says **"Affiliations & Apprenticeships"** — storyteller wins on the
  as-filed tiebreak: the source field is literally `affiliations`, and the drafted-copy
  discipline requires verbatim adoption. The lineage-collision veto is satisfied either way.
- **Q3 — deaths-on-file WARN check ships now**, under the analyst's symmetry rule: the
  report prints the number, so the number's drift guard lands in the same commit. One
  guard suffices (key-presence, not a parse — qa); it attaches to an unlisted asset (compliant).
- **Q4 — curated aliases in known_facts win, with governance teeth.** Engineer's framing
  beats lore's: the alias *bridges the join*; `character_name` keeps SWAPI's as-filed
  spelling — we do not mutate records. Lore's requirement stands: each entry's comment
  states the canon direction (akabab canon-correct, SWAPI typo). Guards: ungated pytest
  for injectivity (Vader/Anakin stay distinct) + every alias load-bearing (key ≠ value
  post-normalization); alias-resolution-against-fixtures assertions dual-snapshot-gated.
  No fuzzy matching, ever; the docs carry one why-not-fuzzy sentence.
- **Q5 — analyst register; storyteller's drafted copy adopted verbatim** (title, opening
  italics, per-table field denominators, closing "'On file' means the curated source
  records it — absence is not survival."). Nested denominators are report-copy discipline
  computed from the data, NOT new checks (qa's ceiling beats analyst's per-field
  baselines — analyst conceded the mechanism, kept the convention). No superlatives from
  sparse lineage fields (masters ~15/87): counts with denominators; affiliations may rank
  only with n disclosed. All five check descriptions subject-only, number/name/payoff-free.
- **Q6 — deferrals confirmed** (site surfacing, `DATA.meta` dual-source format,
  provenance entries, image field, signed-year display). **Carve-out won by
  tech-writer/qa**: the WORDS array is totals-pin ripple, not surfacing — it grows
  through "twenty" in the feature commit with a new pytest pin (`len(WORDS)` must exceed
  every DATA-rendered count). **Written tripwires for the surfacing panel**: (1) the
  Yoda 896+4=900 derivation is pre-vetoed — computing it from `died_year_aby` would
  launder the quoted-testimony audit into data; (2) if `character_biographies` ever
  joins a beat chain, extending the spoiler-pin term sets is part of that landing;
  (3) hiring-manager's screenshot-retake reflex applies when any site/README visual
  shows check/asset counts.

## Final plan (deltas to the approved implementation plan)

1. Column `died` → **`died_year_aby`**; code comment points at `birth_year_bby`'s
   opposite sign convention. No sign-convention asset check.
2. Check renamed **`character_biographies_deaths_on_file_baseline`**; constant
   **`EXPECTED_DEATHS_ON_FILE`**; all report copy says "deaths on file" / "on file",
   never "deceased".
3. galaxy_report section: **"Affiliations & Apprenticeships"**, storyteller's copy,
   nested denominators on every line, no lineage superlatives.
4. Commit 2 additionally carries: WORDS array growth (through "twenty") + new pytest pin
   on WORDS coverage; alias-honesty pytest (injectivity + load-bearing, ungated;
   resolution assertions dual-gated); README ASCII architecture diagram + :16/:79 test
   list + tree comments + Stack attribution ("fan-curated, MIT, effectively frozen;
   SWAPI-derived — reproduces SWAPI's spellings"); WORKSHOP:299 rewritten count-free.
5. QA's seen-to-fail acceptance matrix: before merge, demonstrate grain check failing on
   an inline duplicate-name pair, shape check failing on a missing-`name` record,
   coverage WARN emitting unmatched names both directions.
6. Baselines (`EXPECTED_PROFILE_COUNT`, `EXPECTED_PROFILE_MATCH_COUNT`,
   `EXPECTED_DEATHS_ON_FILE`, final `PROFILE_NAME_ALIASES`) are computed by script from
   the frozen real fixture at commit 4 — three independent surveys disagreed (87/88
   records; died 47/28), proving transcription is not a baseline method.
7. Fixture provenance labeled: akabab fixtures README declares the synthetic period;
   commit 4's message names the synthetic→real transition; masters/apprentices stored as
   JSON strings + counts, display-only, never join keys (prose contamination).

## Newly settled constraints (banked)

- Enrichment-join numbers always carry nested denominators: matched AND field-present.
- Death/`died` data from akabab is "on file" vocabulary everywhere; never "deceased",
  never saga-scoped or canon-complete claims.
- Signed-year columns name their convention in the column name (`_bby` / `_aby`);
  no bare year columns in the warehouse.
- Cross-source derived figures (SWAPI birth × akabab death arithmetic) are
  quoted-testimony territory: pre-vetoed off all surfaces until a surfacing panel rules.
- Name aliases between sources: curated dict in known_facts, canon-direction comment per
  entry, injectivity + load-bearing pytest, no fuzzy matching; aliases bridge joins, they
  never mutate as-filed records.
- The site WORDS number-renderer is a guard surface: it grows (with its pytest pin) in
  the same commit as any DATA-rendered count it must spell.

## CLAUDE.md upkeep

One line added to the hard-constraints digest: nested denominators + on-file vocabulary
+ no cross-source derived figures without a surfacing-panel decision.

## Appendix: full brief

(Verbatim from the prep/debate passes.)

The pipeline gains a SECOND data source: akabab/starwars-api — static MIT-licensed JSON
at https://akabab.github.io/starwars-api/api/all.json (GitHub Pages; ~87 character
records). It enriches the SAME cast SWAPI covers with fields SWAPI lacks:
affiliations[], formerAffiliations[], masters[], apprentices[], born/died (signed
years), bornLocation/diedLocation, cybernetics, image, wiki. Alternatives surveyed and
rejected: swapi.dev/swapi.tech (mirrors), SWAPI /vehicles (reserved as the WORKSHOP.md
reader exercise), Star Wars Databank API (prose-heavy, fuzzy joins, free-tier host),
Wookieepedia/Wikidata (unstructured). 81/82 SWAPI people match akabab by exact name;
sole miss is SWAPI "Ratts Tyerel" vs akabab "Ratts Tyerell"; akabab's other unmatched
records are sequel-era. Site surfacing deferred to a later all-nine panel; this change
touches the site only where tests/test_site_provenance.py:242's totals pin forces it
(assets 11→13, transforms 4→5, checks 15→20) plus ripple that pin creates. Design:
AkababResource; raw_character_profiles (01_raw); character_biographies transform-join
(02_transformed, writer #3); galaxy_report section; 5 checks (2 blocking / 3 WARN) on
the two new unlisted assets; known_facts constants; synthetic-then-real fixtures with a
separate akabab SNAPSHOT.json marker; snapshot script/workflow extension; README/WORKSHOP
ripple. Four commits: resource+guards; atomic feature; snapshot plumbing; freeze reality.
