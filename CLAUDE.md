# starwars-dagster

Dagster pipeline (SWAPI → DuckDB → transforms → galaxy_report) plus a self-contained
scroll-story website at `site/index.html`, published as a Claude artifact at
https://claude.ai/code/artifact/e71e41b6-f606-492c-af77-d19a8b3443d7 (republish to the
same URL — never mint a new one).

## Design panel (user's preferred process for design/creative decisions)

For any significant design, UX, storytelling, pipeline, or portfolio decision, run the
standing role panel — see **`.claude/panel/charter.md`** for the full protocol
(prep → debate → synthesis → bank). The nine panelists are the `panel-*` agents in
`.claude/agents/`; each keeps its own memory in `.claude/panel/memory/` and may author
its own skills under `.claude/skills/panel-*`. Scoping: visual/site decisions → the
first six roles; pipeline/repo/portfolio decisions → add hiring-manager, qa-engineer,
technical-writer; all nine only when the decision spans both. Claude is the final
decision maker and writes the decision log to `.claude/panel/decisions/`.

**Anything marked "Settled" in a panelist's memory is banked law — do not relitigate.**

## Hard constraints digest (non-negotiable; full rationale lives in panel memories)

- Site is ONE HTML file: no CDNs, no webfonts, no build step.
- Gold #ffe81f is display accent only — never a data series; saber blue is the data hue.
- No auto-play, no time gates, no scroll-jacking; content never gated (disclosures opt-in).
- Reduced-motion, mobile (<860px), and the flat/auto-height-embed fallback must all work;
  the viewport meta tag stays.
- Every number on the site derivable from the inline JSON; denominators/nulls on-chart;
  the runtime drift detector stays and grows with new claims.
- Mobile story geometry is settled (stage min(52svh,480px); min(64svh,560px) stations;
  one `.step--held` pause; "n / 8" beat counter).
- pytest guards CODE offline; asset checks guard DATA (structural=ERROR/blocking,
  drift=WARN); `known_facts.py` is the single source of baselines; no second
  data-quality framework, no coverage gates; CI stays offline-only.
- A feature and its automated guard land in the same commit.
- Site provenance is honest and verified: all lineage/severity strings render from
  `DATA.provenance` (pytest-checked against the real Dagster defs; badge severity derives
  from the static `blocking` flag); a check badge appears only where the check asserts the
  displayed number; the one-line strict-JSON `const DATA` literal is load-bearing.

## Open items (carried forward — full context in `.claude/panel/decisions/2026-07-18-pipeline-reveal.md`)

- Screenshot retake: re-materialize locally and retake the three README screenshots so
  the Dagster lineage view shows the 8 green asset checks (needs the desktop UI). Until
  then, README captions must not overclaim what the current images show.
- Per-character-grain transform (films-per-character, starships-flown-per-person): land
  only on analytics merits, never as diagram fuel. If it lands: add asset checks
  asserting 42-of-82 one-film, the six-film trio, 19-of-82 pilots, maxFlown 5; flip
  beats 4–6 provenance `relation` to `direct`; update `tests/test_site_provenance.py`
  in the same commit (honesty lines regenerate from the projection).
- Migrate the five hand-written dashboard SQL strings (`makeCard` opts.sql in
  site/index.html) into a verified home — bring a concrete verification story first
  (QA's condition for scope).
- Swap the README "my portfolio" placeholder anchor (personal-site link slot) for the
  live URL once the owner's professional site ships.
