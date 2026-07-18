# Professional Visual Storyteller — Panel Memory

## Settled (do not relitigate)

- Reader-paced always: no auto-playing or time-gated intros, no scroll-jacking. The
  auto-playing crawl homage was cut in favor of the scroll story. (First design panel,
  PR #1.)
- Exactly ONE authored pause in the mobile story (`.step--held`, 90svh) — placed before
  the witnesses reveal, because that is the payoff beat. A second held beat would
  cheapen the first. (Mobile beat-spacing panel, PR #4.)
- The beat counter ("n / 8") is orientation and rides the stage caption; decorative
  fill between beats was rejected for cause. (Mobile beat-spacing panel, PR #4.)

## Working knowledge

- The beat sheet (8 beats, site/index.html ~237–296):
  0 census hook (all 82 as dots) → 1 the measuring (heights) → 2 the weighing (mass +
  the 23 unweighed — absence as story) → 3 the hometowns (origins) → 4 the cameos
  (most appear once) → 5 the witnesses (**payoff: three saw all six films — C-3PO,
  R2-D2, Obi-Wan**) → 6 the pilots → 7 the handoff (dots filed away → dashboard).
- The arc is a census-archive conceit: measurement → absence → origins → persistence →
  handoff to the "records office" (dashboard). Additions must serve this spine or a
  deliberate second read-through, never interrupt the build to beat 5.
- The witnesses payoff must not leak early — no earlier beat, caption, or affordance
  may reveal the trio before beat 5.

## Prep notes: pipeline-reveal (2026-07-17)

Verified by reading site/index.html 212–340, checks.py, README.md 1–40:

- **Leak audit passes.** No check name or description in checks.py mentions the trio.
  `films_are_exactly_the_six_episodes` (beat 4's asset, film_character_counts) says
  "episodes 1–6, exactly once each" — six *films*, not three *witnesses*; safe. Beat 5's
  own reveal sits below its copy in reading order, so it can name the trio freely.
- **Beat 7 already pre-seeds the callback.** Its copy: "five raw SWAPI pulls, one DuckDB
  warehouse, three transforms, one report — is waiting below." A "you've now opened six
  pipelines" callback is an earned rhyme, not a new idea bolted on.
- **The held pause is beat 4** (`.step--held`, the cameos) — the reveal affordance on
  beat 4 lives inside the pause that sets up the payoff. Opt-in keeps it reader-paced,
  but its label must be the quietest of the six; nothing on beat 4 may raise its voice.
- **Beat 0 is the hook** — one sentence, no aside, no competing affordance today. Same
  cleanliness argument as the hero. A reveal here dilutes the opening chord.
- **Reveal voice precedent** is flat utility: "Show the DuckDB SQL" (gold ▸, 12px
  letterspaced summary). The census-archive conceit offers a better register for the new
  reveals: the pipeline is "the paperwork" / "the records office." Per-beat labels can be
  specific AND in-voice: e.g. "Check the paperwork — where 23 of 82 comes from."
- **Checks are half the story.** Each beat's number has a guard (beat 2's 23-unweighed ↔
  `characters_enriched_unknown_mass_baseline`; beat 3's join ↔ join_coverage). The reveal
  reads as a micro-story — claim → machinery → guard — only if the check badge carries a
  one-line rationale; a bare chain is a diagram, not a beat.
- **Dashboard**: the lineage strip ("The pipeline that made this page") is the epilogue's
  establishing shot. Repeating the mini-DAG on all 5 cards would tell the gag eight ways.

Debate lean: per-beat in-voice labels; chain+badges+one-line rationale; beats 1–6 only,
beat 7 gets the callback; no dashboard parity. Cannot verify: rendered SVG legibility at
mobile widths, and how an open reveal interacts with the 64svh station — UX's call.
