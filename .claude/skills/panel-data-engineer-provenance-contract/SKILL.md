---
name: panel-data-engineer-provenance-contract
description: Technique for putting pipeline provenance on the single-file site without breaking the no-build rule - one provenance object inside DATA, offline pytest cross-check against Dagster defs, runtime internal-consistency checks only.
---

# Provenance-on-site contract (no build step)

How to let `site/index.html` display pipeline lineage/checks honestly when the HTML
is hand-authored and nothing generates it.

## The three-layer contract

1. **One source object.** A single `provenance` key inside the site's `const DATA`
   literal: `{assets: {id: {deps: [...], checks: [{name, blocking, why}]}}, ...}`.
   Every consumer (story beats, dashboard cards, mini-SVG renderer) references asset
   ids from this one object. Never per-beat duplicated diagrams — duplicated
   hand-authored structure is where lies grow.

2. **Offline pytest = truth check.** `starwars_dagster.defs` (Definitions built via
   `load_assets_from_modules` + `load_asset_checks_from_modules`) is importable with
   no network. Extract the `DATA` line from the HTML with a regex
   (`const DATA = ({.*});`), `json.loads` it (it is strict one-line JSON by
   convention), and assert: asset ids exist, dependency edges match the asset graph,
   check names per asset match, and `blocking` flags match `AssetCheckSpec.blocking`.

3. **Runtime drift detector = internal consistency only.** The browser cannot see
   Python, so extend the detector (site/index.html ~481) to check only what it can:
   every referenced asset id resolves in `provenance`, total check count matches the
   copy, badges are derived from `blocking`, not hand-typed.

## Verifiability gotcha (Dagster 1.13.x)

`AssetCheckSpec` carries `name`, `asset_key`, `description`, **`blocking`** — but NOT
severity. `AssetCheckSeverity.WARN` is set at runtime on `AssetCheckResult`. Therefore
the provenance schema must store `blocking` (statically verifiable) and derive any
ERROR/WARN presentation from it. A hand-typed `"severity"` field is unverifiable and
must be rejected in debate.

## Execute-and-compare for displayed SQL (no build step)

When the site shows "here is the SQL" disclosures, the string is a claim and must be
tested like one:

1. Store each string once, inside `DATA` (per-card `sql`); the site renders the
   disclosure from DATA only — never a second inline literal.
2. Snapshot-gated pytest: materialize the whole graph from committed fixtures
   (`dagster.materialize` in an isolated cwd, same fixture as the integration test),
   `duckdb.connect` to the produced DB file, execute each string, and compare results
   to the rows the charts derive from DATA (replicate the small JS derivations in
   Python). Compare as sets where ORDER BY has ties.
3. Audit executability first: strings referencing DataFrame-only "tables" (transform
   outputs never written back to the DB) or using `len()` on JSON-stringified VARCHAR
   columns will run never/wrong. Either persist the transform back
   (`CREATE OR REPLACE TABLE` on the connection the asset already holds — no new
   asset) or rewrite the string to the tables that exist. Untested displayed SQL rots
   silently; this repo had 3 of 5 strings wrong.

## Duplication audit before adding a representation

Count existing hand-authored pipeline representations first (this repo already had
three: lineage strip HTML, five SQL strings, footer line). Any new one must either
consume the single provenance object or replace an existing duplicate — never add a
parallel copy.
