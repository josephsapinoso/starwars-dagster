---
name: panel-graphic-designer-mark-system
description: Inventory of the starwars-dagster site's mark system (chips, disclosures, dots, annotations) and the rules for extending it without fragmenting the visual language. Use when evaluating any proposal that adds a new visual component to site/index.html.
---

# The site's mark system — inventory and extension rules

All selectors live in the single `<style>` block of `site/index.html`. Before any new
component is approved, walk this inventory: the proposal must reuse a mark below or
justify a permanent seat.

## Inventory (verified 2026-07-17; gold ring + hue ladder added 2026-07-19)

| Mark | Selector / lines | Look | Meaning |
|---|---|---|---|
| Dot unit | `.unit` (+ dim/faint/hot) ~80–84 | 7px circle, saber blue `--s1` | one character; the only data series mark in the story |
| Gold hot state | `.unit.hot`, `.chip.hot`, `.anno-name.hot` | `--gold` fill/text | "the one to look at" — display emphasis, never a series; every gold dot is direct-labeled |
| Annotation | `.anno-line`, `.anno-name` ~87–89 | 1px ink-3 line, 12px ink-2 label | callouts on the stage; legibility floor is 12px |
| Chip | `.chip` ~139 | mono 12px, ink-2, `--void` bg, 1px `--line` border, 5px radius | one Dagster asset |
| DAG group | `.dag-group` ~135 | 1px **dashed** `--line` border | pipeline layer grouping — dashed = grouping, do not overload |
| Disclosure | `details.sql, details.prov` ~190–197 | 12px ink-3 summary, .06em tracking, gold `▸/▾` `::before`, `--void` inset body | opt-in depth (SQL + provenance); the ONLY disclosure style |
| Check-badge rail | `.prov-checks / .prov-check` ~204–206 | mono 11.5px ink-3, ◆/◇ glyph + number-free label; flex-wrap | an asset's full check inventory; ◆ blocking, ◇ drift WARN. 11.5px is a Settled whisper pin (authored contrast vs the 12px summary/chip voice) — never propagate, never "fix" |
| Overflow escape | `.dag { overflow-x: auto }` ~134 | horizontal scroll | wide diagrams scroll; type never shrinks below 12px. Dashboard affordance only — story reveals stack vertically |
| Gold ring | ring circles on scatter + registry (r≈8.5, `stroke: var(--gold)`, `fill: none`) | thin gold circle around a mark | asserts a SUPERLATIVE — persistent only on true extremes (added 2026-07-19); named non-extremes get labels, never rings |
| Hue ladder | one palette array: `color-mix(in srgb, var(--s1) N%, var(--panel))`, steps [100, 75, 55, 40, 28] | rank-ordered solid tints of the data hue | ordered categories in ONE hue; the same array feeds SVG fills, HTML legend swatches, and tooltip chips. Second-series tint is the 45% step (films) |

## Extension rules

1. **New disclosures share the `details.sql` treatment** — same summary type, same
   gold marker. Extend the selector list; never fork a second disclosure style.
2. **SVG chips must match CSS chips**: mono 12px, rounded rect, `--line` stroke,
   ink-2 text; `hot` gold for at most ONE emphasized node per diagram.
3. **Status is not a series**: badges (e.g. asset-check markers) stay monochrome ink;
   distinguish severities by weight/glyph/wording, not by adding green/amber/red
   seats. A static page must not fake live pass/fail state with color.
4. **Wide marks scroll, never shrink**: reuse the `.dag` overflow-x pattern —
   dashboards only; story-beat content stacks vertically instead.
5. **Flat-embed parity**: any new story-card component must live inside
   `.step-inner` so the flat fallback (auto-height iframes) inherits it.
6. **The rail is uniform (banked law, 2026-07-18)**: every story beat renders the
   SAME rule — all checks of its chain assets, labels number-free and generated from
   `DATA.provenance`. Spoiler/emphasis fixes belong in the strings (content layer,
   guarded by the standing spoiler-pin test), never in per-beat renderer conditionals
   or filters. Before proposing any badge/rail filter, run its degenerate case
   against every asset's actual check inventory by severity (an all-WARN asset
   collapses "blocking-only" rules to an empty rail). Legend copy is settled:
   "◆ blocking check · ◇ drift warning · full check descriptions live in the
   Dagster UI".
7. **Displayed SQL is executed SQL**: SQL text renders only from DATA via the
   existing `details.sql` treatment, with zero new marks — no "verified SQL" badge
   exists or ever will; ◆/◇ plus prov-note wording already carry "asserted offline".
8. **The gold ring means "extreme" (banked law, 2026-07-19)**: persistent gold rings
   assert superlatives only. If a mark is named for narrative reasons but is not a
   verified extreme (Vader), it gets a label — never a ring. Diluting the ring to
   "interesting" kills the mark.
9. **Tints are solid computed colors, never opacity (2026-07-19)**: any multi-step
   tint of the data hue uses `color-mix(in srgb, var(--s1) N%, var(--panel))` from a
   single palette array shared by SVG fills, HTML legends, and tooltip chips —
   fill-opacity cannot cross into HTML backgrounds, so the colors would diverge.
   When identity across media is the goal, spec the computed VALUE, not the
   rendering trick. No chart paints `--s2`–`--s5`; amber emphasis is dead.
10. **Captions wrap in HTML, not SVG (2026-07-19)**: any caption longer than a short
    label renders as wrapping HTML below the figure — SVG `<text>` clips at narrow
    widths (proven at 390px). Two or more annotations on one strip get staggered
    rows on collision; type never shrinks as the fix.

## The shared tooltip is a data readout (verified 2026-07-19)

`tipShow(evt, title, rows)` (~445–465) is the ONE tooltip: title + rows of
{color chip, value, label}. Its grammar is a data readout, not a prose container —
proposals to pour paragraph-length text (e.g. 113–213-char check `why` strings) into
it fork the mark even though `r.color` is optional. Its complete persistence family
(all one mark, landed fdd3178):
- **hover-follow** — pointermove shows, pointerleave hides (mouse);
- **focus-pin** — keyboard focus pins at screen center until blur (dashboard marks);
- **touch-pin** — the touch analog of focus-pin: a real tap's pointermove shows AND
  sets `tipPinned` (`e.pointerType === "touch"`); pointerleave ignores touch; the
  module-level scroll listener and any hit-test miss call `tipHide`. Dismissal is
  always the reader's own act (next tap or scroll), NEVER a timer. The pointerType
  branch lives only in the stage handlers (~799–802) — the shared module gains one
  flag, zero new marks or styles.
Because the tooltip is real-pixel HTML, it is immune to SVG viewBox scaling: on
small screens it carries a scaled figure's readout at full legibility — but as a
BONUS channel only. Never make the pin load-bearing for accepting scaled-type
illegibility; the warrant must be redundancy in the existing system (a real-pixel
twin in caption/prose for every claim). The census conceit is settled law: the stage
tooltip is the only surface naming most of the 82 individuals, so no input modality
may be cut off from it — suppress-for-touch is banned.

## SVG type audits: effective size, not CSS size (technique, 2026-07-19)

For text inside a scaled `viewBox`, what the eye gets is
`effective px = css px × (rendered width / viewBox width)`. The 700-wide stage
renders 312px @360 viewport → ×.45: `.axis-t` 11.5 → 5.1px, `.anno-name` 12 →
5.3px. Before proposing a compensating media bump, cost it honestly:
1. The needed css value is huge in viewBox units (≈20–22px for ~9–10 effective at
   ×.45) — authored anchor offsets (±10–16 units, tuned to 12px text) and label
   widths (~210 units for a 19-char name at 22px) break across every figure state;
   raise-only law makes that collision re-verification YOUR burden.
2. The style-hygiene guard's parser is not media-query-aware (splits on `}`,
   partitions on first `{` — the inner selector of `@media { .sel { … } }` is
   lost), so a media bump is a parser amendment, not a pin row; and the
   no-font-size-tokens law forbids the variable shortcut.
3. Audit duplication first: HTML captions (`.stage-cap` 13px) and beat prose render
   at REAL pixels and may already carry every anno payoff — if so, the scaled SVG
   text is reinforcement, and the real-pixel tooltip is the interactive substitute.

## Color-token consumption across media (banked 2026-07-19)

- **Data-ink** hex literals belong ONLY in the `:root` token block — including
  ceremony/one-use colors (--cyan, --tip-bg, --axis are precedent).
- **Scenery is not ink:** decorative paints (the aria-hidden starfield canvas,
  #cdd8ef) may stay literals — but only as a guard-pinned entry: exactly one
  occurrence, carrying its required "scenery, not ink" comment. A pin that drifts
  FAILS the test, so the allow-list cannot rot. No getComputedStyle bridge for
  decoration (init-order risk on the hero canvas); bridges are for data ink only,
  ONCE at init, never per frame.
- **Gold's one home:** the #ffe81f literal appears exactly once, in :root; alpha
  ceremony derives via `color-mix(in srgb, var(--gold) N%, transparent)` — the
  rgba(255,232,31,…) triplet is banned. `var(--gold)` itself is free everywhere.
- **SVG presentation attributes** (`fill=`, `stroke=`) DO accept `var(--token)`
  directly — no bridge; prefer a class when the style repeats.
- **Ink adapts to its ground:** on-mark labels (`.seg-pct` pattern) choose ink per
  computed ground from the SAME array that paints the ground (`--void` on full s1,
  `--ink` on tints), every rendered pair ≥4.5:1 verified computationally; the
  fallback is dropping the on-mark label (legend/table carry the data) — never a
  new hex, never one ink that fails somewhere.

## Pixel-art / sprite marks in one file (technique + guardrails, 2026-07-21)

If a proposal replaces a data mark with a per-character sprite (e.g. 8-bit faces for the 82
`.unit` marks), apply these before approving:
1. **Atomic single-fill only.** The `.unit` state machine (applyState :799–802) works because a
   state is a fill/opacity swap of ONE shape (circle → s1/ink-3/gold, faint=opacity .18). A
   sprite preserves base/dim/faint/**hot(gold)** for free ONLY if it is a single-fill silhouette
   (one path, `fill: currentColor`/`var(--s1)`), recolored whole. A fixed-color outline or any
   two-tone portrait breaks dim/faint (they read muddy) — forbid it. Multi-value shading is legal
   for hue only if every value is the Settled tint ladder [100,75,55,40,28], but it still breaks
   atomic state, so not for stateful stage marks.
2. **One hue, no appearance claims.** Full-color sprites (skin tones, character-specific colors)
   are a double veto: new color seats past s1+gold, AND a data-honesty claim about appearance the
   dataset doesn't hold. A silhouette asserts only "a tracked individual," same as the dot.
3. **Decode to one `<path>` per sprite, not `<rect>`-per-pixel.** 82×(up to 64 pixels) ≈ 5k
   nodes, doubled by the flat-embed redraw, is DOM bloat. Pack each sprite as a compact bitmap
   string in the inline JSON (8×8 1-bit ≈ 16 hex chars) and decode to a single path. Budget the
   node count AND the byte count in prep.
4. **A sprite registry is a new honesty + rot surface.** Each sprite asserts identity, must stay
   1:1 with the roster, and needs its own same-commit guard (one-sprite-per-tracked-character,
   palette hygiene, drift extension). No sprite for a character we can't honestly depict —
   generic archetypes imply identity we lack.
5. **Legibility gate is decisive on the mobile stage.** Effective px = css × render ratio (×.45 @
   360). An 8×8 silhouette ≈ 3–4px → a blob that reads worse than a clean dot. Run a
   render/redundancy audit before believing a sprite survives; the honest fallback is sprites on
   the named/canonical subset (or desktop-only) with dots for the anonymous mass — but that is
   TWO mark types, a fragmentation cost to weigh against just keeping dots.

## Type-scale law (banked 2026-07-19; guard: tests/test_site_style_hygiene.py)

- Sanctioned fixed sizes: **{11, 12, 13, 14, 16, 17, 18, 42}** px; clamp() display
  sizes exempt by pattern. font-size is NEVER set from JS/markup — use a class.
- **Whisper-clause pins** (exact selector/value/reason entries in the guard; fail
  loudly on change in EITHER direction): `.axis-t` / `.val-t` / `.anno-t` /
  `.seg-pct` at 11.5 and `.cat-t` at 12.5 — the chart-geometry tier; `.prov-check`
  at 11.5 — the held pause's authored whisper (at 12px the badge would merge with
  `details.prov summary` 12 and `.chip` mono-12, collapsing guard voice into
  machinery voice). Extending the scale or the pins requires a panel, not a commit.
- **Raise-only grants permission, not obligation:** standing still needs no
  evidence; moving chart geometry requires 360/390px collision re-verification, and
  JS fit gates tied to type width (the gender `w > 46`) move with the size.
  Collisions fix by staggering rows, never shrinking.
- **The registry is the test:** the scale and pins live only in the structural
  pytest — no font-size tokens (sizes never co-vary at runtime, unlike the tint
  ladder), no parallel prose lists (prose ledgers rot; executable pins don't).
