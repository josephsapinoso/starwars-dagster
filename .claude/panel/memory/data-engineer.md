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
- Residual open items: NONE as of 2026-07-19 (lock race, snapshot identity, env
  pinning all closed).
- Snapshot identity is reader-visible (2e47baa): `DATA.meta` carries
  source+snapshot date; footer renders only from it; `tests/test_site_data.py:68`
  pins it to SNAPSHOT.json's `fetched_at`; drift detector warns on malformed meta.
- Env reproducibility (same commit): `requirements.lock` pins transitives; both
  workflows install with `-c requirements.lock`; pyproject ranges stay authoritative
  for humans. CI/snapshot runs are reconstructible from the repo. Closed.
- Style guard: `tests/test_site_style_hygiene.py` (a30a5bc) — five tests: hex-in-
  :root census, sanctioned-literal pins, gold single-home, CSS scale-or-pin, and
  no style literals in JS/markup. Scale constant `SANCTIONED_SCALE`
  {11,12,13,14,16,17,18,42}; six `EXEMPT_SELECTORS` pins; one sanctioned literal
  (`#cdd8ef`). Any new size/color fact must land through this file.

## Banked: 2026-07-18 panels (pipeline-reveal, character_stats, cleanup — compacted)

- Propose the data contract firmly, hold the rendering technology loosely (won the
  provenance schema, lost chips-vs-SVG). Trace each displayed number to its
  producing query before designing the contract that encodes it.
- The bank works as a spec: character_stats + its WARN checks built straight from
  banked acceptance criteria. Spelled-out counts and word-lists are hidden duplicate
  facts — grep for prose-encoded numerals on any count change, and refresh my own
  lineage/count bullets in the same banking pass.
- Executing the artifact under test beats arguing about it (the 3-of-5-live-lies
  audit landed the executed-SQL law in my shape). One-home-per-fact is a stronger
  frame than spoiler-hygiene; lead with it. State ordering implications of any
  write-back myself; grep WORKSHOP for exercise collisions near teaching modules.

## Banked: birth registry + polish (2026-07-19, 1f3cf9e…f170379, compacted)

- Won the column spec verbatim and the 7–1 failure-mode separation (both now
  Settled); ABY-synthetic demand landed (tests/test_transforms.py:168). Lost the
  coda digits-pin objection 5–3 — absence pins guard an exemption's PREMISE, not its
  wording (Settled). Executed-SQL law paid rent mid-implementation: `DATA.sql.ages`
  named a table with no write-back and the ungated execute layer caught it →
  `character_stats` became the second declared writer. Lesson: a new DATA.sql
  entry's table-existence/write-back question is part of the card spec at design
  time. Spec a parsed column's guard PAIR and write-back status in the same breath.
- Ghost-server lesson: a listening port is not evidence of the code you think it
  is — kill the process TREE, verify port ownership (`ss -ltnp`), fetch a canary
  string before screenshots.

## Banked: ledger correction (2026-07-19, compacted)

- Sweep "Residual open items" against commits landing AFTER the debate and verify
  closure claims in-repo (grep the test/workflow/comment) before writing CLOSED.

## Banked: token hygiene + style guard (2026-07-19, a30a5bc)

- **Won — the mechanics:** all three JS font-size sites resolved my way (gender
  %-labels are class `.seg-pct`, registry caption is a class, dead 11px attr :747
  deleted — zero JS font-sizes remain); no-fallback-hex held; DATA-line exclusion is
  the guard's first move and asserts it FOUND the line (exclusion is load-bearing);
  seen-to-fail ran at eight planted violations before landing. The guard is one
  offline pytest (`tests/test_site_style_hygiene.py`), CSS+JS scan, no lint framework.
- **Lost Q3 (5–1, no --fs-* tokens):** my rot objection was answered STRUCTURALLY —
  the registry lives in an executable test that fails when the file drifts, unlike
  the prose ledgers that rotted. Minting CSS variables to feed a test is the tail
  wagging the stylesheet. Lesson: my "one home for the fact" doctrine is satisfied by
  ANY machine-checked home; a test constant beats a token layer when nothing at
  runtime consumes the tokens. Distinguish "second registry" (rots) from "second
  home a test derives from" (can't rot) before objecting.
- **Lost the starfield bridge (3–3, broken against me):** `#cdd8ef` stays a pinned
  literal with a required "scenery, not ink" comment, counted exactly once. The
  storyteller's exact-pin shape answers allow-list rot (a drifting pin FAILS), while
  nothing answers a getComputedStyle init-order risk on the hero canvas. Lesson:
  when both sides' failure modes are real, the side whose failure the guard can
  catch wins; my bridge's failure (blank canvas on init race) is unguardable offline.
- `.prov-check` 11.5 stood on my own don't-relitigate line — four roles held Settled
  law and the craft argument (12px merges badge voice into chip/summary voice on the
  held-pause rail). Six whisper pins shipped: .axis-t/.val-t/.anno-t/.seg-pct/
  .prov-check at 11.5, .cat-t 12.5. Gold: byte-pattern pinned exactly once in :root,
  rgba leaks now color-mix derivations, `var(--gold)` explicitly free.
- **Prep differently:** I championed the exact-pin instinct ("no silent holes") but
  the storyteller SHAPED it into the winning clause — next time convert my own
  objection into the mechanism (pins that fail both directions) instead of demanding
  the exception not exist. Also: my census was right and cheap; machine-census-first
  keeps paying — but I should have stress-tested my own bridge for init-order risk
  before proposing it, as I would for any pipeline ordering question.
- Skill `panel-data-engineer-single-file-hygiene-guard` updated to teach the shipped
  whisper-clause shape, not my losing zero-exception derivation.

## Prep notes: watchlist round (2026-07-19)

Brief claims verified in-repo; nothing has been built yet for Q1–Q4 (candidate shapes
only — no toggle listener, no scrollBy, no pointerType branch, no media bump exist).

- **Q1 (badge whys):** confirmed `s.title = k.why` at site/index.html:879 is the sole
  title= in the file; `k.why` is the verbatim check `description=` carried in
  DATA.provenance and pytest-verified against defs. Contract stance: ANY exposure
  surface (focus tooltip, aria-describedby, visible disclosure) must render the same
  k.why string from DATA.provenance — no paraphrase, no truncated variant, no second
  authored copy (one home per fact). Focusable badges reusing the shared tooltip
  (tipShow:445/tipHide:465) would match the dashboard's existing focus/blur parity and
  cost zero new data surface. Whys are number-free by design → spoiler pin unaffected.
- **Q2 (Safari jump):** no compensation code exists. Chromium is verified fine
  (scroll anchoring); Safari is UNVERIFIABLE here — no hardware, no CI path, drift
  detector can't see scrolling. Ungated `scrollBy` would double-compensate on
  anchoring browsers (breaking the verified-good case to maybe-fix the unverifiable
  one). Only honest gate if shipped: `CSS.supports("overflow-anchor: auto")` — fire
  compensation only where anchoring is absent; must never run during user scroll.
  Starfield-bridge lesson applies: prefer the side whose failure our guards can see.
- **Q3 (touch flash):** stage tooltip = svg-level pointermove hit-test (770–781) +
  pointerleave hide (782), riding the ONE shared tooltip. Any tap-to-pin/pointerType
  logic must live in the shared tipShow/tipHide layer, uniformly (dashboard charts at
  1078/1128/1202 have their own handlers) — no stage-only tooltip fork, no second
  tooltip content source. Emulation can't reproduce the flash; spec says it's real.
- **Q4 (stage type) — the brief underspecifies a ripple:** `.axis-t`/`.anno-t` are
  NOT stage-only classes — drawAxis uses them on the stage (742) AND six dashboard
  charts use them at effective 1:1 scale (1059, 1083, 1139–1183, 1199, 1341–1371,
  1362). A naive `@media` bump on `.axis-t` would resize fit-tuned dashboard ink.
  Honest shape: scope inside the existing 860px block (line 115) as
  `.stage .axis-t` / `.anno-name` (anno-name IS stage-only, :97, currently 12px on
  scale). Guard mechanics verified: the rule parser (split on `}`) sees media-inner
  rules fine; pin matching is FIRST-fragment-wins (`next(e[0] in selector)`), so a
  scoped bump needs a more-specific pin (".stage .axis-t", N, reason) inserted BEFORE
  the general (".axis-t", 11.5) pin — back-assertion then fails loudly both
  directions for both contexts. 22 would otherwise fail scale-or-pin. Same-commit
  amendment is mechanically small; the real cost is geometry: ~22px css at scale .45
  ≈ doubles glyph extents in a 700-wide viewBox with 82 dots + collision-staggered
  annos — stagger-never-shrink tuning must be re-verified by hand at 360/390 if any
  bump ships. Guard proves scale membership, not fit.
