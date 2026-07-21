---
name: panel-qa-engineer-production-pattern-guards
description: Guard slate for a "production pattern" asset (partitions, incremental MERGE, SCD2) demonstrated on a STATIC source. Use when a panel proposes adding partitioning/incremental/slowly-changing-dimension capability to prove scale skills, and you must design the tests/asset-checks that prove it works AND keep it honest (no implied CDC that never fires).
---

# Guarding a production pattern on a static source

Banked from the production-pattern prep (2026-07-21). Adding partitions / incremental
MERGE / SCD2 to a portfolio pipeline demonstrates scale skills a full-refresh can't. The
trap: the source is FROZEN, so a history/SCD table never actually changes — surfacing it
as live "change history" is implied-live-status dishonesty. The guard slate must prove
the MECHANISM works while telling the truth that it never fires in production.

## Pick the honest form first

- Static partitions over a REAL key that exists in the data (e.g. `episode_id`,
  endpoint): honest, zero CDC-implication risk — you genuinely reprocess per slice.
  Cheaper guards.
- SCD2 / incremental MERGE on a daily snapshot of a frozen source: STRONGER senior
  signal, but the history has one version per entity forever. Heavier guards + strict
  copy discipline. Only ship if the honesty guards (below) land in the same commit.

## Partitioned-asset guard slate (offline)

1. Partition-roster pin (ungated pytest): partition def keys == the known_facts roster;
   a key absent from the data cannot be defined.
2. Single-partition materialize: assert only that slice persists.
3. Backfill PARITY: materialize ALL partitions, union == full-refresh output for the same
   data. This is the anti-gap / anti-overlap guard at partition seams — the load-bearing
   partition test.
4. Invalid partition key raises or yields empty, never silently mis-writes.
5. New writer joins the declared-writers loop; executor stays in_process.

## SCD2 / incremental MERGE guard slate (offline behavior tests)

Craft day1/day2 records with the inline resource; never depend on fixture content.

1. Merge correctness: valid_from/valid_to/is_current set right; prior version closed.
2. IDEMPOTENCY (the key incremental guard): re-run an identical snapshot → zero new
   history rows. Seen-to-fail: break the merge key → duplicates appear.
3. Change-detection on a SIMULATED delta: change one field between snapshots → exactly
   one new version, prior version closed. Ungated/synthetic — proves the mechanism.
4. No-phantom-change: identical field → NO new version (catches a merge that re-versions
   every run — the false-CDC bug).
5. Static-source HONESTY guard (snapshot-gated): on the real frozen snapshot, history
   holds one current version per entity and zero superseded rows. The pipeline STATES
   "static source, mechanism demonstrated," never implies churn.

## The honesty floor (the part QA owns)

- Two-guard separation applies: "mechanism works" (offline, synthetic, UNGATED) vs
  "source is static / zero changes on file" (snapshot-gated drift). Never let one
  masquerade as the other.
- Vocabulary discipline (kin to "deaths on file"): "as-of snapshot" / "one version on
  file", never "change history" implying churn that never happens.
- No site badge/beat implying live change tracking. If surfaced at all, copy names the
  source as frozen and the pattern as a demonstrated capability.

## Collisions to check every time

- read_only single-writer pin: a MERGE/SCD/partitioned asset is a WRITER → declared-
  writers loop, opens read-write; readers untouched. Holds.
- Executor lock: partition backfill / repeated merge writes to a single-file warehouse
  MUST stay in_process (sequential). Multiprocess backfill races the single-writer lock.
  The access-policy test pins in_process — protects this; do not switch for parallel
  backfill without a panel.
- Offline-CI: mechanism tests use the inline resource (offline); the honesty guard gates
  on the snapshot marker.
- COUNT-RIPPLE: a new asset + checks bump the totals; the site total-count pin and the
  DAG-strip chip set (pinned to real asset keys) move in the SAME commit. "Pipeline-only
  v1" is NOT site-zero-touch — the DAG strip gains a chip and totals shift, and a
  "Limits, by design" line (e.g. "no partitions") gets removed. Flag the ripple owner.
