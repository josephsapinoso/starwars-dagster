---
name: panel-data-analyst-sql-display-audit
description: Audit technique for verifying that SQL text displayed on a site or in docs actually produces the numbers the adjacent chart shows. Use whenever SQL strings are shown to readers as the provenance of displayed data.
---

# Displayed-SQL truth audit

Displayed SQL is a claim ("this query produced these numbers"), so it gets the
same treatment as any number: verify or label. For each shown query, build:

| SQL string (file:line) | Table it names | Real schema of that table | Chart's actual derivation (JS/source) | Match? |

Verdicts per row:
- **EXECUTABLE-TRUE** — runs against the real schema and reproduces the chart's
  rows/denominators. Safe to display; pin with an offline execute-and-compare
  test against the committed fixture snapshot (snapshot-gated if fixtures can be
  synthetic).
- **EXECUTABLE-FALSE** — runs but returns different numbers/labels than shown.
  Worst case: looks authoritative, is wrong. Fix the SQL in the same commit the
  test lands.
- **ILLUSTRATIVE** — cannot run against any real table (hypothetical schema).
  Either rewrite against the real schema or label it as pseudocode on-page.

## Banked law in this repo (2026-07-18 post-landing cleanup, commit c0b97e0)

**Displayed SQL is executed SQL.** Any SQL text shown on the site lives in DATA
(single source; the page renders only from DATA) and is executed against the
fixture-built warehouse by the offline suite — an ungated EXECUTE layer plus a
snapshot-gated COMPARE layer asserting each query's result set equals the rows
the chart derives from DATA (tests/test_site_sql.py). No hand-verified SQL copy
anywhere. Corollaries, each pytest-pinned:
- Authoring-time recodes and leaderboard tiebreaks move INTO the SQL (mirrored
  in the JS sorts) so executed output equals rendered rows.
- Numeric comments inside displayed SQL are a banned class
  (`test_displayed_sql_carries_no_unverified_count_comments`).
- If displayed SQL names a table that doesn't exist, first ask whether the
  table SHOULD exist: a warehouse write-back (same df the asset returns, with a
  parity assertion and frozen expected-table count) can be the stronger honest
  fix — but frame it as closing a warehouse gap, never as "making the site's
  SQL true."
- ILLUSTRATIVE is no longer an acceptable end state here: rewrite against the
  real schema or remove the string.

Traps learned in this repo:
- Storage lies about types: list fields json.dumps'd into VARCHAR make `len()`
  return string length; the honest query is `json_array_length()` — check the
  loader, not the raw API shape.
- Authoring-time recodes (e.g. gender `n/a` → "droid" in the site JSON) don't
  exist in the warehouse; displayed SQL must carry the CASE/REPLACE or the
  chart's labels are unreproducible.
- Hardcoded row-count comments in SQL (`-- 59 of 82 rows`) are a drift surface;
  denominators belong in captions computed from data.
- `LIMIT 10` leaderboards need a full deterministic tiebreak (append name/id) or
  the execute-and-compare test must assert set-with-ties, not order.
- DuckDB specifics that make display-SQL terser: column aliases are legal in
  WHERE/GROUP BY/HAVING; default null ordering is NULLS LAST both directions.
