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
