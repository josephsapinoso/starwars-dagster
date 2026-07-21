---
name: panel-data-engineer-production-pattern-honesty
description: Deciding whether a "senior" production pattern (partitions, incremental MERGE, SCD2, backfills) is HONEST or cargo-cult on a small/static dataset, and how it collides with a single-file DuckDB warehouse pinned to in_process_executor + per-asset read_only. Use when a reviewer asks to "demonstrate scale patterns" on data that doesn't have the dimension the pattern needs.
---

# Production-pattern honesty on a static dataset

## The honesty test (run BEFORE choosing a form)
A production pattern is honest only if the DIMENSION it needs actually exists in the source.
- **Time partitions need a per-record time axis.** If the source is a single static snapshot,
  a `DailyPartitionsDefinition` fabricates a run-date axis and partitions identical data —
  DISHONEST (faked time). Reject outright.
- **Static partitions need a real high-value key.** A real key (e.g. `episode_id`) is honest
  but often HOLLOW if the fetch is whole-endpoint and the load is all-or-nothing: the partition
  degrades to `WHERE key=` on tiny data and buys nothing operationally. Honest ≠ worth it.
- **Incremental/SCD needs a real change signal.** A daily cron over static data produces zero
  deltas → the history table is hollow. Find the REAL cadence that produces real change (here:
  successive DATED snapshot refreshes — upstream drift is observed, not hypothetical). Hook the
  pattern to that, not to a faked cadence.

## The reframe that rescues CDC/SCD2 on "static" data
If the repo re-snapshots the source periodically and those snapshots genuinely differ across
refreshes, then "what changed between snapshot dates" is a REAL question. An as-of dimension
built by MERGE over two date-stamped snapshots is honest — provided the copy/table STATES the
observed delta count (a history table that never changes must say so; sell it as
capability-on-real-cadence, never as a claim of live churn).

## Architecture collision checklist (single-file DuckDB, pinned executor)
- A MERGE/SCD2 asset is a WRITER → make it a declared writer (open read-write; keep it OUT of
  `EXPECTED_DB_TABLES`; don't grow the raw-layer ordering check).
- `in_process_executor` is a FEATURE here: partition backfills run SEQUENTIALLY so the
  single-writer file lock holds. Multiprocess backfill would race the lock. Never switch
  executors to "parallelize the backfill." read_only readers stay read_only.
- SCD2 BREAKS "written table == returned frame" parity. Exclude the MERGE writer from the
  parity loop with a pinned reason; give it its OWN guard: two synthetic snapshots, one changed
  record, assert old version's `valid_to` closes + new version row opens (data-independent),
  plus a WARN drift note on real deltas. (Failure-mode separation applied to CDC.)

## Ripple discipline
- Prefer PIPELINE-ONLY v1: an asset no site claim cites stays off the provenance map.
- Still ripples asset/check COUNTS (README, CLAUDE.md, WORKSHOP, site totals) — same commit.
- CHECK whether the site DAG-strip pin is equality (chips == all real defs) or subset BEFORE
  claiming "site-free": if equality, any new asset forces the strip to render it.
- Adding the pattern REOPENS any "Limits, by design" copy that documented its absence — the
  forcing-trigger wording must change from hypothetical to the real trigger you hooked.

## Bar to clear (from the dagster-duckdb non-adoption bank)
A documented, guarded NON-adoption can out-signal bolted-on machinery. Demonstrated pattern
only wins if it sends a STRONGER 90-second senior signal than the honest documented limit AND
its correctness is really tested (not theater). If the only deltas are synthetic and no real
forcing trigger exists, the documented limit wins.
