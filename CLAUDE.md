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
- Displayed SQL is executed SQL: dashboard SQL strings live only in `DATA.sql` and pytest
  executes every one against the fixture-built warehouse (results compared to the charts'
  DATA-derived rows); no hand-verified SQL copy anywhere.
- Check strings state invariants — rosters/numbers live only in known_facts.py — and must
  never pre-tell a later story beat's payoff (spoiler pin in test_site_provenance.py);
  DATA.provenance carries no narrative fields; the rail rule is uniform across beats.

Open item: re-materialize locally and retake the three README screenshots so the
Dagster lineage view shows the 13 green asset checks (needs the desktop UI).
