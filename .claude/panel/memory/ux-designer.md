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

## Prep notes: pipeline-reveal (2026-07-17, compacted after banking)

Durable facts verified in `site/index.html` (details now settled above are omitted):

- **Desktop growth-jump risk.** Desktop steps are `display:flex; align-items:center`
  with `min-height:min(102svh,880px)`; while content < min-height, anything that grows
  the card re-centers it and shifts the clicked summary UP. Mobile stations are
  `align-items:flex-start`, so growth is purely downward there. Mitigation: reveal
  lives at the bottom of `.step-inner`; keep an eye on real-device scroll anchoring
  (still unverified) whenever any card gains expandable content.
- **Stepper is height-agnostic.** IO fires on center crossing (`rootMargin -45%`); a
  step grown by an open reveal just stays active longer — no auto-close needed.
- **Station math.** `min(64svh,560px)` is a *minimum*; open reveals legitimately add
  scroll distance. Never shrink the stage to make room.
- **Width budget.** At 360px viewport: story pad 24px×2 + card pad 26px×2 ⇒ ~260px of
  card content. Page body must never scroll horizontally; only dedicated containers
  (`.dag` strip precedent) may `overflow-x:auto`.
- **Hit-area precedent was substandard** (`details.sql summary` ≈28px tall); fixed to
  ≥44px as part of this PR — cite WCAG 2.5.8 if anyone tries to regress it.

## Banked: pipeline-reveal (2026-07-18)

**Won:**
- Vertical chain over graphic-designer's horizontal (adjudication #3): my ~260px
  budget argument carried — a horizontal chain needs an overflow escape that hides
  the terminal node. Designer's chip styling specs carried over intact; the
  compromise cost nothing.
- Beats 1–6 only, beat 0 clean, beat-7 callback as plain text (with storyteller/
  lore) over hiring-manager's beat-0 reveal. Winning move: the orchestrator satisfied
  the HM *structurally* — `raw_people` heads every chain, so the census guards appear
  in all six reveals anyway. Lesson: when resisting an extra affordance, offer where
  the underlying need is already served.
- Static build at init inside `.step-inner` (flat-mode parity for free), reader-owned
  open state, no animation, ≥44px hit-area fix, never color-only status — all adopted
  verbatim into the plan.

**Lost / superseded:**
- My prep assumed an inline-SVG mini-DAG (`role="img"` + aria-label wiring). Decided:
  real HTML `.chip` elements instead — and that is *better* on my own axes (native
  text accessibility, no SVG text-measurement hazards at small widths). Lesson: I
  spec'd a11y patches for a technology guess; next time interrogate whether plain
  HTML can render the artifact before designing the ARIA for a graphic.
- "Bottom-anchor the reveal content" was accepted as placement (bottom of
  `.step-inner`) but the desktop center-flex jump itself is mitigated, not eliminated;
  it remains my open real-device verification item.

**Prep differently next time:** measure a prototype's rendered height at 260px before
debate (I flagged this as unverifiable and it stayed unverified); check whether an
existing CSS component (.chip) can be the rendering primitive before proposing new
drawing tech; read checks.py severity semantics myself rather than inheriting the
brief's claims — the beat→asset map being partly false reshaped the whole verdict and
I only had it second-hand from the analyst.

**Watchlist for implementation review:** clicked summary must not move on open
(desktop centered flex); flat-mode render of the chain; `aria-label` generated from
the same provenance data, not hand-written; the shared selector doesn't accidentally
restyle `details.sql` open-state behavior.
