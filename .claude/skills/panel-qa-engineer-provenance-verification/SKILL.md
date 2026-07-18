---
name: panel-qa-engineer-provenance-verification
description: How to verify site-embedded pipeline provenance (mini-DAG lineage claims, check badges) against the real Dagster definitions, fully offline. Use when reviewing or specifying tests for the pipeline-reveal feature or any site copy that cites assets/checks.
---

# Verifying site provenance against the real Dagster graph (offline)

Recipes verified against this repo on 2026-07-17 (Dagster 1.13.14).

## 1. Ground truth: introspect the Definitions, never hand-copy

`from starwars_dagster import defs` is offline-safe — `SWAPIResource()` is
constructed but `fetch()` is never called at import time.

```python
from starwars_dagster import defs

graph = defs.resolve_asset_graph()
true_edges = {
    k.to_user_string(): sorted(p.to_user_string()
                               for p in graph.get(k).parent_keys)
    for k in graph.get_all_asset_keys()
}
true_checks = {
    (spec.asset_key.to_user_string(), spec.name): spec.blocking
    for cd in defs.asset_checks
    for spec in cd.check_specs
}
```

Expected today (post commit 082d9c9, 2026-07-18): 11 assets (raw_* ×5 →
star_wars_db → 4 transforms → galaxy_report); 12 checks, split 4 blocking /
8 warn. If these counts drift, re-introspect — never patch them by hand.

## 2. Severity rule: derive from `spec.blocking`, never hand-type

`AssetCheckSeverity.WARN` is passed at runtime inside `AssetCheckResult` and is
NOT statically introspectable. `spec.blocking` IS. Repo discipline maps
blocking ⇔ ERROR badge, non-blocking ⇔ WARN badge. The cross-check test must
assert every badge in `DATA.provenance` equals this derivation, so flipping
`blocking=` in checks.py breaks the offline suite until the site is updated.

## 3. Extracting `DATA` from site/index.html

The literal is ONE line of strict JSON: `const DATA = {...};` (line ~378).

```python
import json, pathlib, re

html = pathlib.Path("site/index.html").read_text()
m = re.search(r"^const DATA = (\{.*\});$", html, re.M)
assert m, "site DATA literal not found — must stay one-line strict JSON"
data = json.loads(m.group(1))
```

That one-line strict-JSON formatting is load-bearing; the assert message must
say so.

## 4. What the layers each own

- pytest (offline, CI): provenance assets exist, edges ⊆ true graph, cited
  checks belong to the cited asset, badge == f(blocking), beat coverage set is
  exactly the agreed one.
- runtime drift detector: internal consistency only — every rendered beat has a
  provenance entry, badge values are in the two-value enum, counts cited in
  reveal copy match `DATA`. It cannot see Dagster; don't pretend it can.
- humans (analyst/owner): the semantic beat→asset attribution. Not mechanically
  provable; keep it reviewed, not asserted.

## 5. Anti-patterns to veto

- Hand-copied edge lists or check names anywhere (site JS, tests, README).
- A second diagram path for dashboard cards not fed by `DATA.provenance`
  (the existing hand-written SQL strings are already unverified copy — don't
  add more of that pattern).
- Severity labels typed as literals in provenance data.
