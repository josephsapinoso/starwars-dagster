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
- Guard honesty is a visual law too: a check badge may only sit where the check asserts
  the displayed number (or its labeled denominator/structure); derived/unguarded claims
  say so in plain words next to the chain. (Pipeline-reveal panel, 2026-07-18.)
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
  taller than the station, so I expect it holds; but if it doesn't, the fix is layout
  (rail wrapping is already `flex-wrap`; badge labels stay short display labels), never
  shrinking type below the legibility floor and never touching the stage. Flag for a
  mobile pass before the next visual change ships.
- **Also good:** the derived-claim honesty lines on beats 4–6 are gone because the
  claims are now DIRECT and check-guarded — the guard-honesty law worked in both
  directions (the caveat text appeared when unguarded, disappears when guarded, no
  hand-edited copy either way). Beat-7 word-list overflow ("undefined checks" at 12)
  caught and drift-guarded — generated type failing loudly beats silent fabrication.
