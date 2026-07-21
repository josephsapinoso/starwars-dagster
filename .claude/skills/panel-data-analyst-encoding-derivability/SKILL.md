---
name: panel-data-analyst-encoding-derivability
description: Audit whether a PROPOSED visual mark/encoding asserts a claim the dataset
  can back. Use before adopting any new mark shape, color channel, glyph, or per-item
  visual (faces, icons, textures). Tests three gates a mark must pass to be data-honest.
---

# Encoding-derivability audit

A dot on a chart asserts almost nothing: "a row exists here, positioned by its value."
That is why dots are safe. Richer per-item marks (faces, icons, badges, textures) can
smuggle in claims the data has no column for. Before adopting one, run three gates.

## Gate 1 — Source column exists
For every visual attribute the mark varies per item, name the DATA field it renders.
No field → the attribute is fabricated. A per-character *face* renders "appearance";
if the pipeline JSON has no appearance/face column, every face is non-derivable — it
violates "every displayed thing derivable from inline JSON." Count the fabrication:
"of N items, how many have a verifiable value for this attribute?" If most don't,
the maximal form invents (N − verifiable) claims. State that number; it usually kills
the maximal form on its own.

## Gate 2 — A drift guard is possible
Could a pytest/asset-check assert the attribute is *correct* (not just present)?
For position/opacity it can (recompute from DATA). For an invented visual there is no
ground truth to compare against — the guard can only count sprites, never verify them.
A guard-shaped hole is diagnostic: if correctness is uncheckable, the mark is asserting
something the pipeline can't stand behind. Reuse `guard-failure-modes` to enumerate.

## Gate 3 — The new channel doesn't corrupt an existing one
List the channels the current mark already uses (position, opacity, size, the gold-hot
emphasis state) and what each encodes (here: opacity/color = missing-data + group
membership; gold = superlative). A mark with internal luminance structure (features,
edges) competes with a *uniform-opacity* encoding: at low opacity ".18 = missing" only
reads if the mark is a flat disc; internal contrast breaks the linear opacity→ink map,
so the missing-data mass (denominators like "23 not weighed / 61 elsewhere / 1
unmeasured") stops reading as de-emphasized. Per-item hue (skin tones, species colors)
is a categorical *series* — forbidden where one data hue is law.

## Honest degrade ladder (when appetite exceeds what data backs)
1. Uniform sprite, identical for all items — asserts nothing per-item (same as a dot),
   honest, but re-test Gate 3 (does the shape corrupt opacity?).
2. Rich marks only on the already-named/superlative subset (the labeled + gold-hot
   items) — few, canonical, redundant-but-honest; dots for the rest.
3. Rich marks for all — only if every varied attribute clears Gates 1–3.

Record the fabrication count and the guard-shaped hole in the decision log verbatim.
