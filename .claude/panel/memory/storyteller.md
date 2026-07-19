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
  and arithmetically true. Never hand-write pipeline arithmetic into copy; the
  number-word list is drift-guarded against overflow (the "undefined checks" near-miss
  proved why). (2026-07-18; WORDS now runs through "fifteen".)
- Reveal label template is generated, not per-beat bespoke: "The paper trail — where
  {claim} comes from"; beat 4 (the held pause) renders the quietest variant, "The paper
  trail." — identical placement/size everywhere. "Paper trail" is lore's one sanctioned
  bridge word into the archive conceit. (2026-07-18.)
- Guard honesty is voice law, not just data law: a check badge appears only where the
  check asserts the displayed number; derived/unguarded claims say so in plain words.
  The honest third act is part of the story, not a footnote to hide. (2026-07-18.)
- Every provenance/severity string derives from `DATA.provenance`, pytest-verified
  against real Dagster definitions; check rationales are verbatim checks.py
  descriptions. Copy in the reveals is projection, never authorship. (2026-07-18.)
- **Spoiler pin law** (2026-07-18): a standing offline test derives payoff term sets
  from `known_facts` — names AND payoff numbers, phrase-anchored — and asserts no check
  string renders on a beat earlier than its claim's reveal. Every new check passes this
  audit before landing, and the pin must be seen to fail before merge. Extended
  2026-07-19 with the registry payoffs: 896 / Yoda / 39-of-82 banned on all story
  rails, verified seen-to-fail.
- **The rail is uniform; spoiler safety lives in the strings, not the renderer.**
  Every beat renders the same rule (all checks of its chain assets). No beat-indexed
  filtering — a `beat` field would be hand-authored narrative metadata pytest cannot
  verify. Corollary: DATA.provenance carries no narrative fields, ever. (2026-07-18.)
- **Description style rule** (technical-writer's, I enforce the story half): check
  descriptions state the invariant and its stakes, subject-only, number/name-free; run
  metadata carries the particulars; known_facts.py is the only roster/number home. No
  check string quotes another beat's caption or payoff. (2026-07-18; reaffirmed
  2026-07-19 for both registry checks, which rail on beats 4–6.)
- **Quoted-testimony rule** (2026-07-19): external claims (dialogue, canon) may be
  AUDITED in copy but never rendered as site-derived data; derived numbers come only
  from DATA. The quoted figure appears only while the record still agrees — the line
  renders data-conditionally on the exact facts it audits, and disappears rather than
  lie. Shipped instance: the Yoda line ("…his own count, nine hundred years, checks
  out.") renders only inside `if (oldest.name === "Yoda" && oldest.bby === 896)`;
  no derived ~900 exists anywhere.
- **The coda** (2026-07-19): shipped verbatim and is now fixed copy — "The census is
  filed. Nothing here is sealed — every figure above traces to a record, and every
  record is open to a second reading." + re-read anchor "Take the census again ↑"
  looping to #story. Placement: inside main, after the final dashboard grid; the
  footer stays footer. The coda is number/name/payoff-free BY DESIGN — that property
  (not the wording) is pinned by `test_the_coda_stays_number_free`.
- **Absence pins are legitimate guards** (2026-07-19): an element exempted from a
  detector by a property gets a pin asserting that property; pinning wording is
  theater.
- **Audit-canon motif is capped at two uses** — copy that audits a canon claim against
  the filed record. The Yoda line is the second and LAST use; a third would turn a
  motif into a tic. (2026-07-19, my ruling, adopted.)
- Two-register law holds at the repo boundary: the records-office voice lives on the
  site only; README (including "Limits, by design") stays engineering register.
  (2026-07-19.)

## Working knowledge

- The beat sheet (8 beats, site/index.html ~237–296):
  0 census hook (all 82 as dots) → 1 the measuring (heights) → 2 the weighing (mass +
  the 23 unweighed — absence as story) → 3 the hometowns (origins) → 4 the cameos
  (most appear once) → 5 the witnesses (**payoff: three saw all six films — C-3PO,
  R2-D2, Obi-Wan**) → 6 the pilots → 7 the handoff (dots filed away → dashboard).
- The arc is a census-archive conceit: measurement → absence → origins → persistence →
  handoff to the "records office" (dashboard), now closed by the coda's loop back to
  the hook. Additions must serve this spine or a deliberate second read-through.
- The witnesses payoff must not leak early. Leak history: 2026-07-17 PASS; 2026-07-18
  FAIL (four forward leaks via shared chains; fixed in 2aa845e with invariant-subject
  labels — "all-six set" / "pilot census" / "flight record" / "mass baseline"). The
  audit lives on as the standing spoiler pin test; manual re-audit only for payoff
  *concepts* the pin cannot derive from known_facts.
- The held pause is beat 4 (the cameos). Any affordance inside the pause must be the
  quietest voice on the page.
- Reveal micro-story structure: claim → machinery (vertical chip chain, one gold
  `.hot` seat) → guard (◆ blocks / ◇ warns + one-line rationale) → honesty line from
  the NOTE.check template. A bare chain is a diagram, not a beat.
- `raw_people` opens every chain, so the census's best-guarded numbers recur in all
  six reveals — the structural reason beat 0 could stay clean.
- Pipeline carries 15 checks (4 blocking, 11 warn) after the registry's two WARN
  checks (birth-year baseline + parse-honesty). Beats 1 and 4–6 are `guard.kind:
  "check"`; every pytest→check flip has re-projected honesty lines with zero hand
  edits (three data points for generated-over-bespoke).
- Birth registry (2026-07-19): `#card-registry` in the dashboard's Census section —
  part-to-whole bar (39 undated as faint tint) + dot strip, Yoda gold-ringed (the
  ring means "extreme"), Jabba labeled, BBY gloss printed not tooltipped. Coda at
  site/index.html ~395–398; Yoda conditional line ~1371–1375.
- Dashboard lineage strip is the epilogue's establishing shot; per-card mini-DAGs were
  rejected unanimously — telling the gag eight ways.

## Banked: pipeline-reveal + per-character transform (2026-07-18, compacted)

Won: beats 1–6 only, clean hook, beat-7 callback, micro-story shape, quietest label on
the pause, honest third act (hiring-manager independently argued honesty IS the hire
signal). Lost: bespoke in-voice labels → ONE generated template; my "six pipelines"
callback was arithmetically false (lore caught it) — proof hand-authored pipeline copy
drifts. Voice lives in the template and the conceit, not per-instance wording.
Execution (082d9c9) confirmed the template law: beats 4–6 flipped derived→direct with
zero copy edits; my mandated re-audit caught the trio leaking into beat 4 — a check's
blast radius is every beat that cites its asset, not just its own.

## Banked: post-landing cleanup (2026-07-18, decision log 2026-07-18-post-landing-cleanup.md; c0b97e0, 2aa845e)

My cumulative-rail mechanism lost 5–3–1, correctly: placement filtering bought spoiler
safety with an unverifiable hand-authored `beat` field, and the trio roster in a check
description was a one-home-law drift bug owed a fix regardless. My prep claim that
"re-authoring cannot fix the core leak" was wrong — I conflated operational meaning
with rendered phrasing and never drafted the counterexample label before declaring it
impossible. What won: all four leaks fixed (including the "23 unweighed" leak only my
audit caught); the meta-leak companion edit verbatim; the standing spoiler pin with
names AND numbers (my objection to the names-only version carried); the held pause
cleared of beat-5/6 strings. Lessons now in skill rules 9–10: draft the best possible
string before declaring string-fixes impossible; never add an authored field the
verification surface cannot check; lead with the evidence that a problem is
structural, not one bad string.

## Banked: birth registry, coda, hue enforcement (2026-07-19, decision log 2026-07-19-birth-registry-and-polish.md; commits 1f3cf9e, 4d92cb7, f170379)

Won — a clean sweep in my domain, all now promoted to Settled above:
- The coda shipped VERBATIM with ux's mechanics; placement after the final grid held;
  the footer stayed footer. The digits-pin stood 5–3, framed exactly as my
  absence-assertion argument (qa concurring: the pin guards the exemption's premise,
  not the content — wording pins are theater).
- The quoted-testimony rule is banked law and governs the shipped Yoda line: quoted
  canon audited in copy, rendered only while the record agrees, no derived ~900
  anywhere. Lore supplied the gem (896 + 4 = 900, Yoda's own RotJ count); my framing
  decided HOW it could appear. Steelmanning another role's material into my register
  beats vetoing it.
- Audit-canon motif capped at two uses, the Yoda line being the second and last.
- Both new check descriptions subject-only and number/name-free at birth; spoiler
  terms extended with the registry payoffs, seen-to-fail. The pin law is doing its
  job as enforcement, not debate.
- Spine untouched: 8 beats, "n / 8", one held pause, no new story-side beats — the
  registry landed as a dashboard card, exactly where a post-payoff census addendum
  belongs. The records-office voice stayed out of the README per two-register law.

Lost: nothing this round. Caution for future me: a sweep is a reason to check harder
for anchoring next debate, not evidence my instincts need less scrutiny.

Prep differently next time:
- When the deliverable is words, draft the FINAL copy at prep time, not a shape —
  verbatim adoption of the coda was only possible because the exact lines were on the
  table before debate. "I'll write it after we agree" forfeits the strongest argument
  a storyteller has: the text itself.
- When canon offers a number the data cannot derive, reach for quote-and-audit before
  reaching for exclusion — the pattern converts a spoiler/drift risk into voice.

Watch items:
- The Yoda line's data-conditional render is the quoted-testimony rule's enforcement
  half; any future copy edit that unconditionalizes it is a law violation, not a
  style choice.
- The coda is the ONLY post-grid narrative element. Future panels will be tempted to
  append more closing prose there; the frame closes once.

## Prep notes: token hygiene + raise-only type consolidation (2026-07-19)

Verified in site/index.html: token block lines 8–31 (the four "off-token" hexes in the
designer's old ledger ARE tokenized — --tip-bg/--axis/--cyan/--sql-ink); remaining
literals are JS-only (#cdd8ef starfield fill ~489, #fff gender %-label ~1131). No stale
notes of mine touched by this brief — my Yoda-line and coda line refs still match.

Core prep finding — voice lives in register markers, not half-pixels: every small-type
voice on this page is carried by case, letterspacing, color tier (ink-2/ink-3/gold),
and family (disp/mono/body), with size as the fourth cue. So raise-only merges are
narratively safe wherever the register markers survive. Voice pairs that MUST survive
consolidation: aside < body (13.5→14 vs 16: fine, ink-3 does the whispering); crawl
pre < crawl h4 (13 vs 14: both unchanged, hierarchy intact); .prov-check as the
quietest string on the rail (held-pause law) — it must stay BELOW the summary/legend
tier, so raising it to 12 flattens the one voice the pause depends on.

Debate positions:
- Merge map: 12.5→13 (kicker, stage-cap "n / 8", k-label, legend, cat-t?, prov-note,
  tip — all keep register via case/spacing/color); 13.5→14; 16.5→17; 10.5/11 CSS
  micro-labels (g-label, prov-legend) up to one fine-print tier.
- In-SVG chart lettering (axis-t/val-t/anno-t 11.5, JS small-anno 11, gender %-label
  11.5) is GEOMETRY, not typographic voice — collisions were historically fixed by
  staggering, never shrinking. Exempt it from the scale as an allow-list, and make the
  guard encode "stagger, never shrink/resize" as law.
- Guard (Q4): yes, one structural pytest in the existing suite; my ask is that the
  allow-list carries a reason string per exemption, so a future "just shrink the
  label" edit fails loudly.
- Colors (Q1): mostly designer's turf. My one stake: the hero's opening chord must
  not gain a runtime dependency — a getComputedStyle bridge for one never-reused
  star color adds an init failure mode for zero narrative gain; sanctioned literal
  with comment is fine. The SVG #fff label is class-able; no story stake either way.
- Font tokens (Q3): if tokens land, name the kept steps by ROLE/tier (fine-print /
  caption / sub / note), not by pixel — the scale then documents the voice hierarchy.
  Tokens only for kept steps; no story objection to skipping tokens entirely.
