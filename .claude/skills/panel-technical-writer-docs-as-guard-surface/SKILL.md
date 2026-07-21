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

## Idiom-migration corollary (dagster-duckdb panel, 2026-07-21)

When a panel weighs migrating a code IDIOM the tutorial teaches, don't assume the
migration "falsifies the tutorial." First grep whether the tutorial ALREADY teaches
the TARGET idiom in an earlier module. If it does, migrating usually IMPROVES
integrity: it makes the changed layer REINFORCE the earlier lesson instead of
competing with it. (DuckDB case: Module 2 already sells resources — glossary lists
"database" as a resource example — so a hand-rolled `duckdb.connect()` in Layer 2 was
a papered-over self-contradiction; a DuckDBResource resolves it.) The from-zero
"transparent, no-magic" argument for the raw pattern only holds in a tutorial that
never adopted the abstraction. And note which raw usages LEGITIMATELY survive: a
standalone REPL/exploration snippet ("query the DB yourself") should stay raw even
after the pipeline migrates — it teaches the tool, not the wiring. Map the blast
radius by line before debate; count the load-bearing mental-model phrase's echoes
(often it appears once) so you know whether it's a cascade or a single swap.

## Outcome that shipped: the why-NOT, not the migration (dagster-duckdb, 2026-07-21)

The DuckDB migration was BLOCKED by a code fact (`DuckDBResource.get_connection()`
hardcodes `read_only=False`, erasing the tested single-writer lock), so the panel kept
the raw code. But the coherence gap the migration would have closed (Module 2 taught
resources; why is Layer 2 hand-rolling?) is REAL and does not go away just because the
migration doesn't happen. The reusable technique:

1. **A blocked migration still owes the reader the why-not.** The worst outcome is
   "silent status quo" — raw code, no note — which reads as ignorance of the idiom
   rather than a judged choice. Document the non-adoption; it's richer teaching than
   another how-to ("when NOT to adopt an idiom" > "used the resource").
2. **Tooling why-nots live in ONE home as tradeoff-both-ways sections.** Here: WORKSHOP
   Module 10, beside "Why NOT Great Expectations." Name the mechanism, state the cost
   BOTH directions, and "when it would earn its place." Never a one-sided dismissal.
3. **Close the coherence gap with a forward-pointer, not a relocated rationale.** The
   teaching module (Module 2) gets a one-line "see Module 10" note; the rationale stays
   in its single home. Code comments at the choice site (transforms.py) only POINT.
4. **Guard the non-adoption.** Pin a stable rationale marker in the source beside the
   invariant it protects (`"DuckDBResource"` + `"read_only=False"` present in the file),
   so a future "modernize" refactor trips the pin and must re-read the decision. A
   deliberate omission is a guardable artifact, not just prose.

So the blast-radius grep pays off BOTH ways: even arguing against the change, it locates
the coherence gap the why-not must name and forward-point to.

## Companion rule (banked law, lives in checks.py docstring)

Check descriptions state the INVARIANT and its STAKES; run metadata carries
the particulars; rosters and numbers live only in `known_facts.py`. No check
string quotes another beat's caption or payoff. Every check string has TWO
readers — the Dagster operator and the site hover reader — and must serve
both without duplicating a roster whose home is elsewhere.
