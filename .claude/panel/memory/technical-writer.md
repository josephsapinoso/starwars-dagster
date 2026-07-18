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

## Working knowledge

- Doc inventory: README.md (being fully rewritten per the settled order above — old
  tail was truncated mid-word with an unclosed code fence); WORKSHOP.md (769-line,
  15-section beginner tutorial with its own audience and integrity — stays a linked
  teaching appendix, never folded into README); tests/fixtures/swapi/README.md
  (fixture provenance); CLAUDE.md (process rules for the AI collaborator, not
  reader-facing).
- Explanation homes to link, not rewrite: tests-vs-checks philosophy (README testing
  section + WORKSHOP module 9), snapshot rationale (workflow comments + fixtures
  README), severity discipline (checks.py docstring + `description=` strings, e.g.
  lines ~94/136/172).
- Site voice anchors (site/index.html): SQL reveal summary "Show the DuckDB SQL"
  (verb + named payoff, set once in `makeCard`); two-word beat kickers ("The
  census" … "The handoff", lines ~239–292); lineage-strip heading "The pipeline
  that made this page" with a one-line why note. New microcopy rhymes with these.
- Reveal implementation is HTML `.chip` elements (not SVG), so text is natively
  accessible; `aria-label` is generated from the same provenance data — no separate
  hand-written accessible-name strings to drift.
- Ground truth that shapes honest copy (data-analyst's finding): beats 4–6 numbers
  are hand-derived at authoring time from `raw_people[].films` (no asset computes
  them); `galaxy_report` has zero checks; only beats 0, 2, 3 have checks asserting
  the displayed number. `relation: "derived"` + `guard: {kind: pytest|none}` render
  this truth; honesty line per guard type.

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

## Open watch items (mine)

- When the README rewrite lands, confirm the testing-philosophy paragraph links to
  (not duplicates) WORKSHOP module 9 and the checks.py docstring.
- Screenshot retake (8 green checks) is still open; README ships with the current
  screenshot — caption must not overclaim what the image shows.
