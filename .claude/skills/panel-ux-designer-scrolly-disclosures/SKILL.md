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
- Chromium's scroll anchoring absorbs the half-height shift entirely (clicked
  summary moves 0px); Safari/WebKit has NO scroll anchoring → the summary jumps
  ~180px there. **Settled, shipped fix (banked 2026-07-19, commit fdd3178,
  site/index.html ~471–485) — "anchoring restoration is not scroll-jacking":**
  browser-neutral delta compensation, no UA sniffing. A document-level capture
  `click` listener matches `e.target.closest("details.prov summary, details.sql
  summary")` and stores `{ summaryEl, top: rect.top }`; the `toggle` listener
  (capture, since toggle doesn't bubble in all engines) checks
  `e.target.contains(storedSummary)`, measures the new rect.top, clears the stored
  anchor, and `scrollBy({top: delta, behavior: "instant"})` when |delta| > 1.
  Self-noops wherever the browser already anchors and on top-anchored mobile
  stations; runs once, synchronously, only on the reader's own activation. Animated
  or assumed-delta variants are banned. Verification without Apple hardware: inject
  `overflow-anchor:none` on the scroller in Chromium to reproduce the WebKit branch
  — run the 2×2 matrix (anchoring on/off × fix on/off) expecting 0 / −half-growth /
  0 / 0, and re-run it on the landed code as the merge gate; record measured facts
  and real-Safari inference separately (measured-vs-inferred law).
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
container; the page body never scrolls horizontally. SVG `<text>` does not wrap:
any caption/annotation that can clip at 390px belongs in wrapping HTML outside the
SVG (banked 2026-07-19, testimony caption). Verification bar: zero horizontal
overflow at 390px AND 360px.

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

Adopted fix pattern (banked 2026-07-18, provenance rail): keep the tooltip as a
desktop-plus courtesy, but have the legend name the canonical non-hover home instead
of the gesture — "◆ blocking check · ◇ drift warning · full check descriptions live
in the Dagster UI". And because the label is the entire touch/keyboard surface,
author every visible label to be safe and self-sufficient on its own; never park
sensitive or load-bearing content in the tooltip and call it mitigated. When a
content leak has both a string fix and a renderer fix (filters, per-context rules),
cost the string fix first — it preserves uniform, predictable rendering across
surfaces and modes. Second precedent (banked 2026-07-19): unit glosses (e.g. "BBY")
PRINT in the card subtitle; a tooltip may repeat them but never own them.

## 9. Fragment-navigation re-read affordance (coda pattern, banked 2026-07-19)
A "start over / re-read" link at the end of a scroll story is pure HTML, no JS:
- Plain `<a href="#target">` where `#target` is the story section carrying
  `tabindex="-1"` — WITHOUT the tabindex, fragment navigation moves the viewport but
  in several browsers NOT focus, stranding keyboard users at the bottom. With it,
  focus movement is real and headless-testable (assert `document.activeElement`
  after setting `location.hash`).
- Make the anchor block-level with vertical padding so the whole line is the hit
  area (~53px measured beats the 44px touch target with room to spare); never a
  bare inline text link.
- Directional glyphs (↑ ↓ ▾) are decoration: wrap in `<span aria-hidden="true">`.
- No arrival animation, no smooth-scroll JS, no scroll-jacking — native fragment
  jump respects `prefers-reduced-motion` by construction (`scroll-behavior` stays
  default).
- Placement: inside `main` after the last content block, not in the footer — it is
  content-adjacent navigation, not chrome.

## 10. Keyboard parity for labeled/annotated marks
Any chart mark that carries a persistent visible label or annotation is a promise of
interactivity — give it `tabindex="0"` + a self-sufficient `aria-label` (name +
value + unit) and show the shared tooltip on focus. This is enhancement on top of,
never a substitute for, a table view as the keyboard-canonical home for the full
dataset. Applies uniformly: once one renderer does it, all renderers do it, or the
inconsistency itself is the a11y bug.
