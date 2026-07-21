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
- **Pictographic-mark law (8-bit faces, 2026-07-21):** a data mark may gain a picture
  ONLY at emphasis size on a mark the copy already NAMES — never at footprint density
  across the population. Identity is earned, not default: the base census stays uniform
  saber-blue dots; a named/hot mark RESOLVES into a single-fill monochrome silhouette
  (one `<path>` swapped for the `<circle>`, inheriting all four states; hot = gold, the
  one emphasis seat). No outline, no second tone, no skin tone, no per-item hue, no
  procedural-by-field glyph, no external image. The picture must degrade to the base dot
  (a gold blob + label) at small size, and ride ONE shared builder feeding sticky + flat.
  The resolve is a STATIC state class, never an animation/tween. Tooltip stays the sole
  naming surface; no new tabindex. Sourcing is a tiny 1:1-`known_facts`-guarded registry,
  landing with its integrity + spoiler pin in the same commit. (Kills "faces for all 82.")

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

## Banked: 8-bit character faces (2026-07-21, "The Resolving Mark")

**Won (my geometric-impossibility math was decisive; unanimous VETO of all-82):**
- Legibility floor killed the maximal ask outright: a face at dot footprint is ~3–6px
  mud; a readable 8-bit face needs ~24–32px and 82 overlap catastrophically. Leading
  with the numbers (not taste) ended the "faces everywhere" appetite before debate.
- Shipped my one-shared-builder + degrade-to-blob + static-resolve trio verbatim: flat
  verified to render faces identically; mobile faces degrade to a gold blob + label;
  reduced-motion resolve is a display swap, no tween. Naming-surface law held (tooltip
  only, no new tabindex). Single-fill monochrome silhouette carried all four states for
  free (hot = gold = the one emphasis seat) — the color-law point I shared with GD/analyst.

**Refined by the storyteller (I lost the framing, rightly):** my "all-82 shared
silhouette that degrades to a blob" was "the dot with extra nodes" — no delight, asserts
nothing. The winning shape is faces as a REVEAL mechanic on the six named/hot marks only
(Yoda, Poof, Jabba, C-3PO, R2-D2, Obi-Wan); base population stays dots. My degrade-to-blob
property survives as the safety net, not the primary form.

**Prep differently:** I framed the graceful form as a population-wide sprite; I should
have asked "which marks does the story already name?" first — the honest scope was six,
not 82, and that reframes the whole build. When I hold a legibility veto, pair it with
the smallest DELIGHTFUL form, not the largest safe one.

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

## Banked: older rounds (2026-07-18/19, compacted)

- **pipeline-reveal:** won vertical chip chain (260px), beats 1–6 / beat-0 clean, legend
  rider. Lessons: show where a resisted affordance is already served; render plain HTML
  before designing ARIA; measure at 260px before debate; cost string fixes before renderer.
- **birth-registry/coda/hue:** won coda mechanics (now Settled), no-tooltip-content law,
  keyboard parity (all six renderers), legend-for-slivers, "SVG text doesn't wrap." Lost
  rightly: coda digits-pin isn't theater — pinning a PROPERTY is an honest absence
  assertion; name the exact property a guard asserts before objecting. Highest-yield prep:
  fresh-eyes artifact survey → file:line findings shipped without debate capital.
- **token-hygiene / raise-only type:** AA fix shipped better than mine (per-rank `.seg-pct`
  ink from the same ladder index) — run the contrast pair for EVERY ground. Lost
  `.prov-check` 11.5→12 (4–2): load-bearing craft (voice separation), whisper-clause-pinned.
  Cost my own remedies as rigorously as others'; check craft-vs-debt before retiring an
  exception. Durable: charts measure `viz.clientWidth` (verify @360); stage 700×620 viewBox;
  244px rail, summaries 46–64px; gender label gate `w > 46`.
- **watchlist (all four CLOSED):** won Q2 delta-compensation verbatim (anchoring-on 0/0/0,
  Safari −181 proxy); Q1/Q4 acceptances with my tripwires; scroll-tipHide (site:469). Lost
  Q3 5–1: suppress-for-touch fell to the census-conceit veto (stage tooltip is the ONLY
  surface naming most of 82) — audit a tooltip at its FINEST grain; pre-cost the opposing
  veto's compromise with my must-haves attached even when I expect to win.
