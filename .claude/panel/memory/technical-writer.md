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
