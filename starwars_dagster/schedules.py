"""
Schedules
=========
Key Dagster concept — Schedules:
  A schedule runs a job (a selection of assets) on a cron expression.
  This simulates "streaming" by pulling fresh data from the SWAPI on a cadence.

  In a real pipeline, the API would return new records each run.
  For SWAPI (static data), this demonstrates the pattern: you'd swap in
  a live API (e.g., a sports score API, financial data feed) and the
  schedule logic stays identical.
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
    description="Pull fresh Star Wars data daily and rebuild the report",
)

# ── Bonus: a manual-trigger-only job for just the analytics layer ─────────────
analytics_only_job = define_asset_job(
    name="analytics_only",
    selection=AssetSelection.groups("03_analytics"),
    description="Re-run only the reporting layer (useful after tweaking report logic)",
)
