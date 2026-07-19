# UX Designer — Panel Memory

## Settled (do not relitigate)

- No auto-playing or time-gated intros, ever; reader-paced scroll only; no
  scroll-jacking. Content is never gated — disclosures are opt-in. (First design
  panel, PR #1/#2.)
- Scroll-snap was proposed for mobile beat alignment and **rejected for cause** as
  scroll-jacking. (Mobile beat-spacing panel, PR #4.)
- The viewport meta tag must stay: it was once missing and phones silently fell back
  to the ~980px desktop layout — none of the mobile CSS applied on real devices.
  (Mobile beat-spacing panel, PR #4.)
- Settled mobile story geometry: stage pinned at min(52svh, 480px) — never shrink it;
  cards dock top-anchored in min(64svh, 560px) stations at a constant station; exactly
  ONE authored pause (`.step--held`, 90svh) before the witnesses reveal; beat counter
  ("n / 8", NBSP-glued) rides the sticky stage caption. (Mobile beat-spacing panel,
  PR #4.)
- The site must handle reduced-motion, mobile, and the flat/auto-height-embed fallback
  (sticky can't engage there). (First design panel.)
- Provenance reveals (pipeline-reveal, 2026-07-18): beats 1–6 ONLY — beat 0 stays a
  clean hook, beat 7 gets a plain-text provenance-computed callback, never a fake
  disclosure. One disclosure style shared with `details.sql` (extended selector);
  summary hit area ≥44px for BOTH old and new summaries. Reveal is built statically at
  init at the bottom of each `.step-inner` — works unchanged in flat mode; no
  auto-open/close, no animation; reader-owned state survives scroll-away.
- Reveal body is a VERTICAL chain of real HTML `.chip` elements (not SVG, not
  horizontal): every node visible within the ~260px mobile budget, no overflow escape,
  text natively accessible; one gold `.hot` seat; ↓ connectors; check badges are
  monochrome shape-coded ◆ blocks / ◇ warns + visible text — never color-only status.
- Guard honesty is law: a check badge only appears where the check asserts the
  displayed number (or its denominator/structure, labeled); derived/unguarded claims
  say so in plain words. All strings derive from `DATA.provenance` (pytest-verified);
  the one-line strict-JSON `const DATA` format is load-bearing.
- Label template is fixed: "The paper trail — where {claim} comes from"; beat 4 (the
  held pause) renders the quiet variant "The paper trail." — identical placement/size
  everywhere.
- The provenance rail is UNIFORM (post-landing cleanup, 2026-07-18): every beat renders
  the same rule — all checks of its chain assets. Spoiler safety lives in the strings,
  never in the renderer; no per-beat filters, no beat-indexed reveal logic, no hidden
  counts. Labels must be safe on EVERY surface because the label is the entire touch
  and keyboard experience.
- Hover is a side channel, never a promise: `title` tooltips are desktop-plus
  enhancement only; legend/help copy must never instruct "hover ..." — instead it names
  the canonical non-hover home (settled legend text: "◆ blocking check · ◇ drift
  warning · full check descriptions live in the Dagster UI"). Corollary now proven
  twice: content NEVER lives only in a tooltip — the registry's BBY unit gloss prints
  in the card subtitle (2026-07-19).
- Displayed SQL is executed SQL: any SQL text on the site lives in DATA and is executed
  by the offline suite against the fixture warehouse. DATA.provenance carries no
  narrative fields. Spoiler pin law: a standing offline test derives payoff terms from
  known_facts and fails any check string rendering before its claim's reveal beat.
- **Fragment-navigation coda pattern (birth-registry panel, 2026-07-19):** the re-read
  affordance is a plain block-level `<a href="#story">` after the last dashboard grid
  (inside main, never in the footer); `display:block` padding yields a ~53px measured
  hit area; the target `#story` carries `tabindex="-1"` so fragment navigation
  verifiably moves focus (headless-tested); directional glyph is `aria-hidden`; no JS,
  no arrival animation (reduced-motion is a no-op by construction).
- **Absence pins are legitimate guards** (QA's ruling, now law): an element exempted
  from a detector by a property (e.g., the coda is number/name/payoff-free) gets a pin
  asserting that property; pinning WORDING is the theater. I objected and was wrong —
  see Banked 2026-07-19.
- **Keyboard parity for labeled marks:** every chart mark carrying a persistent label
  or annotation gets `tabindex="0"` + `aria-label` + focus-shows-tooltip (all six chart
  renderers now do this, site lines ~1070–1363); the table view stays the
  keyboard-canonical home (registry: all 43 dated rows).
- **Legend conversion beats sliver labels:** tiny segments never get tooltip-only or
  leader-line labels; the legend converts to matching swatches with name + count
  visible, summing to the on-chart total (gender: 82). Gold ring = "extreme" only
  (designer's law); named non-extremes get labels, never rings.
- **SVG text doesn't wrap:** any caption that can clip at 390px becomes wrapping HTML
  outside the SVG (testimony caption precedent, 2026-07-19); no horizontal overflow at
  390/360 is the verification bar.
- **Token hygiene laws (2026-07-19):** (a) *Whisper clause* — every sanctioned style
  exception is an exact (selector, value, reason) pin in `test_site_style_hygiene`,
  failing loudly on change in either direction; unexplained holes are theater.
  (b) *Scenery is not ink* — decorative paint (aria-hidden canvas) may stay a literal
  with a required sanction comment; data ink must be tokenized; no runtime bridges for
  decoration. (c) *Ink adapts to its ground* — on-mark labels pick ink per computed
  ground from the SAME array that drives the ground color, every rendered pair ≥4.5:1
  verified computationally; never one ink that fails somewhere, never a new hex; if no
  pairing passes, drop the on-mark label (legend/table already carry the data).
  (d) *The registry is the test* — the sanctioned type scale {11,12,13,14,17 + pinned
  exemptions} lives only in the structural pytest; no font-size tokens, no parallel
  lists. (e) *Raise-only grants permission, not obligation* — standing still needs no
  evidence; moving chart geometry does. `.prov-check` stays 11.5 (pinned): the badge
  voice must not merge with the 12px summary/chip machinery voice on the rail.

## Working knowledge

- Flat mode: `shouldFlatten()` auto-detects auto-height embeds; `?flat` forces it,
  `?scroll` forces scroll mode; `enterFlat()` renders each step's figure inline BEFORE
  `details.prov` (copy → figure → paper-trail order). Any new per-step element must
  work in both modes. Flat mode shows all beats at once, so spoiler fixes belong in
  strings built at init, never in scroll-aware rendering.
- Reduced motion: a CSS block kills all transitions plus JS guards on the starfield;
  ship new components static-first so there is nothing to gate.
- Native `<details>/<summary>` is the accessibility-cheapest disclosure; touch targets
  ≥44px on summaries/toggles at 360px width; step cards ~44ch.
- Desktop steps are center-flex (`align-items:center`, min-height min(102svh,880px)):
  content growth re-centers the card and can shift a clicked summary UP. Mobile
  stations are top-anchored, growth is downward. Mitigation: expandables live at the
  bottom of `.step-inner`; real-device scroll-anchoring check still open.
- Stepper is height-agnostic (IO at rootMargin -45%); station min-heights are minimums
  — grown steps just add reader-paced scroll. Never shrink the stage to make room.
- Width budget: at 360px viewport ≈260px of card content; page body never scrolls
  horizontally, only dedicated containers (`.dag` strip) may `overflow-x:auto`.
- Baseline hygiene shipped 2026-07-19: doctype + `<html lang="en">` present; story has
  a visually-hidden h2 and each beat kicker is a real `<h3>` — the heading outline gap
  from my survey is closed. Protect these; they are easy to lose in a rewrite.

## Banked: pipeline-reveal + post-landing (2026-07-18, compacted)

- Won: vertical HTML `.chip` chain (260px budget argument); beats 1–6 with beat-0
  clean; legend rider verbatim (no "hover ..." promises); touch-surface analysis
  (label IS the whole touch/keyboard experience) shaped the winning labels.
- Lessons: show where a resisted affordance's need is already served; check plain
  HTML can render an artifact before designing ARIA for a graphic; measure at 260px
  before debate; verify the brief's beat→asset map myself (it was partly false);
  cost the string fix before any renderer fix and draft exact strings in prep;
  riders on other roles' proposals evaporate with them.

## Banked: birth registry, coda, hue enforcement (2026-07-19, compacted)

- Won: coda mechanics shipped exactly as filed (promoted to Settled as the
  fragment-navigation pattern); no-tooltip-content law survived its first offensive
  test (BBY gloss prints in the subtitle); keyboard parity landed wider than my ask
  (all six renderers, not just registry dots — the improvement-survey scatter gap
  closed); sliver protection via legend conversion; testimony-caption clipping caught
  in-flight → "SVG text doesn't wrap" rule.
- Lost, rightly: I called the coda digits-pin theater. QA's distinction stands —
  pinning a PROPERTY (stays number-free, the premise of its detector exemption) is an
  honest absence assertion; pinning WORDING would be theater. Before objecting to a
  guard, name the exact property it asserts; my own guard-honesty law WANTS such pins.
- Prep lesson (my highest-yield yet): the fresh-eyes improvement survey doubling as
  prep — file:line findings became shipped fixes without spending debate capital.
  Keep auditing the artifact between debates and file findings with line numbers.

## Banked: token hygiene + raise-only type (2026-07-19, commit a30a5bc)

**Won:**
- AA-fix-ships-this-pass carried, and got BETTER than my proposal. My prep found the
  live defect (white 11.5px on --s1 ≈3.6:1) and I said "white at 12px is not on the
  menu" — correct. But my remedy (single dark ink) was refined by the orchestrator's
  math: NO single ink passes both labeled segments (--void ≈5.5:1 on full s1 but
  ≈3.7:1 on the 75% tint; --ink ≈4.8:1 on the tint but fails full s1). Landed:
  `.seg-pct` class with per-rank ink from the same ladder index that drives segment
  color (site ~98, ~1131–35). Lesson: when proposing an ink, run the contrast pair
  for EVERY ground it can sit on, not the worst one I happened to check.
- Dead 11px attr deleted with its inert small flags — the JS-attr-precedence find was
  pure prep yield. JS-scan requirement shipped in the guard (shared must-have with
  the analyst; a JS-blind guard would have missed all four literal residues).
- Headless 360/390 re-verify ran pre-merge: no overflow, kickers fit, rails wrap,
  seg-pct inks confirmed rendering var(--void)/var(--ink), zero drift warnings.

**Lost:**
- `.prov-check` 11.5→12 (4–2). The storyteller's craft argument beat my
  retire-the-exception tidiness: summary is 12 and chips are mono 12, so a 12px badge
  merges the guard voice into the machinery voice on the held pause's rail. The
  whisper clause converts the exception from a hole into a pinned law, which answers
  my real objection (unauditable exemptions) better than erasing it. Lesson: my
  target was the HOLE, not the size — when a pin can make an exception loud and
  testable, retiring it buys nothing.
- Chart-lettering raises (3–2): exempted as a pinned geometry tier. Fair — the
  collision/gate evidence burden was real and unfunded, and raise-only grants
  permission, not obligation. My fixed-viewBox stage-legibility find (stage text
  renders ×~0.69 on the 480px mobile stage; 12px ≈ 8.2px effective) is logged as a
  possible FUTURE proposal needing its own evidence. → Watchlist.

**Prep differently:** cost my own remedies with the same rigor I cost others' — the
adaptive-ink refinement was one contrast multiplication away from being MY proposal.
And when defending a raise that retires a settled exception, check first whether the
exception is load-bearing craft (voice separation) rather than accumulated debt.

**Durable working knowledge kept:** six dashboard charts measure `viz.clientWidth`
(true CSS px, verify at 360); stage svg is fixed 700×620 viewBox (scaled text). Rail
density at 360 verified: chips wrap one per row inside a 244px rail, summaries
46–64px ≥44px target; sole cosmetic note is mid-word overflow-wrap of the long check
ref "character_stats_one_film_baseline" — acceptable, revisit only if user-facing
prose starts breaking. Gender label gate `w > 46` untouched (label size stayed 11.5).

**Watchlist (carried + new):** real-device AT exposure of `title` on check badges;
desktop center-flex scroll-anchoring jump on reveal open; stage-dot tooltip flash on
touch tap; NEW — stage viewBox legibility raise (own evidence pass: viewBox-relative
collision check, mobile effective-size table, before/after at 480px stage cap) if I
choose to fund it.

## Prep notes: watchlist round (2026-07-19)

All four E-claims verified at source; three brief-corrections and two proposal
shapes found.

- **Q1 (badge whys).** site:879 verified — sole title attr, zero focus/aria; the
  visible label + "◆ blocks/◇ warns" stands alone. Brief's "number-free" is WRONG:
  whys carry numbers ("82 people", "42 of 82 … exactly one film" — the beat-4
  payoff verbatim). But it's spoiler-safe by ASSET TOPOLOGY: character_stats (which
  owns that check) first enters a chain at beat 4 (beats 1–3 chain
  characters_enriched); and the spoiler pin ALREADY scans `label + why`
  (test_site_provenance.py:211–215; terms for beats 2/5/6/7). So exposing whys adds
  no new spoiler surface. Real exposure cost is elsewhere: whys are 113–213-char
  prose and the shared tooltip is a chip model (name + value rows) — prose doesn't
  fit it; visible rail text would bloat the whisper tier. Whys are verbatim
  spec.description projections (test:95), so the settled legend's canonical home
  (Dagster UI) genuinely holds this exact text. Lean: accept-and-document, trigger
  = any why gaining load-bearing content with no non-hover home.
- **Q2 (Safari jump).** Mechanism verified (desktop center-flex, min(102svh,880px);
  reveal ≈360px → 180px half-shift; Chromium anchoring absorbs it). Proposal shape
  banked: browser-neutral delta compensation — record clicked summary rect.top on
  summary `click` (fires pre-toggle), compare on `toggle`, `scrollBy(0, delta)` if
  |delta|>1. Self-noops where anchoring works AND on top-anchored mobile; instant,
  once per user action — anchoring restoration, not scroll-jacking. Cheap
  verification path: Playwright WebKit genuinely lacks scroll anchoring — reproduce
  the jump AND verify the fix headlessly before shipping. Accept+watch is also
  honest if nobody funds the WebKit pass.
- **Q3 (touch flash).** 770–782 verified: svg-level pointermove hit-test, no
  pointerType handling. Lean suppress-for-touch (`if (e.pointerType==="touch")
  { tipHide(); return; }`): the flash is a glitch, not a feature gap — stage
  tooltips are enrichment; dashboard marks below carry full data with focus parity,
  and keyboard users already get no stage-dot tooltips (accepted state). Tap-to-pin
  costs a state machine + dismissal design + scroll-gesture risk for redundant
  content.
- **Q4 (stage legibility).** Sizes verified (.axis-t 11.5 → 5.1px eff @360; scale
  .446). KILLER FACT the brief missed: the witnesses stack (site:693) spaces three
  hot anno names 20 viewBox units apart — declared font must stay ≲18 to keep any
  gap, capping mobile effective size at ~8.0px @360, BELOW the 9–10px target. A
  media bump cannot deliver its promise without re-authoring anno geometry (a
  viewBox rework — unfunded). Also `.axis-t` is shared with the six measured-px
  dashboard charts, so any bump must scope to `#stageSvg` AND flat-mode `.step-fig
  svg` or it inflates legible desktop-regime text. Redundancy verified line-by-line:
  every anno + caption fact prints in beat copy/asides (Yoda 66, Poof, Jabba 1,358,
  23 unweighed, Naboo 11/Tatooine 10, witness names, Obi-Wan · 5). Lean:
  accept-and-document; trigger = any future anno carrying content NOT in the copy.
