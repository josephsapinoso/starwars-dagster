# Technical Writer — Panel Memory

## Settled (do not relitigate)

- README/WORKSHOP.md are the landing pages; docs must explain the *why* and the
  tradeoffs, not just the how; jargon earns its place. (Recruiter-lens panel, PR #5.)
- One home per explanation — link, don't duplicate; duplicated prose drifts apart.
  (Practice established across PRs #3–#5.)
- Provenance strings are projections, not prose: every provenance/severity string on
  the site derives from `DATA.provenance`; check rationales are VERBATIM projections
  of checks.py `description=`; badge severity derives from `spec.blocking`; all
  pytest-verified against the real Dagster definitions. checks.py is the single
  rationale home. (Pipeline-reveal, 2026-07-18.)
- Guard honesty is copy law: a check badge may only appear where the check asserts
  the displayed number (or its denominator/structure, labeled as such); derived or
  unguarded claims say so in plain words; no fabricated or implied live status.
  (Pipeline-reveal, 2026-07-18.)
- Reveal labels are ONE generated template — "The paper trail — where {claim} comes
  from" ("paper trail" is lore's sanctioned bridge word); beat 4 renders the quiet
  variant "The paper trail."; identical placement/size everywhere. No hand-written
  per-beat variants. (Pipeline-reveal, 2026-07-18.)
- Reveals exist on beats 1–6 only; beat 0 stays a clean hook; beat 7 carries a
  provenance-computed callback line (current text at index.html:941: "One pipeline,
  {WORDS[transforms]} transforms, {WORDS[checks]} checks — and you've now walked the
  paper trail on six of its numbers."). One disclosure style, shared with details.sql.
  (Pipeline-reveal, 2026-07-18.)
- The one-line strict-JSON format of `const DATA` is load-bearing — tests parse it.
  Never reflow it for readability. (Pipeline-reveal, 2026-07-18.)
- README order (decided rewrite): identity sentence (replaces "self-study workshop")
  → live-site link → screenshot → testing-philosophy paragraph incl. the provenance
  sentence ("every number on the site names its asset and its guard — including
  which numbers are guarded offline only") → architecture + quick start → `.claude/`
  panel as one short process section (human as adjudicator) → WORKSHOP.md as linked
  teaching appendix → personal-site link slot. (Pipeline-reveal, 2026-07-18.)
- **Description style rule (MINE, banked law):** a check description states the
  INVARIANT and its STAKES; run metadata carries the particulars; rosters and numbers
  live only in known_facts.py. No check string quotes another beat's caption or
  payoff. Written into checks.py's module docstring (lines 19–23) — the rule now
  lives where authors of new checks will read it. (Post-landing cleanup, 2026-07-18.)
- Displayed SQL is executed SQL: any SQL text shown on the site lives in DATA and is
  executed against the fixture-built warehouse by the offline suite; no hand-verified
  SQL copy anywhere. README's claim is worded to match ("every displayed string is
  executed... so the SQL a reader opens is SQL that provably runs").
  (Post-landing cleanup, 2026-07-18.)
- DATA.provenance carries no narrative fields — everything in it stays derivable
  from the real Dagster definitions plus known_facts; the rail renders uniformly,
  spoiler safety lives in the strings. Spoiler pin law (qa/storyteller): payoff term
  sets derive from known_facts; no check string renders earlier than its claim's
  reveal beat. (Post-landing cleanup, 2026-07-18.)
- galaxy_report stays check-free BY DESIGN: a check there would pre-solve WORKSHOP
  Exercise 8 and duplicate pytest coverage. The gap is deliberately disclosed, not an
  oversight — docs must keep saying so. (Post-landing cleanup, 2026-07-18.)
- **Quoted-testimony rule (docs-genre law, MINE to enforce):** external claims —
  dialogue, canon, anything the repo didn't compute — may be AUDITED in copy but never
  rendered as site-derived data; derived numbers come only from DATA. The Yoda "900"
  precedent: 896 BBY is the derived number; 900 appears only as testimony being
  checked against it. (Birth-registry panel, 2026-07-19.) **Extension (akabab panel,
  2026-07-20):** cross-source derived figures (SWAPI birth × akabab death arithmetic,
  e.g. Yoda 896+4=900) are pre-vetoed off ALL surfaces until a surfacing panel rules —
  computing the derivation would launder the audit into data.
- **WORKSHOP.md is on the permanent count-ripple checklist**, and teaching prose
  states counts count-free unless the count IS the lesson ("a checks file you can
  read in one sitting", WORKSHOP:705). Any copy encoding a count is a drift surface.
  (Birth-registry panel, 2026-07-19.)
- README "Limits, by design" is settled: placed between "How this was built" and
  "Learn Dagster" (honesty-genre continuity → Module-10 handoff); engineering
  register, number-free; bullet shape is limit → why fine now → forcing trigger;
  closes with ONE link to WORKSHOP Module 10 as the sole home of the tooling
  why-nots. (Birth-registry panel, 2026-07-19.)
- Absence pins are legitimate guards: an element exempted from a detector by a
  property (number-free, spoiler-free) gets a pin asserting that property; pinning
  exact wording is theater. Failure-mode separation: a parsed displayed number gets
  BOTH a drift baseline and a parse-honesty invariant — "data moved" and "parser
  broke" must fail differently. (Birth-registry panel, 2026-07-19.)
- **"On file" vocabulary is copy law (akabab panel, 2026-07-20):** akabab
  death/lineage data is "deaths on file" / "on file" everywhere — never "deceased",
  never saga-scoped or canon-complete claims; the report closes with "'On file' means
  the curated source records it — absence is not survival." Akabab is attributed as
  fan-curated + SWAPI-derived, never as canon authority.
- **Nested denominators (akabab panel, 2026-07-20):** every enrichment-join number
  carries matched AND field-present denominators (N of field-present of 81 matched
  of 82). This is report-copy discipline computed from the data, NOT new checks. No
  superlatives from sparse lineage fields; ranking only with n disclosed.
- **Alias governance (akabab panel, 2026-07-20):** curated dict in known_facts,
  canon-direction comment per entry; aliases bridge joins, they never mutate as-filed
  records; no fuzzy matching, and the docs carry exactly ONE why-not-fuzzy sentence.
- **Signed-year columns name their convention in the column name** (`_bby`/`_aby`);
  no bare year columns — the name is the documentation. (akabab panel, 2026-07-20.)
- The site WORDS number-renderer is a guard surface: it grows (with its pytest pin
  that `len(WORDS)` exceeds every DATA-rendered count) in the same commit as any
  count it must spell. (akabab panel, 2026-07-20 — carve-out from the surfacing
  deferral, won by me + qa.)
- **As-filed tiebreak (naming law, learned the hard way):** when a surface is named
  after a source field, the field's literal name wins over a synonym I prefer
  ("Affiliations" beat "Allegiances" because the source field is `affiliations`);
  and drafted copy adopted verbatim beats after-the-fact title edits.
  (akabab panel, 2026-07-20.)

## Working knowledge

- Doc inventory: README.md; WORKSHOP.md (769-line, 15-section beginner tutorial with
  its own audience and integrity — linked teaching appendix, never folded into
  README); tests/fixtures/swapi/README.md (fixture provenance; pattern = synthetic
  disclaimer → awkward-cases list → "not the real dataset, banked tests skip" →
  refresh command — the akabab fixture README mirrors it + MIT attribution);
  CLAUDE.md (process rules for the AI collaborator, not reader-facing).
- Explanation homes to link, not rewrite: tests-vs-checks philosophy (README testing
  bullet + WORKSHOP Module 8, anchor `#12-module-8--testing--asset-checks`),
  snapshot rationale (workflow comments + fixtures README), severity discipline
  (checks.py docstring + `description=` strings), tooling why-nots (WORKSHOP
  Module 10 sole home — verified 2026-07-20 it can carry the weight).
- Site voice anchors (site/index.html): SQL reveal summary "Show the DuckDB SQL";
  two-word beat kickers; lineage-strip heading "The pipeline that made this page".
  galaxy_report house style: topical-noun headings, italic on-page denominators,
  bullet counts, machinery voice with light flavor.
- Ground truth (2026-07-19 commits, PRE-akabab landing): 11 assets / 4 transforms /
  15 checks (4 blocking, 11 warn); `birth_year_bby`; six executed SQL strings;
  WORDS through "fifteen" (index.html:863); README Limits at 117–137; screenshots
  at 15 green (f170379). Akabab landing will ripple to 13/5/20 — see banked plan.
- Jargon-introduction duty (mine): first mention of "akabab" in README and WORKSHOP
  gets the gloss "akabab/starwars-api, a community-maintained static JSON dataset
  (MIT, GitHub Pages)". Proper-noun jargon earns its place by being introduced.
- "Lineage" is reserved vocabulary in this repo (Dagster asset lineage: lineage
  strip, direct lineage, README screenshot) — never reuse it for family-tree /
  master-apprentice content. Veto upheld 2026-07-20.
- Known stray others should fix (not mine to touch): QA's skill file
  `panel-qa-engineer-provenance-verification/SKILL.md:32` still says "13 checks".
- Skill: `.claude/skills/panel-technical-writer-count-ripple/SKILL.md` — the
  count-ripple checklist as a reusable procedure, incl. the word-renderer step.

## Banked: pipeline-reveal + post-landing cleanup (2026-07-18, compacted)

- Wins promoted to Settled above: single-source rationale, generated labels, README
  order, WORKSHOP as appendix, description style rule, displayed-SQL-is-executed-SQL.
- One-home law won Q1 (5–3–1) as an ENGINEERING invariant, not style: a hand-listed
  roster in a check description was a third home that would make the Dagster UI lie.
  Argue it as architecture, it adjudicates architecture.
- Exercise-8 collision precedent: docs are a guard surface — grep WORKSHOP exercises
  before endorsing any new repo feature; shipped code can pre-solve a tutorial.
- Superseded claims update or become explicit PAST-tense history (the "How this was
  built" honesty-arc genre, now two confession beats); copy that encodes a count is
  a drift surface — name, don't enumerate.
- Pre-draft copy for the branch you expect to win, gated on the fix: both my Q2
  drafts shipped near-verbatim and made "same commit" frictionless.

## Banked: birth registry + coda + limits (2026-07-19, compacted)

- Won Q4 whole (Limits placement + Module-10 handoff) on CONTINUITY with the honesty
  genre; won the WORKSHOP:705 count-free retirement — second live exercise of the
  docs-as-guard-surface grep.
- QA's failure-mode separation (7–1) shapes my copy: "the data moved" and "the
  parser broke" are different sentences, so their guards fail differently.
- The style rule in checks.py's docstring worked on authors I never briefed — both
  registry descriptions arrived subject-only. Writing rules belong where writers
  can't avoid them.
- When a verdict promotes a doc to sole-home status, immediately re-verify it can
  carry the weight (done for Module 10, 2026-07-20 — resolved, off the watch list).

## Banked: akabab second source (2026-07-20; decision
`2026-07-20-akabab-second-source.md`; implementation pending, four commits)

- **Won the WORDS carve-out (with qa), my prep's biggest find:** grep proved NO
  pytest pin existed on WORDS coverage — only the runtime console.warn. The verdict
  classifies WORDS growth as totals-pin ripple, not deferred surfacing: it grows
  through "twenty" in the feature commit with a new pytest pin. Second recurrence of
  the beat-7 overflow bug; the count-ripple skill earned its keep. Promoted to
  Settled.
- **Won the docs argument FOR Option C:** WORKSHOP:338 ("all five raw lists") and
  the "5 tables loaded" line stay literally TRUE under the transform-join; under
  Option A they'd both drift. Docs truth adjudicated an architecture question again
  — same muscle as the one-home law. Option C ratified unanimously.
- **Won the lineage-collision veto:** no "Lineage" in the section title; the word
  stays reserved for Dagster lineage. Lore independently proposed the same rename —
  vocabulary vetoes land easier with a co-sponsor.
- **Lost the title word, instructively:** my "Allegiances & Apprenticeships" fell to
  storyteller's "Affiliations & Apprenticeships" on the as-filed tiebreak — the
  source field is literally `affiliations`, and drafted-copy discipline adopts
  verbatim. My veto was satisfied either way, but I proposed a synonym where the
  schema had already chosen the word. Banked as the as-filed naming law.
- **My README-ripple inventory adopted whole into commit 2:** ASCII architecture
  diagram gains the second source (a one-source diagram would make the landing page
  lie), :79 exact-value-tests list, tree comments, Stack attribution ("fan-curated,
  MIT, effectively frozen; SWAPI-derived — reproduces SWAPI's spellings"),
  WORKSHOP:299 rewritten count-free. Ripple-inventory prep is now my standard move.
- **Adopted from others, now mine to enforce in copy:** lore's "on file" vocabulary
  package; analyst's nested denominators (as copy discipline — qa's five-check
  ceiling beat per-field baselines); engineer's aliases-bridge-never-mutate framing
  with lore's canon-direction comments; storyteller's Yoda-derivation pre-veto
  (folded into my quoted-testimony rule). All promoted to Settled.
- **Baselines are computed, never transcribed** — three independent surveys of
  akabab disagreed (87/88 records; died 47/28). Docs corollary: never quote a
  brief's figures as facts; wait for the frozen fixture, then let the script speak.
- Prep differently next time: (1) read the source SCHEMA's own field names before
  proposing any user-facing title — the as-filed word usually wins; (2) when a
  storyteller announces drafted-copy discipline, propose edits INTO their draft
  during debate rather than parallel titles after.

## Banked: akabab site surfacing (2026-07-20; decision
`2026-07-20-akabab-site-surfacing.md`; implementation pending)

- **My whole prep landed, near-verbatim.** The L320/L941 four-vs-five-transforms
  contradiction I flagged as highest-priority-fix-regardless is fixed unconditionally;
  my exact rewrite ("five SWAPI pulls and one akabab pull … five transforms") ships.
  Drafted-copy-gated-on-the-fix discipline paid a fourth time.
- **README "The website" gains the second-source clause — my one-home ruling held.**
  The site's own "what the website shows" paragraph was the last single-source holdout
  (diagram/table/tree already surfaced akabab from the pipeline landing). It now NAMES
  the site's second-source panel (the `#card-biographies` card) and LINKS to the
  pipeline akabab — describe the surface here, don't re-explain the join.
- **Footer + freshness line are projections, not prose — provenance-projection law
  extended to `DATA.meta`.** `DATA.meta` becomes `{sources:[{name,url,snapshot}],
  snapshot}`; footer and freshness render "SWAPI · akabab" FROM the array. No
  hand-typed source string survives. Same muscle as the provenance-strings law.
- **Dashboard card, not a beat — my Q1 lean won unanimous.** The census spine stays
  8 steps / "n/8" / "six of its numbers" untouched; the second source is a second
  *reading* on a dashboard, not a 9th archive step. Re-opening settled geometry was
  not earned by an aggregate-grade join. Zero story-count ripple, as prepped.
- **Zero WORKSHOP ripple confirmed and banked as law:** it is a pipeline tutorial, not
  a site walkthrough; "five SWAPI endpoints / five raw lists" stay literally true
  (akabab is a separate pull). Docs-as-guard grep, third clean exercise.
- **New site-specific laws I now enforce in copy** (promoted to Settled below): the
  second source is a card not a beat; no ranked faction chart on a six-film site
  (canon-scope trap — only saga-safe coverage COUNTS surface); the akabab SQL string
  returns coverage counts, never `died_year_aby` values; `bio` carries a `diedOnFile`
  boolean, no signed year; a dashboard card states denominatored numbers and relies
  on the DAG strip for lineage — no fabricated card-level badge.
- Prep differently next time: I mapped every ripple but under-specified the DATA SHAPE
  (per-row `bio` vs aggregate blob) — the analyst/engineer/qa owned that call and it
  drove my copy's derivability. When a copy claim ("82 of 82 renders from data") depends
  on a data shape, propose the shape in prep so the number's home is settled with the words.

## Settled additions (akabab site surfacing, 2026-07-20)

- The site's second-source surface is a dashboard card (`#card-biographies`, after
  `#card-registry`), never a story beat. The census spine is one archive; the second
  source is a second reading of it.
- No ranked faction/affiliations chart on a saga-scoped site — `affiliations` is
  canon-wide/sequel-inclusive; only saga-safe coverage COUNTS may surface (75/82
  affiliated, not a top-8 bar).
- Footer + freshness line render from `DATA.meta.sources[]`; no hand-typed source
  string. akabab's first SITE mention (card/footer) carries the fan-curated/MIT/
  SWAPI-derived-spellings/not-canon-authority attribution.
- Dashboard cards state denominatored numbers and rely on the DAG strip for lineage —
  no card-level check badge (a badge needs a claim entry, i.e. the beats-1–6 machinery).

## Prep notes: dagster-duckdb migration (2026-07-21)

- **What I knew:** WORKSHOP is a 15-module pipeline tutorial (not a site walkthrough);
  docs-as-guard-surface + count-ripple muscle; one-home law.
- **Full WORKSHOP blast radius of a DuckDBResource migration (verified by grep):** the
  path-string pattern is taught in exactly these places — contained, not sprawling:
  1. DAG diagram edge label "DuckDB path" (`:108`) — small reframe.
  2. Layer-2 code block + **"Note the pattern: assets return data (or paths to data)"**
     callout (`:349-362`): the `-> str` / `return str(DB_PATH)` and the mental model.
     THE one load-bearing rewrite. Replace with "reach your database through a Resource
     (Module 2), not a hand-opened connection."
  3. Layer-3 list "Opens the DuckDB file from the path passed by star_wars_db" (`:367`)
     — reword to "gets a connection from the DuckDBResource."
  4. Write-back exception (`:374`) — SURVIVES verbatim (still `CREATE OR REPLACE`).
  5. "Querying DuckDB yourself" REPL snippet raw `duckdb.connect(...)` (`:378-395`) —
     KEEPS raw. It's a user poking the file in a REPL, not pipeline wiring; the raw
     pattern legitimately belongs here.
  6. Deployment checklist "Move DB_PATH … to a shared volume" (`:642`) — reword to
     resource config. Small.
- **The mental-model phrase appears ONCE (`:362`), echoed nowhere.** No cascade.
- **Key finding — migration IMPROVES tutorial integrity, doesn't falsify it.** Module 2
  already teaches resources hard: glossary "Resource = shared connection to an external
  system (API, **database**, S3)" (`:75`); "the resource abstraction is the point"
  (`:309`); testability/reusability/observability (`:257-262`). A hand-rolled
  `duckdb.connect()` in Layer 2 right after Module 2 is a papered-over self-contradiction.
  A DuckDBResource makes Layer 2 REINFORCE Module 2 instead of competing with it.
- **Q4 answer:** raw `duckdb.connect()` is NOT the better from-zero pattern *for this
  tutorial* — it would be, in a tutorial that never taught resources; this one committed
  to them in Module 2. The one place raw connect() stays right is the REPL snippet.
- **README nearly untouched:** its diagram already labels inputs "Resources" (`:53`) and
  shows data-flow, not a path edge; "In-process executor / DuckDB file lock" Limits
  bullet (`:139`) stays true. A DuckDBResource is consistent with README as written.
- **IO manager (DuckDBPandasIOManager) = large WORKSHOP rewrite:** falsifies the 4-Layer
  architecture diagram, "loads 5 tables," the Layer 2/3 split, and provenance/lineage.
  Docs lane strongly prefers DuckDBResource; oppose the IO-manager idiom.
- **read_only reader/writer discipline is NOT currently taught in WORKSHOP** (grep: zero
  hits). So migration is docs-neutral there — UNLESS it preserves read_only, in which
  case it's a NEW teaching opportunity (the safety contract is currently invisible). If
  it GUTS read_only, that's a code loss docs can't paper over — flag to code roles.
- **Feature + docs in ONE commit: clean and pre-draftable** for DuckDBResource (3-4
  contained edits + the callout replacement). Standard docs-as-guard-surface pre-draft.
- **Can't verify:** whether `DuckDBResource.get_connection()` exposes per-connection
  read_only (code roles own this); the executor-lock/fixture-path interaction under
  centralized resource config; whether provenance edges survive `deps=` rewiring.

## Open watch items (mine)

- Akabab PIPELINE landing shipped (13/5/20; README diagram/table/tree + Stack gloss).
  SURFACING landing is now DECIDED (see Banked above), implementation pending: verify
  in the PR that L320 contradiction is fixed, README "The website" names the card +
  links (not re-explains) the pipeline join, and footer/freshness render from
  `DATA.meta.sources[]` (no hand-typed source string).
- Surfacing-panel tripwires I co-own: Yoda 896+4=900 stays pre-vetoed; if
  character_biographies joins a beat chain, spoiler-pin term sets extend in the same
  landing; screenshot retake whenever a visual shows check/asset counts.
- Two-reader test for check strings: every description serves the Dagster operator
  AND the site hover reader; names/numbers surface per-run in metadata. Keep testing
  on every new check.
- Honesty-arc length: a THIRD confession beat triggers restructuring "How this was
  built" from chronology into a pattern statement plus terse episodes.
