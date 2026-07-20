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
- **Measured-vs-inferred labeling (watchlist round, 2026-07-19):** any decision resting
  on unreachable hardware states its measured facts and its inferences separately,
  verbatim, in the log.
- **Anchoring restoration is not scroll-jacking:** a synchronous, activation-triggered,
  MEASURED-delta scroll correction that no-ops where the browser anchors is the
  sanctioned shape for disclosure-growth compensation; animated or assumed-delta
  variants stay banned.
- **Acceptance is a decision with a tripwire:** an accepted limitation enters the log
  with its reopening trigger written down; a shrug is not a verdict.
- **The census conceit is load-bearing:** the stage tooltip is the only surface naming
  most of the 82 individuals; no input modality may be cut off from it.
- **Exposure changes reach, not content:** widening a verified string's audience
  renders the same string verbatim from its one home; if it doesn't fit the vessel,
  change the vessel. (My verbatim one-home law, promoted even as my Q1 proposal lost.)

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
  pinning, all four ux watchlist items closed).
- Snapshot identity (2e47baa): `DATA.meta` carries source+snapshot date; footer renders
  only from it; pinned to SNAPSHOT.json `fetched_at` at tests/test_site_data.py:68.
  Env reproducibility (same commit): `requirements.lock` pins transitives; both
  workflows install with `-c requirements.lock`; pyproject ranges stay human-facing.
- Style guard: `tests/test_site_style_hygiene.py` (a30a5bc) — five tests: hex-in-
  :root census, sanctioned-literal pins, gold single-home, CSS scale-or-pin, and
  no style literals in JS/markup. Scale constant `SANCTIONED_SCALE`
  {11,12,13,14,16,17,18,42}; six `EXEMPT_SELECTORS` pins; one sanctioned literal
  (`#cdd8ef`). Any new size/color fact must land through this file. Hazard: pin
  matching is FIRST-fragment-wins — a scoped pin must precede the general one.
- Watchlist landings (fdd3178): reveal-delta compensation on `details` toggle
  (capture summary viewport top on click, `scrollBy` the measured delta, instant,
  site/index.html:484) and touch tap-to-pin in the ONE shared tooltip (`tipPinned`
  :468, scroll dismiss :469, pointerType branch :799/:802 — no fork). Hazard on
  record: `.axis-t`/`.anno-t` are shared with measured-px dashboard ink; any stage
  type bump must scope `.stage .axis-t` and re-verify anno geometry by hand.

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

## Banked: token hygiene + style guard (2026-07-19, a30a5bc — compacted)

- Won the mechanics: zero JS font-sizes remain, no-fallback-hex held, DATA-line
  exclusion asserts it FOUND the line, seen-to-fail at eight planted violations; the
  guard is one offline pytest, no lint framework. Lost Q3 5–1 (no --fs-* tokens):
  one-home doctrine is satisfied by ANY machine-checked home — a test constant beats
  a token layer nothing at runtime consumes; distinguish "second registry" (rots)
  from "second home a test derives from" (can't). Lost the starfield bridge 3–3:
  when both sides' failure modes are real, the side whose failure the guard can
  catch wins — my bridge's init-race blank canvas was unguardable offline.
- Convert my own objection into the mechanism (pins failing both directions) instead
  of demanding the exception not exist; stress-test my own proposals for ordering
  risk. Skill `panel-data-engineer-single-file-hygiene-guard` teaches the shipped shape.

## Prep notes: akabab second source (2026-07-20)

Verified live today (WebFetch, akabab.github.io + github.com/akabab/starwars-api):
- all.json: 87 records; ids run 1..88 NON-contiguous (17 absent) — never check id
  contiguity or use id as ordinal; count + shape only. All 87 carry `name`. MIT license
  confirmed on the repo. Endpoint shape is `{base}/all.json` (also `/id/{id}.json`), so
  `fetch(endpoint) → f"{base_url}/{endpoint}.json"`; a SEPARATE ConfigurableResource,
  not a SWAPIResource subclass (URL suffix differs, and subclassing would lie).
- Schema is POLYMORPHIC by kind: droids carry dateCreated/dateDestroyed/creator/
  manufacturer INSTEAD of born/died. `{id,name}` is the only universal contract —
  the blocking shape check is right at exactly that, no more.
- SIGN TRAP: akabab years are ABY-positive (Luke born:-19 = 19 BBY, died:34 = 34 ABY);
  our `birth_year_bby` is BBY-positive. A raw `died` column copied as-is carries the
  OPPOSITE sign convention from birth_year_bby in the same warehouse. One convention
  per warehouse: normalize at transform time (synthetics-tested sign flip) or name the
  column unambiguously (e.g. died_year_aby) — never a bare `died`.
- Prose contamination: apprentices holds "Ben Solo (along with a dozen apprentices)" —
  lineage lists are display strings, not join keys. JSON-string + count columns yes;
  joining/exploding on them, never.

Verified in-repo:
- test_site_provenance.py:242 totals math confirmed: assets=all keys, transforms=
  group 02_transformed minus star_wars_db (so character_biographies MUST be
  02_transformed to make 5), checks=all specs. :76 pins check sets only for LISTED
  provenance assets — new checks on unlisted assets are invisible to it. The spoiler
  pin (:181) scans only claim-chain assets' checks, so new check strings go unscanned
  until site surfacing — write them number/roster-free anyway; they enter scope later.
- test_pipeline.py:155 access policy hardcodes reader/writer lists: character_biographies
  (CREATE OR REPLACE TABLE) becomes writer #3 → same commit must update that test AND
  the test_written_back_tables_match_the_returned_frames parity loop. EXPECTED_DB_TABLES
  stays five; tables_populated untouched; DB ends a full run with EIGHT tables.
- Snapshot plumbing: snapshot.yml only `git add tests/fixtures/swapi` — must widen;
  snapshot_fixtures.py is SWAPI-only. Akabab marker must be its OWN
  tests/fixtures/akabab/SNAPSHOT.json — test_site_data.py:68-71 substring-pins the
  swapi marker's source/fetched_at shape, so never merge markers.
- fixtures/swapi/people.json:1066 "Ratts Tyerel" confirmed vs akabab "Ratts Tyerell"
  (id 47) — the alias map earns its first entry. Governance mechanism: a pytest
  dead-alias detector — every alias source must exist in the akabab fixture and every
  target in people, gated on both snapshot markers.
- Reachability: akabab.github.io WAS reachable from this dev container via the agent
  proxy today; the snapshot workflow remains the sanctioned freeze path regardless.

Cannot verify cheaply: the exact 81/82 match count and died=47/87 sparsity (trusting
the brief's 2026-07-19 fixture audit; re-derive during implementation); whether akabab
has duplicate name strings (the blocking grain check covers fan-out regardless).

## Banked: watchlist round (2026-07-19, fdd3178)

- **Lost Q1 (4–2):** expose-whys-first fell to accept-and-document — 48 new tab stops
  (~15 crossing the held pause) would make the page's quietest voice its loudest
  keyboard path; ux scoped focus-parity to data marks, not whisper-tier chips whose
  visible label+severity is the complete claim. But my verbatim one-home law was
  promoted to Settled as "exposure changes reach, not content", and the reopening
  tripwire (any why gaining load-bearing content with no non-hover home; the legend
  line ceasing to be true) keeps the ground alive. Losing the verdict while winning
  the contract is a good trade — the contract outlives the verdict.
- **Lost Q2's accept:** orchestrator ruled ship 3–2–1 AFTER the analyst's evidence
  gate passed all four proxy branches on landed code (0 / −180 / 0 / 0). The shape —
  capture summary viewport top on click, scrollBy the MEASURED delta on toggle — is
  self-gating: where the browser anchors, the measured delta is 0 and the fix
  no-ops. My feared double-compensation is structurally excluded and my CSS.supports
  gate unnecessary; measured-not-assumed beats feature detection. My no-offline-guard
  objection was resolved by the banked render-only precedent: behavior with no data
  surface gets recorded proxy evidence + review, never a fakeable mechanical pin.
  Lesson: the analyst's gate beat my categorical objection by converting the
  disagreement into a measurement — ask "can the runtime measure this itself?"
  before objecting "we can't verify this."
- **Won Q3 (5–1 tap-to-pin):** my shared-layer-only must-have shipped exactly —
  tipPinned in the tip module, pointerType branch in the stage handlers, dismissal
  by the reader's own tap/scroll, no timer, no fork, no second content source.
  Suppress-for-touch died on the census conceit (now Settled).
- **Q4 accept unanimous** on the analyst's redundancy audit (zero load-bearing
  orphans at 5px; beat-5 witness stack caps any raise at ~8px effective — below
  target). My shared-selector trap and the guard's pin-ordering fact are recorded
  hazards for any future mover (kept in Working knowledge); the Q3 pin is mobile's
  dot-identity bonus, NOT the justification.
- **Prep differently:** before filing a categorical objection (no guard, no
  hardware), first design the measurement that would settle it — the role that
  brings the evidence gate owns the verdict; and check banked precedent
  (render-only evidence) before objecting on guard-shape grounds.
