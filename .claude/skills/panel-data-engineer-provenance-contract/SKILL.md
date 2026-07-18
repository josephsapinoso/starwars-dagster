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

## Duplication audit before adding a representation

Count existing hand-authored pipeline representations first (this repo already had
three: lineage strip HTML, five SQL strings, footer line). Any new one must either
consume the single provenance object or replace an existing duplicate — never add a
parallel copy.
