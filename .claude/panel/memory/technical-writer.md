# Technical Writer — Panel Memory

## Settled (do not relitigate)

- README/WORKSHOP.md are the landing pages; docs must explain the *why* and the
  tradeoffs, not just the how; jargon earns its place. (Recruiter-lens panel, PR #5.)
- One home per explanation — link, don't duplicate; duplicated prose drifts apart.
  (Practice established across PRs #3–#5.)

## Working knowledge

- Current doc inventory: README.md (~129 lines, opens as "self-study workshop" —
  framing predates the portfolio pivot); WORKSHOP.md (769-line, 15-section beginner
  tutorial with its own audience and integrity — a genuine teaching artifact);
  tests/fixtures/swapi/README.md (fixture provenance); CLAUDE.md (process rules for
  the AI collaborator, not reader-facing).
- README structure as of PR #5: CI badge → screenshots → architecture (ASCII DAG +
  asset table) → quick start → stack → testing & data quality → what you'll learn →
  output → website section (with artifact link) → schedule → project structure.
- Explanations that already exist and must be linked rather than rewritten: the
  tests-vs-checks philosophy (README testing section + WORKSHOP module 9), the
  snapshot rationale (workflow comments + fixtures README), severity discipline
  (checks.py docstring).

## Prep notes: pipeline-reveal (2026-07-17)

- Site microcopy precedent (site/index.html): the SQL reveal's summary is
  "Show the DuckDB SQL" (line 850) — verb + named payoff, hand-set once in
  `makeCard`, not per-card. Story beats each carry a two-word "kicker" ("The
  census" … "The handoff") at lines 239–292; any reveal label system should rhyme
  with the kicker voice, not fight it.
- Static lineage strip heading is "The pipeline that made this page" (line 313)
  with a one-line why note — good existing voice to echo in per-beat reveals.
- Drift risk found: checks.py already carries strong one-line rationale
  `description=` strings (e.g. lines 94, 136, 172), and README's testing section
  paraphrases the philosophy. If per-beat reveals hand-write check rationales into
  `DATA.provenance`, that's a THIRD home. The already-decided pytest cross-check
  against real Dagster definitions is the fix: it should assert check names,
  severities, AND rationale text match (or derive from) the code's `description=`
  — making checks.py the single source and `DATA` a verified projection.
- Label question (Q1): a generic template filled with beat-specific numbers
  ("Where 23 of 82 comes from") can be *generated* from provenance data — specific
  voice without eight hand-written variants that drift.
- README (Q6): line 7 "Built as a self-study workshop" is the identity sentence
  to replace; current hero order is badge → screenshots → architecture.
  Portfolio-first reorder must keep WORKSHOP.md's tutorial integrity — it stays a
  linked teaching appendix with its own audience, not folded into README.
- Cannot verify: how the mini-SVG diagrams will be titled/announced to screen
  readers (aria-label text is doc territory — flag in debate); whether the
  `.claude/` panel infrastructure reads as signal or gimmick to a real hiring
  manager (hiring-manager's call; my lane is that wherever it's mentioned, it
  gets its one-sentence why in exactly one place).
