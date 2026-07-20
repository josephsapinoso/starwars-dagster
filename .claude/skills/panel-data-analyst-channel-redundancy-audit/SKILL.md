---
name: channel-redundancy-audit
description: Decide whether a degraded or unreachable presentation channel (hover-only titles, sub-legible SVG text, touch-suppressed tooltips) constitutes a data-honesty problem, by enumerating every claim the channel carries and finding each one's readable twin.
---

# Degraded-channel redundancy audit

When a channel that carries data ink is illegible (~<9px effective), hover-only,
or unreachable on some input modality, do NOT reflex to "honesty violation."
Run this audit first; the verdict is per-claim, not per-channel.

## Procedure

1. **Inventory the channel's claims.** Read the source that renders it (for the
   stage: the BUILDERS' `annos`, `axis` text, `cap`, `tip` in site/index.html).
   List every number, name, and null-disclosure it renders. Distinguish
   *computed-from-DATA* strings (e.g. `String(cnt)` from a PEO filter) from
   *hardcoded literals* (e.g. `"everywhere else · 61"`).
2. **Find each claim's readable twin — AT THE SAME GRAIN.** Search beat copy
   (`.step-inner p`), the HTML caption (`.stage-cap` — unscaled HTML,
   aria-live), captions/asides, and dashboard tables (Chart/Table toggle). A
   claim with a readable twin degrades to decoration when the channel fails —
   not deception. A twin only counts if it matches the claim's grain: an
   aggregate table is NOT a twin for a per-person identity channel. Ask what
   claim DIES if this channel dies for one modality — if the answer is "the
   only surface naming these individuals," that is a load-bearing orphan even
   though every number appears elsewhere. (Learned 2026-07-19: my
   "convenience, not access" Q3 framing lost to exactly this — the stage
   tooltip is the sole surface naming most of the 82 people; the census
   conceit is now settled law.)
3. **Classify the residue.** Claims unique to the degraded channel fall into:
   - *derivable*: arithmetic complement of guarded numbers (61 = 82−11−10) —
     acceptable, note it;
   - *texture*: computed secondary values (mid histogram columns) — acceptable;
   - *load-bearing orphan*: a denominator/null/superlative with no other home —
     THIS is the honesty violation; it must gain a readable channel or the
     claim must move.
4. **Check the guard surface for the residue.** Hardcoded channel literals may
   sit outside the drift detector's `expect` map even when their components are
   guarded. If a computed value is locally available (e.g. `rest.length`),
   propose deriving the string — moves it from warned copy to derived number.
5. **Verdict language.** "Accept" is honest iff step 3 found no orphans; say so
   with the inventory attached. Any exposure/bump fix is then a legibility or
   a11y-parity upgrade, argued on those merits — not on honesty.

## Repo-specific traps (verified 2026-07-19)

- `test_site_style_hygiene.py::test_css_font_sizes_resolve_to_scale_or_pins`
  splits rules naively on `}`: declarations inside `@media` are attributed to
  the `@media ...` selector string, so exemption pins (`e[0] in selector`)
  never match there. Consequence: a media-query bump to an OFF-scale value
  (20/22px) fails loudly, but a bump to an IN-scale value (e.g. 18px) for a
  pinned selector passes silently while the base 11.5 pin stays green. Any
  sanctioned media bump needs its own exact-value media pin (or a parser fix)
  in the same commit.
- `.anno-name` is 12px — in `SANCTIONED_SCALE`, not whisper-pinned; it can move
  within the scale with zero guard noise. Don't claim "the guard pins it."
- Provenance `why` strings are verbatim `checks.py description=` projections
  with numbers interpolated from known_facts (NOT number-free), and the spoiler
  pin audits `label + why` per beat — so any new exposure mechanism (focus,
  visible text, aria) inherits spoiler safety for free, provided it renders
  `k.why` verbatim with no paraphrase (a paraphrase would mint a second,
  unguarded copy surface).
