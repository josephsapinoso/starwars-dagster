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

## Working knowledge

- Dataset scope is the six-episode saga (Episodes I–VI) as served by swapi.info;
  no sequels, no anthology films. Claims like "every film" mean these six.
- The site's story frames the data as a census ("A Galaxy of 82 People") — a
  bureaucratic-archive conceit that is period-appropriate for the Republic/Empire and
  earned rather than decorative. Beat 7 already breaks the fourth wall on purpose
  ("The machinery that counted it … is waiting below"), which is what licenses the
  per-beat reveals: extend, don't invent.
- The opening crawls of all six films are preserved verbatim in a dashboard reveal
  (`DATA.films[].crawl`) — the right home for them: primary-source text, opt-in.
- Beat-6 quote verified: "flying is for droids" is a fair paraphrase of Obi-Wan in
  Revenge of the Sith ("Flying is for droids."); attribution correct as rendered.
- Beat→asset truth (current, post-082d9c9 + cleanup): beats 4–6 are DIRECT, guarded
  by live `character_stats_*` checks (one-film 42, six-film trio, pilot count,
  max-flown); beat 1's "1 unmeasured" is guarded by the WARN check
  `characters_enriched_unknown_height_baseline`. **Fifteen checks total** (4 blocking,
  11 warn) since the birth registry added two WARNs (birth baseline + parse-honesty).
  Trio names surface at runtime in check metadata (`expected: sorted(
  SIX_FILM_CHARACTERS)`) — the roster's single home is known_facts.py.
- Birth-registry verified facts: 43 of 82 dated, 39 undated (the archive's biggest
  gap); oldest Yoda 896 BBY, second Jabba 600 BBY; all dated values BBY. The canon
  gem: 896 BBY birth + death in 4 ABY = 900, matching Yoda's own RotJ count ("When
  nine hundred years old you reach…"). Constants live in known_facts
  (EXPECTED_OLDEST_BIRTH_BBY = 896.0 etc.); "896"/"yoda" are spoiler-pinned terms.
- `characters_enriched` is now a real DuckDB table (write-back on the same df the
  asset returns), so `FROM characters_enriched` in the displayed SQL is true.
- Beat-1 verified facts (bankable copy material): height range Yoda 66 cm → Yarael
  Poof 264 cm; the single unmeasured character is **Arvel Crynyd** — the A-wing
  pilot who took out the Executor's bridge in RotJ. A fitting person for the census
  to have failed to measure; earned if ever named on the page.
- Kitsch veto list for machinery visuals: no Aurebesh in diagrams, no Imperial/Rebel
  iconography as badges, no "these aren't the rows you're looking for".

## Open watch items (compacted from 2026-07-18 survey prep)

- STILL OPEN: upstream SWAPI quirks the site republishes verbatim — candidate
  "clerical errors" disclosure, roster would live in known_facts: "Beru Whitesun
  lars" (lowercase l), "Ayla Secura" (canon Aayla), species "Wookie" (canon Wookiee),
  "Neimodian" (canon Neimoidian), R4-P17 — an astromech droid — filed as species
  Human, gender female. In-universe framing ("as filed") is the honest angle: the
  census records the error rather than silently correcting canon.

## Banked: pipeline-reveal (2026-07-18, compacted)

Won: "six pipelines" killed as false, my computed-callback wording became law;
register separation + "paper trail" bridge adopted; kitsch vetoes held; reveals on
beats 1–6 only. Lost: my cut of the beat-7 callback — storyteller kept it, made
honest by my wording law. Lessons banked: propose the repair, not just the veto;
"which asset computes this number" is a provenance question in MY lane — trace every
displayed number to its computing code before opining on framing.

## Banked: post-landing cleanup (2026-07-18, compacted)

Won: displayed-SQL-is-executed-SQL law in my "misattributed quote" framing; height
WARN check earned; spoiler pin born from my "sequence the quotation" instinct with
derived term sets. Lost 5–3–1: my beat-indexed rail, to the one-home law + QA's
unverifiable-attribution point — re-authoring wasn't bowdlerizing; fidelity can live
in a derived reference (skill corollary rewritten). Lessons banked: ask "how many
homes does this fact have?"; never propose provenance fields pytest can't verify.

## Banked: birth registry, coda, hues, limits (2026-07-19, compacted)

Decision: `2026-07-19-birth-registry-and-polish.md`; commits 1f3cf9e, 4d92cb7,
7d96df5, f170379. Near-sweep: BBY-is-the-dataset's-unit unanimous in my framing;
annotation cap held; gold-ring-means-extreme strengthened gold-ceremony; the
896+4=900 Yoda gem shipped as data-conditional quoted testimony; both register
laws applied by others unprompted — restraint is now ambient. Lessons banked:
I bring facts, but the honest RENDER CONDITION (when a gem appears, when it must
vanish) is my job too; guard plumbing that changes what a displayed number MEANS
(undated vs unparsed) is provenance in my lane — have a position, don't sit out.

## Banked: token hygiene + raise-only type (2026-07-19)

Decision: `.claude/panel/decisions/2026-07-19-token-hygiene.md`; commit a30a5bc
(site/index.html + tests/test_site_style_hygiene.py). Verified landed: gold
rgba leaks → color-mix (lines 53/153); "scenery, not ink" comment at 491; guard
pins #ffe81f once-in-:root, zero 255,232,31, `var(--gold)` free.

Won — clean sweep in my lane: gold single-home pin shipped as I shaped it (pins
byte-patterns, not ceremony; tooltip swatch and `.unit.hot` never endangered);
Q1 split-the-literals carried on failure-mode asymmetry ("machinery built for
decoration is the engineering cousin of kitsch" held); crawl register untouched;
one-home font ruling 5–1; `.prov-check` 11.5 held — I backed the storyteller's
authored-contrast case rather than fronting it. Co-authored pattern (third
straight decision): I name the honesty requirement, someone else builds the
mechanism — pair early with whoever owns the mechanism. Prep lesson: for any
single-home fact, audit its DERIVED encodings too (the rgba/color-mix scrape
found the two leaks); write banked lessons sharp enough to fire as ammunition.

## Prep notes: watchlist round (2026-07-19)

Verified in-repo against the brief (all four items are affordance/mechanics
questions; my lane is what the exposed/illegible/suppressed STRINGS are):

- **Q1 badge whys are register-clean and spoiler-audited already.** `k.why` is a
  VERBATIM projection of the real Dagster check description
  (test_site_provenance.py:95–96), machinery register, zero Star Wars content
  (checks.py descriptions verified). The spoiler pin (:181–223) audits
  `label + why` per beat over the rendered STRING SET — independent of the
  affordance. So exposure (focus/aria/visible) adds reach, not spoiler surface,
  IF AND ONLY IF the same strings render verbatim. Truncation or paraphrase for
  space = a second home + a misquoted check → my veto trigger.
- **Brief correction:** whys are NOT number-free — raw_people's why carries "82
  people" (f-string from known_facts, checks.py:136). Safe: 82 is beat-0's own
  hook; all later-payoff descriptions avoid numbers by design (spoiler law
  working as intended). Don't repeat "number-free" in debate.
- **Legend interaction (Q1):** the settled rail-legend line "full check
  descriptions live in the Dagster UI" (index.html:911) stays TRUE under
  focus/aria exposure but reads as misdirection under a VISIBLE disclosure of
  the same texts. Visible disclosure therefore requires reopening settled copy;
  focus-parity (matching the dashboard charts' existing focus/blur tooltips)
  doesn't. That asymmetry is my Q1 lean.
- **Q3 stakes in my lane:** the stage tooltip (index.html:770–782, shared
  system) is the ONLY place most of the 82 names surface on the stage — annos
  name only the extremes. Suppress-for-touch would cut mobile readers' sole
  access to the census's individuals (incl. Arvel Crynyd's "never measured").
  Tap-to-pin keeps the names; content is in-universe data narration, register
  fine either way.
- **Q4 canon inventory at ~5px effective:** the illegible annos are exactly the
  earned canon references — "Yoda · 66 cm", "Yarael Poof · 2.64 m", "Jabba ·
  1,358 kg", the trio's three names (gold, beat 5), "Obi-Wan · 5 starships"
  (gold). EVERY one also lives legibly in beat copy or caption — beat-5 copy
  (index.html:305) names the trio in full, so no canon fact is mobile-lost by
  accepting. But the gold `.anno-name.hot` emphasis at 5px is an unreadable
  gold smudge: ceremony you can't read is decoration, which argues for a
  raise-only bump (uniform across stage text — never bump only the hot annos;
  that would re-rank emphasis). Raise-only grants permission; the mechanism and
  the guard amendment are the engineers' call.
- **Q2 (Safari jump):** no lore stake; defer to mechanics. Only settled law I
  watch: any compensation must not fight the reader's own scrolling.
- Cannot verify: real-iOS/macOS behavior (jump E2, flash E3) — headless
  evidence only; spec-based inference stands unconfirmed on hardware.
