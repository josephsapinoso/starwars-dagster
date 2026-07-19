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

## Displayed SQL is executed SQL (settled repo law, landed c0b97e0)

Any SQL text shown on the site is a claim and gets tested like one. No hand-verified
SQL copy anywhere.

1. Store each string once, inside `DATA` (per-card `sql`); the site renders the
   disclosure from DATA only — never a second inline literal. Drift detector asserts
   every SQL disclosure resolves a nonempty DATA entry (internal consistency only).
2. Two pytest layers (`tests/test_site_sql.py`): an UNGATED execute layer (every
   string runs at all against the fixture-built warehouse) and a SNAPSHOT-GATED
   compare layer (executed rows == the rows the charts derive from DATA — replicate
   the small JS derivations in Python; compare as sets where ORDER BY has ties). Ride
   the existing full_run materialization read-only; don't build a second DB path.
3. Executed output must equal RENDERED rows: any presentation logic the page applies
   (droid recode, tiebreaks, denominators) moves INTO the SQL string, or the compare
   is comparing different things. Ban stale count comments (`-- 59 of 82`) inside the
   strings — unexecuted assertions rot.
4. Audit executability first, by executing: strings referencing DataFrame-only
   "tables" or using `len()` on JSON-stringified VARCHAR run never/wrong (this repo
   had 3 of 5 wrong, silently, incl. 1222 "characters" for one film). Never eyeball.
5. If a string needs a table that doesn't exist, the execute layer WILL catch it
   (it did: DATA.sql.ages named character_stats before that asset had a write-back,
   2026-07-19). Better: settle table existence at design time — a new DATA.sql
   entry's spec includes whether its table needs a write-back. A write-back forced
   this way is verification-driven (the executed-SQL law demands a real table), not
   presentation-driven; it still must make warehouse sense (queryable grain).
   Conditions per writer: `CREATE OR REPLACE TABLE ... AS SELECT * FROM df` on the
   same df the asset returns (one code path, parity-asserted in the integration
   test, which loops over ALL declared writers), and no existing check grows to
   cover it if that check guards an UPSTREAM asset — the table doesn't exist yet at
   that check's runtime (ordering lie).
6. Encode the warehouse access policy in code, not tribal knowledge (DuckDB = many
   readers OR one writer per file): pure-reader assets open `read_only=True`,
   writers are an enumerated list, the executor is in-process/sequential, and one
   test inspects source + `defs.executor` to pin all three. Adding a writer means
   updating that test's writer list in the same commit.

## Parsed columns get a guard PAIR (settled law, 2026-07-19)

Any displayed number derived through a parse ships with TWO checks, because two
failure modes must fail differently: a WARN drift baseline against known_facts
("the data moved") and a data-independent parse-honesty invariant comparing the
parsed layer to the raw layer, e.g. parsed NULLs == raw sentinel count via
`additional_ins` on the upstream asset ("the format broke"). One check conflating
them lets the headline number lie under a glowing badge. Corollary: every parse
branch — including ones empty in the current snapshot (ABY) — gets a synthetic
pytest, or it is dead code.

## Check strings are site copy (settled, landed 2aa845e)

When provenance projects check labels/descriptions onto the site, those strings
become page copy with page rules: state the invariant and its stakes; particulars
(rosters, payoff numbers) live in run metadata and `known_facts.py` only — a name
list inside a `description=` is a second (or third) home for one roster and will
drift. A standing spoiler pin derives payoff term sets from known_facts and asserts
no check string renders on a beat earlier than its claim's reveal. Provenance itself
carries no narrative fields (no hand-authored `beat` index) — everything in it must
stay verifiable against the real Dagster defs plus known_facts; and the rail renders
one uniform rule per beat, because spoiler safety belongs in the strings, not the
renderer.

## Duplication audit before adding a representation

Count existing hand-authored pipeline representations first (this repo already had
three: lineage strip HTML, five SQL strings, footer line). Any new one must either
consume the single provenance object or replace an existing duplicate — never add a
parallel copy.
