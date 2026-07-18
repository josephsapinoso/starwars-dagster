---
name: panel-ux-designer-scrolly-disclosures
description: UX rules for opt-in disclosure widgets (details/summary reveals) placed inside sticky-stage scrollytelling steps — growth direction, flat-embed parity, hit areas, and non-color status encoding. Use when adding or reviewing any expandable element inside a story beat card.
---

# Disclosures inside scrollytelling steps

Checklist for any opt-in reveal (`<details>`) living inside a story beat card that
shares a viewport with a sticky stage. Derived from `site/index.html` during the
pipeline-reveal prep (2026-07-17).

## 1. Growth direction — the clicked summary must not move
- Top-anchored steps (`align-items: flex-start`, the settled mobile geometry): content
  growth is purely downward. Safe by construction.
- Center-anchored steps (`align-items: center` + min-height, the desktop geometry):
  opening a details re-centers the card, shifting its top UP by half the reveal
  height — motion under the pointer. Mitigate: keep reveals compact, place the
  details at the card bottom, and verify browser scroll anchoring on a real device.
- Never shrink the sticky stage to make room; the station min-height is a minimum —
  a grown step just adds reader-paced scroll distance. IO center-crossing steppers
  are height-agnostic, so nothing else needs to change.

## 2. State is the reader's — never auto-toggle
No auto-open on beat activation, no auto-close on scroll-away. An open reveal stays
open when the reader scrolls away and back. No open/close animation (also makes
reduced-motion a no-op).

## 3. Flat/auto-height-embed parity for free
Build the reveal and its contents (including any SVG) statically at init into
`.step-inner`, not lazily on scroll activation. Anything already inside `.step-inner`
survives `enterFlat()` unchanged. Lazy-on-IO widgets silently vanish in flat mode.

## 4. Hit areas
The legacy `details.sql` summary (~28px tall) is the floor precedent, not the target.
New summaries: ≥24px CSS box (WCAG 2.5.8), aim ~44px on touch; make the summary row
full card width so the whole line is tappable.

## 5. Width budget on narrow screens
Inside a padded card at 360px viewport expect ~260px of content. Horizontal chains
must either restack vertically or scroll inside their OWN `overflow-x:auto`
container; the page body never scrolls horizontally.

## 6. Status encoding (e.g. ERROR vs WARN badges)
Never color-only (WCAG 1.4.1): encode by shape/weight + glyph + visible text label,
color as reinforcement only. Respect the project color budget (gold = display accent,
never a data/status series).

## 7. A11y wiring
Native `<details>/<summary>` — no ARIA re-plumbing of the toggle. Any inline SVG
diagram inside gets `role="img"` + an `aria-label` that states the whole meaning
(chain + status counts), matching the site's `.dag` strip precedent.

## 8. `title` tooltips are a desktop-only side channel
A `title` attribute is unreachable on touch and keyboard and only inconsistently
exposed by AT. Audit rule: every visible label must stand alone without its tooltip
— treat the tooltip as desktop-plus enhancement, never as the mitigation for
sensitive/verbose content ("the details are only on hover" is false on phones: touch
users get LESS text, not gated text). Corollary: legend/help copy must not instruct
"hover ..." unless the same information has a non-hover path; and any editorial
review of disclosure text must review labels and tooltips as two different surfaces
with two different audiences.
