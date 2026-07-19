---
name: panel-ux-designer-svg-chart-type
description: UX rules for typography and color inside SVG charts — presentation-attribute vs CSS precedence, viewBox-scaled vs measured-px geometry regimes, effective mobile font size, and small-text contrast on colored marks. Use when auditing or changing any font-size, fill, or label inside an inline SVG chart.
---

# Type and color inside SVG charts

Derived from site/index.html during the token-hygiene prep (2026-07-19).

## 1. Presentation attributes lose to ALL CSS
An SVG `font-size="11"` or `fill="#fff"` attribute set from JS is overridden by any
matching CSS rule, however weak (class, element, anything). Audit rule: for every
JS-set style attribute, check whether a CSS rule on the same element makes it dead
code (found live: a `font-size` attr silently overridden by the element's class —
the label rendered at the class size for its whole life). Prefer classes consuming
tokens; attributes are the drift vector no stylesheet review ever sees.

## 2. Two geometry regimes — know which one you're in
- **Fixed viewBox, responsive render** (e.g. a 700-unit-wide stage scaled into a
  480px mobile column): font-size is in viewBox units. Label collisions are
  width-INDEPENDENT (everything scales together — check once, any width), but
  *effective* rendered size = declared × (rendered/viewBox width). A "12px" label
  can really be ~8px on a phone; raising declared size is a mobile legibility win.
- **Measured width** (`viz.clientWidth`, viewBox rebuilt per render): font-size is
  true CSS px. Legibility is constant, but collisions and fit gates (e.g. "label
  only when segment > 46px") are worst at 360px — that's where you re-verify.
A raise-only type consolidation must run BOTH checks: viewBox-relative collision
pass for fixed charts, 360/390px pass for measured charts.

## 3. Small text on colored marks: do the contrast math
In-segment / on-mark labels below ~18.7px bold need 4.5:1 against the mark color.
White on mid-saturation brand hues commonly lands 3–3.6:1 and FAILS; raising the
font size does not fix it. Escapes, in order: dark ink on light-enough segments
(often passes >5:1); move the label outside the mark; rely on a legend/table that
already carries name + value (redundancy softens harm but does not satisfy strict
AA — say so honestly rather than calling it mitigated).

## 4. Token bridges for canvas only
SVG text should get its colors/sizes via classes → CSS → tokens; no JS bridge.
`<canvas>` cannot consume `var()`: read the token ONCE at init via
`getComputedStyle(document.documentElement).getPropertyValue(...)`, cache it in a
const, and never call getComputedStyle inside a rAF loop or resize handler. Works
the same in flat/auto-height iframes. For a purely decorative `aria-hidden` canvas
a commented sanctioned literal is an acceptable alternative to a bridge.
