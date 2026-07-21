---
name: panel-data-engineer-dagster-duckdb-api
description: Verified API facts for the dagster-duckdb integration (DuckDBResource, DuckDBPandasIOManager) — used when evaluating whether/how to migrate a hand-rolled duckdb.connect() pipeline to the framework-native idiom. Covers the per-connection read_only gap and the one-asset-one-table IO-manager constraint.
---

# dagster-duckdb API — the facts that decide a migration

Source: dagster master `python_modules/libraries/dagster-duckdb/dagster_duckdb/resource.py`,
official docs, DuckDB `access_mode`. Re-verify against the repo's PINNED versions before acting.

## DuckDBResource
- Pydantic fields: `database: str` and `connection_config: dict[str, Any]` (default `{}`).
  No `schema` field on the resource itself.
- `get_connection()` is a `@contextmanager` taking **no parameters** (self only). It passes
  `connection_config` as `config=` to `duckdb.connect()` and **hardcodes `read_only=False`**.
- Usage: `with duckdb.get_connection() as con: con.execute(...)`. Explicit SQL is preserved;
  the asset graph is preserved via `deps=` when the asset no longer returns a value the
  downstream reads.

### The read_only gap (the load-bearing fact)
- There is **no per-connection `read_only` argument**. The only read-only path is
  resource-level config: `DuckDBResource(connection_config={"access_mode": "read_only"})`.
- That configures the WHOLE resource instance. To keep a per-asset reader/writer distinction
  you need **two resource instances** (`duckdb_ro` / `duckdb_rw`) wired to different assets.
  A single shared resource cannot express "these transforms are pure readers".
- UNVERIFIED / must-test: whether `access_mode: read_only` in config conflicts with the
  hardcoded `read_only=False` kwarg on the pinned duckdb build.

## DuckDBPandasIOManager
- Names the destination table by the **asset key/name** (schema via `key_prefix`). One asset
  produces exactly one table.
- Therefore it **cannot** make a single asset load N differently-named raw tables. An
  ingestion/"load raw" asset that fans out to five tables must be decomposed into five assets
  to use the IO manager — which deletes the fan-out node and rewrites the asset graph.

## Migration decision heuristic
- If a "load raw" asset produces multiple differently-named tables AND downstream tests pin
  the asset graph edges / a site lineage strip / an `EXPECTED_DB_TABLES` count → the IO
  manager is OUT (it forces graph decomposition). Prefer `DuckDBResource` for path/config
  centralization while keeping explicit SQL.
- A tested reader/writer `read_only` discipline is a stronger seniority signal than "used the
  resource". Migrating to `DuckDBResource` DROPS the `read_only=True` source literal; a
  source-introspection pin must be rewritten to assert resource BINDING (RO vs RW instance),
  or the safety contract is lost. Weigh churn (rewrite the pin + falsify any tutorial that
  teaches the path-string pattern, same commit) against the 90-second-scan payoff.
- SHIPPED PRECEDENT (starwars-dagster, 2026-07-21): this panel resolved to NON-adoption.
  A read-only single-writer lock enforced by DuckDB and pinned by source-introspection is a
  RARER senior signal than "used the resource"; expressing RO/RW as two same-file resource
  instances is idiomatic-but-invisible on the scan at best, enforcement theater at worst.
  The winning move was to keep raw `duckdb.connect()` and DOCUMENT the deliberate why-not
  (a "when not to adopt an idiom" teaching beat) + pin a rationale marker so a future
  "modernize" trips the guard. A documented, guarded non-adoption can beat a migration.
