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
- **The whisper clause** (2026-07-19, token-hygiene): every sanctioned style exception
  is an exact (selector, value, reason) pin in the guard, failing loudly on change in
  EITHER direction and printing its reason. Unexplained holes are theater; pinned
  exceptions are law. Shipped as `EXEMPT_SELECTORS` in test_site_style_hygiene.py.
- **`.prov-check` stays 11.5 — the whisper tier.** `details.prov summary` is 12 and
  `.chip` is mono 12; at 12 the guard voice merges into the machinery voice on the
  rail the held pause depends on. Pinned with reason "whisper tier — the held pause's
  authored contrast (Settled)". (4–2, 2026-07-19.)
- **Chart lettering is pinned geometry, not typography** (3–2): .axis-t/.val-t/.anno-t
  11.5, .cat-t 12.5, .seg-pct 11.5 (its `w > 46` gate is tuned to it). Collisions are
  fixed by staggering, never by shrinking; **raise-only grants permission, not
  obligation** — standing still needs no evidence, moving chart geometry does.
- **Scenery is not ink** (2026-07-19): decorative paints (aria-hidden canvas) may stay
  literals with a required sanction comment, counted exactly once; data ink must be
  tokenized. No runtime bridges for decoration — the hero's opening chord takes no
  init dependency for a one-use star color.
- **Ink adapts to its ground** (2026-07-19): on-mark labels choose ink per computed
  ground from the same array that drives the ground; every rendered pair ≥4.5:1,
  verified computationally. Never one ink that fails somewhere; never a new hex.
- **The style registry is the test** (5–1): the sanctioned type scale's one
  machine-readable home is the structural pytest (`SANCTIONED_SCALE`); no font-size
  tokens, no parallel lists.

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

## Banked: birth registry, coda, hue enforcement (2026-07-19, decision log 2026-07-19-birth-registry-and-polish.md; 1f3cf9e, 4d92cb7, f170379; compacted)

Clean sweep, all outcomes promoted to Settled above (coda verbatim + digits-pin 5–3
as my absence-assertion argument; quoted-testimony rule governing the Yoda line;
audit-canon motif capped at two; subject-only descriptions + spoiler terms extended;
spine untouched — registry landed as a dashboard card). Lessons carried forward: draft
the FINAL copy at prep time, the text itself is the strongest argument; reach for
quote-and-audit before exclusion when canon offers an underivable number; a sweep
means check harder for anchoring next debate. Watch: unconditionalizing the Yoda
line's data-gated render is a law violation, not a style choice; the coda is the ONLY
post-grid narrative element — the frame closes once.

## Banked: token hygiene + type consolidation (2026-07-19, decision log 2026-07-19-token-hygiene.md; a30a5bc)

Won — the whisper clause is the guard's architecture, and it carried both contested
holds:
- `.prov-check` 11.5 held 4–2 with my craft argument quoted as decisive (summary-12 +
  chip-mono-12 would swallow the badge voice on the held pause's rail). Note WHY it
  won: not "Settled says so" but the concrete adjacent-voices math. Precedent survives
  best when re-argued from the surface, not the statute.
- "Merge the prose, exempt the geometry" adopted as the whole Q2 shape (3–2 on chart
  lettering); all my voice-safe merges shipped verbatim (12.5→13, 13.5→14, 16.5→17,
  fine-print tier 11). Register markers (case/spacing/color/family) carried every
  merged voice, exactly as prep predicted.
- The scenery-is-not-ink split won the starfield question: my exact-pin shape ANSWERED
  the engineer's allow-lists-rot objection — a pinned entry that drifts fails the
  test, so the sanction can't rot silently. No bridge on the opening chord; the hook
  keeps zero new init dependencies.
- Q3 fell my way from the same root (5–1, no tokens): the executable test is the
  registry. My rule-6 token-naming prep was moot — right instinct (one home for the
  scale), wrong medium (I assumed the home would be CSS).

Lost: nothing outright; my "cat-t?" merge hedge resolved to exempt (12.5 pinned as
geometry), which was the better answer — I'd flagged it with a question mark for a
reason.

Prep differently next time:
- Bring the pin TABLE, not the pin idea. I argued for (selector, px, reason) shape;
  the adjudication still had to assemble which selectors and which reasons. Drafting
  the literal exemption list at prep time is the typescale equivalent of drafting the
  final copy — the text itself is the strongest argument.
- When two roles collide on a mechanism (bridge vs literal), check whether MY shape
  dissolves the objection before picking a side; the whisper clause turned a 3–3 split
  into a resolution, which is worth more than a vote.

Watch items:
- The pins now carry story rationale in executable form ("whisper tier — the held
  pause's authored contrast"). Any future edit to `.prov-check`'s size is a law
  violation surfaced by pytest, not a debate — point at the failing reason string.
- Ux's fixed-viewBox stage-legibility observation was noted for a possible FUTURE
  proposal with its own evidence. If it returns, raise-only-grants-permission puts
  the burden on the mover; the geometry pins are not an invitation.

## Prep notes: watchlist round (2026-07-19)

Verified in-source; narrative judgments formed for debate.

- **Q1 (badge whys).** `title=k.why` at site/index.html:879 is the page's only
  title attr. Whys are VERBATIM check descriptions (test_site_provenance.py:95)
  — already governed by the description style rule AND already inside the spoiler
  pin's audited surface (line 212 audits `label + why` per beat). So ANY exposure
  path is spoiler-safe by construction; no new pin needed. Voice stance: 48
  focusable badges = ~15 tab stops through the held pause's quietest voice; a
  visible disclosure triples rail length. Legend already routes honestly to the
  Dagster UI (settled copy). Lean accept-and-document; if exposed, mechanism is
  ia/ux's, my constraints: no new visible rail strings, nothing on beat 4 louder
  than its summary.
- **Q2 (Safari jump).** Reveal-arc rule 7: opening a reveal must never move the
  reader. The Safari jump violates it at the exact opt-in moment — so a toggle
  compensation is position-PRESERVING, not scroll-jacking. But: Chromium already
  compensates via scroll anchoring, so an unconditional scrollBy would
  double-compensate and break the verified-good browser; and we cannot verify
  Safari hardware here. Lean accept-and-watch unless someone brings an
  anchoring-aware shape; if built: instant, toggle-event-only, never during
  user scroll.
- **Q3 (touch flash).** Tooltip is deixis (dot→name), redundant with prose;
  spine survives its absence. Tap-to-pin is reader-paced (reader shows AND
  dismisses). Oppose suppress-for-touch — see cross-finding below.
- **Q4 (stage type).** viewBox 700×620 (line 327); .anno-name 12 (97), .axis-t
  11.5 (184). CRITICAL: beat 5's annos ARE the witnesses' names (line 693, hot
  gold), stacked at 20 viewBox-units spacing — a bump to the needed 20–22px makes
  the three payoff names OVERLAP. The naive css-only fix breaks precisely the
  payoff beat; stagger-never-shrink means any bump demands stagger rework. Prose
  carries every payoff name (beat 5 names the trio; beat 6 names Obi-Wan · 5),
  so annos are deixis, not delivery. Lean accept; burden on the mover includes
  the 20-unit collision math, per raise-only-grants-permission.
- **Cross-finding (Q3×Q4).** On mobile today, dot identity reaches readers by NO
  path (5px annos + no touch tooltip). Acceptable ONLY because prose is the
  payoff carrier — any "accept" verdict should state that reason. If exactly one
  targeted fix ships, legible beat-5 witness names is the highest narrative
  value on the page.
- Cannot verify: real Safari/iOS behavior; hardware touch event order.
