---
name: static-source-cdc-honesty
description: Audit an SCD2 / incremental-merge / change-history / partitioned asset built on a source that never mutates records, for honesty of the CLAIM it implies. Use when a panel proposes "demonstrate a production pattern" (CDC, SCD2, backfills, partitions) on a small static dataset.
---

# Auditing a change-data-capture pattern on a static source

A change-history table on a frozen source records ZERO changes. Machinery is not a claim;
the QUESTION is what the table makes a reader believe, and whether the data proves it.

## The honesty test
1. **Name the implied claim.** A table labeled "change history" / "SCD2" IMPLIES CDC that
   fires. If the source never mutates a record, that capability is never exercised — the
   implication is false-by-default.
2. **State the claim the data DOES support**, with a denominator: "0 changes observed
   across N snapshots" (N = disclosed denominator; the zero is the story, like "23 of 82").
   The table must SAY 0, on-surface, not carry an empty history silently.
3. **The guard-shaped-hole tell**: if the only possible correctness guard can COUNT rows
   but never sees the mechanism fire (never a second version), the mechanism is vanity.

## Simulated deltas
- A synthetic changed record may exercise the merge's change-branch ONLY in a labeled
  TEST (a data-independent invariant: given a delta, the merge emits a correct new version).
- A synthetic delta must NEVER contaminate a real snapshot count or a displayed number.
- If demonstration change surfaces anywhere, label = "demonstration/synthetic," explicitly.

## Two-guard shape (failure-mode separation)
- Baseline: "0 versions across the frozen fixtures" (data-drift guard).
- Mechanism invariant: "merge detects a synthetic change correctly" (parser-broke twin).
- "Nothing changed" and "the merge can detect change" must FAIL DIFFERENTLY.

## Partition denominator trap
- Partitioning a many-to-many key (episode_id: a person in K films → K partitions) means
  per-partition counts DON'T sum to the census. Reshuffles the same rows, invents no
  number, and breaks cross-foot to the total.
- The honest static partition is a DISJOINT key (independent endpoints/entities): reprocess
  one is real, no fan-out. Any partitioned count on a public surface must cross-foot to the
  known total or disclose why it can't.
- **Topology caveat (before calling a partition "contained"):** if each endpoint/entity is
  ALREADY its own asset, a per-endpoint partition COLLAPSES N assets into 1 partitioned asset
  — dropping the asset count, rewriting lineage lessons, and rippling any site total/DAG pin.
  The "honest disjoint partition" can be the LARGER ripple, not the smaller one. Count the
  assets and site-pins the change touches before endorsing it as the contained version.

## When every demonstration is contrived
On a static, small, heterogeneous, few-row snapshot the source lacks the DIMENSION every
candidate pattern needs (no time axis; join keys many-to-many; endpoints heterogeneous; SCD
detects nothing). When SCD, partition, AND incremental are all contrived, a documented
"Limits, by design" why-not that names each ceiling with its forcing-trigger is the stronger
senior signal than bolted-on machinery. Then hunt the ONE non-contrived defect: copy/docs
that CLAIM a capability the code lacks (a scheduler on a static source is a full refresh —
say so). Fixing the over-claim, not adding the pattern, is the real work.

## Scope gate
Pipeline-only v1 ⇒ no provenance/DATA/drift-detector change. The moment ONE number
surfaces: derivable-from-JSON, denominator on-chart, guard same commit, count-ripple.
