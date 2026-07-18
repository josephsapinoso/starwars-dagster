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
- Beat→asset truth (from data-analyst's prep, adjudicated): beats 1–3 read from
  `characters_enriched`; the 42-one-film and six-film-trio numbers are per-CHARACTER
  and are computed by NO asset (hand-derived from `raw_people[].films` at authoring
  time, guarded offline by pytest vs `known_facts.py`). Reveals must render this as
  `relation: derived` honestly — my trio fact is guarded by pytest, not a live check.
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

## Prep notes: post-landing cleanup (2026-07-18)

**Q1 — the leak is wider than the brief says.** `chainEl` (site/index.html:823-843)
renders ALL checks of every chain asset. Beats 4–6 share raw_people → star_wars_db →
character_stats, so beat 4's rail shows all four character_stats labels: "42 one-film
cameos" (its own), plus **"six-film trio" (beat 5's payoff), "19 pilots" AND
"max flown = 5" (beat 6's payoffs)**. Beat 5's rail likewise pre-leaks beat 6. Hover
`why` strings name Obi-Wan verbatim in BOTH `character_stats_six_film_trio` and
`character_stats_max_flown_baseline` (checks.py:214-256). The brief's Q1 framing
(trio only) understates it — any fix must handle all three forward leaks or it's
half a fix.

**My Q1 position, grounded:** option (a) — rewriting label/description spoiler-free —
is self-defeating in my lane. The trio description naming C-3PO, R2-D2, AND Obi-Wan is
the canon correction this project exists to make; scrubbing names from the Dagster-UI
source to protect a webpage beat bowdlerizes the primary source, and any *accurate*
label for a set-of-three baseline still leaks the count ("trio" IS the spoiler). Fix
belongs in rendering (option b): sequence the quotation, don't rewrite the source —
e.g. each beat's rail shows blocking checks + checks guarding claims at ≤ the current
beat; beat 6 shows the full rail. That preserves verbatim-projection law untouched.

**Q2 verification story:** a displayed SQL string that isn't the executed, verified
string is a misattributed quote — same class of sin as a number credited to the wrong
asset. The candidate (SQL into DATA; offline pytest EXECUTES each string against the
fixture DB and matches inline numbers) makes display = execution = truth. Support.
Register note: SQL stays machine-shop voice — no Star Wars aliases/comments creeping
in during the move.

**Q3 facts verified from DATA:** beat 1's range is Yoda 66 cm → Yarael Poof 264 cm;
the single unmeasured character is **Arvel Crynyd** (the A-wing pilot who hit the
Executor's bridge, RotJ — a fitting person for the census to have failed to measure).
"The measuring" beat flipping pytest → WARN check mirrors beat 2's mass baseline
exactly; earned, not decorative. Q3(b) galaxy_report structural check: no lore stake;
defer to engineers under the coverage-theater law.

**Also noted:** rail-render-everything was never itself banked law — the
pipeline-reveal decision specified "check rail per chip" but not which checks; a
per-beat filter rule contradicts nothing settled.
