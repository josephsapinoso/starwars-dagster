---
name: panel-qa-engineer-sql-verification
description: Execute-and-compare pattern for verifying displayed SQL strings (site dashboard disclosures) against the real pipeline-built DuckDB, fully offline. Use when reviewing tests/test_site_sql.py, adding a new SQL disclosure, or auditing any site copy that claims to be runnable SQL.
---

# Verifying displayed SQL against the pipeline's own warehouse (offline)

Designed 2026-07-18; LANDED same day in commit c0b97e0 as
`tests/test_site_sql.py` (post-landing-cleanup decision, unanimous adopt).
Principle: a displayed SQL string is a CLAIM ("this query produced these
numbers"). The only honest verification is executing it against the database
the real pipeline builds, and comparing results to the numbers the site shows.
Before this guard existed, 3 of 5 displayed strings were wrong (two queried a
nonexistent table; one measured string length of stringified JSON).

## 1. Single source: SQL strings live in DATA.sql

The five strings (keys `films/gender/scatter/homeworlds/hyper`) live in the
one-line strict-JSON `const DATA` literal; the site renders disclosures ONLY
from `DATA.sql`. Pins that keep it that way:

- `test_data_sql_has_exactly_the_five_chart_entries` — key set exact, none empty.
- `test_no_inline_sql_strings_remain_in_the_page` — asserts `const sql = \``
  never reappears in a chart IIFE.
- `test_displayed_sql_carries_no_unverified_count_comments` — no digit in any
  `--` comment (the old `-- 59 of 82 rows` drifted silently; a number in a
  comment is an unexecutable claim).

## 2. Build the DB the honest way: the pipeline builds it

As landed: a module-scoped `warehouse` fixture in test_site_sql.py runs
`materialize([raw_* ×5, star_wars_db, characters_enriched])` with
`FakeSWAPIResource` in a tmp cwd, then tests use
`duckdb.connect(path, read_only=True)` on the `data/star_wars.duckdb` the
pipeline itself wrote. (My original spec said reuse test_pipeline's `full_run`;
the landed module-local fixture is equivalent in principle and avoids
cross-file fixture coupling — accepted deviation.)

NEVER build a bespoke DB, and NEVER create views/tables in the test that the
pipeline doesn't create — that verifies the SQL against a warehouse that does
not exist (the exact lie this suite exists to catch).

Companion law from the same decision: `characters_enriched` write-back is ONE
code path — `CREATE OR REPLACE TABLE characters_enriched AS SELECT * FROM df`
(transforms.py:131) on the same df the asset returns, guarded by
`test_pipeline.py::test_characters_enriched_table_matches_the_returned_frame`
(assert_frame_equal). `EXPECTED_DB_TABLES` stays five;
`star_wars_db_tables_populated` must not assert a downstream asset's table
(ordering lie).

## 3. Two assertion layers, gated differently (as landed)

- **Ungated EXECUTE (runs on synthetic fixtures too):**
  `test_every_displayed_string_executes_against_the_warehouse` (parametrized
  over the five keys; asserts rows returned). Catches missing tables/columns,
  schema drift after a transform rename, syntax rot.
- **Snapshot-gated COMPARE (`requires_real_snapshot`):** five tests —
  `test_films_sql_reproduces_the_films_chart`,
  `test_gender_sql_reproduces_the_gender_chart`,
  `test_scatter_sql_reproduces_the_scatter_points`,
  `test_homeworlds_sql_reproduces_the_top_ten`,
  `test_hyper_sql_reproduces_the_leaderboard` — each asserts executed rows ==
  the rows the chart derives from DATA's inline arrays (recompute the site's
  derivation in Python). Exact values are drift baselines; synthetic fixtures
  legitimately differ, hence the gate.
- Any recode/tiebreak the chart applies must live IN the SQL (droid recode,
  ORDER BY tiebreaks) so executed output equals rendered rows exactly.

## 4. Failure modes this names (map each to a layer)

1. SQL references nonexistent table/column → ungated execute fails.
2. SQL runs but computes the wrong thing → gated compare fails.
3. DATA numbers edited without SQL (or vice versa) → gated compare fails.
4. Snapshot refreshed, SWAPI drifted, site now stale → gated compare fails —
   desired: re-publish the site, same as every other DATA number.
5. Inline SQL string creeps back into the page → no-inline pin fails.
6. Numeric claim hidden in a comment → comment pin fails.
7. DATA literal format broken → extraction assert fails loudly (existing law).

## 5. Runtime detector scope (do not overreach)

The browser cannot execute SQL (one-file site, no CDN ⇒ no DuckDB-wasm). The
runtime drift detector owns ONE internal-consistency claim: rendered sql
disclosures ↔ `DATA.sql` keys are 1:1 and non-empty. Truth stays in pytest.

## 6. Adding a sixth disclosure (checklist)

New key in DATA.sql + site renders from it; extend `SQL_KEYS`; the execute
test picks it up via parametrize; write its compare test against the
DATA-derived rows; if the chart shows a denominator, it goes on-card from
DATA, never in a SQL comment. Same commit as the chart.
