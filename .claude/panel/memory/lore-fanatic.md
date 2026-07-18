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
  `characters_enriched_unknown_height_baseline`. Thirteen checks total (4 blocking,
  9 warn). Trio names surface at runtime in check metadata (`expected: sorted(
  SIX_FILM_CHARACTERS)`) — the roster's single home is known_facts.py.
- `characters_enriched` is now a real DuckDB table (write-back on the same df the
  asset returns), so `FROM characters_enriched` in the displayed SQL is true.
- Beat-1 verified facts (bankable copy material): height range Yoda 66 cm → Yarael
  Poof 264 cm; the single unmeasured character is **Arvel Crynyd** — the A-wing
  pilot who took out the Executor's bridge in RotJ. A fitting person for the census
  to have failed to measure; earned if ever named on the page.
- Kitsch veto list for machinery visuals: no Aurebesh in diagrams, no Imperial/Rebel
  iconography as badges, no "these aren't the rows you're looking for".

## Banked: pipeline-reveal (2026-07-18)

**Won:**
- The "six pipelines" callback was killed as factually false; my alternative framing
  survived as the wording *law* — the shipped line is computed from provenance counts
  so it can never drift into a lie.
- Register separation adopted wholesale: reveals live in the engineering register,
  with "paper trail" as the single sanctioned bridge word, baked into the generated
  label template (adjudication point 7).
- Kitsch vetoes held without contest: monochrome ◆/◇ severity, no allegiance
  iconography, gold confined to the single `.hot` chip seat (display accent —
  consistent with gold-is-ceremony).
- Coverage: beats 1–6 only, beat 0 clean — my position, shared with storyteller/ux/
  designer, beat the hiring-manager's beat-0 reveal (satisfied structurally instead:
  `raw_people` heads every chain, so the 82-census guards appear in all six reveals).

**Lost:**
- My cut of the beat-7 callback. Storyteller won on keeping it; the compromise is my
  wording law applied to their structure. Right outcome — the callback earns its
  place once it is true and drift-detected. Lesson: propose the repair, not just the
  veto; the panel keeps lines I would cut when someone makes them honest.

**Prep differently next time:** my prep verified quotes and registers but not the
beat→asset map — the data-analyst caught that the brief's map was partly false, and
that finding reshaped the whole spec. "Which asset actually computes this number" is
a provenance/authenticity question squarely in my lane (a number attributed to the
wrong asset is a misattributed quote). Next machinery topic: trace every displayed
number to its computing code before opining on framing.

**Watch item:** the open per-character-grain transform would upgrade beats 4–6 to
DIRECT — if it lands, the trio and 42-count get real checks; reveal wording for those
beats must be updated from "derived" the same commit, or the honesty line becomes the
new lie. → LANDED 2026-07-18 (commit 082d9c9); beats 4–6 now direct + check-guarded.

## Banked: post-landing cleanup (2026-07-18)

**Won:**
- Q2 outright and unanimously, in my framing: displayed SQL that isn't executed SQL
  is a misattributed quote. Now law. Register held in implementation (c0b97e0): the
  five DATA SQL strings are pure machine-shop voice, the stale "-- 59 of 82" comment
  is dead, no Star Wars aliases or quote-jokes entered during the move.
- Q3(a): the height-null WARN check landed (2aa845e); beat 1's guard flipped
  pytest→check honestly, per my "mirrors beat 2, earned not decorative" read. Q3(b)
  galaxy_report stays disclosed-not-checked — my defer-to-engineers call held.
- Q1 substance despite losing the mechanism: nothing kitsch or bowdlerized entered
  checks.py — the trio check still asserts the exact three-name set, and the names
  still surface at runtime in metadata; my "sequence the quotation" instinct became
  the standing spoiler pin; and my must-have #2 (derived, never hand-listed) is
  literally how the pin builds its term sets from known_facts.
- My prep widened the leak audit from "the trio" to all three forward leaks
  (trio + 19 pilots + max-flown), and the fix covered all of them.

**Lost:**
- Q1 mechanism, 5–3–1: cumulative beat-indexed rail lost to re-authoring. Decisive:
  the technical-writer's one-home law (the prose roster was a THIRD home for the
  trio — a drift bug that could make the Dagster UI lie, independent of spoilers)
  plus QA's point that a `beat` index is hand-authored attribution pytest cannot
  verify. I framed re-authoring as bowdlerizing; it wasn't. "Matches
  known_facts.SIX_FILM_CHARACTERS" is more precise than prose, and fidelity can
  live in a derived reference, not only in a verbatim quotation. My skill's
  "sequence the quotation" corollary is rewritten to match.

**Prep differently next time:** before defending any prose that carries a canon
fact, ask "how many homes does this fact have?" — single-sourcing a roster is as
much an authenticity question as getting the roster right. And check the pytest
verifiability of any field I'd add to provenance before proposing it; unverifiable
attribution on the machine-checked object is its own kind of misattribution.
