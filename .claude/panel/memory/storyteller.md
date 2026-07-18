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
- README rewrite reorders the project's front door; the site's story arc is unchanged,
  but any future README storytelling should mirror the census conceit, not invent a
  second voice.

## Banked: per-character transform landed (2026-07-18, commit 082d9c9)

Execution note, no debate — the pipeline-reveal open item shipped as banked. What
changed in my domain:

- Beats 4–6 upgraded derived → direct exactly as my watch item predicted; honesty
  lines re-projected via the NOTE.check template automatically — the template law
  (voice in the template, strings from provenance) paid off: zero copy hand-edits
  were needed for the flip. Bank this as evidence for generated-over-bespoke.
- The beat-7 callback now truthfully computes "One pipeline, four transforms, twelve
  checks", and two latent hazards I care about were fixed en route: the number-word
  list stopped at "nine" (would have rendered "undefined checks") and hardcoded
  "three transforms" prose. Lesson re-confirmed: every count in copy must be computed
  AND its rendering path drift-guarded, including the word list itself.
- My mandated re-audit found the one thing execution missed: the new
  `character_stats_six_film_trio` check leaks the trio into beat 4's paper trail
  (details in Working knowledge). The audit-on-string-change rule earned its keep;
  raise this at the next panel touchstone rather than relitigating the reveal design.
- Beat count, "n / 8", beat sheet, held pause: all untouched — spine intact.

Prep differently next time: when a shipped check exists to guard a *reveal* beat, ask
in prep whether its name/label/description can appear on any *earlier* beat's chain —
shared-chain rendering means a check's blast radius is every beat that cites its
asset, not just its own.

Still open upstream: dashboard SQL strings; README screenshot retake (12 green checks).

## Prep notes: trio-leak blast radius + SQL/coverage story stakes (2026-07-18)

Full cross-beat audit of chainEl (index.html:823-843) against the DATA.provenance
literal (line 390) and checks.py descriptions. A check renders on EVERY beat whose
chain contains its asset; hover `why` = verbatim description.

Leak table (severity order):
1. **Beat 4 rail → "six-film trio"** (label states three-saw-all-six; hover names
   C-3PO/R2-D2/Obi-Wan AND quotes "the 'Ben counts' beat" — the beat-5 caption
   itself). Inside the held pause, one beat before THE payoff. Critical.
2. **Beat 4 rail → "19 pilots" + "max flown = 5"** — beat 6's number and punchline
   two beats early; max-flown hover names Obi-Wan ("punchline of the pilots beat"),
   a double leak (he's also a witness). High.
3. **Beat 5 rail → same two labels** one beat before beat 6. Moderate (post-payoff
   slope, but still front-runs the Obi-Wan punchline).
4. **Beat 1 rail → "23 unweighed"** — beat 2's absence-beat number one beat early
   (characters_enriched carries it; beats 1-3 share that chain). Mild: beat 2's
   power is framing more than surprise, and the label lacks the denominator. The
   brief missed this one — it proves the problem is structural, not one bad string.
Clean: "homeworld joins" before beat 3 (no numbers); all backward-looking renders;
beat 6 rail; structural check labels everywhere.

Fix ranking by cost to the spine:
- **(b) per-beat rail filtering — my pick, near-zero spine cost, positive side
  effect.** Hide on beat N any check that is the guard.ref of a claim with
  beat > N (derivable from DATA alone: kills leaks 1, 3, 4 and the trio hover).
  max_flown guards no claim, so the rule needs one small data hook — e.g. an
  optional per-check `spoilerBeat`/earliest-beat field in DATA.provenance.assets —
  to catch leak 2. Bonus: beat 4's rail drops from four WARN chips to one, making
  the held pause's affordance genuinely the quietest on the page (currently it's
  the noisiest rail). Guard: drift detector + pytest assert no future-beat guard
  check ever renders early — my one-off audit becomes a standing spoiler guard.
- **(a) re-author label/description — cannot fix the core leak.** The check's
  operational meaning IS "exactly three saw all six"; any accurate label/description
  states it. Re-authoring only mutes hover meta-leaks (naming beats/punchlines),
  and those phrases are good ops copy in the Dagster UI. (a) alone = lobotomize the
  check or keep the spoiler. Acceptable as a light companion (drop the literal
  "Ben counts"/"punchline" phrasings) but not as the fix.
- **(c) accept — reject.** Opt-in + hover mitigation doesn't cover the label, and
  the worst seat in the house (held pause) hosts the worst spoiler. Three of six
  reveals leak forward; "mitigated" is not a pacing strategy.

Q2 (SQL-in-DATA + executed-fixture pytest): no beat copy touched; disclosure text
becomes provably true — supports it as an extension of guard-honesty voice law.
Watch only that the drift-detector claim, if added, stays console-silent for readers.
Q3a (height WARN check): flips beat 1's honesty line pytest→check via the NOTE
template automatically — zero hand edits, restores beat 1/beat 2 symmetry; the new
label ("1 unmeasured" or similar) is beat 1's own claim, so it renders forward-clean
on beats 2-3. No spoiler risk; I'm for it. Q3b (galaxy_report structural check):
epilogue-side, no rail renders it; pure hiring-manager/qa territory — neutral,
defer, but insist any new check's label/description pass the spoiler audit before
landing (feature + guard same commit should include the spoiler guard).

Cannot verify: how a filtered rail reads at 390px with the drop (headless geometry
was checked pre-fix); whether Dagster-UI copy edits under (a) matter to
hiring-manager's lineage-view story — his call, not mine.
