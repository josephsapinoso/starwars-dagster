# Star Wars Dagster Pipeline

An end-to-end data engineering pipeline built with [Dagster OSS](https://dagster.io) that pulls live Star Wars data from the [SWAPI](https://swapi.info) REST API, transforms it with DuckDB, and generates an analytics report.

Built as a self-study workshop for learning Dagster fundamentals.

## Architecture

```
SWAPI (live API) → Raw JSON → DuckDB tables → SQL transforms → Markdown report
     ↑                ↑              ↑                ↑               ↑
  Resource        01_raw         star_wars_db    02_transformed   03_analytics
```

**10 assets across 3 groups:**

| Group | Assets | Description |
|---|---|---|
| `01_raw` | `raw_films`, `raw_people`, `raw_planets`, `raw_starships`, `raw_species` | HTTP pulls from SWAPI |
| `02_transformed` | `star_wars_db`, `characters_enriched`, `film_character_counts`, `starship_stats` | DuckDB storage + SQL |
| `03_analytics` | `galaxy_report` | Markdown summary report |

## Quick start

```bash
# 1. Install dependencies
pip install -e .

# 2. Launch Dagster UI
python -m dagster dev

# 3. Open http://localhost:3000 → Assets → Materialize all
```

## Stack

- **[Dagster](https://dagster.io)** — orchestration (open-source, free)
- **[DuckDB](https://duckdb.org)** — embedded analytics database
- **[SWAPI](https://swapi.info)** — Star Wars REST API (free, no auth)
- **Pandas** — DataFrame transforms
- **Python 3.11+**

## What you'll learn

Working through the `WORKSHOP.md` file covers:

- Software-Defined Assets and the Dagster asset graph
- Resources (configurable API clients)
- Layered pipeline architecture (raw → staging → transform → analytics)
- SQL transforms with DuckDB's JSON functions
- Schedules for recurring runs
- Re-executing from failure (not from scratch)
- Maintenance and observability patterns

## Output

After a successful run, `data/output/` contains:

- `galaxy_report.md` — characters, homeworlds, starship stats by film
- `characters_enriched.csv` — all characters joined with homeworld data
- `film_character_counts.csv` — cast size and starship count per episode
- `starship_stats.csv` — cleaned starship performance data

## Schedule

The pipeline includes a daily schedule (6 AM) that re-pulls from SWAPI — the same pattern you'd use for any REST API data feed.

```python
# schedules.py
daily_refresh_schedule = ScheduleDefinition(
    cron_schedule="0 6 * * *",
    job=full_pipeline_job,
)
```

## Project structure

```
starwars_dagster/
├── pyproject.toml
├── WORKSHOP.md                   ← self-study guide (~3-4 hours)
├── README.md
└── starwars_dagster/
    ├── __init__.py               ← Definitions (entry point)
    ├── schedules.py
    ├── assets/
    │   ├── ingestion.py          ← Layer 1: SWAPI pulls
    │   ├── transforms.py         ← Layers 2+3: DuckDB + SQL
    │   └── analytics.py          ← Layer 4: report
    └── resources/
        └── swapi_resource.py     ← SWAPI HTTP client
```

---

*May the Force be with your data platform.*
