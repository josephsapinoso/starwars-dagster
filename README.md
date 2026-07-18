# A Galaxy of 82 People

[![CI](https://github.com/josephsapinoso/starwars-dagster/actions/workflows/ci.yml/badge.svg)](https://github.com/josephsapinoso/starwars-dagster/actions/workflows/ci.yml)

An end-to-end [Dagster](https://dagster.io) pipeline — SWAPI → DuckDB → transforms → report —
and a data story that shows its work: every number on the site names the asset that computed
it and the check that guards it.

**▶ [Open the live site](https://claude.ai/code/artifact/e71e41b6-f606-492c-af77-d19a8b3443d7)** —
a scroll-told census of the 82 characters the saga keeps records on, ending in a chart
dashboard. Open any beat's **"paper trail"** to see the exact pipeline lineage and data-quality
checks behind that figure.

Part of [my portfolio](#) <!-- personal-site link slot: swap in the live URL when it ships -->

![Asset Lineage Graph](screenshots/dagster_asset_lineage.png)

## The engineering, in one minute

- **Two guard layers, deliberately split.** pytest proves the *code* offline against committed
  fixtures; Dagster asset checks judge the *data* at materialization. Structural breakage
  **blocks** the run; upstream drift only **warns** — SWAPI is someone else's dataset, and
  freezing it would be pretending otherwise. Baselines live once, in
  [`known_facts.py`](starwars_dagster/known_facts.py), imported by both layers.
- **Provenance you can't fake.** The site's per-beat pipeline reveals are rendered from one
  `provenance` object embedded in the page, and
  [`tests/test_site_provenance.py`](tests/test_site_provenance.py) cross-checks every asset,
  dependency edge, check name, severity flag, and rationale string against the real Dagster
  definitions — including which numbers are guarded *offline only*, stated in plain words on
  the page rather than dressed up as live checks.
- **A drift detector in the page itself.** The site recomputes its headline stats from its own
  embedded data at load and warns on any mismatch with the prose — copy can't silently rot.
- **Deliberately absent:** a second data-quality framework, coverage gates, a CI matrix. One
  green offline workflow and Dagster-native checks carry the weight.

## Architecture

```
SWAPI (live API) → Raw JSON → DuckDB tables → SQL transforms → Markdown report
     ↑                ↑              ↑                ↑               ↑
  Resource        01_raw         star_wars_db    02_transformed   03_analytics
```

**11 assets across 3 groups, 12 asset checks (4 blocking, 8 warn):**

| Group | Assets | Description |
|---|---|---|
| `01_raw` | `raw_films`, `raw_people`, `raw_planets`, `raw_starships`, `raw_species` | HTTP pulls from SWAPI |
| `02_transformed` | `star_wars_db`, `characters_enriched`, `film_character_counts`, `starship_stats`, `character_stats` | DuckDB storage + SQL |
| `03_analytics` | `galaxy_report` | Markdown summary report |

## Quick start

```bash
# 1. Install dependencies
pip install -e .

# 2. Launch Dagster UI
python -m dagster dev

# 3. Open http://localhost:3000 → Assets → Materialize all
```

Run the offline test suite (no network needed):

```bash
pip install -e ".[dev]" && pytest -v
```

`scripts/snapshot_fixtures.py` freezes a dated real-API snapshot and unlocks the exact-value
tests (82 people, 3 six-film characters, 23 unknown masses, 42 one-film cameos, 19 pilots).
A daily 6 AM schedule re-pulls from SWAPI — the same pattern you'd use for any REST feed.

## Stack

- **[Dagster](https://dagster.io)** — orchestration (open-source, free)
- **[DuckDB](https://duckdb.org)** — embedded analytics database
- **[SWAPI](https://swapi.info)** — Star Wars REST API (free, no auth)
- **Pandas** — DataFrame transforms
- **Python 3.11+**

## The website

[`site/index.html`](site/index.html) is one self-contained file: no build step, no CDNs, no
webfonts — open it straight from disk. It respects `prefers-reduced-motion`, works on mobile,
and degrades to per-step figures inside auto-height embeds. The scroll story rearranges one
unit chart of 82 dots (height, mass, homeworlds, film appearances, pilots), then hands off to
a dashboard carrying the Dagster lineage strip and the DuckDB SQL behind every chart.

## How this was built

The design process is itself in the repo: a standing panel of nine role agents (data engineer,
analyst, UX, storyteller, QA, hiring-manager lens, and more) defined in
[`.claude/agents/`](.claude/agents/), each with its own persistent memory and self-authored
skills. Before every debate the panelists research the codebase and update their own knowledge;
afterwards they bank what won and lost. The human adjudicates every verdict, and each decision
is logged in [`.claude/panel/decisions/`](.claude/panel/decisions/) — the pipeline-reveal
feature on the site was specified this way, including the panel catching that three of the
site's headline numbers were computed by no pipeline asset at all. Those beats shipped honestly
labeled as authoring-time tallies pinned by pytest; later the `character_stats` transform landed
on its own merits, computed them in the pipeline, and flipped those beats to direct lineage
with asset-check badges.

## Learn Dagster with this repo

[`WORKSHOP.md`](WORKSHOP.md) is a 15-module, from-zero tutorial written alongside the pipeline:
software-defined assets, resources, DuckDB SQL transforms, schedules, offline testing, asset
checks, and re-execution from failure.

## Project structure

```
starwars-dagster/
├── pyproject.toml
├── README.md
├── WORKSHOP.md                   ← from-zero Dagster tutorial (15 modules)
├── starwars_dagster/
│   ├── __init__.py               ← Definitions (assets, checks, schedules, resources)
│   ├── known_facts.py            ← single source of verified baselines
│   ├── schedules.py
│   ├── assets/
│   │   ├── ingestion.py          ← 01_raw: five SWAPI pulls
│   │   ├── transforms.py         ← 02_transformed: DuckDB + SQL
│   │   ├── analytics.py          ← 03_analytics: galaxy_report
│   │   └── checks.py             ← 12 asset checks (4 blocking, 8 warn)
│   └── resources/
│       └── swapi_resource.py
├── site/
│   └── index.html                ← the whole website, one file
├── tests/
│   ├── conftest.py               ← fake + inline SWAPI resources
│   ├── test_pipeline.py          ← full offline materialization + banked facts
│   ├── test_transforms.py
│   ├── test_swapi_resource.py
│   ├── test_site_provenance.py   ← site provenance vs real Dagster defs
│   └── fixtures/swapi/           ← committed fixtures + dated snapshot marker
├── scripts/
│   └── snapshot_fixtures.py      ← refresh fixtures from the live API
└── .claude/                      ← the design-panel agents, memories, decisions
```
