---
name: enrichment-denominators
description: Vet any displayed number sourced from a sparse enrichment join (a second data source matched onto the primary cast) — nests the match denominator inside the field-present denominator, freezes baselines against a real fixture not a survey, and guards fan-out inflation separately from join loss.
---

# Enrichment-source denominator audit

Use when a number reaches the report/site from a SECOND source LEFT-JOINed onto the
primary grain (e.g. akabab profiles joined onto the 82 SWAPI people). Sparse enrichment
sources fail differently from the primary pull; the honesty burden is heavier, not lighter.

## Procedure

1. **Name both denominators.** Every enrichment number carries TWO: matched (rows that
   joined, e.g. 81 of 82) AND field-present (of the matched rows, how many have the field
   — the source is sparse). The displayed claim must read `N of {present} of {matched} of
   {total}` in spirit — never a bare N. A single "of 82" hides the sparsity; a single "of
   matched" hides the join loss. Both go on-page/on-chart.
2. **Superlative gate on tiny denominators.** If field-present is small (dozens or fewer:
   masters/apprentices/lineage-type fields), a ranked leaderboard or "top X" cannot carry a
   superlative honestly. Either disclose n hard next to the rank, or present as a list not a
   ranking. Small-n is exactly where a dataset can't prove the claim.
3. **Freeze against reality, not the survey.** Brief/survey/quick-fetch sparsity counts are
   NOT verifiable — fast models miscount large JSON, surveys drift. All expected baselines
   (record count, match count, field-present counts) are computed by code at a dedicated
   "freeze reality" step against the real fixture snapshot and read from the single
   known_facts home. A survey number must never become a displayed number.
4. **Guard fan-out separately from join loss.** A LEFT JOIN on a name key can fan out when
   the enrichment source has duplicate keys (Anakin/Vader-style collisions). This INFLATES
   counts silently — the opposite of join loss (which shrinks them). It earns its own
   BLOCKING grain check: `rows == primary_count AND key unique`. The coverage/miss check
   catches loss; it does NOT catch inflation. Both, always.
5. **Don't pre-guard an unsurfaced denominator.** A baseline check guarding a number that
   nothing yet displays is guard-for-guard's-sake — the inverse of coverage theater. Add the
   drift baseline in the same commit as the displayed claim, not before. Grain + coverage
   are the right guards while surfacing is deferred.

## The two-guard test still applies

A displayed enrichment count is a "presence-parsed display number": `N present` can silently
become `N still parseable` if the source reshapes the field. If surfaced, it needs a drift
baseline AND the coverage guard (see guard-failure-modes skill). Enumerate the derivation
path first: source drift / join loss / fan-out inflation / field-format breakage / render
drift — and confirm each fires a guard alone.
