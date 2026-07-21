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
- **Tooling why-nots live in WORKSHOP Module 10 as tradeoff-both-ways sections**
  (beside "Why NOT Great Expectations"): name the mechanism (`read_only=False`
  hardcode), state the cost BOTH ways, and "when it would earn its place." A
  forward-pointer FROM the teaching module (Module 2 → Module 10) resolves a "why
  isn't the idiom used here?" coherence gap without moving the rationale. The
  rationale has ONE home; code comments only POINT to it, never restate.
  (dagster-duckdb panel, 2026-07-21.)
- **A deliberate technology NON-adoption is a guardable artifact, not just prose:**
  pin a stable rationale marker in the source (e.g. `"DuckDBResource"` +
  `"read_only=False"` present in transforms.py) beside the invariant it protects, so
  a future "modernize" refactor trips both the pin and the marker and must re-read the
  decision. "Silent adoption-of-the-status-quo" (keeping raw code with no note) is the
  worst outcome — worse than either migrating or documenting. (dagster-duckdb, 2026-07-21.)

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
  Module 10 sole home — now carries TWO: "Why NOT Great Expectations" and "Why NOT
  DuckDBResource"; both tradeoff-both-ways; transforms.py + Module 2 point in).
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

## Banked: pipeline-reveal + birth-registry (2026-07-18/19, compacted)

- Wins now in Settled: single-source rationale, generated labels, README order, WORKSHOP
  as appendix, description style rule, displayed-SQL-is-executed, Limits placement +
  Module-10 handoff, WORKSHOP:705 count-free retirement.
- **One-home law won Q1 (5–3–1) as an ENGINEERING invariant, not style** — a hand-listed
  roster in a check description was a third home that would make the Dagster UI lie. Argue
  a docs rule as architecture and it adjudicates architecture (the recurring muscle).
- **Docs are a guard surface (Exercise-8 collision):** grep WORKSHOP exercises before
  endorsing any repo feature; shipped code can pre-solve a tutorial. Copy that encodes a
  count is a drift surface — name, don't enumerate.
- Writing rules belong where writers can't avoid them (the checks.py docstring rule shaped
  authors I never briefed). Pre-draft the branch you expect to win, gated on the fix —
  makes "same commit" frictionless. QA's failure-mode separation shapes my copy: "data
  moved" and "parser broke" are different sentences with different guards.

## Banked: akabab second source + site surfacing (2026-07-20, compacted; decisions
`2026-07-20-akabab-second-source.md`, `2026-07-20-akabab-site-surfacing.md`)

- Wins now in Settled: WORDS carve-out (grep proved no pytest pin existed — count-ripple
  skill earned its keep), "on file" vocabulary, nested denominators, alias governance,
  signed-year column names, second-source-is-a-card-not-a-beat, no ranked faction chart,
  DATA.meta source-array projection, footer/freshness projections. Lost the title word
  (Affiliations) on the as-filed tiebreak — also now Settled law.
- **Docs truth adjudicated architecture THREE more times:** Option C won because
  WORKSHOP:338/"5 tables" stay literally true under it (Option A drifts); README diagram
  would lie if single-source; the L320/L941 four-vs-five-transforms contradiction was
  fix-regardless. My ripple-inventory prep (README diagram, :79 tests, tree comments,
  Stack gloss) adopted whole — now my standard move.
- **Baselines are computed, never transcribed** — three surveys of akabab disagreed
  (87/88 records; died 47/28). Never quote a brief's figures as facts; let the script speak.
- Prep differently: read the source SCHEMA's field names before proposing a title (as-filed
  usually wins); propose edits INTO a storyteller's draft during debate, not parallel titles
  after; when a copy claim depends on DATA SHAPE (per-row `bio` vs blob), settle the shape
  in prep so the number's home lands with the words.

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

## Banked: dagster-duckdb why-not (2026-07-21; decision
`2026-07-21-dagster-duckdb-decision.md`; shipped)

- **My position won (A: don't migrate, document the why-not).** Center of gravity was
  mine: 2 firm-A, 1 lean-A, 1 conditional-B. Shipped exactly as argued — Module 10 gains
  "Why NOT DuckDBResource" beside "Why NOT Great Expectations" (names `read_only=False`,
  tradeoff both ways); Module 2 gains a forward-pointer resolving the Module 2→3 coherence
  gap; transforms.py comment POINTS to Module 10 (never restates); the "silent A" I warned
  against was avoided. Feature + guard + docs in ONE commit; no dep added; 13 assets / 20
  checks unchanged. Both new laws promoted to Settled above.
- **The decisive win was the FRAMING: a documented non-adoption is richer teaching than
  another how-to.** "When NOT to adopt an idiom" beats "used the resource." The external
  fact (`get_connection()` hardcodes `read_only=False`, no per-connection arg, stable
  1.7–1.13) that killed migration was code roles' find — but MY job was proving the WORKSHOP
  cost was low and the coherence gap was real, which is what made (A) shippable rather than
  a cop-out. Docs cost adjudicated an architecture question a FIFTH time.
- **My blast-radius grep prep was over-built for the outcome that shipped** — I mapped every
  edit for a migration that didn't happen. But the SAME grep proved the Module 2→3 gap was
  real and localized, which sold the forward-pointer. Reusable: even when I argue AGAINST a
  change, mapping its blast radius surfaces the coherence gap the why-not must name.
- **qa's "deliberate omission is guardable" married my "silent A is worst":** the rationale
  marker pin in transforms.py is the mechanism that makes the why-not un-erasable. A doc
  decision and its guard landed together — docs-as-guard-surface's strongest form yet.
- Prep differently next time: when a portfolio "ding" arrives, lead prep with "what's the
  cheapest honest FRAMING" before mapping the expensive fix — the answer here was a 3-edit
  why-not, and I nearly over-invested in migration-edit choreography.

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
