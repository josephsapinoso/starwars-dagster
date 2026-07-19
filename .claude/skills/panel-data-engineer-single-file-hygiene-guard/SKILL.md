---
name: panel-data-engineer-single-file-hygiene-guard
description: Technique for guarding style-token hygiene (hex colors, font-size scale) in a hand-authored single-file site with one offline pytest structural test - no stylelint, no node, no build step; exceptions live as exact whisper-clause pins, and the test itself is the registry.
---

# Single-file style-hygiene guard (no lint framework)

How to pin "all colors are tokens, all small type is on the scale" for a hand-authored
`site/index.html` when the repo law forbids build steps and second frameworks. This
records the shape that SHIPPED (token-hygiene decision, 2026-07-19, commit a30a5bc;
reference implementation `tests/test_site_style_hygiene.py`) — including where it
differs from the zero-exception design I originally argued.

## Census first, by machine

Never trust a ledger of off-token values — ledgers go stale (2026-07-19: four
"off-token" hexes had already been tokenized a commit earlier). Run the census
yourself before proposing anything:

- Hexes: `rg -n -o '#[0-9a-fA-F]{3,8}\b' site/index.html` → compare line numbers
  against the `:root` block's range.
- Sizes: `rg -n 'font-size' site/index.html` → split CSS declarations from JS
  attribute/cssText occurrences. SVG `font-size` attributes are bare numbers (no
  `px`), so a px-anchored regex will miss them.
- The scan must cover JS, not just `<style>`: in practice every literal residue
  lived in script. A style-only scraper is coverage theater.

## The registry is the test

The panel ruled (5–1, against my token-derivation proposal): do NOT mint `--fs-*`
CSS variables so the test can derive the scale. A rot-proof registry needs to be
EXECUTABLE, not mirrored — a test constant fails when the file drifts, unlike prose
ledgers, and tokens nothing at runtime consumes are the tail wagging the stylesheet.
So the sanctioned scale is a plain set in the test
(`SANCTIONED_SCALE = {11, 12, 13, 14, 16, 17, 18, 42}`), and that set plus the pins
below are the single machine-readable home of the style law.

## Exceptions: the whisper clause, not an allow-list

My "allow-lists rot" objection is answered by making every exception an EXACT pin
that fails loudly on change in either direction:

- Fonts: `EXEMPT_SELECTORS = [(selector_fragment, exact_px, reason), ...]` — the
  test asserts each pinned selector exists at exactly that size (a raise OR a
  shrink breaks it and prints the reason), and any unpinned off-scale size fails.
- Colors: `SANCTIONED_LITERALS = [(hex, required_marker_comment)]` — scenery is not
  ink: a decorative paint (aria-hidden canvas) may stay a literal, but only counted
  exactly once and carrying its sanction comment on the same line. Data ink must be
  tokenized (SVG takes `fill: var(--...)` via a class directly — no bridge needed).
- Singleton brand color: pin the byte-pattern itself — literal exactly once, in
  :root, `rgba(r,g,b,…)` spellings banned (derive with
  `color-mix(in srgb, var(--gold) N%, transparent)`), `var(--gold)` explicitly free.
  Pin bytes, never ceremony.

Why no canvas `getComputedStyle` bridge for the decorative literal: the bridge's
failure mode (init-order race → blank hero canvas) is unguardable offline, while
the pinned literal's failure mode (drift) is exactly what the pin catches. When
both sides' failure modes are real, prefer the side whose failure the guard can see.

## Structure that shipped

One pytest module beside the existing structural checks, module-scoped fixture that:
(1) strips the one-line `const DATA` literal FIRST and asserts it found the line —
the exclusion is load-bearing, and future DATA content must never trip a style
census; (2) extracts `<style>` and `:root`; (3) keeps a "nonstyle" remainder for
the JS scan. Five tests: hex census (everything in :root or sanctioned), sanctioned
literals pinned+commented+counted, gold single-home, CSS sizes on-scale-or-pinned
(with the pin-exists back-assertion), and zero `font-size`/hex-fill in JS or markup
(JS text must set classes, not styles; delete dead style-setting attrs).

## Gotchas

- `clamp()` display sizes are exempt by pattern, not by pin — scope the size
  invariant to fixed values or the regex fights fluid type.
- Convert JS font-size attrs/cssText to classes BEFORE writing the guard, so the
  "no font-size outside `<style>`" invariant is absolute rather than pinned.
- Seen-to-fail is part of landing: plant violations (one per invariant — eight in
  the shipping pass), watch each fail with a readable message, revert.
- A raised SVG label size is a geometry change: the guard proves scale membership,
  not fit. Raise-only grants permission, not obligation — standing still needs no
  evidence; manual narrow-viewport re-verification stays a human step.
