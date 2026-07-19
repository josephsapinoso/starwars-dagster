---
name: docs-as-guard-surface
description: Treat tutorials and exercises as a guard surface when evaluating new repo features — grep teaching docs for collisions before endorsing code, because shipped code can silently pre-solve an exercise or falsify a doc claim.
---

# Docs are a guard surface

Established by the post-landing-cleanup panel (2026-07-18): WORKSHOP Exercise 8
("add an asset check to galaxy_report...") was exactly the check proposed in
Q3(b). Shipping it would have turned a hands-on exercise into answer-key
copying. The collision finding flipped QA's vote and made disclose-only
unanimous. Teaching integrity can veto a feature, not just a phrasing.

Second exercise (birth-registry panel, 2026-07-19): the prep grep caught
WORKSHOP:705's hardcoded "five tables and thirteen checks" before the 13→15
ripple would have falsified it; it shipped count-free ("a checks file you can
read in one sitting") in the same commit, and WORKSHOP is now on the permanent
count-ripple checklist — teaching prose states counts count-free unless the
count is the lesson.

## Procedure (run during PREP for any proposed repo feature)

1. **Grep the teaching docs for the feature's nouns.** For this repo:
   `WORKSHOP.md` exercises and modules; also README claims. Search the asset
   name, check name, table name, and the behavior ("fails if", "add a check",
   the file/threshold involved).
2. **Classify each hit:**
   - *Pre-solved exercise* — the feature IS an exercise's answer. Remedy:
     block the feature, or re-point the exercise (different assertion, or
     "compare with the shipped check") in the SAME commit.
   - *Falsified claim* — a doc sentence becomes untrue or newly true. Remedy:
     correct or strengthen the sentence in the same commit (e.g. README's
     "SQL behind every chart" strengthened to "executed against the
     fixture-built warehouse" only once that became true).
   - *Count drift* — any copy encoding a count (README totals, tree comments,
     number-word lists, provenance totals) moves atomically with the feature.
3. **Pre-draft the winning-branch copy.** Write the doc edits conditional on
   the feature landing, during prep. Both post-landing Q2 doc edits shipped
   near-verbatim from prep drafts — this is what makes "feature and guard and
   doc in the same commit" frictionless instead of rushed.

## Companion rule (banked law, lives in checks.py docstring)

Check descriptions state the INVARIANT and its STAKES; run metadata carries
the particulars; rosters and numbers live only in `known_facts.py`. No check
string quotes another beat's caption or payoff. Every check string has TWO
readers — the Dagster operator and the site hover reader — and must serve
both without duplicating a roster whose home is elsewhere.
