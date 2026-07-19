---
name: panel-data-engineer-single-file-hygiene-guard
description: Technique for guarding style-token hygiene (hex colors, font-size scale) in a hand-authored single-file site with one offline pytest structural test - no stylelint, no node, no build step, no allow-lists.
---

# Single-file style-hygiene guard (no lint framework)

How to pin "all colors are tokens, all small type is on the scale" for a hand-authored
`site/index.html` when the repo law forbids build steps and second frameworks.

## Census first, by machine

Never trust a ledger of off-token values — ledgers go stale (2026-07-19: four
"off-token" hexes had already been tokenized a commit earlier). Run the census
yourself before proposing anything:

- Hexes: `rg -n -o '#[0-9a-fA-F]{3,8}\b' site/index.html` → compare line numbers
  against the `:root` block's range.
- Sizes: `rg -n 'font-size' site/index.html` → split CSS declarations from JS
  attribute/cssText occurrences. SVG `font-size` attributes are bare numbers (no
  `px`), so a px-anchored regex will miss them.

## Design for a zero-allow-list invariant

The strongest guard has NO exception list, because exception lists are a second
registry that rots. Get there by moving facts, not by widening the test:

1. JS color literals → one `getComputedStyle(document.documentElement)
   .getPropertyValue('--token')` read at init (once, never per-frame). Runtime, not
   a build step. No hard-coded fallback hex in the JS — a fallback is a second home
   for the value. Canvas is the only consumer that genuinely needs the bridge; SVG
   text can take a class with `fill: var(...)` instead.
2. JS font-size attributes/cssText → classes, so every font-size fact lives in
   `<style>` alone and the test's scope claim ("scrape the style block") is honest.
3. Sanctioned scale → if the kept steps are `:root` tokens, the test DERIVES the
   allowed set from the `:root` block instead of hard-coding a parallel list. One
   home for the scale; a merge edits one line.

Resulting invariants, one pytest test beside the existing structural checks
(doctype/lang precedent at tests/test_site_provenance.py:103):

- every hex literal in the file sits inside the `:root` block;
- no `font-size` occurrence outside `<style>`;
- every sub-body font-size literal in `<style>` is (or resolves to) a `:root` step.

## Gotchas

- Exclude the one-line `const DATA` literal before regexing the file — its
  load-bearing one-line strict-JSON format makes extraction trivial, and future DATA
  content must never trip a style census.
- `clamp()` display sizes are not scale members; scope the size invariant to fixed
  sub-body values or the regex fights fluid type.
- `rgba(...)` literals are a separate tokenization question — flag, don't let the
  hex guard's scope silently expand mid-review.
- A raised SVG label size is a geometry change: the guard proves scale membership,
  not fit. Manual narrow-viewport re-verification stays a human step.
