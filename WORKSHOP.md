# 🌌 Dagster Workshop: Building a Star Wars Data Pipeline

> **Audience:** Complete beginners to Dagster and data orchestration  
> **Format:** Self-study — work through each module at your own pace  
> **Time estimate:** ~3–4 hours total  
> **What you'll build:** A fully working pipeline that pulls Star Wars data from a live API, transforms it with DuckDB, and produces an analytics report — all orchestrated by Dagster

---

## Table of Contents

1. [Is Dagster Free?](#1-is-dagster-free)
2. [What Is Dagster — and Why Use It?](#2-what-is-dagster--and-why-use-it)
3. [Architecture Overview](#3-architecture-overview)
4. [Setup and Installation](#4-setup-and-installation)
5. [Module 1 — Core Concepts](#5-module-1--core-concepts)
6. [Module 2 — Resources (The API Connection)](#6-module-2--resources-the-api-connection)
7. [Module 3 — Ingestion Assets (Layer 1)](#7-module-3--ingestion-assets-layer-1)
8. [Module 4 — Transform Assets (Layers 2 & 3)](#8-module-4--transform-assets-layers-2--3)
9. [Module 5 — Analytics Asset (Layer 4)](#9-module-5--analytics-asset-layer-4)
10. [Module 6 — Running the Pipeline in the Dagster UI](#10-module-6--running-the-pipeline-in-the-dagster-ui)
11. [Module 7 — Schedules (Simulated Streaming)](#11-module-7--schedules-simulated-streaming)
12. [Module 8 — Testing & Asset Checks](#12-module-8--testing--asset-checks)
13. [Module 9 — Maintenance Playbook](#13-module-9--maintenance-playbook)
14. [Module 10 — Going Further](#14-module-10--going-further)
15. [Cheat Sheet](#15-cheat-sheet)

---

## 1. Is Dagster Free?

**Yes — the open-source version is completely free.**

| Tier | Cost | What you get |
|---|---|---|
| **Dagster OSS** (what this workshop uses) | Free forever | Full orchestrator, local UI, all core features |
| **Dagster+ Solo** | ~$10/month + usage | Cloud-hosted, auth, alerting |
| **Dagster+ Starter** | ~$100/month + usage | Teams, SSO, advanced observability |

For learning, local development, and small-to-medium production workloads, **OSS is all you need**. The code in this workshop runs entirely on your laptop with zero cloud dependencies.

---

## 2. What Is Dagster — and Why Use It?

### The problem it solves

Imagine you have 20 Python scripts that:
- Pull data from APIs
- Transform it with SQL
- Load it into a database
- Generate a report

Running them in order manually works… until one fails halfway through, and you're not sure which step broke, which data is stale, and what to rerun.

**Dagster solves this** by letting you define your data pipeline as a graph of *assets* — pieces of data — rather than a sequence of tasks. It tracks what exists, what's stale, and what failed, and lets you rerun just the broken piece.

### How Dagster compares to other tools

| Tool | Mental model | Best for |
|---|---|---|
| **Dagster** | "What data do I have?" (asset-centric) | Modern data engineering, lineage, testing |
| Airflow | "What tasks do I run?" (task-centric) | Legacy ETL, lots of operators |
| Prefect | Hybrid | Python-heavy workflows |
| dbt | SQL transforms only | The T in ELT |

Dagster is increasingly the standard for new data engineering projects because it was designed from the start around **data lineage** and **testability**.

### Key terms you'll see everywhere

| Term | Simple definition |
|---|---|
| **Asset** | A piece of data your pipeline produces (a table, file, model) |
| **Asset materialization** | The act of running code to create/update an asset |
| **Resource** | A shared connection to an external system (API, database, S3) |
| **Job** | A named selection of assets to run together |
| **Schedule** | A cron-based trigger for a job |
| **Sensor** | An event-driven trigger (e.g., "run when a file appears") |
| **Definitions** | The top-level object that wires everything together |

---

## 3. Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    STAR WARS PIPELINE                        │
│                                                             │
│  ┌──────────────┐                                           │
│  │  SWAPI       │  ← Live REST API (swapi.info)             │
│  │  Resource    │    Films, People, Planets, Ships, Species │
│  └──────┬───────┘                                           │
│         │ HTTP GET                                          │
│         ▼                                                   │
│  ┌─────────────────────────────────────────────┐           │
│  │  Layer 1: Raw Ingestion                      │           │
│  │  raw_films  raw_people  raw_planets          │           │
│  │  raw_starships  raw_species                  │           │
│  │  → saves JSON to data/raw/                   │           │
│  └─────────────────┬───────────────────────────┘           │
│                    │ Python lists                           │
│                    ▼                                        │
│  ┌─────────────────────────────────────────────┐           │
│  │  Layer 2: DuckDB Storage                     │           │
│  │  star_wars_db                                │           │
│  │  → loads 5 tables into data/star_wars.duckdb │           │
│  └─────────────────┬───────────────────────────┘           │
│                    │ DuckDB path                            │
│                    ▼                                        │
│  ┌─────────────────────────────────────────────┐           │
│  │  Layer 3: SQL Transforms                     │           │
│  │  characters_enriched  (people + planets)     │           │
│  │  film_character_counts (films aggregated)    │           │
│  │  starship_stats       (cleaned + typed)      │           │
│  │  character_stats      (per-person counts)    │           │
│  │  → saves Parquet to data/output/             │           │
│  └─────────────────┬───────────────────────────┘           │
│                    │ DataFrames                             │
│                    ▼                                        │
│  ┌─────────────────────────────────────────────┐           │
│  │  Layer 4: Analytics Report                   │           │
│  │  galaxy_report                               │           │
│  │  → data/output/galaxy_report.md              │           │
│  └─────────────────────────────────────────────┘           │
│                                                             │
│  Orchestration: daily_refresh_schedule (6am daily)         │
└─────────────────────────────────────────────────────────────┘
```

### Data source: SWAPI

The [Star Wars API](https://swapi.info) (`swapi.info`) is a free, no-auth REST API with:
- No rate limits
- Sub-50ms global response times
- 100% uptime SLA
- 6 endpoints: `/films/`, `/people/`, `/planets/`, `/starships/`, `/vehicles/`, `/species/`

This simulates a real streaming data source — each scheduled run pulls the latest snapshot, exactly like you'd do with a financial data API, IoT sensor feed, or social media API.

---

## 4. Setup and Installation

### Prerequisites
- Python 3.11 or 3.12
- pip
- A terminal

### Step 1 — Navigate to the project

```bash
cd path/to/starwars_dagster
```

### Step 2 — Create a virtual environment

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### Step 3 — Install dependencies

```bash
pip install -e ".[dev]"
```

This installs: `dagster`, `dagster-webserver`, `duckdb`, `pandas`, `requests`,
plus `pytest` for the test suite (Module 8).

### Step 4 — Verify installation

```bash
dagster --version
# Should print: dagster, version 1.x.x
```

### Step 5 — Launch the Dagster UI

```bash
dagster dev
```

Open your browser to **http://localhost:3000**

You should see the Dagster Launchpad with your pipeline loaded.

> **Troubleshooting:** If you get a `ModuleNotFoundError`, make sure your virtual environment is activated (`source .venv/bin/activate`).

---

## 5. Module 1 — Core Concepts

### What is a Software-Defined Asset?

Open `starwars_dagster/assets/ingestion.py` and look at this:

```python
@asset(group_name="01_raw", description="All Star Wars films from SWAPI")
def raw_films(context: AssetExecutionContext, swapi: SWAPIResource) -> list[dict]:
    films = swapi.fetch("films")
    context.add_output_metadata({"record_count": len(films)})
    _save_json("films", films)
    return films
```

Break it down:

| Part | What it means |
|---|---|
| `@asset` | Tells Dagster "the return value of this function IS a data asset" |
| `group_name="01_raw"` | Groups this asset in the UI with other raw assets |
| `swapi: SWAPIResource` | Dagster injects the API resource automatically |
| `context: AssetExecutionContext` | Lets you log metadata, emit events |
| `return films` | The Python object is the asset's value, passed to downstream assets |

### The asset graph

In the Dagster UI, click **Assets** in the left sidebar. You'll see a visual graph showing:
- Which assets depend on which
- Which assets are materialized (have fresh data) vs. stale
- Metadata from the last run

This graph is built **automatically** from your function signatures — you never manually define dependencies.

### ✅ Exercise 1

1. Open the Dagster UI at http://localhost:3000
2. Click **Assets** in the sidebar
3. Find `raw_films` and click it
4. What does the asset detail page show?
5. Click **Materialize** in the top right — what happens?

---

## 6. Module 2 — Resources (The API Connection)

Open `starwars_dagster/resources/swapi_resource.py`.

```python
class SWAPIResource(ConfigurableResource):
    base_url: str = "https://swapi.info/api"
    timeout_seconds: int = 30

    def fetch(self, endpoint: str) -> list[dict]:
        url = f"{self.base_url}/{endpoint}/"
        response = requests.get(url, timeout=self.timeout_seconds)
        response.raise_for_status()
        ...
```

### Why use a Resource instead of just `requests.get()`?

1. **Testability** — swap in a `MockSWAPIResource` that returns static data without hitting the real API
2. **Reusability** — one resource, many assets; change `base_url` in one place
3. **Observability** — Dagster tracks resource usage per run
4. **Configuration** — override `timeout_seconds` at launch time without changing code

### How resources are wired in

Open `starwars_dagster/__init__.py`:

```python
defs = Definitions(
    assets=all_assets,
    resources={
        "swapi": SWAPIResource(),   # key "swapi" matches parameter name in assets
    },
    ...
)
```

The key `"swapi"` must match the parameter name in your assets. Dagster injects it automatically — your asset functions never import or instantiate the resource directly.

> **Heads-up for later:** resources aren't the right answer for *every* external system. The
> transform layer (Module 3) deliberately opens DuckDB with a raw `duckdb.connect()` instead of a
> `DuckDBResource`, to keep an access-control guarantee the framework resource can't express.
> [Module 10](#14-module-10--going-further) explains exactly why — a worked example of choosing
> *not* to adopt an idiom.

### ✅ Exercise 2

Try calling the API manually to see what it returns:

```python
import requests
r = requests.get("https://swapi.info/api/films/")
import json
print(json.dumps(r.json()[0], indent=2))
```

Note how `characters`, `planets`, etc. are lists of URLs (not embedded objects). This is why our transform layer needs to join them.

---

## 7. Module 3 — Ingestion Assets (Layer 1)

Open `starwars_dagster/assets/ingestion.py`.

The raw assets all follow the same pattern:
1. Call `resource.fetch(endpoint)`
2. Log metadata to the Dagster UI with `context.add_output_metadata()`
3. Save JSON to `data/raw/<name>.json` for debugging
4. Return the data for downstream assets

Five of them pull SWAPI endpoints through `SWAPIResource`. The sixth,
`raw_character_profiles`, applies the *same pattern to a different resource* —
`AkababResource`, a second data source serving static JSON character profiles.
Compare the two asset definitions side by side: only the injected resource and
the endpoint change. That symmetry is the point of the resource abstraction,
and it's what Exercise 3 below asks you to reproduce.

### Materializing the raw layer

In the Dagster UI:
1. Click **Assets**
2. Click **View global asset lineage** to see the full graph
3. Filter to group `01_raw`
4. Click **Materialize all**

Watch the run logs in real time. Each asset shows:
- Which step is running
- Logs from `get_dagster_logger()`
- Metadata like `record_count`

### Inspecting raw output

After the run, check:
```bash
ls data/raw/
cat data/raw/films.json | python -m json.tool | head -60
```

### ✅ Exercise 3

The pipeline currently fetches five SWAPI endpoints: films, people, planets, starships, and species. Add a `raw_vehicles` asset following the same pattern. The endpoint is `/vehicles/`. Then add it to `assets/__init__.py`.

---

## 8. Module 4 — Transform Assets (Layers 2 & 3)

Open `starwars_dagster/assets/transforms.py`.

### Layer 2: star_wars_db

This asset takes all five raw lists and loads them into DuckDB tables:

```python
@asset(...)
def star_wars_db(
    context,
    raw_films,       # ← Dagster passes these automatically from Layer 1
    raw_people,
    raw_planets,
    raw_starships,
    raw_species,
) -> str:
    con = duckdb.connect(str(DB_PATH))
    ...
    return str(DB_PATH)   # downstream assets get the DB file path
```

**Note the pattern:** assets return data (or paths to data). The return value of `star_wars_db` is a file path string that the Layer 3 assets use to open a connection.

### Layer 3: SQL transforms

Each transform asset:
1. Opens the DuckDB file from the path passed by `star_wars_db`
2. Runs a SQL query
3. Returns a Pandas DataFrame
4. Saves a Parquet file as a side effect

The SQL uses DuckDB-specific functions like `json_array_length()` to handle the JSON arrays that SWAPI stores inline (e.g., a film's list of character URLs).

One deliberate exception to the pattern: `characters_enriched` additionally writes its result back into the warehouse (`CREATE OR REPLACE TABLE`) so the enriched grain is queryable with plain SQL — which is also what lets the dashboard's displayed SQL strings be executed against the real database by the offline test suite.

### Querying DuckDB yourself

```python
import duckdb
con = duckdb.connect("data/star_wars.duckdb")

# What tables exist?
print(con.execute("SHOW TABLES").fetchdf())

# Preview the people table
print(con.execute("SELECT name, birth_year, homeworld FROM people LIMIT 10").fetchdf())

# Characters from Tatooine
print(con.execute("""
    SELECT p.name, pl.name AS planet
    FROM people p
    JOIN planets pl ON p.homeworld = pl.url
    WHERE pl.name = 'Tatooine'
""").fetchdf())
```

### ✅ Exercise 4

Add a new transform asset `species_summary` that counts how many characters belong to each species. Hint: you'll need to handle the fact that `people.species` is a JSON array of URLs, and you'll need to look up the species name from the `species` table.

---

## 9. Module 5 — Analytics Asset (Layer 4)

Open `starwars_dagster/assets/analytics.py`.

The `galaxy_report` asset assembles the three transform DataFrames into a Markdown report and writes it to `data/output/galaxy_report.md`.

### Key pattern: MetadataValue.md

```python
context.add_output_metadata({
    "preview": MetadataValue.md(report[:2000]),
})
```

This renders a **Markdown preview directly in the Dagster UI asset page** — no need to open the file. This is extremely useful for "showing your work" to stakeholders without building a separate dashboard.

### After running

```bash
cat data/output/galaxy_report.md
```

You'll see tables with character counts per film, top homeworlds, gender breakdown, and the fastest starships in the galaxy.

### ✅ Exercise 5

Modify `galaxy_report` to add a new section: **"Most Dangerous Planets"** — defined as planets with `climate` containing `"arid"` or `"frozen"`. List them with their terrain and population.

---

## 10. Module 6 — Running the Pipeline in the Dagster UI

### Launching a full run

1. In the Dagster UI, click **Jobs** in the left sidebar
2. Click **full_star_wars_pipeline**
3. Click **Launch Run**
4. Watch the asset graph animate as assets complete in order

### The run page

Each run shows:
- **Asset graph** with green/red completion states
- **Logs** panel with structured log output
- **Asset materializations** — click any asset to see its metadata

### Re-running failed assets

If one asset fails (e.g., the API times out):
1. Click the failed asset in the run graph (shown in red)
2. Click **Re-execute from failure**
3. Dagster skips already-completed assets and retries only from the failure point

This is the single biggest productivity win over raw scripts — you don't rerun everything from scratch.

### Viewing asset history

Click **Assets** → click `galaxy_report` → click **Activity** tab. You'll see every time this asset was materialized, with links to the metadata from each run.

---

## 11. Module 7 — Schedules (Simulated Streaming)

Open `starwars_dagster/schedules.py`.

```python
daily_refresh_schedule = ScheduleDefinition(
    name="daily_star_wars_refresh",
    job=full_pipeline_job,
    cron_schedule="0 6 * * *",   # 6:00 AM every day
)
```

### Cron quick reference

| Expression | Meaning |
|---|---|
| `0 6 * * *` | 6:00 AM every day |
| `0 * * * *` | Every hour |
| `*/15 * * * *` | Every 15 minutes |
| `0 9 * * 1` | 9:00 AM every Monday |

### Activating a schedule

1. In the Dagster UI, click **Schedules** in the left sidebar
2. Find `daily_star_wars_refresh`
3. Toggle it **ON**

Dagster's built-in scheduler will now trigger the pipeline at 6am every day as long as `dagster dev` is running. In production, you'd use the Dagster daemon (`dagster-daemon run`) as a background service.

### Why this simulates streaming

Real streaming pipelines (Kafka, Kinesis) process events as they arrive. For REST APIs, the practical equivalent is **polling on a schedule** — you pull the delta or full snapshot at regular intervals. The pattern here (schedule → job → assets) is identical to how you'd wire up:
- A sports score API polled every 5 minutes
- A financial data feed polled hourly
- A government data portal polled nightly

Swap `SWAPIResource` for any other HTTP resource and the orchestration layer stays the same. The repo demonstrates this claim in code: `AkababResource` is exactly that swap — a second static-JSON source behind the same asset pattern, and nothing downstream of the resource had to change shape.

---

## 12. Module 8 — Testing & Asset Checks

A pipeline you can't rerun deterministically isn't tested — it's rehearsed. This
module adds two complementary layers of verification, and the distinction between
them is the single most useful idea to take away:

> **Tests guard the code at dev time. Asset checks guard the data at run time.**
> You need both, because SWAPI can change under you without a single line of your
> code changing.

### Pattern 1 — Unit test with a fake resource

Because `SWAPIResource` is injected by Dagster rather than imported directly,
tests can substitute a fake that reads committed fixture JSON instead of calling
the network (`tests/conftest.py`):

```python
class FakeSWAPIResource(SWAPIResource):
    def fetch(self, endpoint: str) -> list[dict]:
        return json.loads((FIXTURE_DIR / f"{endpoint}.json").read_text())
```

*Why injection beats `requests-mock`:* you're testing your pipeline, not the
`requests` library. Swapping the resource swaps the whole network layer in one
line, and the same fake works for every asset that uses the resource.

### Pattern 2 — Full-graph integration test with `materialize()`

`dagster.materialize()` runs an asset graph in-process — no UI, no daemon
(`tests/test_pipeline.py`):

```python
result = materialize(ALL_ASSETS + ALL_CHECKS, resources={"swapi": fake_swapi})
assert result.success
```

One such test proves resource injection, DuckDB loading, every SQL transform,
and the report render, end to end, offline, in seconds. It runs in a temporary
directory so it can never touch your real `data/`.

### Pattern 3 — Asset checks for runtime data quality

`@asset_check` attaches a data assertion to an asset; its pass/fail state shows
up on the lineage graph in the UI (`starwars_dagster/assets/checks.py`):

```python
@asset_check(asset=raw_people, blocking=True,
             description="Records must carry the keys downstream joins depend on.")
def raw_people_has_required_shape(raw_people: list[dict]) -> AssetCheckResult:
    ...
```

*The severity tradeoff:* structural breakage (empty tables, missing keys) is
`blocking=True` — stop before corrupting downstream assets. Value drift (SWAPI
gains person #83) is a **WARN** — upstream data isn't ours to freeze, so the
verified baselines live in `starwars_dagster/known_facts.py` and drift warns
instead of breaking. Getting this severity split wrong in either direction is
the classic data-quality failure mode: block on drift and every upstream edit
bricks your pipeline; warn on breakage and you ship corrupt data.

### Running it

```bash
pip install -e ".[dev]"
pytest -v          # offline; test names read as a table of verified facts
```

Tests run against small **synthetic** fixtures by design (see
`tests/fixtures/swapi/README.md`). To freeze a real dated snapshot of the API —
which also activates the exact-value tests (82 people, 3 six-film characters…) —
run `python scripts/snapshot_fixtures.py` once and commit the result.

### ✅ Exercise 8

Add an asset check to `galaxy_report` that fails if the report file is under
1 KB (a truncated render). Then break it on purpose — comment out a section of
the report — and watch where the failure surfaces in the UI.

---

## 13. Module 9 — Maintenance Playbook

### Daily operations

**Check asset freshness**  
In the Dagster UI, the **Assets** page shows a freshness indicator next to each asset. Green = recently materialized, yellow = stale. A quick scan takes 30 seconds.

**Investigate a failure**
1. **Runs** → filter by **Failed**
2. Click the failed run → find the red asset
3. Expand logs → look for `ERROR` lines
4. Common causes: API timeout (retry), schema change in API response (update transform), disk full (clear `data/raw/`)

**Re-run after fixing**  
Use **Re-execute from failure** — don't rerun the full pipeline unless ingestion data is stale.

### Weekly operations

**Check data quality**  
Connect to DuckDB and run sanity checks:
```sql
-- People count hasn't dropped
SELECT COUNT(*) FROM people;  -- expect ~82

-- No nulls in critical fields
SELECT COUNT(*) FROM people WHERE name IS NULL;  -- expect 0

-- Films still have characters
SELECT title, json_array_length(characters) FROM films;
```

**Review logs**  
In Dagster UI → **Runs** → sort by **Duration**. If a run is suddenly 5x slower, investigate API latency or local disk issues.

### Updating the pipeline

**Adding a new asset:**
1. Write the `@asset` function in the appropriate module (`ingestion.py`, `transforms.py`, or `analytics.py`)
2. Add it to `assets/__init__.py`
3. Restart `dagster dev` — the new asset appears in the UI automatically

**Changing a transform:**
1. Edit the SQL or Python logic
2. Restart `dagster dev`
3. Materialize the changed asset and all downstream assets using **Materialize with dependencies**

**Updating dependencies:**
```bash
pip install --upgrade dagster dagster-webserver
# Then test: dagster dev
```

### Production deployment checklist

When you're ready to move beyond `dagster dev`:

- [ ] Run `dagster-daemon run` as a background service (handles schedules and sensors)
- [ ] Set `DAGSTER_HOME` env var to a persistent directory for run history storage
- [ ] Move `DB_PATH` and `RAW_DIR` to a shared/mounted volume
- [ ] Add alerting: email or Slack on run failure (built into Dagster+, or DIY with a sensor)
- [ ] Add retries to assets: `@asset(retry_policy=RetryPolicy(max_retries=3))`
- [ ] Add freshness policies: warn if `galaxy_report` hasn't materialized in 25 hours

---

## 14. Module 10 — Going Further

### Add a Sensor (event-driven runs)

A sensor watches for an external event and triggers a job. For example, trigger a rerun when a new file appears:

```python
from dagster import sensor, RunRequest, SensorEvaluationContext
import os

@sensor(job=analytics_only_job)
def new_data_sensor(context: SensorEvaluationContext):
    """Trigger analytics when raw data files are newer than last run."""
    newest = max(os.path.getmtime(f) for f in pathlib.Path("data/raw").glob("*.json"))
    if newest > float(context.cursor or 0):
        yield RunRequest(run_key=str(newest))
        context.update_cursor(str(newest))
```

### Add Partitions (process data by episode)

Partitions let you run the pipeline separately for each subset of data:

```python
from dagster import StaticPartitionsDefinition

film_partitions = StaticPartitionsDefinition(
    ["Episode I", "Episode II", "Episode III", "Episode IV", "Episode V", "Episode VI"]
)

@asset(partitions_def=film_partitions)
def raw_film_by_episode(context: AssetExecutionContext, swapi: SWAPIResource):
    episode = context.partition_key
    ...
```

This unlocks incremental processing — only reprocess new or changed episodes.

### Add dbt for SQL transforms

Replace `transforms.py` with a dbt project for more powerful SQL lineage:

```bash
pip install dagster-dbt dbt-duckdb
```

Then define your transforms as dbt models and load them as Dagster assets with `@dbt_assets`.

### Why NOT Great Expectations or Soda?

A common next step in other tutorials is bolting on a dedicated data-quality
framework. This repo deliberately doesn't — and the reasoning is a lesson in
itself:

- **Dagster-native `@asset_check`s already cover the need here** (Module 8):
  they run with materialization, show up on the lineage graph, and share
  Python with the transforms they guard. A second framework would mean a
  second place to define expectations, a second config surface, and a second
  set of failure semantics — cost without new coverage at this scale.
- **When would one earn its cost?** When checks must be authored by people
  who don't write pipeline code (a data steward writing YAML expectations),
  when you need cross-orchestrator portability, or when a catalog of hundreds
  of table-shape assertions outgrows hand-written Python. None of that is
  true for a handful of tables and a checks file you can read in one sitting.

The tradeoff, not the tool, is the takeaway: add a data-quality framework
when its authorship or scale story applies to you — not because a tutorial
listed it as a next step.

### Why NOT `dagster-duckdb`'s `DuckDBResource`?

Dagster ships a first-party [`dagster-duckdb`](https://docs.dagster.io/integrations/libraries/duckdb)
integration, and Module 2 just taught you to reach for resources — so why does the transform
layer hand-roll `duckdb.connect()` instead of injecting a `DuckDBResource`? Because the resource
**can't express this pipeline's safety contract**, and that omission is the more interesting lesson:

- **The gap.** `DuckDBResource.get_connection()` **hardcodes `read_only=False`** and takes no
  per-call arguments. DuckDB allows *many readers OR one writer* on a file, so the pure-read
  transforms here open with `read_only=True` — a lock DuckDB itself enforces, pinned by source
  introspection in `tests/test_pipeline.py`. Through the resource, every asset would open
  read-write and the reader/writer distinction would collapse into a naming convention, not an
  enforced lock. Two resource instances ("reader"/"writer") or a subclass could paper over it —
  but a subclass just re-hand-rolls the exact `read_only=` line the migration was meant to remove.
- **What we keep by not migrating.** A clean, uniform data-flow story (`star_wars_db` returns a
  path; each transform opens it) *and* a real, tested single-writer safety invariant.
- **When would `DuckDBResource` earn its place?** When you want per-environment database paths from
  config, connection pooling, or you're standardizing DuckDB access across many pipelines and
  uniform wiring matters more than the read-only guarantee.

The tradeoff, not the idiom, is the takeaway: reach for the framework-native resource when its
configuration story helps you more than an explicit, enforced access policy does.

Asset checks appear in the Dagster UI as pass/fail badges on each asset.

### Swap in a real streaming API

Replace `SWAPIResource` with any live API:
- **Sports:** ESPN API, SportsDB
- **Finance:** Alpha Vantage, Yahoo Finance
- **Weather:** OpenWeatherMap
- **Space (still Star Wars adjacent):** NASA Exoplanet Archive

The Dagster plumbing doesn't change — only the resource implementation.

---

## 15. Cheat Sheet

```bash
# Start the UI
dagster dev

# Run the full pipeline from CLI (no UI)
dagster job execute -m starwars_dagster -j full_star_wars_pipeline

# Materialize a single asset from CLI
dagster asset materialize -m starwars_dagster --select raw_films

# Materialize an asset + all its dependencies
dagster asset materialize -m starwars_dagster --select raw_films+

# List all assets
dagster asset list -m starwars_dagster

# Check pipeline loads without errors
python -c "from starwars_dagster import defs; print('OK')"
```

### File structure reference

```
starwars_dagster/
├── pyproject.toml                    ← dependencies & dagster entry point
├── WORKSHOP.md                       ← this file
├── data/
│   ├── raw/                          ← JSON dumps from SWAPI
│   ├── output/                       ← Parquet + Markdown report
│   └── star_wars.duckdb             ← embedded analytics database
└── starwars_dagster/
    ├── __init__.py                   ← Definitions (wires everything together)
    ├── schedules.py                  ← cron schedules and job definitions
    ├── assets/
    │   ├── ingestion.py             ← Layer 1: raw API pulls
    │   ├── transforms.py            ← Layers 2+3: DuckDB + SQL
    │   └── analytics.py             ← Layer 4: report generation
    └── resources/
        └── swapi_resource.py        ← SWAPI HTTP client
```

### Key Dagster UI pages

| Page | What it's for |
|---|---|
| **Assets** | View lineage graph, freshness, materialize |
| **Jobs** | Launch runs manually |
| **Schedules** | Enable/disable cron triggers |
| **Runs** | History of all executions, logs, re-run |
| **Resources** | Inspect resource configuration |

---

*Built with [Dagster OSS](https://dagster.io) + [SWAPI](https://swapi.info) · May the Force be with your data platform.*
