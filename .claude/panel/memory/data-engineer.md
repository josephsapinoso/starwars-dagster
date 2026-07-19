# Data Engineer — Panel Memory

## Settled (do not relitigate)

- Single HTML file for the site: no CDNs, no webfonts, no build step. Anything that
  needs a compile/bundle step is out — honesty must be architectural. (First design
  panel, PR #1.)
- Every number on the site must be derivable from the inline pipeline JSON; a runtime
  drift detector in `site/index.html` warns when data and copy diverge. (First design
  panel.)
- `starwars_dagster/known_facts.py` is the single source of verified baselines,
  imported by both pytest and asset checks. No duplicated constants. (Testing panel,
  PR #3.)
- Severity discipline: structural breakage = ERROR/blocking asset checks; upstream
  drift = WARN — SWAPI is not ours to freeze. (Testing panel, PR #3.)
- `scripts/snapshot_fixtures.py` (and the `snapshot.yml` workflow) refresh the frozen
  fixture snapshot; the workflow exists because remote dev containers may not reach
  swapi.info while GitHub runners can. CI (`ci.yml`) is offline-only. (Testing panel,
  PR #3.)
- No second data-quality framework (no Great Expectations/Pandera). Dagster-native
  checks + one green workflow carry the signal. (Testing panel, PR #3.)
- ONE `DATA.provenance` object is the sole source of every provenance/severity string
  on the site: `assets` keyed by id (`deps`, `checks[{name,label,blocking,why}]`, `why`
  verbatim from checks.py `description=`) + `claims[]` (`chain`, `hot`,
  `relation: direct|derived`, `guard: {kind: check|pytest|none, ref}`). Badge severity
  derives from `blocking` — never a hand-typed severity string. (Pipeline-reveal panel.)
- Guard honesty: a check badge may only appear where the check asserts the displayed
  number (or its denominator/structure, labeled as such); derived/unguarded claims say
  so in plain words. No fabricated or implied live status. (Pipeline-reveal panel.)
- `tests/test_site_provenance.py` cross-checks the site provenance blob against
  `defs.resolve_asset_graph()` + `check_specs` offline: real assets/edges, check
  ownership, blocking flags, verbatim rationales, claim coverage, honest guard typing.
  A feature and its automated guard land in the same commit. (Pipeline-reveal panel.)
- The one-line strict-JSON format of `const DATA` is load-bearing — tests parse it by
  extraction; changing the format must fail loudly. (Pipeline-reveal panel.)
- No assets added primarily to make a diagram truthful — presentation-driven pipeline
  design is out; label the derivation honestly instead. (`character_stats` cleared the
  bar on analytical merits, commit 082d9c9.) (Pipeline-reveal panel.)
- Exact-value baselines are WARN drift checks — never blocking. Provenance-map
  membership is claim-driven: an asset no claim cites leaves the map rather than
  lingering as decoration. (Per-character-transform landing.)
- Displayed SQL is executed SQL: any SQL text shown on the site lives in `DATA.sql`
  (one entry per card; the site renders disclosures from DATA only) and is executed
  against the fixture-built warehouse by the offline suite — execute layer ungated,
  compare layer (SQL rows == the rows the charts derive from DATA) snapshot-gated.
  No hand-verified SQL copy anywhere. (Post-landing cleanup.)
- Check strings are site copy: descriptions state the invariant and its stakes; run
  metadata carries the particulars; `known_facts.py` is the only roster/number home;
  no check string quotes another beat's caption or payoff. The standing spoiler pin
  derives payoff term sets from known_facts; new checks pass it before landing, and
  the pin must be seen-to-fail before merge. (Post-landing cleanup.)
- `DATA.provenance` carries no narrative fields — everything in it must stay
  verifiable against the real Dagster definitions plus known_facts; a hand-authored
  `beat` index is out. The rail is uniform: every beat renders the same rule; spoiler
  safety lives in the strings, not the renderer. (Post-landing cleanup.)
- Write-backs pass the merit test on warehouse grounds only — never "to make the
  site's SQL true". But the executed-SQL law can legitimately FORCE one: a table named
  in `DATA.sql` must exist in the warehouse or the ungated execute layer fails, and
  that is verification-driven, not presentation-driven. Conditions per writer: same-df
  parity assertion (one code path), `EXPECTED_DB_TABLES` frozen at five, and
  `tables_populated` does NOT grow (it guards `star_wars_db`, which materializes
  before any write-back — growing it would be an ordering lie). Two declared writers:
  `characters_enriched` and `character_stats`. (Post-landing cleanup; birth registry.)
- **Failure-mode separation law (2026-07-19, 7–1):** a displayed number derived
  through a parse gets TWO guards — a WARN drift baseline ("the data moved") and a
  data-independent parse-honesty invariant ("the parser/format broke"). Conflating
  them lets the headline number lie under a glowing badge.
- Birth registry column spec: ONE column `birth_year_bby DOUBLE` on `character_stats`;
  sign-safe regexp parse inside the SQL (BBY positive, ABY negative, unparseable →
  NULL); the raw string lives only in `people` — no duplicate. Every parse branch,
  including the snapshot-empty ABY path, is pytest-covered on synthetics: an untested
  branch is dead code. (Birth-registry panel.)
- Warehouse access policy is repo code, not tribal knowledge: pure-reader transforms
  open `read_only=True`; exactly the declared writers write back (`CREATE OR REPLACE
  TABLE`); `defs.executor is in_process_executor` serializes writes on DuckDB's
  one-writer file lock. Pinned by `test_warehouse_access_policy_is_encoded_in_code`.
  (Closed the 2026-07-18 lock-race finding.)
- Absence pins are legitimate guards: an element exempted from a detector by a
  property (number-free, name-free) gets a pin asserting that property; pinning
  wording would be the theater. (QA's ruling, 5–3 — I lost this one; it is law.)
- Quoted-testimony rule: external/canon claims may be audited in copy but never
  rendered as site-derived data; derived numbers come only from DATA. (Birth-registry
  panel.)
- WORKSHOP.md is on the permanent count-ripple checklist; teaching prose states
  counts count-free unless the count is the lesson. (Birth-registry panel.)
- **Whisper clause (token-hygiene panel, 2026-07-19):** every sanctioned style
  exception is an exact (selector, value, reason) pin in the guard, failing loudly on
  change in EITHER direction and printing its reason. Unexplained holes are theater;
  pinned exceptions are law.
- **Scenery is not ink:** decorative paints (aria-hidden canvas) may stay literals with
  a required sanction comment, counted exactly once; data ink must be tokenized. No
  runtime bridges for decoration.
- **Ink adapts to its ground:** on-mark labels choose ink per computed ground from the
  same array that drives the ground; every rendered pair ≥4.5:1, verified
  computationally; never a single ink that fails somewhere, never a new hex.
- **The style registry is the test:** the sanctioned type scale's one machine-readable
  home is the structural pytest (`tests/test_site_style_hygiene.py`) — no `--fs-*`
  tokens, no parallel lists. (I lost this 5–1; it is law.)
- **Raise-only grants permission, not obligation:** standing still needs no evidence;
  moving chart geometry does. `.prov-check` stays 11.5 (Settled; four roles hold it).

## Working knowledge

- Lineage: `SWAPIResource → raw_{films,people,planets,starships,species}
  (assets/ingestion.py) → star_wars_db (transforms.py, DuckDB at data/star_wars.duckdb)
  → {characters_enriched, film_character_counts, starship_stats, character_stats} →
  galaxy_report (analytics.py)`. Eleven assets in three groups. Site totals:
  11 assets / 4 transforms / 15 checks.
- Fifteen asset checks in `assets/checks.py`: four blocking ERROR (people shape,
  tables populated, exactly six episodes, no null names) and eleven WARN, including
  the two birth-registry checks on `character_stats`: `birth_year_baseline`
  (undated + oldest vs known_facts) and `birth_year_parse_honesty` (parsed NULLs ==
  raw `'unknown'` count, read live from both layers via `additional_ins` on
  `star_wars_db`). Parse honesty is WARN because a birth_year format change is
  upstream drift, not our structural breakage.
- Two write-backs, same contract: `characters_enriched` (transforms.py:131) and
  `character_stats` (transforms.py:256) each `CREATE OR REPLACE TABLE` from the same
  df they return; parity in `test_written_back_tables_match_the_returned_frames`
  (test_pipeline.py:93, loops both writers). The DB ends a full run with SEVEN
  tables; `EXPECTED_DB_TABLES` stays five and `tables_populated` checks only the raw
  layer (ordering).
- known_facts.py birth constants (lines 43–46): `EXPECTED_UNDATED_BIRTH_COUNT = 39`,
  `EXPECTED_DATED_BIRTH_COUNT = 43`, `EXPECTED_OLDEST_BIRTH_BBY = 896.0`,
  `OLDEST_DATED_CHARACTER = "Yoda"`.
- The site's `const DATA` literal is hand-authored, one-line strict JSON — no asset
  writes the HTML. Contract enforced by the runtime drift detector plus offline tests,
  not by generation. DuckDB is not a Dagster resource; assets connect via the path
  string threaded through `star_wars_db`; list/dict fields are JSON-stringified.
- `DATA.sql` now holds SIX entries (ages joined the five dashboard strings);
  `tests/test_site_sql.py` executes all of them (execute ungated, compares
  snapshot-gated, riding full_run's DB read-only).
- `character_stats` (02_transformed): per-person `film_count` / `starships_flown` via
  `json_array_length()` plus `birth_year_bby` via
  `TRY_CAST(regexp_extract(...'^([0-9.]+)(BBY|ABY)$'...)) * CASE WHEN ... ABY THEN -1`
  (transforms.py:246); CSV side effect; feeds `galaxy_report`.
- Residual open items: NONE as of 2026-07-19 — the 2026-07-18 survey items (lock
  race, snapshot identity, env pinning) are all closed; see the two bullets below
  and Banked: ledger correction.
- Snapshot identity is reader-visible (commit 2e47baa): `DATA.meta =
  {"source":"swapi.info","snapshot":<date>}`; the footer freshness line renders only
  from DATA.meta; `tests/test_site_data.py:68`
  `test_meta_matches_the_committed_snapshot` pins it to SNAPSHOT.json's `fetched_at`;
  the runtime drift detector warns on missing/malformed meta.
- Env reproducibility (same commit): `requirements.lock` (uv pip compile) pins
  transitives; both workflows install with `-c requirements.lock` (ci.yml:20,
  snapshot.yml:27); pyproject ranges stay authoritative for humans — my recommended
  shape. Local installs without `-c` may drift, but CI/snapshot runs are
  reconstructible from the repo, which was the claim that mattered. Closed.

## Banked: pipeline-reveal (2026-07-18, compacted)

- Won the provenance data contract (schema adopted nearly verbatim); lost only the
  rendering technology (HTML chips beat my mini-SVG). Lesson: propose the data
  contract firmly, hold the rendering technology loosely. Second lesson: the brief's
  beat→asset map was partly false and the analyst caught it — trace each displayed
  number to its producing query before designing the contract that encodes it.

## Banked: per-character transform landed (2026-07-18, 082d9c9, compacted)

- The bank worked as a spec: `character_stats` + four WARN checks built straight from
  banked acceptance criteria; known_facts needed zero changes. Latent-bug lesson:
  spelled-out counts and word-lists are hidden duplicate facts (the "nine" overflow) —
  grep for prose-encoded numerals whenever a count changes, and refresh my own
  lineage/count bullets in the same banking pass.

## Banked: post-landing cleanup (2026-07-18, c0b97e0 + 2aa845e, compacted)

- Executed-SQL law landed in exactly my shape after the 3-of-5-live-lies audit —
  executing the artifact under test beats arguing about it (technique in the
  provenance-contract skill). One-home-per-fact is a stronger frame than
  spoiler-hygiene; lead with it. QA supplied conditions I should have specified
  (same-df parity, the tables_populated ordering argument) — state ordering
  implications of any write-back myself, and grep WORKSHOP for exercise collisions
  before recommending coverage near the teaching modules.

## Banked: birth registry + polish (2026-07-19, commits 1f3cf9e / 4d92cb7 / 7d96df5 / f170379)

- **Won:** column spec landed verbatim (one `birth_year_bby DOUBLE`, sign-safe parse,
  no raw duplicate); two-check failure-mode separation carried 7–1 and is now LAW;
  my ABY-synthetic demand landed as `test_birth_year_parse_covers_every_format_branch`
  (tests/test_transforms.py:168); Q4 no-history bullet shipped and "unpinned env" was
  dropped per my call.
- **Lost:** the coda digits-pin objection (5–3). QA's frame was right — the pin guards
  the exemption's PREMISE (the coda stays number/name-free), not its content; my
  "theater" charge attacked wording-pinning, which nobody proposed. Absence assertions
  are honest guards; promoted to Settled.
- **Executed-SQL law paid rent mid-implementation:** `DATA.sql.ages` named
  `character_stats` — a table that did not exist in the warehouse (the asset had no
  write-back). The ungated execute layer caught it before landing, exactly the failure
  it was built for. Resolution per the write-back law: `character_stats` became the
  SECOND declared writer; the parity test extended to both writers; the access-policy
  test now enumerates two writers with in-process sequential execution serializing
  them. Lesson: a new DATA.sql entry's table-existence question is part of the card
  spec — decide the write-back at design time, don't let the test discover it.
- **QA nit — RESOLVED same day (2026-07-19):** test_pipeline.py's access-policy
  header comment now reads "every writer is declared below (write-back law)"
  (line ~159); verified in-repo, and QA's memory records the fix. Hand-off complete.
- **Reproducibility ghost story:** the first screenshot pass photographed YESTERDAY'S
  orphaned webserver, still serving a deleted instance through open file handles. A
  listening port is not evidence of the code you think it is. Technique: kill the
  process TREE (not just the pid), verify port ownership (`ss -ltnp` / `lsof -i`),
  and fetch a canary string from the new build before shooting.
- **Prep differently:** when a debate adds a parsed column, spec its guard PAIR and
  its warehouse write-back status in the same breath — both were mine to own and one
  arrived mid-implementation. Counts refreshed this pass (15 checks, 6 SQL entries,
  7 end-state tables) per the standing rule.

## Banked: ledger correction (2026-07-19, compacted)

- All three 2026-07-18 survey items closed in-repo (2e47baa + same-day nit fix).
  Lesson: sweep "Residual open items" against commits landing AFTER the debate, and
  verify closure claims in-repo (grep the test/workflow/comment) before writing CLOSED.

## Prep notes: token hygiene + small-type consolidation (2026-07-19)

- Census verified myself (rg `#[0-9a-fA-F]{3,8}` on site/index.html): exactly TWO hex
  literals outside :root, both in JS — `#cdd8ef` canvas star fill (line 489) and
  `#fff` SVG gender %-label (line 1131). No hex anywhere in the DATA literal. :root
  block lines 8–31; the brief is right that the four ledger hexes are already tokens
  (--tip-bg, --axis, --cyan, --sql-ink present).
- Exactly THREE JS font-size occurrences: :747 `attrs["font-size"] = 11` (small
  anno), :1132 `"11.5"` (gender % label), :1374 cssText `font-size:13px` (registry
  caption). All three sit beside existing class patterns (anno-name, axis-t) — all
  movable to classes, so every font-size fact can live in `<style>` alone.
- Guard precedent confirmed: `tests/test_site_provenance.py:103`
  (`test_site_declares_standards_mode_and_language`) scrapes the HTML offline. The
  new hygiene guard belongs beside it — ONE pytest test, regex census, no stylelint,
  no node, no second lint framework.
- My Q1 line: tokenize BOTH leftovers rather than sanction literals — allow-lists
  rot (this very brief opened on a stale ledger note). Canvas bridge = one
  `getComputedStyle(document.documentElement).getPropertyValue()` read at init
  (runtime, not a build step; NOT per-frame). No hard-coded fallback hex in the JS —
  that would be a second home. Guard asserts the token exists in :root and the JS
  references it by token name (structural, offline-checkable without running JS).
- My Q3 line: kept sub-body steps become :root tokens so the sanctioned scale has
  ONE home and the test DERIVES the allowed set from :root instead of hard-coding a
  parallel list. clamp()/display sizes stay literal and out of the scale's scope.
- Guard implementation gotchas: extract-and-exclude the one-line `const DATA`
  literal before regexing (its load-bearing one-line format makes this trivial);
  rgba() literals (lines 13, 52, 224) are OUT of scope this round — hex-only
  invariant, flag but don't expand; SVG attr font-sizes are bare numbers, not px.
- Q2 is typography — defer merges to the graphic designer. My demands: 11.5px lives
  in BOTH CSS (.axis-t/.val-t/.anno-t/.prov-check) and JS (:1132) today, so any
  merge must sweep JS attrs or it silently misses a home; SVG label sizes are
  geometry-load-bearing → manual 360/390px re-verify after any raise (collisions
  are fixed by staggering, never shrinking — settled).
