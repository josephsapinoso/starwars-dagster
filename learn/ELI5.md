# ELI5: What this project is, and why it's built this way

> A 10-minute mental-model map of the whole repo. Read this first, then use
> [`flashcards.md`](flashcards.md) to make it stick, then go deep with
> [`../WORKSHOP.md`](../WORKSHOP.md) (the 4-hour, from-zero Dagster tutorial).
> This primer sits *above* the WORKSHOP: it's the big picture and the "why,"
> not a re-teaching of the mechanics.

---

## In one breath

It's a **data pipeline** that pulls Star Wars data from two sources, loads it into a
small database, runs some SQL, and produces a report — **plus a website that tells the
story of that data and is machine-checked against the pipeline that produced it.** Every
number on the site names the pipeline step that computed it and the check that guards it;
every SQL string the site shows is actually run against the database by the test suite. So
what a reader opens is *provably* what runs.

The dataset is deliberately tiny — **82 characters** — because a dataset you can verify by
hand is what lets the guard layer *prove* the data story instead of just decorating it.

## The map

```
  SWAPI (live REST API) ─┐
                         ├─▶  Layer 1: raw JSON   ─▶  Layer 2: DuckDB file
  akabab (static JSON) ──┘        (6 assets)            (1 asset loads tables)
                                                              │
                                                              ▼
                          Layer 4: Markdown report  ◀─  Layer 3: SQL transforms
                               (1 asset)                    (5 assets, incl. the
                                                             cross-source join)
```

- **13 assets** total, in **3 groups** (`01_raw` = 6, `02_transformed` = 6, `03_analytics` = 1).
- **2 upstream sources**: SWAPI (a live REST API) and akabab (a frozen fan-curated JSON dump).
- **20 asset checks** guard the data as it runs — **6 blocking**, **14 warn** (more on that below).
- The whole thing is orchestrated by **Dagster**; the database is **DuckDB** (one file, no server).

An "asset" is just *a piece of data the pipeline produces* — a raw pull, a table, a report.
That's the one idea Dagster is built around, and it's the first mental model below.

---

## Five mental models to walk away with

### 1. Assets, not tasks

Most pipelines are written as "run step A, then B, then C." Dagster flips it: you declare
the **data** each step produces (an `@asset`), and Dagster figures out the order. Even the
*dependencies* are inferred — a transform that needs `raw_people` just names `raw_people`
as a function parameter, and Dagster wires the graph. You describe *what data exists*, not
*what tasks to run*. That's why the UI can show lineage, tell you what's stale, and re-run
just the broken piece. → `starwars_dagster/assets/*.py`, WORKSHOP Module 1.

### 2. Resources are swappable plugs

Anything that talks to the outside world — the SWAPI API, the akabab dump — is a
**Resource**, injected into assets by name rather than hard-coded with `requests.get()`.
Why bother? Because in a test you swap the real plug for a fake one that reads a saved JSON
file, and **the entire pipeline runs offline in seconds** with no network. The proof this
abstraction works: adding the second source (akabab) meant writing one new resource and one
new asset — *nothing downstream changed shape.* → `starwars_dagster/resources/`, WORKSHOP Module 2.

### 3. Two guard layers, deliberately split

This is the conceptual heart of the repo:

| Layer | Guards | Runs | When it fails |
|---|---|---|---|
| **pytest** | your **code** | offline, against saved fixtures | your logic broke |
| **asset checks** | the **data** | at materialization, on real data | the data looks wrong |

You need both because **the upstream data can change without your code changing.** And
within the data checks there's a second split that's the whole lesson:

- **Blocking** (6 of them) — *structural* breakage: an empty table, a missing key, the wrong
  number of films. Stop the run before it corrupts everything downstream.
- **Warn** (14 of them) — *drift*: SWAPI quietly adds person #83. That's not yours to freeze,
  so you *warn*, you don't break.

Getting this split wrong in either direction is the classic data-quality failure: block on
drift and every upstream edit bricks your pipeline; warn on breakage and you ship corrupt
data. → `starwars_dagster/assets/checks.py`, WORKSHOP Module 8.

### 4. One source of truth

Every expected number — 82 people, the 3 characters in all six films, 19 pilots — lives in
exactly **one file**, [`known_facts.py`](../starwars_dagster/known_facts.py), and *both*
guard layers import it. Change a baseline in one place and everything that checks it updates.
No number is transcribed twice. (This same discipline is why these learning docs have their
own tiny guard — see the note at the bottom.)

### 5. Honesty by construction

The website can't quietly lie about its own data, because three mechanisms make lying fail loudly:

- **A drift detector inside the page** recomputes the headline stats from the page's own
  embedded data on load and warns if the prose disagrees. Copy can't silently rot.
- **The lineage/provenance strip** ("paper trail" under each beat) is *rendered from* a data
  object, and a test cross-checks every asset, edge, check name, and severity flag against the
  real Dagster definitions.
- **Displayed SQL is executed SQL.** The SQL strings the dashboard shows live in the page's
  data payload, and the test suite runs each one against the real database and compares the rows.

The theme: don't *assert* the site is honest — *build it so dishonesty breaks a test.*

---

## What makes this build distinctive

Two things go beyond a standard tutorial pipeline and are worth studying closely.

**The second-source join is done honestly.** akabab is a *different trust level* than SWAPI —
fan-curated and effectively frozen — and the pipeline treats it that way:

- Profiles attach by **exact normalized name** (casefold + collapse whitespace) plus a **curated
  alias map** — **no fuzzy matching, ever.** An unmatched name stays unmatched and is *counted*,
  not guessed. The one alias on file corrects a SWAPI-side typo and says so in a comment.
- Every enriched number carries **nested denominators**: not just "47 deaths on file" but "47 of
  the 82 matched profiles." You can always see what the number is a fraction *of*.
- Death data is reported as **"on file," never "deceased"** — the source logs sequel-era deaths
  and lags canon, so *presence in the source* is the only honest claim to make.
- Signed-year columns **name their convention** (`_bby` vs akabab's `_aby` — opposite signs), so
  nobody silently adds a BBY number to an ABY number.

**The most senior signal is the "why NOT" decisions.** The repo deliberately does *not*:

- adopt Dagster's own `DuckDBResource` (it hardcodes `read_only=False`, which would erase the
  single-writer safety lock the transforms rely on),
- bolt on a second data-quality framework like Great Expectations or Soda (Dagster's native
  checks already cover the need at this scale),
- add partitions / incremental-merge / change-history (right for a big or changing dataset;
  pure cargo-cult on an 82-row static snapshot).

Each non-adoption is written down with the concrete signal that *would* flip the decision. That's
the recurring meta-lesson of the whole project:

> **The tradeoff, not the tool, is the takeaway.** Knowing where a ceiling is — and what would
> raise it — is the engineering judgment. The absence itself isn't.

---

## Go deeper

| To really understand… | Read this |
|---|---|
| Assets, resources, the asset graph | `../WORKSHOP.md` Modules 1–2; `starwars_dagster/assets/`, `resources/` |
| DuckDB SQL transforms & the join | `../WORKSHOP.md` Module 4; `starwars_dagster/assets/transforms.py` |
| The two-guard philosophy | `../WORKSHOP.md` Module 8; `starwars_dagster/assets/checks.py` |
| Every baseline number | `starwars_dagster/known_facts.py` (small; the hub everything imports) |
| The "why NOT" decisions | `../WORKSHOP.md` Module 10; `.claude/panel/decisions/2026-07-21-dagster-duckdb-decision.md`, `…-production-pattern.md` |
| The self-verifying site | `site/index.html` + its `tests/test_site_*.py` guards |
| Why each choice was made | `.claude/panel/decisions/` (a dated log per decision) |

When you can explain **why the transforms open DuckDB read-only**, **why drift warns but breakage
blocks**, and **why the project chose *not* to add partitions**, you've absorbed the parts of this
build that a tutorial usually skips.
