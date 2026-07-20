# Star Wars Lore Fanatic — Panel Memory

## Settled (do not relitigate)

- The characters appearing in all six saga films are **THREE**: C-3PO, R2-D2, and
  Obi-Wan Kenobi. "Just the droids" is a canon error the site once nearly shipped.
  (First design panel, PR #1/#2.)
- Verified census facts: 82 people in the dataset; 23 lack mass; Naboo 11 residents,
  Tatooine 10. Any Star Wars framing must fit these numbers, not legend. (First design
  panel.)
- Gold #ffe81f — the crawl's color — is ceremony: display accent only, never a data
  series, never a status color. Using the crawl gold to paint bars or encode
  ERROR/WARN is kitsch. (First design panel; reaffirmed pipeline-reveal.)
- No auto-playing crawl intro. The original crawl homage was cut for a reader-paced
  story; homage that takes control of the reader is not homage. (First design panel,
  PR #1.)
- **Two-register law (pipeline-reveal, 2026-07-18):** story beats speak in-universe
  (bureaucratic census audit); machinery speaks plain engineering, Star-Wars-free.
  Exactly ONE sanctioned bridge word crosses the line: "paper trail". Reveal label
  template is generated: "The paper trail — where {claim} comes from"; beat 4 (the
  held pause) renders the quietest variant, "The paper trail."
- **The "six pipelines" claim is false and stays dead.** It is ONE pipeline, three
  transform assets, six queries. The beat-7 callback is provenance-computed and
  arithmetically true: "One pipeline, three transforms, eight checks — the full
  record is below." (Pipeline-reveal.)
- Reveals exist on beats 1–6 only; beat 0 stays a clean hook; beat 7 carries the
  callback line, not a reveal. (Pipeline-reveal.)
- **Guard-honesty wording law:** a check badge may appear only where the check
  asserts the displayed number (or its labeled denominator/structure); derived or
  unguarded claims say so in plain words; no fabricated or implied live status.
  Severity badges are engineering facts — monochrome ◆ blocks / ◇ warns — never
  faction iconography, never lightsaber colors. (Pipeline-reveal.)
- **Description style rule (post-landing cleanup, 2026-07-18):** check descriptions
  state the invariant and its stakes; run metadata carries the particulars;
  `known_facts.py` is the ONLY home for canon rosters and payoff numbers. "Matches
  known_facts.SIX_FILM_CHARACTERS" is MORE precise than a hand-listed roster, not
  vaguer — a prose roster is a second home and a drift bug that can make the Dagster
  UI lie. No check string quotes another beat's caption or payoff.
- **Spoiler pin law (post-landing cleanup):** a standing offline test derives payoff
  term sets — names AND numbers — from known_facts and asserts no check string
  renders on a beat earlier than its claim's reveal beat. Term sets are derived,
  never hand-listed; every new check passes the spoiler audit; the pin was
  seen-to-fail before merge.
- **Displayed SQL is executed SQL (post-landing cleanup):** any SQL text shown on
  the site lives in DATA and is executed against the fixture-built warehouse by the
  offline suite. A displayed query that isn't the executed one is a misattributed
  quote — same sin as a number credited to the wrong asset.
- **Provenance carries no narrative fields (post-landing cleanup):** everything in
  DATA.provenance stays derivable from / verifiable against the real Dagster
  definitions plus known_facts. No hand-authored story attribution (e.g. a `beat`
  index on checks) on the one object whose credibility is "machine-checked".
- **The rail is uniform (post-landing cleanup):** every beat renders the same rule —
  all checks of its chain assets. Spoiler safety lives in the strings, not the
  renderer. My cumulative beat-indexed rail is dead; do not re-propose it.
- **Quoted-testimony rule (birth registry, 2026-07-19):** external claims — dialogue,
  canon numbers — may be *audited* in copy but never rendered as site-derived data;
  derived numbers come only from DATA. The Yoda line ("filed at 896 BBY — his own
  count, nine hundred years, checks out") renders ONLY while the record still agrees;
  if the data moves, the audit line vanishes rather than lie.
- **BBY is the dataset's own unit (birth registry):** `birth_year_bby` is positive;
  "-896" never displays (pinned in the SQL compare test); the gloss "years before the
  Battle of Yavin" prints visibly, not tooltip-only; NO ABY appears on card, column
  copy, or checks — zero ABY records exist, and the parser's ABY branch lives only in
  synthetic pytest cases. Claims must never imply ABY data we don't have.
- **The gold ring means "extreme" (birth registry / Q3):** persistent gold emphasis
  asserts superlatives only — Yoda alone ringed on the registry, the three true
  extremes on the dashboard. Named non-extremes (Vader) get labels, never rings.
  Amber is dead. This extends gold-is-ceremony; it does not soften it.
- **Annotation cap (birth registry):** the registry dot strip carries exactly two
  annotations — Yoda and Jabba. More would be decoration.
- **Failure-mode separation law (birth registry):** a displayed number derived
  through a parse gets TWO guards — drift baseline + data-independent parse-honesty —
  because "the data moved" and "the parser broke" must fail differently; otherwise
  "39 undated" can silently mean "39 unparsed" under a glowing badge.
- **Absence pins are legitimate guards (birth registry):** an element exempted from a
  detector by a property (the coda: number/name/payoff-free) gets a pin asserting
  that property; pinning the wording itself is theater.
- **The README "Limits, by design" section is Star-Wars-free** — machinery register,
  per the two-register law; number-free, one link to WORKSHOP Module 10.
- **Gold has exactly ONE home (token hygiene, 2026-07-19):** the byte-patterns
  #ffe81f / 255,232,31 appear once, in :root; every derivation goes through
  `var(--gold)` / color-mix. The guard pins the PATTERN, never the ceremony —
  the line-693 tooltip swatch and `.unit.hot` spotlights remain settled uses.
  Never propose (or accept) a "no gold in JS" rule; it relitigates ceremony.
- **The whisper clause (token hygiene):** every sanctioned style exception is an
  exact (selector, value, reason) pin in the guard, failing loudly on change in
  EITHER direction. Unexplained holes are theater; pinned exceptions are law.
- **Scenery is not ink (token hygiene):** decorative paints (the aria-hidden
  starfield #cdd8ef) may stay literals with a required sanction comment; data ink
  must be tokenized; no runtime bridges built for decoration. And ink adapts to
  its ground: on-mark labels take per-ground ink from the array that drives the
  ground, every rendered pair ≥4.5:1 verified computationally, never a new hex.
- **The style registry is the test (token hygiene):** the sanctioned type scale's
  one machine-readable home is `test_site_style_hygiene.py` — no font-size tokens,
  no parallel lists. Raise-only grants permission, not obligation: standing still
  needs no evidence; moving chart geometry does. `.prov-check` stays 11.5 —
  the held pause's authored whisper tier.
- **The census conceit is load-bearing (watchlist round, 2026-07-19):** the stage
  tooltip is the ONLY surface naming most of the 82 individuals; no input modality
  may be cut off from it. Tap-to-pin lives in the shared tooltip layer; dismissal
  is the reader's own next tap or scroll, never a timer.
- **Exposure changes reach, not content (watchlist round):** widening a verified
  string's audience renders the SAME string verbatim from its one home; if it
  doesn't fit the vessel, change the vessel. Truncation/paraphrase for space is a
  second home and a misquoted check — my veto trigger, now law.
- **Acceptance is a decision with a tripwire (watchlist round):** an accepted
  limitation enters the log with its reopening trigger; a shrug is not a verdict.
  Q1 trips on a why gaining load-bearing content with no non-hover home, or the
  legend line ceasing to be true; Q4 trips on any anno carrying content absent
  from copy/caption, and viewBox reworks must cost the anchor re-verification.
- **Measured-vs-inferred labeling (watchlist round):** any decision resting on
  unreachable hardware states its measured facts and its inferences separately,
  verbatim, in the log.
- **Anchoring restoration is not scroll-jacking (watchlist round):** a synchronous,
  activation-triggered, measured-delta scroll correction that no-ops where the
  browser already anchors is the sanctioned disclosure-compensation shape;
  animated or assumed-delta variants remain banned.
- **On-file vocabulary law (akabab, 2026-07-20):** akabab death data is
  sequel-inclusive AND canon-incomplete (Luke/Han on file from the sequels; Leia
  absent — pre-TROS vintage), so every surface says "deaths on file" / "on file",
  never "deceased", never saga-scoped or canon-complete claims. Closer line:
  "'On file' means the curated source records it — absence is not survival."
- **Aliases bridge joins, never repair records (akabab):** curated dict in
  known_facts; `character_name` keeps SWAPI's as-filed spelling. Each entry's
  comment states the canon direction (akabab "Ratts Tyerell" is canon; SWAPI holds
  the typo). Injectivity + load-bearing pytest ungated; no fuzzy matching, ever.
- **Cross-source derived figures are quoted testimony (akabab):** SWAPI-birth ×
  akabab-death arithmetic — the Yoda 896+4=900 gem — is pre-vetoed off all
  surfaces; computing it from `died_year_aby` would launder the audited quote into
  data. Only a surfacing panel may unseal it; written tripwire in the log.
- **Signed-year columns name their convention (akabab):** `_bby` / `_aby` suffixes,
  no bare year columns in the warehouse. Storage may hold signed years; the
  settled BBY *display* law is untouched.
- **Nested denominators (akabab):** every enrichment-join number carries matched
  AND field-present denominators — report-copy discipline computed from data, not
  new checks. No superlatives from sparse lineage fields; affiliations rank only
  with n disclosed.
- **Akabab is never canon authority:** attributed as fan-curated, MIT, effectively
  frozen, SWAPI-derived (it reproduces SWAPI's typos — that's why 81/82
  exact-match). Its values are "as filed by the profile source", not canon (e.g.
  Han born -29 vs current canon ~32 BBY).
- **"Affiliations & Apprenticeships" is the section title:** as-filed field name
  (`affiliations`) plus drafted-copy discipline beat my "Allegiances"; don't
  re-propose.
- **A ranked affiliations/faction chart is BANNED on the six-film site (akabab
  surfacing, 2026-07-20):** `affiliations` is canon-wide/sequel-inclusive (the
  computed top-8 includes New Republic 11, CIS 11), so a ranked bar is a ranking
  *claim* a saga-scoped site cannot honestly make. Only saga-safe COVERAGE COUNTS
  surface (75 of 82 affiliated, denominatored). Unanimous; do not re-propose.
- **The second source is a dashboard CARD, never a story beat (akabab
  surfacing):** the census spine is one archive — eight steps, "n/8", exactly-8
  kickers — all untouched (BUILDERS.length=8). `#card-biographies` sits after
  `#card-registry`, a second *reading* of the census, headline **82 of 82
  matched** (the only akabab number both complete AND pipeline-guarded). Ladder
  beneath, every number nested-denominatored, "on file" vocabulary. No 9th beat.
- **akabab attribution shipped verbatim (akabab surfacing):** fan-curated, MIT,
  SWAPI-derived, effectively frozen — NEVER canon authority. "On file" / "absence
  is not survival" shipped verbatim. The 896+4=900 derivation stays SEALED off all
  surfaces; the displayed `bios` SQL returns coverage COUNTS, never `died_year_aby`
  values; the per-row `bio` object carries a `diedOnFile` boolean, no signed year.
- **A dashboard card carries no live check badge (akabab surfacing):** a badge
  needs a claim entry (beats-1–6 machinery); cards state numbers with denominators
  and lean on the DAG strip for lineage. The DAG chip set is now a guarded surface,
  pinned to the real Dagster asset keys.

## Working knowledge

- Dataset scope is the six-episode saga (Episodes I–VI) as served by swapi.info;
  no sequels, no anthology films. Claims like "every film" mean these six.
- The census conceit ("A Galaxy of 82 People") is period-appropriate and earned;
  beat 7's fourth-wall break licenses the per-beat reveals: extend, don't invent.
- All six opening crawls preserved verbatim in `DATA.films[].crawl` —
  primary-source text, opt-in; the right home for them.
- Beat-6 quote verified: "flying is for droids" is a fair paraphrase of Obi-Wan in
  Revenge of the Sith ("Flying is for droids."); attribution correct as rendered.
- Beat→asset truth: beats 4–6 DIRECT via live `character_stats_*` checks; beat 1's
  "1 unmeasured" via the WARN `characters_enriched_unknown_height_baseline`.
  **Fifteen checks total** (4 blocking, 11 warn). Trio names surface only via
  check metadata (`expected: sorted(SIX_FILM_CHARACTERS)`); roster's single home
  is known_facts.py.
- Birth-registry facts: 43 of 82 dated, 39 undated; oldest Yoda 896 BBY, second
  Jabba 600 BBY. Canon gem: 896 BBY + death 4 ABY = 900, matching Yoda's RotJ
  count. Constants in known_facts; "896"/"yoda" are spoiler-pinned terms.
- `characters_enriched` is now a real DuckDB table (write-back on the same df the
  asset returns), so `FROM characters_enriched` in the displayed SQL is true.
- Beat-1 facts: height range Yoda 66 cm → Yarael Poof 264 cm; the single
  unmeasured character is **Arvel Crynyd** (the A-wing pilot who took out the
  Executor's bridge in RotJ) — earned if ever named on the page.
- Kitsch veto list for machinery visuals: no Aurebesh in diagrams, no Imperial/Rebel
  iconography as badges, no "these aren't the rows you're looking for".
- Akabab durable facts (verified live all.json, 2026-07-20): coverage on the frozen
  fixture — 82/82 matched, 47/82 deaths on file, 75/82 affiliated, 14 masters, 12
  apprentices. `affiliations` is canon-wide/sequel-inclusive (Luke: "New Republic",
  "Resistance") → the ranked-chart ban. `masters` strings carry parentheticals
  ("Qui-Gon Jinn (informal Jedi Master)") — counts safe, verbatim names need care.
  No Legends contamination (Chewbacca has no `died`). Death year VALUES stay sealed.
- Check counts: 15→20 total (blocking 4→6, warn 11→14) with akabab landed; totals
  pin stays 13/5/20. The surfacing card carries no live badge, so its checks
  (`character_biographies_join_coverage` 82/82, `_deaths_on_file_baseline` 47/82,
  both WARN) guard the numbers without hitting the 8-step story rail.

## Open watch items

- STILL OPEN: SWAPI quirks republished verbatim — candidate "clerical errors"
  disclosure (roster in known_facts): "Beru Whitesun lars", "Ayla Secura",
  "Wookie", "Neimodian", R4-P17 (astromech filed Human/female), and now "Ratts
  Tyerel" (the one typo akabab fixed). Honest angle is in-universe "as filed":
  record the error, never silently correct canon.
- STILL OPEN: galaxy_report's legacy closer ("May the Force be with your data
  pipeline.") predates the two-register law — off-site, out of the akabab brief's
  scope, but it's a quote-joke in machinery register. Raise at the next report or
  surfacing round.

## Banked: pipeline-reveal + post-landing cleanup (2026-07-18, compacted)

Won: "six pipelines" killed as false; computed-callback wording, register
separation, "paper trail" bridge, kitsch vetoes, reveals-on-1–6 all law;
displayed-SQL-is-executed-SQL in my "misattributed quote" framing; spoiler pin
born from my "sequence the quotation" instinct. Lost: beat-7-callback cut
(storyteller kept it, made honest); beat-indexed rail 5–3–1 to the one-home law.
Lessons: propose the repair, not just the veto; trace every displayed number to
its computing code; ask "how many homes does this fact have?"; never propose
provenance fields pytest can't verify.

## Banked: birth registry, coda, hues, limits (2026-07-19, compacted)

Decision: `2026-07-19-birth-registry-and-polish.md`; commits 1f3cf9e..f170379.
Near-sweep: BBY-unit unanimous in my framing; annotation cap held; gold-ring-
means-extreme strengthened ceremony; the Yoda gem shipped as data-conditional
quoted testimony. Lessons: the honest RENDER CONDITION (when a gem appears,
when it vanishes) is my job too; guard plumbing that changes what a number
MEANS (undated vs unparsed) is provenance in my lane — don't sit out.

## Banked: token hygiene + raise-only type (2026-07-19, compacted)

Decision: `2026-07-19-token-hygiene.md`; commit a30a5bc. Clean sweep in my lane:
gold single-home pin shipped as I shaped it (pins byte-patterns, not ceremony);
split-the-literals carried ("machinery built for decoration is the engineering
cousin of kitsch"); one-home font ruling 5–1; `.prov-check` 11.5 held. Lessons:
pair early with whoever owns the mechanism (I name the honesty requirement,
they build it); for any single-home fact, audit its DERIVED encodings too.

## Banked: watchlist round (2026-07-19, compacted)

Decision: `2026-07-19-watchlist-round.md`; commit fdd3178 (tap-to-pin landed:
lines 799/802/469/484). Won: suppress-for-touch veto 5–1; census conceit law
in my framing (stage tooltip = the 82's only roll-call; Arvel Crynyd reachable
by every modality); Q4 flip quoted in adjudication. Lost Q1 4–2 softly —
"fallback: accept" was pre-named, both conditions banked (legend line stays
true; verbatim-or-nothing became law). Lessons: rank fallbacks explicitly;
audit channel redundancy before defending legibility; bring counted
interruptions across the held pause; pre-sort evidence measured vs inferred.
Durable: badge whys are verbatim Dagster descriptions, not number-free —
raw_people's "82" is safe as beat-0's own hook; hover `title=` stays a
desktop bonus with no non-hover twin, by decision.

## Banked: akabab site surfacing (2026-07-20)

Decision: `2026-07-20-akabab-site-surfacing.md`. Near-sweep in my lane.

Won: my ranked-affiliation trap became the unanimous D5 veto — the computed top-8
(New Republic 11, CIS 11) proved the canon-scope trap was live, so the ranked bar
is banned and only saga-safe coverage counts (75/82) surface. My Q1 dashboard-card-
not-a-9th-beat framing carried unanimous (D1): spine untouched at BUILDERS.length=8.
"82 of 82 matched" headline (D2) — the one number both complete and guarded. "On
file" / "absence is not survival" shipped verbatim; my fan-curated/MIT/SWAPI-derived/
never-canon attribution held. The 896+4 pre-veto held under pressure: the `bios` SQL
returns COUNTS, the `bio` object holds a `diedOnFile` boolean — no `died_year_aby`
value ever reaches the page. My L320/L941 contradiction flag drove the unconditional
fix ("five SWAPI pulls and one akabab pull … five transforms").

Lost nothing of substance. Adjacent rulings I didn't own but should note: Claude ruled
PIN over render for the DAG chip set (a guarded surface now), and boolean `diedOnFile`
over the engineer's `diedAby|null` — both tightened my honesty laws further than I'd
asked.

Prep differently: (1) I flagged the ranked-affiliation trap in *prep* as "disclose the
frame or cut" — the panel went straight to cut. Trust the harder line sooner when a
claim's scope can't be honestly narrowed. (2) Draft the card copy verbatim next time;
the storyteller's "A second reading" stat-block led because it was drafted, and my role
was reduced to an attribution gloss on it. Bring the whole block, not just the vocabulary.

## Banked: akabab second source (2026-07-20, compacted)

Decision: `2026-07-20-akabab-second-source.md`. Option C unanimous. Won: the
deaths-on-file package unopposed (my per-record audit — Luke/Han sequel deaths,
Leia absent — proved it); alias canon-direction comments law; my attribution
language near-verbatim in README; my 896+4-becomes-derivable flag became the
written pre-veto tripwire. Lost instructively: "Affiliations & Apprenticeships"
beat my "Allegiances" (my own as-filed principle + drafted copy against me);
alias framing went to engineer's "bridges the join" (my comment requirement
survived). Lessons: bring COMPUTED facts not counted ones (three transcribed
surveys disagreed 87/88, 47/28 — baselines now script-computed from the frozen
fixture); DRAFT copy I care about; check the as-filed field name first; file my
own tripwire when a settled rule gains a new threat vector.
