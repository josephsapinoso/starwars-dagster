"""
Schedules
=========
Key Dagster concept — Schedules:
  A schedule runs a job (a selection of assets) on a cron expression.

  What this demonstrates: cron-driven orchestration of the whole graph.
  What it deliberately does NOT do: SWAPI is a static snapshot, so each run
  re-pulls the same records and rebuilds the warehouse from scratch — a full
  refresh, not an incremental or streaming load, and not change capture (see
  "Full refresh, no history" under "Limits, by design" in the README). Point
  the same schedule at a live, changing source and the orchestration is
  identical; the incremental/merge logic a changing source would need is
  honestly absent here, because this source never changes.
"""

from dagster import (
    ScheduleDefinition,
    define_asset_job,
    AssetSelection,
)

# ── Define a job that materializes ALL assets in order ───────────────────────
full_pipeline_job = define_asset_job(
    name="full_star_wars_pipeline",
    selection=AssetSelection.all(),
    description="Ingest → transform → report for all Star Wars data",
)

# ── Schedule: run every day at 6am ───────────────────────────────────────────
daily_refresh_schedule = ScheduleDefinition(
    name="daily_star_wars_refresh",
    job=full_pipeline_job,
    cron_schedule="0 6 * * *",   # 6:00 AM every day
    description="Re-pull SWAPI and rebuild the report daily (full refresh; the snapshot is static)",
)

# ── Bonus: a manual-trigger-only job for just the analytics layer ─────────────
analytics_only_job = define_asset_job(
    name="analytics_only",
    selection=AssetSelection.groups("03_analytics"),
    description="Re-run only the reporting layer (useful after tweaking report logic)",
)
