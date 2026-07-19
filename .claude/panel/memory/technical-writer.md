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
- Ground truth (updated 2026-07-18, commits c0b97e0 + 2aa845e): 11 assets /
  4 transforms / 13 checks (4 blocking, 9 warn) — the 13th is the WARN height-null
  baseline guarding beat 1's "1 unmeasured". `characters_enriched` now writes back
  to the warehouse (`CREATE OR REPLACE TABLE`; EXPECTED_DB_TABLES stays five). The
  five dashboard SQL strings live in DATA and are executed + compared offline.
  README's "How this was built" now carries TWO past-tense honesty beats: the
  hand-derived numbers, then the three-of-five false SQL strings.

## Banked: pipeline-reveal (2026-07-18)

- Won: single-source rationale — my drift-risk finding (checks.py `description=` vs
  a hand-written third home in `DATA.provenance`) became banked law; the pytest
  suite asserts verbatim match. Won: generated-label principle — one template
  filled from provenance, though the winning wording is lore's "paper trail" bridge,
  not my number-filled "Where 23 of 82 comes from" draft. Lesson: I supply the
  mechanism (generate, don't hand-write); voice is a shared decision.
- Won by proxy: my aria concern about SVG titling dissolved when HTML chips beat
  SVG (adjudication #4) — real text needs no aria re-plumbing; labels still
  generate from the one data source.
- Won: README rewrite lands with the decided order, including the identity-sentence
  swap I flagged and WORKSHOP.md preserved as a linked appendix. The `.claude/`
  panel gets exactly one short process section with its one-sentence why — my
  "signal or gimmick" question resolved as: show it, briefly, human as adjudicator.
- Lost/deferred: nothing of mine cut; the analyst's per-character transform and the
  SQL-string migration are open items — if the transform lands, beats 4–6 upgrade
  to DIRECT and their honesty lines must be regenerated, not patched (the
  projection architecture makes this automatic; verify tests force it).
- Prep differently next time: I verified the site's microcopy but not the accuracy
  of the brief's beat→asset map — the analyst's falsification of it reshaped
  everything, including the copy I'd have to write. Before drafting explanation
  systems, check whether the thing being explained is true.

## Banked: per-character transform landed (2026-07-18, commit 082d9c9)

- Execution note, not a debate (decision file:
  `2026-07-18-per-character-transform-landed.md`). The transform open item from
  pipeline-reveal is CLOSED; the SQL-string migration stays open (blocked on a
  verification story).
- My "regenerate, don't patch" prediction held: the projection architecture flipped
  beats 4–6 to direct/check-guarded by changing provenance data, and README counts
  updated everywhere they appear (headline line 44, asset table, tree comment).
- Narrative win worth reusing: the "How this was built" paragraph retold the
  derived-first story in PAST tense — the honest-labeling episode became proof of
  process instead of stale copy. Count also corrected "two" → "three" hand-derived
  numbers. Pattern: when facts change, superseded claims either update or become
  explicit history; they never linger as present tense.
- Docs caught two latent copy bugs the pipeline change exposed: beat-7 number-word
  list overflow ("undefined checks" at 12) and hardcoded "three transforms" in
  prose + DAG-strip aria label. Lesson: any copy that encodes a count is a drift
  surface — prefer generation from provenance, or a detector that warns on overflow.
- Screenshot caption discipline held without edits: caption "Asset Lineage Graph"
  describes without counting, so the old image doesn't overclaim. Captions that
  name, not enumerate, survive data changes.

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

## Prep notes: improvement survey (2026-07-19)

- WORKSHOP currency audit: write-back taught (line 367, one sentence), character_stats
  in the diagram (115), NO hardcoded check counts anywhere (drift-proof, good). Gap:
  Module 8 stops at three patterns — test_site_provenance.py and the executed-SQL
  suite are absent from the tutorial, yet README:26 names Module 8 the long-form home
  of the testing philosophy.
- WORKSHOP Module 10 "Add Great Expectations or Soda" (~line 690) is a mislabeled
  stub: its code sample is a plain Dagster @asset_check duplicating Module 8, and it
  recommends the one thing the repo's hard constraints deliberately exclude, with no
  why/tradeoff.
- README:14 renders a literal dead `#` portfolio anchor above the fold (slot is
  settled; rendering it dead is not).
- Decision-log discoverability OK-ish: decisions/README.md exists; repo README links
  the folder, not an exemplar decision file.

## Open watch items (mine)
- Screenshot retake still open — target is now 13 green checks. Caption ("Asset
  Lineage Graph") names without counting, so it doesn't overclaim; keep it
  count-free until the retake lands.
- Two-reader test for check strings (kept from prep): every description serves the
  Dagster operator AND the site hover reader; names/numbers surface per-run in
  metadata (e.g. six_film_characters/expected) — exactly where an operator looks.
  Function names render only on their payoff beat, so no rename churn.
- Watch the honesty arc's length: two confession beats read as process; a third
  should prompt asking whether the paragraph needs restructuring into a pattern
  statement rather than a growing list.
