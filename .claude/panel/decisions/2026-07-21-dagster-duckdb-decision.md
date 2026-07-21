# Decision: do NOT migrate to dagster-duckdb; document the deliberate why-not

Date: 2026-07-21 · Scope: pipeline + portfolio-presentation · Panelists: the pipeline four
(data-engineer, qa-engineer, technical-writer, hiring-manager).
Orchestrator/final decision: Claude (main session).

## Brief

A portfolio assessment flagged the pipeline's DuckDB integration as the one thing a senior
Dagster reviewer would ding: DuckDB is threaded as a **path string** returned by `star_wars_db`
and reopened per asset with hand-rolled `duckdb.connect()` (`transforms.py`), instead of the
framework-native `dagster-duckdb` `DuckDBResource`/`DuckDBPandasIOManager`. The owner asked to
"pick up" this fix. On investigation it touches a banked safety test (`test_pipeline.py:189-219`,
the `read_only` source-introspection pin), the `in_process_executor` lock rationale, the
provenance/edge tests, and the WORKSHOP tutorial — so it went to panel. Full brief in the
session scratchpad (`panel-brief-duckdb.md`).

## Per-role verdicts (one line each)

- **data-engineer**: conditional (B) two-instance `DuckDBResource` IF the API enforces read-only;
  IO-manager OUT (one table per asset can't emit `star_wars_db`'s five raw tables); veto (C) subclass.
- **qa-engineer**: lean (A); would allow (B) ONLY with a *behavioral* "write raises" test, never a
  binding-introspection substitute; (C) is a trap. A deliberate omission CAN be guarded (marker pin).
- **technical-writer**: (A) — a documented why-not is richer teaching ("when not to adopt an idiom")
  than another `DuckDBResource` how-to; WORKSHOP cost is low and a forward-pointer fixes the Module 2→3
  coherence gap; IO-manager opposed; "silent A" (no note) is the worst outcome.
- **hiring-manager**: (A) — the tested single-writer contract is a rarer, stronger senior signal than
  "used the resource"; (B)'s two same-file instances are likely enforcement theater (guard-honesty veto).

## Adjudication

Verified fact (data-engineer + qa-engineer, external): `DuckDBResource.get_connection()` **hardcodes
`read_only=False`** and takes no per-connection args, stable across Dagster 1.7–1.13; `dagster-duckdb`
is not even a current dependency. Consequences:
- **IO-manager**: unanimously OUT — names one table per asset key, so `star_wars_db` (five raw tables)
  can't map to it without decomposition that breaks the provenance graph + site lineage strip.
- **(C) subclass**: unanimously vetoed — restoring `read_only` in a subclass re-hand-rolls the exact line
  the migration deletes, adding a dependency and indirection for zero added enforcement.
- **(B) two resource instances**: the reader/writer distinction would move from a DuckDB-enforced,
  source-tested lock into Definitions *wiring*, and it is uncertain `connection_config` read-only is even
  honored through the hardcoded kwarg. Best case it is idiomatic-but-invisible on the 90-second scan;
  worst case it is enforcement theater. Either way it trades a rare, proven signal for a common one.
- **(A) documented why-not**: keeps the enforced `read_only` contract untouched, closes the real
  criticism (a Module 2→3 tutorial-coherence gap) with a forward-pointer, and turns the "ding" into
  demonstrated judgment. Robust — it does not depend on the unverified API behavior.

The owner chose (A). It is also the panel's center of gravity (2 firm-A, 1 lean-A, 1 conditional-B-else-A).

## Final plan (shipped this commit)

1. `WORKSHOP.md` Module 10 — new "Why NOT `dagster-duckdb`'s `DuckDBResource`?" subsection beside the
   existing "Why NOT Great Expectations" why-not: names the `read_only=False` hardcode, states the
   tradeoff both ways, and "when it would earn its place."
2. `WORKSHOP.md` Module 2 — a forward-pointer note to Module 10 (resolves the "Module 2 taught resources,
   why is Module 3 hand-rolling?" coherence gap).
3. `starwars_dagster/assets/transforms.py` — one comment at the connection sites naming the deliberate
   choice and pointing to Module 10 (points, never restates).
4. Guard — `tests/test_pipeline.py::test_warehouse_access_policy_is_encoded_in_code` keeps the `read_only`
   pin unchanged and adds a rationale-marker assertion (`"DuckDBResource"` + `"read_only=False"` present in
   `transforms.py` source), so a future "modernize" refactor trips both the pin and the marker.
5. `CLAUDE.md` — one-line settled-constraint digest entry.

Feature + guard + docs landed in one commit. No dependency added; assets stay 13, checks 20; 99 tests pass.

## Newly settled constraints (candidates to bank)

- **The pipeline keeps raw `duckdb.connect()` deliberately; `dagster-duckdb`'s `DuckDBResource` is NOT
  adopted** because `get_connection()` hardcodes `read_only=False`, which would erase the per-asset
  read-only single-writer lock. Rationale home is WORKSHOP Module 10; guarded in `test_pipeline.py`. Do
  not "modernize" without a panel.
- **A deliberate technology non-adoption is a guardable artifact**, not just prose: pin a stable rationale
  marker in the source alongside the invariant it protects, so a future refactor must re-read the decision.
