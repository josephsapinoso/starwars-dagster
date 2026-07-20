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
- **Second-source join shape (akabab panel, 2026-07-20, unanimous):** enrichment joins
  live in a 02_transformed transform (`character_biographies`, declared writer #3);
  `star_wars_db` stays byte-identical, `EXPECTED_DB_TABLES` stays 5, `tables_populated`
  untouched; coverage misses are check metadata, not new raw tables. Separate
  `AkababResource` (the `.json` URL shape makes subclassing a lie); the blocking shape
  contract is exactly `{id,name}` — the schema is polymorphic by kind.
- **Signed-year columns name their convention in the column name** (`_bby`/`_aby`);
  never a bare year column — akabab is ABY-positive, `birth_year_bby` is BBY-positive,
  so a bare `died` would smuggle the opposite sign into the same warehouse. Column is
  `died_year_aby`; no sign-convention check — naming plus pytest suffice.
- **Enrichment numbers carry nested denominators** (N of field-present of 81 matched of
  82) as report-copy discipline computed from data — not per-field checks; five checks
  per feature is qa's ceiling. Akabab deaths are "on file" vocabulary everywhere —
  never "deceased", never saga-scoped or canon-complete claims.
- **Cross-source derived figures are quoted-testimony territory** (SWAPI birth × akabab
  death arithmetic, e.g. Yoda 896+4=900): pre-vetoed off all surfaces (surfacing panel
  left them sealed — coverage COUNTS only).
- **akabab surfacing law (surfacing panel, 2026-07-20):** the second source surfaces as a
  dashboard card (`#card-biographies` after `#card-registry`), never a story beat — the
  census spine stays 8 steps / "n/8" / BUILDERS.length=8. Coverage renders from per-row
  `DATA.people[].bio` (nested object or null), never an aggregate blob; `bio` carries
  `diedOnFile: bool` — NO signed year (I proposed `diedAby|null`; adjudicated to the boolean).
  The displayed `bios` SQL returns coverage COUNTS (matched/deaths_on_file/affiliated), never
  `died_year_aby` values; the test_site_sql warehouse fixture materializes both akabab assets
  via `FakeAkababResource()`. A ranked affiliations chart is BANNED (`affiliations` is
  canon-wide/sequel-inclusive; a ranked bar is a claim a six-film site can't make). Dashboard
  cards carry no check badge (a badge needs a claims[] entry); lineage lives on the DAG strip.
  The DAG strip chip set is PINNED to the real Dagster asset keys (I wanted a full render; the
  adjudication was PIN — a guard asserts chips == real defs).
- **Alias governance:** curated dict in known_facts BRIDGES the join, never mutates
  as-filed records (`character_name` keeps SWAPI's spelling, typo and all);
  canon-direction comment per entry; injectivity + every-alias-load-bearing pytest
  ungated, resolution-vs-fixtures assertions dual-snapshot-gated; no fuzzy matching,
  ever.
- **The site WORDS number-renderer is a guard surface:** it grows, with its pytest pin
  (`len(WORDS)` exceeds every DATA-rendered count), in the same commit as any count it
  must spell. Baselines are computed by script from the frozen fixture, never
  transcribed — three independent akabab surveys disagreed (87/88 records; died 47/28).

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
- Akabab landing hazards (implementation pending, four commits): ids 1..88
  NON-contiguous (17 absent) — count + shape only, never id-as-ordinal; droids carry
  dateCreated/dateDestroyed instead of born/died; years ABY-positive (Luke born:-19,
  died:34); masters/apprentices are prose-contaminated display strings ("Ben Solo
  (along with a dozen apprentices)") — JSON-string + count columns, never join keys.
- Akabab ripple on landing: totals pin 13 assets / 5 transforms / 20 checks;
  test_pipeline.py:155 reader/writer lists + write-back parity loop gain
  `character_biographies` (writer #3) same commit; DB ends a full run with EIGHT
  tables. Provenance :76 pins check sets only for LISTED assets; spoiler pin (:181)
  scans only claim-chain checks — new check strings go unscanned until surfacing;
  write them number/roster-free anyway.
- Akabab snapshot plumbing: snapshot.yml `git add`s only tests/fixtures/swapi (widen);
  akabab gets its OWN tests/fixtures/akabab/SNAPSHOT.json (test_site_data.py:68-71
  substring-pins the swapi marker — never merge markers). First alias: SWAPI "Ratts
  Tyerel" (people.json:1066) ↔ akabab "Ratts Tyerell" (id 47). Baselines re-derived
  by script from the frozen fixture at commit 4, never transcribed.
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

## Banked: birth registry + polish + ledger correction (2026-07-19, compacted)

- Won the column spec verbatim and the 7–1 failure-mode separation (both Settled);
  lost the coda digits-pin 5–3 — absence pins guard an exemption's PREMISE, not its
  wording. Executed-SQL law paid rent: `DATA.sql.ages` named a table with no
  write-back and the ungated execute layer caught it → `character_stats` became
  writer #2. Lesson: a new DATA.sql entry's table-existence/write-back question is
  part of the card spec at design time; spec a parsed column's guard PAIR and
  write-back status in the same breath.
- Ghost-server: a listening port is not evidence of the code you think it is — kill
  the process TREE, verify port ownership, fetch a canary before screenshots. Ledger
  hygiene: verify closure claims in-repo (grep the test/workflow) before writing
  CLOSED; sweep "Residual open items" against post-debate commits.

## Banked: token hygiene + style guard (2026-07-19, a30a5bc — compacted)

- Won the mechanics (one offline pytest, no lint framework, seen-to-fail at eight
  planted violations). Lost Q3 5–1: one-home doctrine is satisfied by ANY
  machine-checked home — a test constant beats a token layer nothing consumes at
  runtime; distinguish "second registry" (rots) from "second home a test derives
  from" (can't). Lost the starfield bridge 3–3: the side whose failure the guard can
  catch wins. Convert my objection into the mechanism (pins failing both directions)
  instead of demanding the exception not exist. Skill:
  `panel-data-engineer-single-file-hygiene-guard`.

## Banked: watchlist round (2026-07-19, fdd3178 — compacted)

- Lost Q1 4–2 (expose-whys-first), but my verbatim one-home law was promoted to
  Settled as "exposure changes reach, not content" — losing the verdict while winning
  the contract is a good trade; the contract outlives the verdict. Lost Q2's accept:
  the analyst's MEASURED-delta gate beat my categorical no-guard objection (where the
  browser anchors, the delta is 0 and the fix no-ops; render-only precedent covers the
  guard shape). Ask "can the runtime measure this itself?" and check banked precedent
  before objecting "we can't verify this." Won Q3 5–1 (tap-to-pin, shared layer only,
  no fork); Q4 accept unanimous — hazards kept in Working knowledge.

## Banked: akabab site surfacing (2026-07-20)

The surfacing panel adopted my whole data-shape contract; I lost one adjudication and one
data-type call, both to sharper versions of my own principles.

Won:
- DASHBOARD CARD, not a 9th beat — unanimous. My going-in Q1 blast-radius argument
  (8-step/"n/8"/exactly-8-kicker/claims-1..6/"six of its numbers" pins) was the record.
  `#card-biographies` after `#card-registry`; BUILDERS.length stays 8, spine 100% untouched.
- Per-row derivability — unanimous. akabab numbers render from `DATA.people[].bio`, never an
  aggregate blob (aggregate isn't drift-recomputable → violates the derivable-from-JSON law).
- Executable `bios` SQL — YES, my verification-driven framing held: a table named in
  `DATA.sql` must exist in the warehouse, so `FakeAkababResource()` materializes
  `raw_character_profiles`+`character_biographies` in the test_site_sql fixture. The query
  returns coverage COUNTS only (matched/deaths_on_file/affiliated) — never `died_year_aby`
  VALUES, dodging both the ABY-sign display and the pre-vetoed 896+4 derivation.
- Both akabab assets into `DATA.provenance.assets` (verbatim `why`, exact check sets,
  chain-checks 13→18 ≤20); `DATA.meta` becomes `sources[]`, footer projects it — my Q6.
- No per-card badge — a badge needs a claim entry (beats-1–6 machinery); dashboard cards
  state denominatored numbers and lean on the DAG strip for lineage (registry-card precedent).

Lost / adjudicated against me:
- `bio` carries `diedOnFile: bool`, NOT my proposed `diedAby|null`. Claude ruled the boolean
  so no signed ABY year ever enters the page (honors signed-year + quoted-testimony laws);
  deaths-on-file stays presence-derivable. A cleaner read of my own convention law — I was
  about to leak the sign I spent last panel walling out.
- DAG strip: I wanted a full RENDER from real defs; qa offered "or pin the chip set"; the
  adjudication was PIN. Chips stay HTML, a new guard asserts the chip set == real Dagster
  asset keys, aria-label corrected to six raw / five transforms. Same guarantee, less churn.
  Noted: my render instinct over-built; a pin catches the exact silent-contradiction failure.
- Ranked affiliations chart DROPPED (unanimous, lore-led) — I'd already conceded it in prep;
  `affiliations` is canon-wide/sequel-inclusive, a ranked bar is a claim a six-film site
  can't make. Coverage COUNT (75/82 affiliated) carries the fact saga-safe.

Prep differently: I brought the derivability crux and the SQL-fixture cost as evidence, which
won them outright — the pattern from last panel (name the mechanism, own the cost) held. But
I under-thought the data-TYPE inside my own contract: proposing `diedAby|null` contradicted
my own just-banked signed-year law. Next time, run each new field past my own Settled section
before proposing it — the type is as load-bearing as the shape.

## Banked: akabab second source (2026-07-20)

- Won every contested point by naming mechanisms, not objections. The `died_year_aby`
  veto: a bare `died` would smuggle ABY-positive years into a warehouse whose
  `birth_year_bby` is BBY-positive — the column NAME carries the convention, no
  runtime check needed (hiring-manager independently seconded naming-over-check).
  Separate `AkababResource` over subclassing: the `{base}/all.json` URL shape makes
  inheritance a lie — live-fetching the endpoint in prep made that unanswerable.
  Blocking contract exactly `{id,name}`: the polymorphic droid schema I verified in
  prep killed any richer shape check before qa had to. Alias-bridges-never-mutates
  beat lore's "correct the canon into the records" framing because it satisfied both
  laws at once: records stay as-filed, lore keeps the canon-direction comment.
  Reusable frame: give the other role's requirement a home that doesn't touch the data.
- Nothing major lost: my writer-#3 access-policy ripple and separate-SNAPSHOT.json
  amendments were adopted verbatim. The section title went to storyteller's drafted
  copy on the as-filed tiebreak (the source field is literally `affiliations`) — my
  own kind of argument, applied to a title I had no stake in. Good law.
- Prep differently: the live fetch of the real source was the highest-value hour —
  id non-contiguity, schema polymorphism, and the sign trap all came from reading
  actual records, not docs. But I trusted the brief's 81/82 and died=47 counts rather
  than deriving them; three surveys then disagreed (87/88; 47/28), which is what
  forced the compute-not-transcribe baseline rule. Next time run the counting script
  IN prep and bring numbers as evidence, not trust.
