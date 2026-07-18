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

## Working knowledge

- Flat mode: `shouldFlatten()` auto-detects auto-height embeds; `?flat` forces it,
  `?scroll` forces scroll mode; `enterFlat()` renders each step's figure inline. Any
  new per-step element must work in both modes.
- Reduced motion is handled by a CSS block that kills all transitions plus JS guards
  on the starfield; new components should ship static-first so there is nothing to
  gate.
- Native `<details>/<summary>` is the accessibility-cheapest disclosure: keyboard
  focusable and toggleable for free, no ARIA wiring beyond labels on graphics.
- Touch targets: summaries and toggles need comfortable hit areas at 360px width; the
  step cards are constrained to ~44ch.

## Prep notes: pipeline-reveal (2026-07-17)

Verified in `site/index.html` for the per-beat provenance reveal:

- **Desktop growth-jump risk.** Steps are `display:flex; align-items:center` with
  `min-height:min(102svh,880px)` (line 65). While card content < min-height, an opening
  `<details>` re-centers the card, shifting its top edge UP by half the reveal height —
  layout motion under the user's pointer. Mobile stations are `align-items:flex-start`
  (line 112) so growth is purely downward there. Fix candidates: bottom-anchor the
  reveal content, or rely on browser scroll anchoring plus keeping reveals short; the
  clicked summary must not move.
- **Stepper is height-agnostic.** IO fires on center crossing (`rootMargin
  -45%/-45%`, lines 727–738); a step grown by an open reveal simply stays active
  longer. No auto-close needed or wanted — an open reveal must survive scrolling away
  and back.
- **Station geometry holds.** `min(64svh,560px)` is a *minimum*; an open reveal
  legitimately grows the step and adds scroll distance for that beat. Never shrink the
  stage (min(52svh,480px)) to make room; card content scrolls under the pinned stage
  as it always has.
- **Flat-mode parity is nearly free.** `enterFlat()` (748–768) appends figures into
  `.step-inner`; a reveal built statically/at-init into `.step-inner` renders in both
  modes with zero extra code. Build the mini-DAG SVG once at init from
  `DATA.provenance`, mode-independent — do NOT build it lazily on IO activation.
- **Hit-area precedent is substandard.** `details.sql summary` = 12px text, `padding
  9px 0 7px` (~28px tall). New beat summaries need ≥24px CSS target (WCAG 2.5.8) and
  ideally ~44px on touch; full-width summary row inside the card is the cheap win.
- **Width budget for the mini-DAG.** At 360px viewport: story pad 24px×2 + card pad
  26px×2 ⇒ ~260px of content. A left-to-right chain won't fit legibly; either a
  vertical/stacked chain or the `.dag`-strip precedent (`overflow-x:auto` on its own
  container, line 134) — page body must never scroll horizontally.
- **ERROR vs WARN cannot be color-only** (WCAG 1.4.1) and gold is display-only
  anyway: encode blocking vs drift by shape/weight + glyph + visible text label
  (e.g. filled ▪ "blocks" vs outline ▫ "warns"), color as reinforcement at most.
- **A11y wiring.** Mini-DAG SVG: `role="img"` + `aria-label` naming the chain and
  check count, matching the `.dag` strip (line 316) and stage precedents; keep
  `<summary>` native (no ARIA re-plumbing); no open/close animation, so
  reduced-motion needs nothing new.
- **Coverage instinct going in**: a consistent affordance across the 6 insight beats
  (1–6... i.e. data-steps 0? beats 0 and 7 are meta per brief); mixed presence is fine
  if placement/wording is identical wherever it appears; the handoff callback must be
  plain text, not a fake disclosure.

Still cannot verify: real-device behavior of scroll anchoring when a centered flex
child grows (needs manual testing); exact rendered height of a mini-DAG at 260px.
