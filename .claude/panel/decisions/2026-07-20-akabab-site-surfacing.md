# Decision: surfacing the akabab second source on the site

Date: 2026-07-20 · Scope: site-visual + data/pipeline surfacing (spans both) · Panelists:
all nine (graphic-designer, data-analyst, ux-designer, storyteller, lore-fanatic,
data-engineer, qa-engineer, hiring-manager, technical-writer).
Orchestrator/final decision: Claude (main session). This is the surfacing panel the
2026-07-20 akabab-second-source decision explicitly deferred to.

## Brief

The pipeline fully wires akabab (raw_character_profiles, character_biographies, 5 checks,
report section, frozen fixtures), but `site/index.html` surfaces NONE of it: provenance.assets
lists only the 4 beat assets, claims cover beats 1–6, the DAG strip shows 5 raw / 4 transforms,
the footer credits SWAPI only. `provenance.totals` was already bumped to 13/5/20, so tests pass
— but everything reader-facing is single-source, and beat-7 static prose ("four transforms",
L320) contradicts the JS-rendered sentence ("five transforms", L941). Computed fixture figures:
82/82 matched, 47/82 deaths on file, 75/82 affiliated (82 field-present), 14 masters on file,
12 apprentices on file. Full brief + debate addendum preserved in the session scratchpad.

## Per-role verdicts (one line each)

- **graphic-designer**: dashboard card, no beat; akabab chips stay monochrome `.chip` reuse (no
  source hue — a provenance color is a data seat that breaks the one-hue law); one `.kpi`
  headline; no ranked chart (manufactures a superlative + smuggles canon-scope); no gold ring.
- **data-analyst**: `#card-biographies` mirroring registry; per-row akabab fields in DATA.people
  (aggregate blob is not derivable); nested denominators; checked (82/82, 47/82) vs uncheckable
  (75/14/12 render-computed, no badge) split stated; pay the SQL fixture cost; guard the DAG strip.
- **ux-designer**: card leaves BUILDERS.length=8 untouched, flat-embed parity free; disclosures
  use the settled `details` shape, downward growth, ≥44px, content never gated; meta as sources[].
- **storyteller**: card after `#card-registry` — the coda's "second reading" is its pre-authored
  referent; drafted "A second reading" copy; 82/82 leads (complete AND guarded); no ranked chart.
- **lore-fanatic**: drop the ranked affiliations chart (top-8 includes sequel-era New Republic/CIS
  — a ranked claim can't be honestly saga-scoped); coverage stat-block only; "on file"/"not canon"
  attribution; the 896+4 derivation stays sealed.
- **data-engineer**: per-row nullable akabab fields in DATA.people; one executable `bios` SQL over
  character_biographies returning coverage COUNTS (not died_year_aby values); render/guard the DAG
  strip from real defs; `DATA.meta.sources` as an array, footer projects it.
- **qa-engineer**: exact guard slate — per-row flags so 82/82 & 47/82 are drift-recomputable;
  `FakeAkababResource` in the warehouse fixture the moment akabab SQL ships; DAG-strip guard; no
  per-card badge (a badge needs a claim, i.e. the beats-1–6 machinery); totals stay 13/5/20.
- **hiring-manager**: surface the multi-source join (strongest scan signal) via DAG chips + footer
  + one card; executable SQL is non-negotiable (every dashboard chart has executed SQL); fix the
  contradiction truth-first; no 9th beat (reads as churn).
- **technical-writer**: fix L320/L941 unconditionally; drafted README "The website" clause + the
  L320 rewrite ("five SWAPI pulls and one akabab pull … five transforms"); footer from meta.sources;
  zero WORKSHOP ripple (its "five SWAPI" counts stay literally true).

## Adjudication (unanimous where not noted)

- **D1 Placement — dashboard card, no 9th beat. Unanimous.** A `#card-biographies` card in `#dash`
  after `#card-registry`, before the coda. A beat would break four pins (exactly-8 kickers,
  claims-cover-1..6, drift `"1,2,3,4,5,6"`, the L941 "six of its numbers") and re-open settled
  "eight steps"/"n/8" geometry to carry aggregate-grade enrichment that never touches census grain.
  Unearned. The spine stays 100% untouched (BUILDERS.length=8).
- **D2 Content — coverage stat-block, no ranked chart. Unanimous.** Headline (one `.kpi`):
  **82 of 82 matched** — the only akabab number that is both complete and pipeline-guarded. Ladder
  beneath: 47 of 82 deaths on file · 75 of 82 affiliated (82 carry the field) · 14 masters on file ·
  12 apprentices on file. Every number nested-denominatored, "on file" vocabulary.
- **D5 Ranked affiliations chart — DROPPED. Unanimous.** The computed top-8 (Galactic Republic 39
  … New Republic 11, CIS 11) proves the canon-scope trap is live: `affiliations` is canon-wide and
  sequel-inclusive, and a ranked bar is a ranking *claim* a six-film site cannot honestly make. The
  saga-safe coverage count (75/82 affiliated) carries the fact with no beyond-saga implication.
- **D3 Executable SQL — YES.** One `bios` string added to `DATA.sql` and `SQL_KEYS`; the
  `warehouse` fixture materializes `raw_character_profiles`+`character_biographies` with
  `FakeAkababResource()`. The query returns coverage COUNTS only —
  `SELECT COUNT(*) matched, COUNT(died_year_aby) deaths_on_file,
  COUNT(*) FILTER (WHERE affiliation_count>0) affiliated FROM character_biographies
  WHERE profile_id IS NOT NULL` — never `died_year_aby` VALUES (dodges ABY-sign display AND the
  pre-vetoed derivation). Gated compare recomputes the same row from DATA.people.
- **D4 Provenance & lineage.** Add `raw_character_profiles` + `character_biographies` to
  `DATA.provenance.assets` (verbatim `why`, exact deps, exact 2- and 3-check sets — validated by
  the existing real-defs assertion; chain-checks rise 13→18 ≤ 20). Add both chips to the DAG strip
  and correct the aria-label to six raw / five transforms. **Adjudication (engineer wanted a full
  render; qa offered "or pin chip-set"): I rule PIN, not render** — the chips stay HTML but a NEW
  guard asserts the DAG chip set equals the real Dagster asset keys, so it can never silently
  contradict totals again; less churn, same guarantee. **No per-card badge** — a live badge needs a
  claim (beats-1–6 machinery); the DAG strip is the lineage surface (registry-card precedent).
- **D6 Footer/meta.** `DATA.meta` becomes `{sources:[{name,url,snapshot}...], snapshot}`; the footer
  and freshness line render "Sources: SWAPI · akabab" from the array, never a hand-typed string.
- **Per-row data shape (adjudication).** DATA.people gains a nested `bio` object (or null when
  unmatched): `{diedOnFile: bool, aff: int, masters: int|null, appr: int|null}`. **Engineer wanted
  `diedAby|null`; qa wanted a flag — I rule the boolean `diedOnFile`**, so no signed ABY year value
  ever enters the page (honors the signed-year and quoted-testimony laws) while deaths-on-file stays
  derivable by presence-count. All card numbers render from `bio` in JS; no numeric literal in HTML.
- **Contradiction fix — unconditional.** L320 → "five SWAPI pulls and one akabab pull, one DuckDB
  warehouse, five transforms, one report"; the count renders/reads consistent with L941 and totals.
- **Checked-vs-uncheckable honesty.** 82/82 (`character_biographies_join_coverage`, WARN) and 47/82
  (`character_biographies_deaths_on_file_baseline`, WARN) are pipeline-guarded and pinned to
  known_facts; 75/14/12 are render-computed copy discipline with the drift detector as their only
  guard. The card carries no badge, so it never implies a live check on any of them.

## Final plan (deltas to the approved implementation plan)

1. New `#card-biographies` dashboard card after `#card-registry`: `.kpi` headline "82 of 82",
   storyteller's "A second reading" stat-block copy with lore's attribution gloss, `details.sql`
   disclosure of the `bios` query. Numbers render from `DATA.people[].bio`.
2. DATA.people gains `bio` (nested object or null). DATA.sql gains `bios`. DATA.provenance.assets
   gains the two akabab assets (verbatim checks). DATA.meta becomes `sources[]`.
3. DAG strip: +2 chips, corrected aria-label; new guard pins chip set to real defs.
4. Drift detector: expect{} grows matched/deathsOnFile/affiliated/masters/apprentices, all
   recomputed from `bio`; the two baselined values also pinned to known_facts by pytest.
5. Guards (same commit): `bios` in SQL_KEYS + warehouse-fixture akabab materialization +
   `FakeAkababResource`; gated `bios` compare test; DAG-strip real-defs guard. Totals stay 13/5/20;
   WORDS stays through "twenty" (no new Dagster objects).
6. Fix L320/L941 contradiction. README "The website" gains the second-source clause (tech-writer's).
   Footer dual-source from meta. No WORKSHOP ripple. DAG screenshot already at 13/20 (no retake).

## Newly settled constraints (banked)

- The site's second-source surface is a dashboard card, never a story beat — the census spine is
  one archive (8 steps, "n/8"); the second source is a second *reading* of it, a dashboard act.
- A ranked affiliations (faction) chart is banned on a six-film-scoped site: `affiliations` is
  canon-wide/sequel-inclusive; only saga-safe coverage COUNTS may surface.
- akabab coverage numbers render from per-row `DATA.people[].bio`, never an aggregate blob; the
  `bio` object carries no signed year (a `diedOnFile` boolean, not `died_year_aby`).
- A displayed akabab SQL string returns coverage counts, never `died_year_aby` values.
- A per-card check badge requires a claim entry; dashboard cards state numbers with denominators
  and rely on the DAG strip for lineage — no fabricated card-level live status.
- The DAG strip chip set is a guarded surface: pinned to the real Dagster asset keys.

## CLAUDE.md upkeep

No new hard-constraint line required: the surfacing obeys the existing digest (nested denominators,
on-file vocabulary, no cross-source derived figures, one-data-hue, provenance rendered from DATA).
The two new site-specific laws (no ranked faction chart; second source is a card not a beat) live
here and in role memories, not the global digest.
