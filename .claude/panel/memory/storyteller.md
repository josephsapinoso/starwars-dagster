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
  and arithmetically true (currently thirteen checks after 2aa845e). Never hand-write
  pipeline arithmetic into copy; the number-word list is drift-guarded against overflow
  (the "undefined checks" near-miss proved why). (2026-07-18.)
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
- **Spoiler pin law** (post-landing cleanup, 2026-07-18): a standing offline test
  derives payoff term sets from `known_facts` — names AND payoff numbers,
  phrase-anchored — and asserts no check string renders on a beat earlier than its
  claim's reveal. Every new check passes this audit before landing, and the pin must
  be seen to fail before merge. My one-off leak audits are retired into this test.
- **The rail is uniform; spoiler safety lives in the strings, not the renderer.**
  Every beat renders the same rule (all checks of its chain assets). No beat-indexed
  filtering — a `beat` field would be hand-authored narrative metadata pytest cannot
  verify. Corollary: DATA.provenance carries no narrative fields, ever. (2026-07-18.)
- **Description style rule** (technical-writer's, I enforce the story half): check
  descriptions state the invariant and its stakes; run metadata carries the
  particulars; known_facts.py is the only roster/number home. No check string quotes
  another beat's caption or payoff. (2026-07-18.)

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
  may reveal the trio before beat 5. Audit history: 2026-07-17 PASS; 2026-07-18 FAIL
  (four forward leaks via the shared character_stats/characters_enriched chains —
  the trio, "19 pilots", "max flown = 5", "23 unweighed" all rendered early); fixed
  in 2aa845e via re-authored strings (labels now "all-six set" / "pilot census" /
  "flight record" / "mass baseline" — invariant-subject, number-free, name-free).
  The audit is now the standing spoiler pin test; manual re-audit only for strings
  the pin cannot derive from known_facts (new payoff *concepts*, not new numbers).
- The held pause is beat 4 (the cameos). Any affordance living inside the pause must be
  the quietest voice on the page — the pause's job is to set up beat 5.
- Reveal micro-story structure: claim → machinery (vertical chip chain, one gold `.hot`
  seat on the beat-relevant asset) → guard (◆ blocks / ◇ warns + one-line rationale) →
  honesty line. A bare chain is a diagram, not a beat.
- `raw_people` opens every chain, so the census's best-guarded numbers (shape blocking,
  82-count warn) recur in all six reveals — the structural reason beat 0 could stay
  clean without losing the hiring-manager's scannability concern.
- Beats 4–6 are `relation:"direct"` since commit 082d9c9: they ride the
  raw_people → star_wars_db → character_stats chain with `guard.kind:"check"`
  (WARN drift checks under the re-authored spoiler-safe labels). Honesty lines
  render from the NOTE.check template — "The figure is asserted in the pipeline
  itself by the {ref} check." Beat 1 flipped pytest→check the same way in 2aa845e
  (`characters_enriched_unknown_height_baseline`), zero hand edits both times.
  Pipeline now carries 13 checks (4 blocking, 9 warn); WORDS list runs through
  "thirteen".
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

## Prep notes: post-landing cleanup (2026-07-18) — compacted after banking

Full leak audit found four forward leaks (trio in the held pause; pilots count and
max-flown punchline two beats early; "23 unweighed" one beat early — the last one
the brief missed, proving the problem structural). All four fixed in 2aa845e; the
audit method survives as skill rule 8 and the standing spoiler pin test. My fix
ranking (filter > re-author > accept) was adjudicated and my top pick lost — see
Banked below for why my "(a) cannot fix the core leak" claim was wrong.

## Banked: post-landing cleanup (2026-07-18, decision log 2026-07-18-post-landing-cleanup.md; commits c0b97e0, 2aa845e)

**Q1 — my mechanism lost 5–3–1; my audit won everything it was for.** The
cumulative-rail (beat-indexed clearance) proposal fell to two arguments I should
have pre-empted: the one-home law (the trio description hand-listing the roster
was a drift bug against known_facts.py regardless of spoilers — the fix was owed
anyway) and qa's kill shot, that a `beat` field is hand-authored narrative
attribution pytest cannot verify, sitting inside the one object whose credibility
is "everything here is machine-checked." Sequencing lost to string-fixing because
placement filtering required buying spoiler safety with an unverifiable field —
and I of all people should not trade verified provenance for pacing. My prep
claim that "re-authoring cannot fix the core leak because the check's meaning IS
the payoff" was simply wrong: I conflated operational meaning with rendered
phrasing. "All-six set" states the invariant's subject without its count;
"flight record" without its punchline. I never drafted the counterexample label
before declaring it impossible. That is the lesson.

What won, and it is the part that mattered:
- All four leaks fixed, including the "23 unweighed" leak only my audit caught.
- My meta-leak companion edit landed verbatim — no checks.py string quotes
  another beat's caption ("'Ben counts' beat" and "punchline of the pilots beat"
  are gone); now law via the description style rule.
- My "make the law executable" demand IS the remedy's spine: the standing
  spoiler pin, and my objection to qa's names-only version carried — the pin
  derives names AND payoff numbers from known_facts, seen-to-fail before merge.
  My one-off audit is honorably retired into a test.
- Must-have #3 achieved: the held pause carries no beat-5/6 string on any
  surface. The hook, beat sheet, "n / 8", and held pause are untouched.

**Q3a played out exactly as predicted:** beat 1's honesty line flipped
pytest→check through the NOTE template with zero hand edits — third data point
for generated-over-bespoke. **Q2** landed engineer's shape; displayed-SQL-is-
executed-SQL is now an extension of guard-honesty voice law, no beat copy touched.

Prep differently next time:
- Before pitching a mechanism, ask whether it adds any authored field the
  existing verification surface cannot check. If yes, the panel will (rightly)
  kill it; find a strings-side path first.
- Before declaring a string fix impossible, draft the best possible string —
  steelman the re-author option by actually writing the label. If the invariant's
  *subject* can be named without its *payoff*, re-authoring works.
- When my audit finds a leak the brief missed, lead with it: "structural, not
  one bad string" was my strongest evidence and I buried it at severity 4.

Watch item: screenshot retake now targets 13 green checks; any future check's
strings pass the spoiler pin at birth — that is enforcement, not debate.
