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
- Provenance reveals exist on beats 1–6 ONLY. Beat 0 stays a clean hook — no aside, no
  competing affordance; beat 7 carries a provenance-computed callback line instead of a
  reveal. One disclosure style, shared with details.sql. (Pipeline-reveal panel,
  2026-07-18.)
- Beat-7 callback wording is computed from provenance counts so it is drift-detectable
  and arithmetically true — since commit 082d9c9 it renders "One pipeline, four
  transforms, twelve checks". Never hand-write pipeline arithmetic into copy; the
  number-word list is drift-guarded against overflow (the "undefined checks" near-miss
  proved why). (2026-07-18.)
- Reveal label template is generated, not per-beat bespoke: "The paper trail — where
  {claim} comes from"; beat 4 (the held pause) renders the quietest variant, "The paper
  trail." — identical placement/size everywhere. "Paper trail" is lore's one sanctioned
  bridge word into the archive conceit. (2026-07-18.)
- Guard honesty is voice law, not just data law: a check badge appears only where the
  check asserts the displayed number; derived/unguarded claims say so in plain words.
  The honest third act (some numbers are guarded offline only) is part of the story,
  not a footnote to hide. (2026-07-18.)
- Every provenance/severity string derives from `DATA.provenance`, pytest-verified
  against real Dagster definitions; check rationales are verbatim checks.py
  descriptions. Copy in the reveals is projection, never authorship. (2026-07-18.)

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
  may reveal the trio before beat 5. Re-audit whenever provenance strings change.
  Audit history: 2026-07-17 PASS (no check named the trio). 2026-07-18 re-run after
  commit 082d9c9: **FAIL on beat 4** — `character_stats_six_film_trio` (label
  "six-film trio"; hover why names C-3PO, R2-D2, Obi-Wan Kenobi verbatim) renders in
  beat 4's paper trail, because beats 4–6 share the character_stats chain and chainEl
  shows every check on every asset in the chain. Mitigated (opt-in details, hover for
  the names) but the label alone gives away "three saw all six" inside the held pause,
  one beat before the payoff. Flagged to the panel; fix is not mine to write.
- The held pause is beat 4 (the cameos). Any affordance living inside the pause must be
  the quietest voice on the page — the pause's job is to set up beat 5.
- Reveal micro-story structure: claim → machinery (vertical chip chain, one gold `.hot`
  seat on the beat-relevant asset) → guard (◆ blocks / ◇ warns + one-line rationale) →
  honesty line. A bare chain is a diagram, not a beat.
- `raw_people` opens every chain, so the census's best-guarded numbers (shape blocking,
  82-count warn) recur in all six reveals — the structural reason beat 0 could stay
  clean without losing the hiring-manager's scannability concern.
- Beats 4–6 are `relation:"direct"` since commit 082d9c9: they ride the
  raw_people → star_wars_db → character_stats chain with `guard.kind:"check"` (four
  WARN drift checks: 42-of-82, the trio, 19-of-82, maxFlown 5). Their honesty lines
  now render from the NOTE.check template — "The figure is asserted in the pipeline
  itself by the {ref} check." The old derived-tally wording survives only as the
  unused NOTE.pytest derived branch; the honest-third-act line softened accordingly
  (guarded-offline-only now applies to fewer numbers, and beat 7's prose says "four
  transforms" truthfully).
- Dashboard: the lineage strip is the epilogue's establishing shot; per-card mini-DAGs
  were rejected unanimously — telling the gag eight ways.

## Banked: pipeline-reveal (2026-07-18)

Won:
- Beats 1–6 only; beat 0 untouched; beat 7 callback kept (over lore's cut) — my three
  core spine defenses all carried into law.
- Claim → machinery → guard micro-story shape adopted; rationale rides each badge.
- Beat 4 gets the quietest label; the held pause stays undisturbed.
- Honest third act embraced — hiring-manager independently argued honesty IS the hire
  signal, which made the honesty line a feature, not a concession.

Lost / adjusted:
- My prep leaned toward per-beat bespoke in-voice labels ("Check the paperwork — where
  23 of 82 comes from"). The panel chose ONE generated template with a single bridge
  word ("paper trail"), all other strings projected from provenance. Right call: my
  "six pipelines" callback instinct was arithmetically false (lore caught it) — proof
  that hand-authored pipeline copy drifts. Voice now lives in the template and the
  conceit, not in per-instance wording.
- "Inline SVG diagram" became HTML `.chip` elements, vertical — implementation was
  never mine, and vertical chains read top-down like a manifest, which suits the
  archive voice better anyway.

Prep differently next time:
- When proposing callbacks that cite counts, verify the arithmetic against the actual
  defs before debate — or propose them as computed-from-data from the start.
- My open question (open-reveal vs 64svh station interaction) resolved via ux's
  bottom-anchored placement; when I flag a pacing hazard I can't verify, name the role
  whose lever fixes it in the same breath — it landed better as a joint concern.

Watch items for future panels:
- If the per-character transform ships, beats 4–6 honesty lines change — the reveal
  copy must be re-projected, and the trio leak audit re-run on any new check names.
- README rewrite reorders the project's front door; the site's story arc is unchanged,
  but any future README storytelling should mirror the census conceit, not invent a
  second voice.
