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

## Banked: pipeline-reveal (2026-07-18)

**Won:**
- Chip reuse spec adopted wholesale — mono 12px, rounded rect, `--line` stroke, single
  `.hot` gold seat per chain. Adjudication went further than my SVG-imitation plan:
  chains render as real HTML `.chip` elements, which is a *stronger* version of my own
  must-have (CSS reused verbatim, accessibility free, no SVG text-measurement hazards
  at small widths). Lesson: when arguing "match the existing CSS," propose *using* the
  existing CSS — imitation in another medium was the weaker form of my own principle.
- Monochrome ◆/◇ badge system won unanimously; severity derives from `spec.blocking`
  so the mark can never lie. My "static artifact can't claim live status" argument
  aligned with data-engineer/qa and became banked law.
- Shared disclosure selector (`details.sql, details.prov`) won; the 28px hit-area
  precedent gets fixed once for both (≥44px).
- No dashboard per-card mini-DAGs — my mark-multiplication objection held (unanimous
  minus a conditional).

**Lost:**
- Horizontal chain with `overflow-x` escape lost to ux-designer's vertical stack. Right
  call: at ~260px a horizontal chain hides the terminal node behind a scroll, and the
  terminal node is the payoff. I imported the `.dag` strip's overflow pattern without
  re-checking whether the escape hatch itself was acceptable in a *narrative* reveal —
  the dashboard strip tolerates it because it's reference material, not a story beat.
  Bank the distinction: overflow-x is a dashboard affordance, not a story affordance.

**Prep differently next time:** measure the actual content budget (chip count × min
label width vs container) before proposing an axis; and when the spec says "SVG
diagram," treat the technology as a guess to challenge, not a constraint to design
within — HTML reuse beat SVG on every axis I care about.

**Open items I track visually:** *(vertical-budget watch resolved into the concrete
observation below, 2026-07-18.)* README screenshot retake unchanged (now needs 12 green
checks; desktop UI required).

## Banked: per-character transform landed (2026-07-18)

Execution close-out of the pipeline-reveal open item (commit `082d9c9`, decision note
`2026-07-18-per-character-transform-landed.md`) — no new debate; system held.

- **Mark system survived intact.** Zero new mark types: beats 4–6 now render a
  three-chip vertical chain (`raw_people → star_wars_db → character_stats`) using the
  existing `.chip` + ↓ connector vocabulary, and `character_stats` carries a four-badge
  `.prov-check` rail (all ◇ WARN — exact-value baselines are drift, per known_facts
  law). The only addition anywhere is one more `.chip` in the static DAG strip
  (`character_stats` under "02 · Transforms"); `.hot` gold seat unchanged
  (`galaxy_report` only). Verified in site source. This is the reuse-first outcome the
  chip law was written for.
- **Concrete open observation (was the vertical-budget watch item):** beats 4–6 grew
  taller — 3 chips + 2 connectors + a 4-check rail replaces the old 1–2-chip derived
  chain plus honesty line. Nobody has eyeballed this on a real mobile viewport yet. The
  settled station geometry (min(64svh,560px)) tolerates an open reveal growing the card
  taller than the station, so I expect it holds. **RESOLVED 2026-07-18:** headless
  re-check at 390x844 and 360x740 PASSED — reveals grow downward, no horizontal
  overflow, stage cap holds. The watch item is closed; the floor rules (never shrink
  type, never touch the stage) remain the fix path if a future change regresses it.
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

## Prep notes: open improvement survey (2026-07-19)

Fresh-eyes audit of site/index.html found three color-budget leaks the one-data-hue
law never reached (dashboard predates the law's enforcement there):
- Scatter (~line 1145): labeled outliers get an amber `--s3` dot painted OVER the
  blue dot — a second emphasis hue competing with gold's banked "the one to look at"
  mark. Story precedent: gold-hot + direct label is the emphasis mark.
- Hyperdrive leaderboard (~1242): single-series bars in green `--s2` while the
  homeworlds bars sit in blue — hue change carries zero meaning.
- Gender chart (~1050): five-hue palette [s1,s4,s3,s5,s2]; films chart adds green as
  a second series. Only films has a defensible need for a second visual channel.
- Off-token hex colors: `#0a0f1c` (tip bg), `#2a3550` (.baseline), `#4bd5ee` (hero
  opener), `#9fd0ff` (SQL code ink) — color budget not auditable from :root alone.
- Type-scale drift: ~9 distinct sizes between 10.5 and 13.5px across captions,
  legends, badges, asides. Floor laws intact; the scale itself is fragmented.
Proposed (survey): 1) enforce one-data-hue on dashboard charts, 2) small-type-scale
consolidation (raise-only), 3) token hygiene pass. None touches settled geometry.
