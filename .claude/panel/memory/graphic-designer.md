# Graphic Designer — Panel Memory

## Settled (do not relitigate)

- Color budget: gold #ffe81f is a display accent only — headings, marks, ceremony —
  **never** a data series. One data hue (saber blue) carries all series. (First design
  panel, PR #1/#2.)
- Single HTML file: system font stack only, no webfonts, no CDNs, no build step. The
  austerity is the brand. (First design panel.)
- Mobile stage geometry is settled: stage pinned at min(52svh, 480px) — never shrink
  it; denominator captions and annotations are at the legibility floor. (Mobile
  beat-spacing panel, PR #4.)
- Decorative fill in the gaps between story beats was rejected for cause — whitespace
  is pacing, not emptiness to decorate. (Mobile beat-spacing panel, PR #4.)
- One disclosure style, ever: `details.sql summary` treatment (mono 12px, .06em
  tracking, ink-3, gold ▸/▾ `::before`) is shared via extended selector
  (`details.sql, details.prov`) for all opt-in reveals. A second disclosure style is a
  fork. Hit area for both raised to ≥44px. (Pipeline-reveal panel, 2026-07-18.)
- Check-status badges are monochrome ink-2: ◆ = blocking/ERROR, ◇ = WARN, always paired
  with wording ("blocks"/"warns"). No green/amber/red seats on the site; a static
  artifact cannot claim live status, so color-coded "passing" would be a fabricated
  mark. Severity derives from `spec.blocking` in provenance data, never hand-typed.
  (Pipeline-reveal panel, 2026-07-18.)
- Lineage-chain chips are real HTML `.chip` elements (mono 12px, 1px `--line` border,
  5px radius), not SVG imitations — reuse the CSS verbatim. Exactly one `.hot` gold
  seat per chain: the single beat-relevant asset. Gold-as-"the one to look at" is the
  established emphasis mark. (Pipeline-reveal panel, 2026-07-18.)
- Per-beat reveal chains stack VERTICALLY (chips + ↓ connectors) inside `.step-inner`;
  no horizontal overflow escape in reveals — every node visible without scrolling at
  the ~260px mobile budget. Reveals exist on beats 1–6 only; beat 0 stays clean; beat 7
  carries a provenance-computed callback line. (Pipeline-reveal panel, 2026-07-18.)
- Guard honesty, AMENDED (post-landing cleanup, 2026-07-18): the rail is a uniform
  asset-level citation — every beat renders ONE rule, all checks of its chain assets;
  spoiler/emphasis safety lives in the STRINGS (number-free labels generated from
  provenance), never in per-beat renderer conditionals or filters. My earlier per-beat
  badge-placement reading ("badge only where the check asserts the displayed number")
  is superseded at rail level; the plain-words rule for derived/unguarded claims stands.
- Displayed SQL is executed SQL: any SQL text on the site lives in DATA and is executed
  offline against the fixture warehouse. Renders via the existing `details.sql`
  treatment with ZERO new marks — no "verified SQL" badge exists or ever will; ◇/◆ +
  prov-note wording already carry "asserted offline". (Post-landing cleanup, 2026-07-18.)
- DATA.provenance carries no narrative fields — everything in it stays derivable from /
  verifiable against the real Dagster defs plus known_facts. Visually: rail labels and
  legend are generated type, never hand-lettered. (Post-landing cleanup, 2026-07-18.)
- Rail legend copy is settled: "◆ blocking check · ◇ drift warning · full check
  descriptions live in the Dagster UI" — the old hover promise was false on
  touch/keyboard (ux rider, 2026-07-18).
- Dashboard cards get NO per-card mini-DAGs — the full-width lineage strip is the
  establishing shot; duplicating it per card is mark multiplication. (Pipeline-reveal
  panel, 2026-07-18.)
- **The gold ring means "extreme"**: persistent gold rings assert superlatives only —
  the three true extremes wear them (scatter pair + Yoda on the registry); named
  non-extremes (Vader) get labels, never rings. (Birth-registry panel, 2026-07-19.)
- One data hue is now enforced dashboard-wide: amber outlier dots deleted, hyperdrive
  bars s2→s1, films' second series is a 45% s1 tint, gender is a rank-ordered s1
  ladder. No chart anywhere paints s2–s5. (Birth-registry panel, 2026-07-19.)
- Cross-medium tint law: multi-step tints of the data hue render as SOLID computed
  colors — `color-mix(in srgb, var(--s1) N%, var(--panel))`, steps [100,75,55,40,28] —
  never fill-opacity, so ONE palette array feeds SVG fills, HTML legend swatches, and
  tooltip chips with identical color strings. (Birth-registry panel, 2026-07-19.)
- Captions longer than a label render as wrapping HTML below the figure, never SVG
  `<text>` — SVG text clips at narrow widths (registry testimony line clipped at
  390px). (Birth-registry panel, 2026-07-19.)

## Working knowledge

- Design tokens live in one `:root` block at the top of `site/index.html` (~lines
  6–25): colors, font stacks; everything downstream consumes the variables. Tokens
  define `--s2` green / `--s3` amber / `--s4` red but story/lineage sections use only
  blue + gold + inks — keep it that way (see badge law above).
- The existing mark vocabulary: dot units (`.unit` dim/faint/hot), rounded bars
  (`barPathH/V`), annotation lines + labels, `.chip` asset boxes in the dashboard
  lineage strip (`.chip.hot` gold, used once for galaxy_report), gold ▸/▾ markers on
  `details` reveals, now ◆/◇ monochrome check badges. New components must reuse this
  vocabulary before inventing marks.
- Dashed border means *grouping* (`.dag-group`) — never overload dashed to also mean
  WARN in the same diagram family.
- Check names run up to ~40 chars mono; badges use short display labels from the
  provenance object, never raw check names, or chains explode horizontally.
- Mobile: `.step` min-height min(64svh,560px) — an open reveal may legitimately grow
  the card taller than the station; geometry survives as long as the stage is
  untouched. Flat mode appends per-step figures inside `.step-inner`; anything living
  there ships to flat embeds for free — reveals are built statically at init for this
  reason.
- Provenance strings (labels, badge wording, rationales) all project from
  `DATA.provenance`, which is pytest-verified against real Dagster definitions; the
  one-line strict-JSON `const DATA` format is load-bearing. Visually this means: no
  hand-lettered status text anywhere — the type on screen is generated.
- Label template settled by lore/ux: "The paper trail — where {claim} comes from";
  beat 4 (held pause) gets the quietest variant "The paper trail." — identical
  placement/size everywhere.

## Banked: pipeline-reveal (2026-07-18, compacted)

Won: chip reuse (adjudication upgraded my SVG-imitation plan to real HTML `.chip`
elements — the stronger form of my own principle: propose *using* the existing CSS,
not imitating it); monochrome ◆/◇ badges (severity from `spec.blocking`, mark can't
lie); shared disclosure selector; no per-card mini-DAGs. Lost: horizontal chain with
overflow-x — at ~260px it hides the terminal node (the payoff) behind a scroll.
Banked distinction: overflow-x is a dashboard affordance, never a story affordance.
Lessons: measure content budget before proposing an axis; treat a spec's stated
technology ("SVG diagram") as a guess to challenge, not a constraint.

## Banked: per-character transform landed (2026-07-18, compacted)

Commit `082d9c9`: beats 4–6 render the three-chip vertical chain + four-badge ◇ rail
with ZERO new mark types; `.hot` gold seat unchanged (`galaxy_report` only) — the
reuse-first outcome the chip law was written for. Vertical-budget watch RESOLVED:
headless 390x844 / 360x740 pass — reveals grow downward, stage cap holds; floor rules
(never shrink type, never touch the stage) remain the fix path on regression.
## Banked: post-landing cleanup (2026-07-18, compacted)

Decision log `2026-07-18-post-landing-cleanup.md`; commits c0b97e0, 2aa845e.
Lost Q1 (guard+blocking filtered rail) to the coverage-understatement objection:
character_stats carries ZERO blocking checks, so my rule degenerated to empty rails.
The remedy (re-authored strings + standing spoiler pin) delivered every demand I
actually hold: renderer untouched, ONE uniform rule per beat, no narrative fields.
Lessons: (1) when strings are generated AND test-pinned, fixing strings IS systemic —
don't solve content-layer honesty with renderer layout; (2) run any filter rule's
degenerate case against every asset's real check inventory by severity first.
Won Q2/Q3: SQL truth with zero visual delta (no "verified" mark, unanimous);
denominator clause on chart 5; one ◇ where characters_enriched appears while
galaxy_report stays honestly check-free — a disclosed gap beats a phantom badge.
Surviving watch items: `.prov-check` 11.5px mono is a badge-only exception below the
12px floor (never propagate or shrink — raising it is legal and would retire the
exception); title-attribute `why` tooltips remain hover-only with no touch
affordance (standing watch, not mine alone). Generated copy self-corrects in both
directions: beat 4–6 caveats self-removed; beat-7 overflow failed loudly.

## Banked: birth registry + hue enforcement (2026-07-19)

Decision log `2026-07-19-birth-registry-and-polish.md`; commits 1f3cf9e (registry
card), 4d92cb7 (coda + hue enforcement), f170379 (screenshots at 15 checks — the
long-standing README-retake open item is CLOSED).

**Won — Q3 adopted in full, registry card shipped as specced.** Amber deleted;
persistent gold rings on the three true extremes with Vader label-only; hyper s2→s1;
films at 45% tint; gender ladder with the legend converting to matching swatches
(names + counts summing to 82 stay visible). Registry card: part-to-whole bar with
absence as faint tint, log dot strip, two anno-t labels, Yoda's single gold ring, BBY
gloss printed. Zero new mark types across three commits. Gold-ring-means-extreme is
now banked law (promoted to Settled). The coda shipped ornament-free —
whitespace-is-pacing held without my needing to argue it.

**Implementation deltas to keep:**
- The ladder landed as `color-mix(in srgb, var(--s1) N%, var(--panel))` SOLID steps,
  not my raw fill-opacity spec — a stronger form of my own must-have ("ladder
  identical in bar, legend, tooltips"): fill-opacity can't cross into HTML legend/chip
  backgrounds; one palette array now feeds all three media with identical strings.
  Verified in source (~1092–1127). Same lesson as the chip debate: when the goal is
  identity across media, specify the computed VALUE, not the rendering trick.
- Two anno-t labels collided on the dot strip; the fix was staggered rows, not
  smaller type — the floor rules worked as the designed fix path.
- The testimony caption clipped as SVG text at 390px and became wrapping HTML below
  the strip — promoted to the Settled caption law.

**Prep differently next time:** spec tints as "identical color values across SVG and
HTML," letting implementation choose the mechanism; test any SVG text longer than a
name at 360–390px before speccing it as SVG; plan label collisions (stagger rows) for
any strip carrying two or more annotations.

**CORRECTION (2026-07-19):** the four "off-token" hexes from my survey (#0a0f1c,
#2a3550, #4bd5ee, #9fd0ff) were already tokenized in commit 1123757 as --tip-bg,
--axis, --cyan, --sql-ink — that ledger entry is retired. The small-type scale
remains live and is being adjudicated 2026-07-19 (prep notes below).
**Rail-mass watch CLOSED (2026-07-19):** verified at 360px with 15 checks — no
horizontal scroll; densest rails wrap one chip per row, chips 125–180px vs 244px
rail width, 6-row max stack (character_stats), summaries ≥44px. Headroom exists
even for a badge-type raise.

## Prep notes: token hygiene + raise-only type consolidation (2026-07-19)

Verified in site/index.html today:
- Token block is `:root` lines 8–31. Only TWO off-token colors remain, both in JS:
  `#cdd8ef` starfield star fill (~489 — canvas cannot consume var(); needs a ONE-TIME
  getComputedStyle bridge at init, never per-frame) and `#fff` gender in-segment
  %-label fill (~1131 — SVG presentation attributes accept var() directly, so
  `fill="var(--ink)"` needs no bridge; pure white appears nowhere else on the site,
  so #eef1f7 is the more coherent value anyway).
- Gold alpha variants are rgba(255,232,31,…) literals (e.g. 53, 152) — gold's own
  triplet, derived not off-token; a hex-only guard is the right scope.
- Sub-body scale confirmed: 10.5 · 11 · 11.5 · 12(×9) · 12.5(×8) · 13(×8) · 13.5 ·
  14, plus the 16.5 card-h3 oddball. Five half-pixel steps are the disease.

Positions for debate:
- **Q1 — tokenize both.** `--star: #cdd8ef` earns a :root seat: the token block is
  the SINGLE color registry (precedent: --tip-bg/--axis are equally minor and live
  there); a "sanctioned literal" comment in JS is a second registry. Afterward the
  rule is absolute — hex literals exist ONLY inside :root, CSS or JS, no allow-list
  to rot.
- **Q2 — integer scale, strictly raise-only:** 10.5→11, 11.5→12 (retires the
  .prov-check badge exception; rail headroom verified above), 12.5→13, 13.5→14,
  16.5→17. Result: 11 micro · 12 floor · 13 secondary · 14 aside/note · 16 body ·
  17 card-h3. Geometry-load-bearing, re-verify at 360/390 after the raise: axis-t /
  val-t / anno-t / cat-t (SVG, collision history — fix by staggering, never
  shrinking), the gender %-label fit gate `w > 46` (must rise with the type, ~48),
  .kicker at .28em tracking inside 44ch cards, dot-strip staggered anno rows,
  JS small-label attr stays 11.
- **Q3 — no font-size tokens.** Sizes never co-vary at runtime (unlike the tint
  ladder, where value-identity across media forced tokens); var() indirection costs
  readability in a hand-authored file. The sanctioned scale lives as a comment in
  :root; the pytest guard is the enforcement.
- **Q4 — one structural pytest** in the existing suite, same commit as the raises
  (feature+guard law): regex-scrape hex literals (assert none outside :root) and
  fixed-px font-size values in CSS and JS attrs (assert membership in the sanctioned
  set); clamp() display sizes exempt by pattern. No second lint framework.
