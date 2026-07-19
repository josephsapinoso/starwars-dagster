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

The six strings (keys `films/gender/scatter/homeworlds/hyper/ages` — `ages`
added 2026-07-19, birth-registry commit 1f3cf9e) live in the one-line
strict-JSON `const DATA` literal; the site renders disclosures ONLY from
`DATA.sql`. Pins that keep it that way:

- `test_data_sql_has_exactly_the_chart_entries` — key set == `SQL_KEYS` exact,
  none empty. (Renamed count-free when `ages` landed; the key list lives once
  in `SQL_KEYS`, so the test name no longer hardcodes a count.)
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

Companion law (amended 2026-07-19): write-back is ONE code path per writer —
`CREATE OR REPLACE TABLE <name> AS SELECT * FROM df` on the same df the asset
returns. There are now TWO declared writers: `characters_enriched` and
`character_stats` (the ungated execute layer itself forced the second — the
`ages` SQL referenced `character_stats`, which didn't exist in DuckDB until it
was written back; the guard caught the lie mid-implementation, exactly its
job). The parity test loops both writers (assert_frame_equal against the
table). `EXPECTED_DB_TABLES` stays five and `star_wars_db_tables_populated`
must not assert a downstream asset's table (ordering lie). The full access
policy — readers `read_only=True`, writers declared, executor pinned
in-process — is itself pinned by
`test_pipeline.py::test_warehouse_access_policy_is_encoded_in_code`.

## 3. Two assertion layers, gated differently (as landed)

- **Ungated EXECUTE (runs on synthetic fixtures too):**
  `test_every_displayed_string_executes_against_the_warehouse` (parametrized
  over `SQL_KEYS`; asserts rows returned). Catches missing tables/columns,
  schema drift after a transform rename, syntax rot.
- **Snapshot-gated COMPARE (`requires_real_snapshot`):** six
  `test_*_sql_reproduces_the_*` tests (films chart, gender chart, scatter
  points, top-ten homeworlds, hyper leaderboard, birth registry) — each
  asserts executed rows == the rows the chart derives from DATA's inline
  arrays (recompute the site's derivation in Python). Exact values are drift
  baselines; synthetic fixtures legitimately differ, hence the gate.
- Any recode/tiebreak the chart applies must live IN the SQL (droid recode,
  ORDER BY tiebreaks) so executed output equals rendered rows exactly.
- A compare test may also pin a UNIT invariant:
  `test_ages_sql_reproduces_the_birth_registry` adds `all(r[1] > 0)` because
  the site displays positive-BBY years — a signed value in the result set
  would falsify the unit on display even if rows otherwise matched.

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

## 6. Adding a new disclosure (checklist — exercised for real on `ages`)

New key in DATA.sql + site renders from it; extend `SQL_KEYS`; the execute
test picks it up via parametrize; write its compare test against the
DATA-derived rows; if the chart shows a denominator, it goes on-card from
DATA, never in a SQL comment. Same commit as the chart.

Field report (2026-07-19, first real use): the checklist held with two
additions worth keeping. (1) The ungated execute test earned its keep
immediately — it failed because the query's table (`character_stats`) wasn't
persisted to DuckDB, which forced the honest fix (declare a second writer +
parity + access-policy pin) instead of a bespoke test-side view (the exact
anti-pattern in §2). Expect a new disclosure to surface warehouse gaps; fix
the PIPELINE, never the fixture. (2) If the displayed numbers carry a unit
convention (positive BBY), pin it in the compare test. Also: renaming the
key-set pin count-free (`SQL_KEYS` as single home) removed a needless count
ripple — do that from the start next time.
