---
name: panel-graphic-designer-mark-system
description: Inventory of the starwars-dagster site's mark system (chips, disclosures, dots, annotations) and the rules for extending it without fragmenting the visual language. Use when evaluating any proposal that adds a new visual component to site/index.html.
---

# The site's mark system — inventory and extension rules

All selectors live in the single `<style>` block of `site/index.html`. Before any new
component is approved, walk this inventory: the proposal must reuse a mark below or
justify a permanent seat.

## Inventory (verified 2026-07-17)

| Mark | Selector / lines | Look | Meaning |
|---|---|---|---|
| Dot unit | `.unit` (+ dim/faint/hot) ~80–84 | 7px circle, saber blue `--s1` | one character; the only data series mark in the story |
| Gold hot state | `.unit.hot`, `.chip.hot`, `.anno-name.hot` | `--gold` fill/text | "the one to look at" — display emphasis, never a series; every gold dot is direct-labeled |
| Annotation | `.anno-line`, `.anno-name` ~87–89 | 1px ink-3 line, 12px ink-2 label | callouts on the stage; legibility floor is 12px |
| Chip | `.chip` ~139 | mono 12px, ink-2, `--void` bg, 1px `--line` border, 5px radius | one Dagster asset |
| DAG group | `.dag-group` ~135 | 1px **dashed** `--line` border | pipeline layer grouping — dashed = grouping, do not overload |
| Disclosure | `details.sql, details.prov` ~190–197 | 12px ink-3 summary, .06em tracking, gold `▸/▾` `::before`, `--void` inset body | opt-in depth (SQL + provenance); the ONLY disclosure style |
| Check-badge rail | `.prov-checks / .prov-check` ~204–206 | mono 11.5px ink-3, ◆/◇ glyph + number-free label; flex-wrap | an asset's full check inventory; ◆ blocking, ◇ drift WARN. 11.5px is a badge-only exception to the 12px floor — do not propagate |
| Overflow escape | `.dag { overflow-x: auto }` ~134 | horizontal scroll | wide diagrams scroll; type never shrinks below 12px. Dashboard affordance only — story reveals stack vertically |

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
