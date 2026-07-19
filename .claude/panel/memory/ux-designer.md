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

## Banked: pipeline-reveal (2026-07-18, compacted)

- Won: vertical HTML `.chip` chain over horizontal SVG (my ~260px budget argument);
  beats 1–6 only with beat-0 kept clean — the orchestrator satisfied the
  hiring-manager *structurally* (raw_people heads every chain). Lesson: when resisting
  an extra affordance, show where the underlying need is already served.
- Lost/lesson: I spec'd ARIA for an SVG mini-DAG that never existed — interrogate
  whether plain HTML can render the artifact before designing the ARIA for a graphic.
- Prep lesson: measure a prototype at 260px before debate; read severity semantics
  myself instead of inheriting the brief's beat→asset map (it was partly false).

## Banked: post-landing cleanup (2026-07-18, compacted)

- Won: legend rider verbatim (no "hover ..." promises); my touch-surface analysis
  (label IS the whole touch/keyboard experience) was cited by both camps and shaped
  the winning spoiler-free labels. A precise surface analysis steers outcomes even
  when the headline proposal loses.
- Lost: cumulative beat-indexed rail (5–3–1) — a hand-authored `beat` field is
  unverifiable narrative metadata; re-authoring strings bought uniformity AND spoiler
  safety. Lesson: cost the string fix before any renderer fix; draft exact
  replacement strings during prep. Riders on other roles' proposals evaporate with
  them — spend debate words on my own proposal's survivable parts.

## Banked: birth registry, coda, hue enforcement (2026-07-19)

**Won (verified in site/index.html, commits 1f3cf9e/4d92cb7/f170379):**
- Coda mechanics shipped exactly as filed: block anchor (`.coda a` display:block,
  14px vertical padding → 53px measured hit area, line 140), `#story tabindex="-1"`
  (line 257) with headless-verified focus movement, `aria-hidden` ↑ glyph (line 397),
  no JS, no arrival animation. Promoted to Settled as the fragment-navigation pattern.
- No-tooltip-content law held its first offensive test: the BBY gloss PRINTS in the
  card subtitle instead of hiding in a `title`.
- Keyboard parity landed wider than my ask: not just the new annotated registry dots —
  all six renderers now give marks tabindex + aria-label + focus tooltips, closing the
  scatter-dot gap from my improvement survey. Registry table (43 rows) is the
  keyboard-canonical home; denominators visible.
- Sliver protection: converted gender legend keeps name + count summing to 82; no
  segment depends on a tooltip.
- Mobile regression caught in-flight: testimony caption clipped in SVG at 390px and
  was rebuilt as wrapping HTML; 390/360 no-horizontal-overflow verified. Banked as the
  "SVG text doesn't wrap" rule.

**Lost (only one, and rightly):**
- I called the coda digits-pin theater. QA's distinction is correct: pinning a
  PROPERTY (stays number-free — the premise of its exemption from the drift detector)
  is a cheap, honest absence assertion; pinning WORDING would be the theater, and
  nobody proposed that. Lesson: before objecting to a guard, name the exact property
  it asserts; "this pins prose" and "this pins the absence that justifies an
  exemption" are different objects. My own guard-honesty law actually WANTS the pin.

**Prep differently next time:** the fresh-eyes improvement survey doubling as prep was
the highest-yield prep I've done — file:line-specific findings (scatter parity, caption
clipping risk class, doctype/lang, heading outline) became shipped fixes without
spending debate capital. Keep auditing the artifact between debates and file findings
with line numbers; small a11y debts get swept into big commits essentially for free.

**Watchlist (carried, still open):** real-device AT exposure of `title` on check
badges; desktop center-flex scroll-anchoring jump when a reveal opens (unverified on
hardware); stage-dot tooltip flashes on touch tap (pointerleave on release — minor);
rail density at 360px now that the check count is 15.
