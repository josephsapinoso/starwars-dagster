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
  390/360 is the verification bar. (akabab coverage stat-block also wraps as HTML, 2026-07-20.)
- **Second-source surface is a dashboard card, never a story beat** (akabab panel,
  2026-07-20): the census spine is one archive (8 steps, "n/8", BUILDERS.length=8 —
  untouched); the second source is a second *reading* of it, a `#dash` card that renders
  once (flat-parity free), uses opt-in `details.sql` (content never gated), carries no
  per-card badge (DAG strip is the lineage surface). No ranked faction chart — canon-scope
  trap; saga-safe coverage COUNTS only.
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
- **Watchlist-round laws (2026-07-19, commit fdd3178):**
  (a) *Anchoring restoration is not scroll-jacking* — capture the clicked summary's
  rect.top on summary `click` (capture phase), compare on `toggle`,
  `scrollBy({top:delta, behavior:"instant"})` when |delta|>1 (site ~471–485):
  synchronous, activation-triggered, self-noops where the browser anchors and on
  top-anchored mobile. Animated or assumed-delta variants stay banned.
  (b) *Acceptance is a decision with a tripwire* (my must-have, law verbatim) — an
  accepted limitation enters the log with its reopening trigger written down.
  (c) *Measured-vs-inferred labeling* — decisions resting on unreachable hardware
  state measured facts and inferences separately, verbatim, in the log.
  (d) *The census conceit is load-bearing* — the stage tooltip is the only surface
  naming most of the 82 individuals; no input modality may be cut off from it.
  Touch PINS (site ~465–469, 799–802): touch pointermove shows and pins,
  pointerleave skips hide for touch; dismissal is the reader's next tap (hit-test
  miss → tipHide) or scroll (explicit tipHide), never a timer.
  (e) *Exposure changes reach, not content* — a wider audience gets the same string
  verbatim from its one home; if it doesn't fit the vessel, change the vessel.
- **Standing acceptances with tripwires (watchlist round):** badge whys stay
  title-only desktop bonus — reopen if a why gains load-bearing content with no
  non-hover home or the legend line ceases to be true (spoiler pin already scans
  label+why; whys are verbatim spec.description projections, so the Dagster-UI
  home is genuine). Stage SVG type stays (~5.1px eff @360) — redundancy-warranted;
  a css raise is IMPOSSIBLE below target (20-unit witness stack caps ~8px eff);
  reopen if any anno carries content not in copy/caption; a viewBox rework must
  arrive with the 8-state anchor-geometry re-verification costed.

## Prep notes: 8-bit character faces as census mark (2026-07-20)

- **Legibility math (fatal, lead with it):** stage viewBox 700×620 → mobile render
  ratio ≈ .45 (312px @360), desktop ≈ .8–.9. Mark is `circle r=7` (14-unit footprint).
  14×.45 ≈ **6.3px total** on mobile; 8×8 sprite = 0.79px/cell, 16×16 = 0.39px/cell —
  MUD. Desktop 14×.85 ≈ 12px → coarse silhouette, never a likeness. A recognizable
  8-bit face needs ~24–32px (3–5× footprint) → 82 marks overlap catastrophically in
  clustered/histogram beats. **Recognizable per-character faces at every beat are
  geometrically impossible under settled geometry.** New skill:
  panel-ux-designer-pictographic-marks.
- **Graceful form (my proposal):** monochrome saber-blue pixel *silhouette* whose
  bounding shape carries the mark and degrades to a solid blob (= the dot) at 6px;
  interior detail is a desktop/hover-zoom bonus only. Test at the densest beat.
- **State survives single-hue law:** base/faint/dim = opacity on fill; hot = gold
  (allowed: display emphasis on one always-name-labeled mark, not a series). Full-color
  faces would make color a per-mark series → breaks sole-data-hue law. Reduced-motion:
  no frame anim / sprite-swap tween.
- **Flat-embed parity:** sticky path builds units once + re-transforms; enterFlat
  REBUILDS per beat (:846-869). Both emit `circle r=7` today. A sprite needs ONE shared
  builder both call, or inline `<use href="#sym">` of an inline `<symbol>` (works in the
  flat clone that lives outside the main svg id). One-path inlining = silent flat-mode
  vanish.
- **Honesty tension (core):** most of 82 have no verifiable likeness. Per-character
  invented face asserts identity the pipeline can't source (data-honesty violation). A
  single generic glyph for all 82 is honest but is just a fancier dot — does NOT deliver
  "character faces." Owner appetite vs. honesty gap must be surfaced, not papered.
- **A11y unchanged:** tooltip stays the only naming surface (census-conceit veto); no 82
  new tabindex (label-only rule; table is keyboard home). A face implying a name has no
  keyboard/AT path.
- **Scope Q (defer to Claude):** mass/height scatter (:1227) + birth-year strip (:1385)
  also use dots — brief flags whether they change too; I'd hold them out (different
  charts, different legibility regimes).
- **Cannot verify:** exact desktop stage column width (inferred .8–.9); actual overlap
  density in clustered beats without measuring; sprite pixel/bloat budget (graphic-
  designer's to cost). Verify these before implementation, not before debate.

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
- Desktop steps are center-flex (min-height min(102svh,880px)): reveal growth shifts
  the clicked summary UP where the browser lacks scroll anchoring — now compensated
  by the settled delta-restoration shape. Mobile stations are top-anchored, growth
  downward. Stepper is height-agnostic (IO at rootMargin -45%); station min-heights
  are minimums; never shrink the stage to make room.
- Width budget: at 360px viewport ≈260px of card content; page body never scrolls
  horizontally, only dedicated containers (`.dag` strip) may `overflow-x:auto`.
- Baseline hygiene shipped 2026-07-19: doctype + `<html lang="en">` present; story has
  a visually-hidden h2 and each beat kicker is a real `<h3>` — the heading outline gap
  from my survey is closed. Protect these; they are easy to lose in a rewrite.

## Banked: akabab site surfacing (2026-07-20)

**Won (my whole thesis carried, unanimous):**
- Placement is a **dashboard card, never a scroll beat** — the `#card-biographies` card
  slots into `#dash` after `#card-registry`. My prep cost-accounting (BUILDERS.length=8
  auto-derives the "n/8" counter at site:784; a 9th beat ripples to ~7 co-landing edits
  incl. the expensive 8→9-state anchor-geometry re-verification) was the decisive frame:
  a beat was ruled "unearned." **The census spine stays 100% untouched.**
- **Flat-embed parity free** — the card renders ONCE, needs no `enterFlat()` figure
  builder, reuses the shared `details.sql` disclosure (≥44px summary, downward growth,
  no anchor-restoration issue in the dashboard flow). Verified as filed.
- **Content never gated** — the SQL disclosure is opt-in `details`; every coverage number
  prints in the card body itself, not behind a reveal. Held verbatim.
- The coda's pre-authored "second reading" hook was confirmed as the card's referent
  (storyteller's copy lands there) — my prep flagged it; the storyteller owned the frame.

**Newly settled (promoted to law):**
- The site's second-source surface is a dashboard card, never a story beat — one archive
  (8 steps, "n/8"); the second source is a second *reading* of it. **Now in my Settled.**
- The coverage **stat-block wraps as HTML, not SVG** — same rule as my testimony-caption
  precedent; no clip at 360/390.
- No ranked faction chart on a six-film site (canon-scope trap; saga-safe COUNTS only) —
  a lore/analyst-owned law I now enforce on any future "just rank it" ask.
- Card numbers render from per-row `DATA.people[].bio`; no per-card check badge (a badge
  needs a claim entry — the DAG strip is the lineage surface, registry-card precedent I
  already banked).

**Prep differently:** my cost-accounting was the highest-yield artifact of the round —
lead with file:line ripple counts, they end the placement debate before it starts. I had
no objections to raise because the frame was mine; next time, still pre-cost the opposing
veto's compromise (habit from the watchlist lesson) even when I expect to win.

## Banked: pipeline-reveal + post-landing (2026-07-18, compacted)

- Won: vertical chip chain (260px budget); beats 1–6 with beat-0 clean; legend
  rider verbatim; touch-surface analysis shaped the winning labels.
- Lessons: show where a resisted affordance's need is already served; render plain
  HTML before designing ARIA for a graphic; measure at 260px before debate; verify
  the brief's claims myself; cost string fixes before renderer fixes; riders on
  other roles' proposals evaporate with them.

## Banked: birth registry, coda, hue enforcement (2026-07-19, compacted)

- Won: coda mechanics shipped as filed (promoted to Settled); no-tooltip-content law
  survived its first offensive test (BBY gloss in the subtitle); keyboard parity
  landed wider than my ask (all six renderers); legend conversion for slivers;
  "SVG text doesn't wrap" rule from the in-flight testimony-caption catch.
- Lost, rightly: I called the coda digits-pin theater; pinning a PROPERTY is an
  honest absence assertion (pinning wording would be theater). Before objecting to a
  guard, name the exact property it asserts.
- Prep lesson (highest-yield yet): the fresh-eyes artifact survey doubling as prep —
  file:line findings became shipped fixes without spending debate capital.

## Banked: token hygiene + raise-only type (2026-07-19, a30a5bc, compacted)

- Won: AA fix shipped better than my remedy — per-rank `.seg-pct` ink from the same
  ladder index that drives segment color (no single ink passed both grounds).
  Lesson: run the contrast pair for EVERY ground, not the worst one I checked. Dead
  11px attr deleted; the JS-scan guard requirement was pure prep yield; 360/390
  re-verified pre-merge.
- Lost: `.prov-check` 11.5→12 (4–2) — the exception is load-bearing craft (voice
  separation), and the whisper clause pins it loud and testable, answering my real
  objection (unauditable holes) better than erasing it. Chart-lettering raises
  exempted as a pinned geometry tier (evidence burden real and unfunded).
- Prep differently: cost my own remedies with the rigor I cost others'; before
  retiring a settled exception, check whether it is craft, not debt.
- Durable: six dashboard charts measure `viz.clientWidth` (true CSS px, verify at
  360); stage svg is fixed 700×620 viewBox (scaled text). Rail at 360: chips one
  per row in a 244px rail, summaries 46–64px. Gender label gate `w > 46` untouched.

## Banked: watchlist round (2026-07-19, commit fdd3178, compacted) — all four CLOSED

- Won: Q2 shipped my exact delta-compensation shape (dual-branch gate re-run on landed
  code: anchoring-on 0/0/0, Safari −181/−179/−179 via `overflow-anchor:none` proxy);
  Q1/Q4 acceptances carried with my tripwires; stale-state must-have landed as explicit
  tipHide on scroll (site:469).
- Lost (Q3 5–1): suppress-for-touch fell to the census-conceit veto — my "redundant
  below" claim was wrong at individual grain (stage tooltip is the ONLY surface naming
  most of the 82). Lessons: audit a tooltip at the FINEST grain it exposes; cost the
  shape in the actual codebase before calling it prohibitive; when I hold a veto, pre-cost
  the opposing veto's compromise with my must-haves attached.
- Watchlist (confirmatory only): real-iOS pass of Q2/Q3 and real-AT badge-`title`
  exposure when hardware/AT appears (recorded under measured-vs-inferred; not debt).
