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
  provenance-computed callback line ("One pipeline, three transforms, eight checks —
  the full record is below"). One disclosure style, shared with details.sql.
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
  checked against it. (Birth-registry panel, 2026-07-19.)
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

## Working knowledge

- Doc inventory: README.md (being fully rewritten per the settled order above — old
  tail was truncated mid-word with an unclosed code fence); WORKSHOP.md (769-line,
  15-section beginner tutorial with its own audience and integrity — stays a linked
  teaching appendix, never folded into README); tests/fixtures/swapi/README.md
  (fixture provenance); CLAUDE.md (process rules for the AI collaborator, not
  reader-facing).
- Explanation homes to link, not rewrite: tests-vs-checks philosophy (README testing
  bullet + WORKSHOP **Module 8** — section heading "## 12. Module 8 — Testing & Asset
  Checks", anchor `#12-module-8--testing--asset-checks`; I previously misfiled this as
  module 9), snapshot rationale (workflow comments + fixtures README), severity
  discipline (checks.py docstring + `description=` strings).
- Site voice anchors (site/index.html): SQL reveal summary "Show the DuckDB SQL"
  (verb + named payoff, set once in `makeCard`); two-word beat kickers ("The
  census" … "The handoff", lines ~239–292); lineage-strip heading "The pipeline
  that made this page" with a one-line why note. New microcopy rhymes with these.
- Reveal implementation is HTML `.chip` elements (not SVG), so text is natively
  accessible; `aria-label` is generated from the same provenance data — no separate
  hand-written accessible-name strings to drift.
- Ground truth (updated 2026-07-19, commits 1f3cf9e/4d92cb7/7d96df5/f170379):
  11 assets / 4 transforms / 15 checks (4 blocking, 11 warn) — 14th/15th are the
  registry's WARN pair (birth-date baseline + parse-honesty). `birth_year_bby`
  column; registry card in the Census section; six SQL strings in DATA, all
  executed + compared offline; WORDS through "fifteen" (index.html:842); coda after
  the last grid with a digits-pin. README: Limits section at 117–137; screenshots
  retaken at 15 green checks (f170379). "How this was built" carries TWO past-tense
  honesty beats: hand-derived numbers, then the three-of-five false SQL strings.
- Known stray others should fix (not mine to touch): QA's skill file
  `panel-qa-engineer-provenance-verification/SKILL.md:32` still says "13 checks".

## Banked: pipeline-reveal + transform landing (2026-07-18, compacted)

- Wins now promoted to Settled: single-source rationale (checks.py `description=`,
  pytest-verified verbatim), generated labels from one template, README order,
  WORKSHOP as linked appendix. Lesson kept: I supply the mechanism (generate,
  don't hand-write); voice is a shared decision — lore's "paper trail" beat my
  number-filled label draft.
- "Regenerate, don't patch" held when the transform landed (082d9c9): provenance
  data flipped beats 4–6 to direct and all counts moved with it. Superseded claims
  either update or become explicit PAST-tense history — never linger as present
  tense (the "How this was built" honesty-arc pattern).
- Copy that encodes a count is a drift surface (beat-7 WORDS overflow, hardcoded
  "three transforms"); captions that name-not-enumerate survive data changes.
- Prep lesson: before drafting explanation systems, check whether the thing being
  explained is true — the analyst falsified the brief's beat→asset map once.

## Banked: post-landing cleanup (2026-07-18, commits c0b97e0 + 2aa845e)

- **WON Q1, and the one-home law was the DECISIVE argument (5–3–1):** the trio
  description hand-listing C-3PO/R2-D2/Obi-Wan wasn't primarily a spoiler — it was a
  THIRD home for a roster whose single source is known_facts.py, a drift bug that
  would make the Dagster UI lie if the snapshot changed. The decision log cites this
  as what settled re-authoring over the cumulative rail. Reach lesson: the one-home
  law is not a docs-hygiene rule; it adjudicates ARCHITECTURE questions (which
  renderer, which data fields exist). Argue it as an engineering invariant, not a
  style preference.
- **My description style rule is now banked law and lives in code:** checks.py's
  module docstring carries it verbatim ("descriptions state the INVARIANT and its
  STAKES; run metadata carries the particulars; rosters and numbers live only in
  known_facts.py"). This is my authorship rule for every future check string — and
  proof that the best home for a writing rule can be a docstring the writers of new
  checks cannot avoid reading. My trio description shipped near-verbatim (checks.py
  ~240: "matches the verified snapshot in known_facts.py... the story's late payoff
  leans on this exact set — if it shifts, that beat is wrong, not just stale").
- **Same-commit doc must-haves all landed:** README:92–94 strengthened honestly
  ("every displayed string is executed against the fixture-built warehouse... SQL
  that provably runs"); honesty arc gained the second-false-claim sentence (108–111)
  — the past-tense-confession pattern now has two instances and is officially a
  genre, not a one-off; WORKSHOP Module 4 gained exactly ONE write-back sentence
  (line 367, "One deliberate exception to the pattern...") — Layer-3 framing and
  diagram untouched, tutorial integrity held.
- **Exercise-8 collision is a reusable precedent: docs are a guard surface.** My
  prep grep found that the proposed galaxy_report check IS WORKSHOP Exercise 8;
  QA retracted their weak-yes on that basis and Q3(b) went disclose-only
  unanimously. Technique to keep: before endorsing any new repo feature, grep
  WORKSHOP exercises for collisions — shipped code can silently pre-solve a
  tutorial. Teaching integrity vetoes features, not just phrasings.
- **Count-ripple discipline held:** 12→13 landed atomically (README 48 + tree
  comment 134, provenance totals, WORDS through "thirteen") BEFORE any screenshot
  retake — truth-then-tell sequencing worked as designed.
- Prep differently next time: my Q2 prep pre-drafted both the strengthened README
  clause and the WORKSHOP one-liner conditional on the fix landing — both shipped
  near-verbatim. Drafting copy for the branch you expect to win, gated on the fix,
  is cheap and makes "same commit" frictionless. Do it again.

## Banked: birth registry + coda + limits (2026-07-19; decision
`2026-07-19-birth-registry-and-polish.md`; commits 1f3cf9e/4d92cb7/7d96df5/f170379)

- **Won Q4 whole:** my placement (between "How this was built" and "Learn Dagster")
  and closing Module-10 link adopted, with the hiring-manager's bullet shape
  (limit → why fine now → forcing trigger). What won was CONTINUITY — the section
  extends the honesty genre the arc established, then hands off to Module 10
  instead of duplicating the tooling why-nots.
- **Won the WORKSHOP:705 catch:** "five tables and thirteen checks" retired
  count-free in the same commit ("a checks file you can read in one sitting");
  WORKSHOP joined the permanent count-ripple checklist as banked law. Second real
  exercise of the docs-as-guard-surface skill — the prep grep found a live drift
  surface before it lied in public.
- **No stake lost:** the one-vs-two-check fight wasn't mine; QA's failure-mode
  separation won 7–1 and shapes my copy anyway — "the data moved" and "the parser
  broke" are different sentences, so the guards that catch them must be too.
- Description discipline held WITHOUT me: both registry check descriptions arrived
  subject-only, 39/43/896/Yoda in known_facts only — the style rule living in
  checks.py's docstring did its job on authors I never briefed.
- Quoted-testimony rule banked (storyteller's framing; the docs version is mine to
  own): audit external claims in words, never render them as derived data.
- 13→15 ripple verified post-landing: README:48 + :160, WORKSHOP:705, WORDS through
  "fifteen" (index.html:842), screenshots at 15 green (f170379). One stray outside
  the ripple's reader-facing scope: QA's provenance-verification skill still says
  "13 checks" — flagged upward; each role owns its own memory/skill drift.
- Prep differently: my survey flagged Module 10's Great-Expectations stub as a
  mislabeled duplicate; the verdict then made Module 10 the SOLE home of the
  tooling why-nots. When a verdict promotes a doc to sole-home status, immediately
  re-check that the doc can carry the weight — don't wait for the next survey.

## Open watch items (mine)

- Module 10 is now README's only pointer for "why one check framework / no coverage
  gates" — next prep, verify its text actually argues the why/tradeoff rather than
  the old "add Great Expectations or Soda" stub framing.
- Two-reader test for check strings: every description serves the Dagster operator
  AND the site hover reader; names/numbers surface per-run in metadata — exactly
  where an operator looks. Held for the registry pair; keep testing on every new
  check.
- Honesty-arc length: the SQL-truth sentence is the SECOND confession beat. A THIRD
  is the trigger to restructure "How this was built" from a growing chronological
  list into a pattern statement (the process keeps catching false claims — name the
  pattern once, then list episodes tersely).
