# starwars-dagster

Dagster pipeline (SWAPI → DuckDB → transforms → galaxy_report) plus a self-contained
scroll-story website at `site/index.html`, published as a Claude artifact at
https://claude.ai/code/artifact/e71e41b6-f606-492c-af77-d19a8b3443d7 (republish to the
same URL — never mint a new one).

## Design panel workflow (user's preferred process for design/creative decisions)

For any significant design, UX, storytelling, or portfolio/engineering-craft decision
on this project (e.g. adding tests or asset checks, restructuring the README, CI), run
the owner's **role-panel debate** before implementing:

1. Spawn parallel subagents, one per role, each given the same factual brief
   (current state, constraints, available data) and asked for: a verdict, ONE concrete
   proposal, their top 3 must-haves, and their top 3 objections to what the *other*
   roles will likely propose. Keep each position short (≤500 words) and opinionated.
2. The roles:
   - Star Wars Lore Fanatic — authenticity; what's earned vs. kitsch
   - Data Engineer — lineage, reproducibility, data honesty, no build-step creep
   - Data Analyst — which claims the data actually supports; denominators and nulls
   - Graphic Designer — typography, color budget, one coherent mark system
   - UX Designer — user control, accessibility, mobile, embeds; never gate content
   - Professional Visual Storyteller — narrative spine, hook, beat sheet, pacing
   - Data Engineering Hiring Manager — the 90-second portfolio scan; what signal each
     choice sends (README first impression, commit history, visible tradeoffs); what
     questions it would raise in an interview
   - QA / Data Quality Engineer — tests, Dagster asset checks, schema/null validation,
     failure modes when SWAPI changes; nothing ships unverified
   - Technical Writer — README/WORKSHOP.md as the landing page; docs must explain the
     *why* and the tradeoffs, not just the how; jargon earns its place

   Scoping: for pure visual/site decisions the original six roles carry the debate;
   for pipeline, repo, or portfolio-presentation decisions the last three must be
   included. Don't run all nine unless the decision genuinely spans both.
3. Claude acts as **final decision maker**: adjudicate conflicts explicitly (say who
   won each argument and why), then present one synthesized plan — not a menu.

Lessons already banked from the first panel (do not relitigate):
- No auto-playing or time-gated intros, ever; reader-paced scroll only, no scroll-jacking.
- Every number on the site must be derivable from the inline pipeline JSON; disclose
  denominators/nulls on-chart (a runtime drift-detector in `site/index.html` warns on
  mismatch between data and copy).
- Verified data facts: 82 people; THREE characters appear in all six films (C-3PO,
  R2-D2, Obi-Wan — not just the droids); 23 lack mass; Naboo 11 + Tatooine 10.
- Site constraints: single HTML file, no CDNs/webfonts/build step; gold #ffe81f is
  display accent only, never a data series; must handle reduced-motion, mobile, and
  the flat/auto-height-embed fallback (sticky can't engage there).
