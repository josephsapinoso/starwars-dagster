---
name: panel-technical-writer-count-ripple
description: Checklist for landing any change to a displayed or documented count
  (assets, transforms, checks, tables, people) in the starwars-dagster repo without
  leaving a stale copy anywhere. Use whenever a number that appears in prose, a
  diagram, a tree comment, or a word-renderer changes.
---

# Count-ripple checklist

Copy that encodes a count is a drift surface. When a pipeline count changes, every
surface below must move in the SAME commit as the change (truth-then-tell: ripple
lands before any screenshot retake). Grep for both the digits and the spelled word.

## The law

1. Prefer count-free phrasing ("a checks file you can read in one sitting") unless
   the count IS the lesson. Every surface you exempt this way never ripples again.
2. Superseded claims either update or become explicit past tense — never linger as
   present tense.

## Surfaces (verified 2026-07-20; re-grep, don't trust line numbers)

- **README.md** — headline counts (:48), ASCII architecture diagram (:42–46 — a new
  source/group/stage must appear in the drawing, not just the table), group table
  (:52–54), exact-value-tests list (:79), Stack list, project-structure tree comments
  (:157 "five SWAPI pulls", :160 "15 asset checks", plus any new files/dirs).
- **WORKSHOP.md** — pattern sentences that enumerate ("The five raw assets…" :299,
  "all five raw lists" :338), quoted code snippets (Module 2 resources dict — a `...`
  can absorb additions; a fully-quoted dict cannot), exercises (a new feature must
  not pre-solve one — grep every Exercise before endorsing).
- **site/index.html** — the provenance totals triple (`"totals":{...}`, ~:413), AND
  every renderer that maps numbers to words: the `WORDS` array (~:863) must cover the
  new totals or the beat-7 sentence renders "undefined". The runtime detector only
  console.warns on overflow; ask QA for an offline pin if none exists.
- **Tests** — pinned strings in test_site_provenance.py (totals pin, per-asset check
  sets), any test that hardcodes rosters/counts outside known_facts.py.
- **Screenshots** — retake only AFTER the ripple lands (counts visible in the Dagster
  UI: check totals, asset counts).
- **Check descriptions / known_facts.py** — numbers live ONLY in known_facts;
  descriptions state invariant + stakes, so they never ripple. If a proposed
  description contains a digit or roster, that's the bug.

## Procedure

1. `grep -rn` the old digits AND the old spelled-out word (`15`, `fifteen`) across
   README.md, WORKSHOP.md, site/, tests/, starwars_dagster/, .github/.
2. Classify each hit: update / rewrite count-free / explicit past tense.
3. Check word-renderers and diagrams separately — grep misses drawings and arrays
   indexed by the count rather than containing it.
4. Land the whole ripple with the feature (feature + guard + copy, one commit).
5. Only then retake screenshots.
