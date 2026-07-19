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
