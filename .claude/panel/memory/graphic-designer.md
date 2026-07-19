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
## Prep notes: post-landing cleanup (compacted 2026-07-18)

Superseded by the Banked section below. Surviving facts worth keeping:
- Rail CSS lives at site/index.html:204–207; `.prov-check` is 11.5px mono — a
  pre-existing badge-only exception below the 12px floor; do not propagate it to any
  other mark, and never shrink it further.
- Title-attribute `why` tooltips remain hover-only with no touch affordance; the
  legend fix removed the false promise but not the gap. Standing watch, not mine alone.
- The guard-honesty caveat lines on beats 4–6 self-removed when claims became direct
  and check-guarded — generated copy worked in both directions, no hand edits.
- Beat-7 word-list overflow ("undefined checks") was caught by the drift guard —
  generated type failing loudly beats silent fabrication.

## Banked: post-landing cleanup (2026-07-18)

Decision log `2026-07-18-post-landing-cleanup.md`; commits c0b97e0 (SQL truth),
2aa845e (spoiler fix + height check).

**Lost (Q1), and why it's the right loss:** my guard+blocking filtered rail fell to
the coverage-understatement objection — character_stats carries ZERO blocking checks,
so under my rule the final beats would render near-empty rails forever, visually
understating real coverage. Re-authoring won 5–3–1 on the one-home law (the trio
description hand-listed a roster whose single source is known_facts.py — a drift bug
independent of spoilers). But the remedy delivers every demand I actually hold:
renderer untouched, ONE rule on every beat, no per-beat conditionals, no narrative
fields in provenance; my whack-a-mole objection is answered structurally by the
standing spoiler pin (term sets derived from known_facts, seen-to-fail before merge).
Two lessons banked: (1) I proposed a renderer-layer fix for a content-layer problem —
when strings are generated AND pinned by a test, fixing the strings IS systemic;
filtering the renderer was solving honesty with layout. (2) Before proposing any
filter rule, run its degenerate case against every asset's actual inventory — one
all-WARN asset collapsed "guard+blocking" into an empty rail.

**Won (Q2/Q3):** SQL truth landed with zero visual delta — existing `details.sql`
treatment, no new "verified" mark, unanimous; chart 5's subtitle gained its
denominator clause (data-analyst's point, but it's the on-chart-denominator law
paying out). Q3(a) landed clean: one ◇ badge where characters_enriched appears,
WORDS extended through "thirteen" in the same commit, galaxy_report stays check-free
— a disclosed gap beats a phantom badge.

**Rail-mass watch (open, visual):** uniform rail means beats 1–3 now show four
characters_enriched badges (up one) and beat 1 additionally carries the
height-baseline ◇. Labels are number-free and short, and the rail flex-wraps, so I
expect the 360px budget holds — but nobody has re-eyeballed the densest rails since
the count went to 13. Next site-touching prep: headless pass at 360×740 counting
wrapped rail lines; flag any rail exceeding ~2 lines.

**Prep differently next time:** enumerate each asset's checks BY SEVERITY before
designing any rail/badge rule, and test the rule against both the sparsest and the
densest asset; state which layer (renderer vs strings) a fix belongs to as part of
the proposal, not as an afterthought.

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

**Still open (from the survey, not adjudicated):** off-token hex colors (`#0a0f1c`
tip bg, `#2a3550` .baseline, `#4bd5ee` hero, `#9fd0ff` SQL ink) and the ~9-size
small-type scale — token hygiene + raise-only consolidation remain future proposals.
Rail-mass watch continues at 15 checks (re-eyeball densest rails at 360px next
site-touching prep).
