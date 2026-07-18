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
  warning · full check descriptions live in the Dagster UI").
- Displayed SQL is executed SQL: any SQL text on the site lives in DATA and is executed
  by the offline suite against the fixture warehouse. DATA.provenance carries no
  narrative fields (nothing pytest can't verify against real Dagster defs +
  known_facts). Spoiler pin law: a standing offline test derives payoff terms from
  known_facts and fails any check string rendering before its claim's reveal beat.

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

## Prep notes: trio-leak / SQL / coverage (2026-07-18, compacted after banking)

Durable facts (settled outcomes moved above):

- Check `why` renders as `s.title = k.why` on an 11.5px `.prov-check` span — if anyone
  ever proposes tap-to-expand `why`, that needs ≥24px targets and is a
  disclosure-inside-a-disclosure; the defensible model is "supplemental on hover,
  canonical in Dagster," which the settled legend now states.
- Flat-mode ordering precedent to protect: `enterFlat()` inserts the inline figure
  BEFORE `details.prov`, preserving copy → figure → paper-trail order in every beat.
- Spoilers are scroll-mode-only by nature: flat mode shows all beats' full text at
  once, so leak fixes never need a flat-mode variant — another reason fixes belong in
  strings built at init, not in scroll-aware rendering.
- Two-surface audit ladder for disclosure text: label (≤20 chars, all devices) vs
  description/`why` (desktop hover + Dagster). Verbatim-rendering laws bind only the
  projection; the authored strings are ours to write on both surfaces.

## Banked: post-landing cleanup (2026-07-18)

**Won:**
- The legend rider landed verbatim: the false "hover a check for its why" promise is
  gone, replaced by shape legend + a pointer to the canonical non-hover home
  (`site/index.html:869`). This is now settled law and skill rule #8.
- My touch/keyboard finding (hover-why is a `title` attribute; the label IS the whole
  touch surface) was cited by BOTH camps and shaped the winning remedy: labels are now
  spoiler-free everywhere ("all-six set", "pilot census", "flight record", "mass
  baseline") — the fix I said would "fix the whole touch surface" is exactly what
  shipped. Lesson: a precise surface analysis can steer the outcome even when your
  proposal loses.
- Q2 landed render-identical as I demanded (SQL into DATA, zero UX delta); Q3(a) gave
  beat 1 the same badge machinery as beat 2 — my cross-beat-consistency point.

**Lost:**
- The cumulative beat-indexed rail I backed lost 5–3–1 to re-authoring. The decisive
  arguments were outside my lane but correct on mine too: a `beat` field is
  hand-authored narrative metadata pytest cannot verify (QA), and the one-home law
  makes hand-listed rosters drift bugs (tech-writer). I traded rail uniformity for
  spoiler safety when re-authoring buys both — I underweighted "spoiler safety lives
  in the strings" because I was anchored on renderer-side solutions.
- My "+N hidden" count-line rider died with the designer's filter; nothing is hidden
  now, so it was moot. Riders on OTHER roles' proposals evaporate with them — spend
  debate words on my proposal's survivable parts.

**Prep differently:** when a leak/content problem has both a string fix and a renderer
fix, cost the string fix FIRST — it usually preserves uniformity and predictability,
which are my values. Draft the exact replacement strings during prep; the analyst's
concrete number-free labels were half of why re-authoring won.

**Watchlist (still open):** real-device AT exposure of `title` on the check badges;
desktop center-flex scroll-anchoring jump when a reveal opens (still unverified on
hardware); verify the "13 checks" ripple didn't change rail density assumptions at
360px (four badges per chip row was the prior worst case).
