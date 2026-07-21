# Flashcards: starwars-dagster

Active-recall deck for the concepts in this build. Read a **Q**, answer out loud, then
check the **A**. Pair with [`ELI5.md`](ELI5.md) (the mental-model map) and
[`../WORKSHOP.md`](../WORKSHOP.md) (the deep tutorial).

For spaced-repetition apps, import [`flashcards.tsv`](flashcards.tsv) (Anki:
*File → Import*, tab-separated, "Basic" note type). The two files are kept in lockstep by
`tests/test_learn_docs.py`.

> Note on numbers: only the headline counts (82 characters, 13 assets, 20 checks, etc.) are
> stated as hard answers — those are guarded against the real pipeline. Other baselines
> (pilots, deaths-on-file, unknown-mass counts) live in `known_facts.py` on purpose, so the
> cards point you there rather than duplicating a number that could drift.

---

## Dagster core

**Q:** What is a "software-defined asset"?
**A:** A piece of *data* the pipeline produces (a raw pull, a table, a report), declared with `@asset`. You describe what data exists, not what tasks to run — Dagster derives the order and lineage.

**Q:** How does Dagster know one asset depends on another?
**A:** From the function signature. An asset that names an upstream asset as a parameter (e.g. `star_wars_db(raw_films, raw_people, …)`) gets that data injected, and Dagster wires the dependency edge automatically. Nothing is connected by hand.

**Q:** What are asset groups for?
**A:** UI organization and the layered architecture. This repo uses `01_raw`, `02_transformed`, `03_analytics` to mirror the four-layer flow.

**Q:** Why use a Resource instead of just calling `requests.get()` in an asset?
**A:** Testability, reuse, and config. A Resource is an injectable plug for an external system; in tests you swap the real one for a fake that reads saved JSON, so the whole pipeline runs offline in one line's change.

**Q:** How does a resource get into an asset?
**A:** By name. The asset takes a parameter (`swapi: SWAPIResource`); Dagster matches it to the key in `Definitions.resources` (`"swapi": SWAPIResource()`) and injects it. The asset never imports or instantiates the resource itself.

**Q:** What is the `Definitions` object?
**A:** The single top-level entry point Dagster reads. It wires together assets, asset checks, resources, schedules, and jobs. Lives in `starwars_dagster/__init__.py`.

**Q:** How are the assets and checks registered?
**A:** Auto-discovery: `load_assets_from_modules` and `load_asset_checks_from_modules` scan the modules for `@asset` / `@asset_check` functions — no manual list to keep in sync.

**Q:** How many assets does the pipeline have, and in which groups?
**A:** 13 assets: 6 in `01_raw`, 6 in `02_transformed`, 1 in `03_analytics`.

**Q:** What triggers the pipeline to run on its own?
**A:** A cron `ScheduleDefinition` — a daily 6 AM refresh. Polling a REST API on a schedule is the honest stand-in for streaming when the source publishes no change events.

**Q:** Why is `in_process_executor` pinned in code instead of the default?
**A:** The default multiprocess executor races steps on the single DuckDB file lock. Running steps sequentially serializes on that lock. The safe execution mode lives in code, not tribal knowledge — the graph is small, so sequential is fast.

**Q:** What's the single biggest productivity win of an asset-based pipeline over raw scripts?
**A:** Re-execute from failure: Dagster skips already-materialized assets and retries only from the broken one, instead of rerunning everything from scratch.

**Q:** What's the difference between a job and a schedule?
**A:** A job is a named selection of assets to run together (e.g. the full pipeline, or analytics-only); a schedule is a cron trigger that launches a job.

## DuckDB warehouse pattern

**Q:** What database does the pipeline use, and where does it live?
**A:** DuckDB — an embedded analytical database that's a single file on disk. Zero server, zero infrastructure.

**Q:** What is DuckDB's concurrency rule?
**A:** Many readers **OR** one writer per file — not both at once. DuckDB itself enforces this with a lock.

**Q:** Why do the pure-read transforms open DuckDB with `read_only=True`?
**A:** To make the reader/writer split a real, DuckDB-enforced lock rather than a naming convention. It's the safety invariant a pytest pins by source introspection.

**Q:** Which asset opens the warehouse read-write?
**A:** The writer, `star_wars_db`, which loads the tables; the transform assets downstream open the same file read-only.

**Q:** How does the SQL count a film's characters when SWAPI stores them as a JSON array of URLs?
**A:** With DuckDB's `json_array_length()` — it counts the inline array without unnesting.

**Q:** How does the SQL handle dirty values like `"unknown"` or `"5,000"` in a numeric column?
**A:** `TRY_CAST` coerces uncastable strings to NULL instead of erroring, and coverage/loss is then measured by a check so "castable" is never mistaken for "complete."

**Q:** Why does the enriched grain get written back with `CREATE OR REPLACE TABLE`?
**A:** So the enriched table is queryable with plain SQL — which is what lets the site's displayed SQL strings be executed against the real database by the offline test suite.

**Q:** How are SWAPI foreign keys resolved, given relations are stored as URLs?
**A:** With SQL joins on the URL, e.g. `LEFT JOIN people → planets ON people.homeworld = planets.url`.

**Q:** What's the interchange format between the SQL layer and the report?
**A:** pandas DataFrames — transforms return `.df()` results, the join uses `.merge()`, and side-effect CSV/Parquet files are written out.

## Testing & guards

**Q:** The two guard layers — what does each one guard?
**A:** pytest guards the **code** (offline, against committed fixtures); Dagster asset checks guard the **data** (at materialization, on real data).

**Q:** Why do you need both layers?
**A:** Because the upstream data can change without your code changing. Code tests can't catch data drift; data checks can't catch a logic bug in a branch that didn't run.

**Q:** Blocking vs WARN checks — what's the rule?
**A:** Structural breakage that would corrupt downstream is `blocking=True` (stop the run). Upstream value drift you don't own is WARN (don't break — you don't get to freeze someone else's dataset).

**Q:** Give an example of a *blocking* check condition.
**A:** An empty table, a raw record missing a key downstream joins need, the film set not being exactly the six episodes, or the join producing more than one row per character.

**Q:** Give an example of a *WARN* check condition.
**A:** The people count no longer matching the verified baseline — e.g. SWAPI adds person #83. Real, worth surfacing, but not a reason to break the build.

**Q:** Where do all the expected baseline numbers live?
**A:** In `known_facts.py`, the single source of truth — imported by both pytest and the asset checks so a baseline is never transcribed twice.

**Q:** How does a test run the whole pipeline offline?
**A:** `dagster.materialize(ALL_ASSETS + ALL_CHECKS, resources={...})` runs the asset graph in-process — no UI, no daemon, no network — in a temp directory so it never touches real data.

**Q:** How do the tests avoid hitting the network?
**A:** They inject a fake resource that subclasses the real one and reads committed fixture JSON instead of calling the API. Swapping the resource swaps the whole network layer in one line.

**Q:** Why is resource injection better than `requests-mock` here?
**A:** You're testing your pipeline, not the `requests` library. One fake resource covers every asset that uses it, at the seam you actually own.

**Q:** How many asset checks are there, and what's the split?
**A:** 20 asset checks — 6 blocking, 14 warn.

**Q:** What classic data-quality failure does the blocking/WARN split avoid?
**A:** Both directions of getting it wrong: block on drift and every upstream edit bricks the pipeline; warn on breakage and you silently ship corrupt data.

**Q:** Is CI online or offline?
**A:** Offline-only — pytest runs against committed fixtures with no network, so a green build never depends on a live API.

## Second-source enrichment (the akabab join)

**Q:** What is akabab, and how is its trust level different from SWAPI?
**A:** A second source: a fan-curated, MIT-licensed, effectively frozen static JSON dump of character profiles. Its failure mode is the host disappearing, not drift — a different trust level than the live SWAPI API, and the pipeline treats it that way.

**Q:** How do profiles attach to the census?
**A:** By exact **normalized name** (casefold + collapse whitespace) plus a small **curated alias map** — a plain, auditable join key.

**Q:** Is fuzzy matching used? What happens to an unmatched name?
**A:** No fuzzy matching, ever. An unmatched name stays unmatched and is *counted*, not guessed into a match.

**Q:** What does the one curated alias on file correct?
**A:** A SWAPI-side typo: it files the canon-spelled akabab profile under SWAPI's as-filed (misspelled) record. The comment states the canon direction.

**Q:** What is a "nested denominator" and why carry one?
**A:** Every enriched figure shows *both* how many characters matched a profile *and* how many of those carry the field — so a reader always sees what a number is a fraction of, and "matched" is never mistaken for "complete."

**Q:** Why is death data reported as "on file" and never "deceased"?
**A:** The source records sequel-era deaths (beyond the six-film frame) and lags canon — it's neither saga-scoped nor canon-complete. So *presence in the source* is the only honest claim.

**Q:** Why do the year columns carry `_bby` / `_aby` suffixes?
**A:** They name opposite sign conventions (BBY-positive vs ABY-positive). Naming the convention on the column stops anyone from silently adding a BBY number to an ABY one.

**Q:** What stops a duplicate profile name from silently inflating the counts?
**A:** A blocking grain check asserting exactly one row per census character, so a fan-out (many profiles matching one person) fails loudly instead of double-counting.

**Q:** Does the alias map ever change the character's displayed name?
**A:** No. Aliases bridge the join only; the displayed `character_name` always keeps SWAPI's as-filed spelling.

**Q:** Why exact-normalized-name + a curated map instead of a smarter matcher?
**A:** Because a curated join is auditable and honest about coverage. A fuzzy matcher would manufacture matches you can't defend and hide the true miss rate.

## The self-verifying site

**Q:** What is `site/index.html`, structurally?
**A:** The entire website in one self-contained file — no build step, no CDNs, no webfonts. You can open it straight from disk.

**Q:** What is the site's runtime drift detector?
**A:** On load, the page's JS recomputes its headline stats from its own embedded data and warns on any mismatch with the hardcoded prose — so the copy can't silently rot out of sync with the data.

**Q:** What's special about the `const DATA = {...};` line, and why?
**A:** It's a single strict-JSON line, and that format is load-bearing: the offline tests regex-parse it to verify the site. Reformatting it would break the guards.

**Q:** How is the per-beat "paper trail" lineage kept honest?
**A:** It's rendered from a `provenance` object in the page, and a test cross-checks every asset, dependency edge, check name, blocking flag, and rationale string against the real Dagster definitions.

**Q:** What does "displayed SQL is executed SQL" mean?
**A:** The dashboard's SQL strings live only in the page's data payload, and the test suite executes each one against a fixture-built warehouse and compares the rows to the chart. There's no hand-copied SQL that could drift from what runs.

**Q:** How does the site degrade for reduced-motion, mobile, and flat embeds?
**A:** It respects `prefers-reduced-motion`, has a mobile layout below 860px, and falls back to per-step figures inside auto-height embeds — no content is ever gated behind motion or scroll.

**Q:** What colour rule does the site enforce, and why?
**A:** Gold `#ffe81f` is a display accent only, never a data series; the data hue is saber blue. Reserving the iconic colour keeps it from being misread as encoding a value.

**Q:** How is style-token hygiene enforced with no build step?
**A:** By an offline pytest that acts as the registry — it checks the hex-colour allowlist and the font-size scale directly in `index.html`. No stylelint, no Node, no CSS-var layer.

**Q:** What does the census unit chart show as you scroll?
**A:** One set of 82 dots (one per character) rearranged across beats — by height, mass, homeworld, film appearances, and pilots — before handing off to the dashboard.

## Judgment / meta

**Q:** What is the recurring meta-lesson of the whole repo?
**A:** "The tradeoff, not the tool, is the takeaway." Knowing where a ceiling is — and the concrete signal that would raise it — is the engineering judgment; the absence itself isn't.

**Q:** Why does the pipeline NOT adopt Dagster's own `DuckDBResource`?
**A:** `DuckDBResource.get_connection()` hardcodes `read_only=False`, which would collapse the reader/writer distinction into a naming convention and erase the tested single-writer lock. The framework resource can't express this pipeline's safety contract.

**Q:** Why NOT add Great Expectations or Soda?
**A:** Dagster-native `@asset_check`s already cover the need at this scale, sharing Python with the transforms they guard. A second framework would add a second place to define expectations, a second config surface, and second failure semantics — cost without new coverage.

**Q:** Why NOT add partitions / incremental merge / SCD / change history?
**A:** The dataset is one small static snapshot with no time dimension. Bolting a scale pattern onto 82 static rows signals less judgment than knowing not to. It becomes worth it when a source is too big to re-pull, or a consumer asks "what changed since yesterday?"

**Q:** What is the "Limits, by design" section?
**A:** An explicit list of ceilings chosen to fit a small static dataset — full-refresh-no-history, single-file DuckDB, no partitions, cron-not-sensors, in-process executor — each paired with the concrete signal that would force it to change.

**Q:** Why is the dataset kept deliberately small (82 characters)?
**A:** Because a dataset you can verify entirely by hand is what lets the guard layer *prove* the data story rather than just decorate it.

**Q:** What rule ties a feature to its safety net?
**A:** A feature and its automated guard land in the same commit — the fix and its test are never separated.

**Q:** Where is the reasoning behind each design choice recorded?
**A:** In `.claude/panel/decisions/` — one dated log per significant decision, including the deliberate non-choices. The review process itself lives in the repo.
