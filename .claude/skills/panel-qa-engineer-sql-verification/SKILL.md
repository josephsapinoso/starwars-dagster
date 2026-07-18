---
name: panel-qa-engineer-sql-verification
description: Execute-and-compare design for verifying displayed SQL strings (site dashboard disclosures) against the real pipeline-built DuckDB, fully offline. Use when specifying or reviewing tests for any site copy that claims to be runnable SQL, or when auditing SQL text vs the actual warehouse schema.
---

# Verifying displayed SQL against the pipeline's own warehouse (offline)

Designed 2026-07-18 for the five dashboard SQL disclosures in site/index.html.
Principle: a displayed SQL string is a CLAIM ("this query produced these
numbers"). The only honest verification is executing it against the database
the real pipeline builds, and comparing results to the numbers the site shows.

## 1. Single source: SQL strings live in DATA

Move strings out of chart IIFEs into the one-line strict-JSON `const DATA`
literal (a `sql` map: chart-id → string; `\n` escapes are legal strict JSON).
Site renders disclosures ONLY from `DATA.sql`. Extraction recipe is in the
provenance skill (regex on `^const DATA = (\{.*\});$`, loud failure).

## 2. Build the DB the honest way: reuse the pipeline

Reuse the existing `full_run` fixture (tests/test_pipeline.py): one
`materialize(ALL_ASSETS + ALL_CHECKS)` with `FakeSWAPIResource` in
`isolated_cwd`, then:

```python
con = duckdb.connect(str(cwd / "data" / "star_wars.duckdb"), read_only=True)
rows = con.execute(data["sql"][chart_id]).df()
```

NEVER build a bespoke DB, and NEVER create views/tables in the test that the
pipeline doesn't create — that verifies the SQL against a warehouse that does
not exist (the exact lie this test exists to catch: in 2026-07 audit, 2 of 5
strings queried `characters_enriched`, which was never a DuckDB table, and a
third used `len()` on stringified JSON = string length).

## 3. Two assertion layers, gated differently

- **Ungated (always runs, synthetic fixtures included):** every string
  EXECUTES without error and returns the expected column names. Catches
  missing tables/columns, schema drift after a transform rename, syntax rot.
- **Snapshot-gated (`requires_real_snapshot`):** executed rows/values equal
  the expectations derived from DATA's inline arrays (recompute the site's
  derivation in Python — e.g. per-film character_count == DATA film entry;
  gender GROUP BY == gender counts; scatter row count == points with both
  height and mass). Exact values are drift baselines; synthetic fixtures
  legitimately differ.
- **Comment claims:** if a SQL string embeds a count in a comment
  (`-- 59 of 82 rows`), assert it equals the executed row count. Numbers in
  comments are still displayed numbers.

## 4. Failure modes this names (map each to a layer)

1. SQL references nonexistent table/column → ungated execute fails.
2. SQL runs but computes the wrong thing → gated compare fails.
3. DATA numbers edited without SQL (or vice versa) → gated compare fails.
4. Snapshot refreshed, SWAPI drifted, site now stale → gated compare fails —
   desired: the site must be re-published, same as every other DATA number.
5. DATA literal format broken → extraction assert fails loudly (existing law).

## 5. Runtime detector scope (do not overreach)

The browser cannot execute SQL (one-file site, no CDN ⇒ no DuckDB-wasm). The
runtime drift detector gets ONE internal-consistency claim only: rendered sql
disclosures ↔ `DATA.sql` keys are 1:1 and non-empty. Truth stays in pytest.

## 6. Fix-agnostic stance

If displayed SQL wants `FROM characters_enriched`, the pipeline must actually
persist that table (transform change), or the SQL must be re-authored against
real tables. The test doesn't care which; it only cares that display == truth.
Whoever changes the warehouse or the strings trips the same detector.
