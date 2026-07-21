---
name: panel-ux-designer-pictographic-marks
description: UX rules for replacing abstract data marks (dots) with pictographic/sprite marks (icons, faces, glyphs) in an inline SVG chart — legibility floor math at mobile render ratio, graceful degradation so a sprite still reads as a mark when its detail can't resolve, flat-embed parity for a non-circle mark, and honesty limits on what a pictograph asserts. Use for any "make the dots into pictures/faces/icons" ask.
---

# Pictographic marks (turning dots into pictures)

Derived from the "8-bit character faces" census panel (2026-07-20). The stage is a
fixed 700×620 viewBox scaled into a ~312px column at a 360 viewport → render ratio
≈ **.45 mobile**, ≈ **.8–.9 desktop** (two-column). The current mark is a
`circle r=7` (14-unit footprint).

## 1. The legibility floor is fatal to detail at dot footprint — do the math first
Effective on-screen size = (viewBox footprint) × (render ratio). A 14-unit mark:
- Mobile: 14 × .45 ≈ **6.3px total**. An 8×8 sprite = 0.79px/cell; 16×16 = 0.39px/cell.
  Sub-pixel cells are MUD — the reader sees a smudge, not a face.
- Desktop: 14 × .85 ≈ **12px total**. 8×8 = 1.5px/cell — a coarse silhouette at best,
  never a recognizable likeness.
A recognizable 8-bit face needs ~24–32px (3–5× the dot footprint). At that size 82
marks overlap catastrophically in the clustered/histogram beats. **Conclusion: a
recognizable per-character face at every beat is geometrically impossible under the
settled stage geometry — say this with the numbers, not as taste.**

## 2. A pictographic mark must still read as a mark when detail can't resolve
The escape is a sprite whose *silhouette/bounding shape* carries the mark, and whose
interior detail is a bonus that only resolves at large size (desktop, hover/focus
zoom). Design so that at 6px the sprite = a solid filled blob (i.e. it degrades to
the dot it replaced) — never a scatter of loose pixels that reads as noise or dirt.
Test at the FINEST clustered beat, not the sparse hero beat.

## 3. State must survive without a second hue (single-hue law holds)
Base/faint/dim are opacity states on the fill; `hot` is gold — allowed ONLY because
gold is display emphasis on a single mark that is ALSO name-labeled (not a series).
A monochrome (saber-blue) sprite keeps all four states for free (opacity + the one
gold emphasis). Full-color faces (skin tones, Vader-black) would make color a
per-mark series → breaks the sole-data-hue law. Reduced-motion: no frame animation,
no sprite-swap tween; state changes are the existing opacity/transform transitions,
killed under `prefers-reduced-motion` like the dots.

## 4. Flat-embed parity: one shared mark builder, not two
The sticky path builds units ONCE and re-transforms them (`applyState`); `enterFlat()`
REBUILDS every beat's marks inline. Both currently emit `circle r=7`. A sprite must
come from a SINGLE builder both paths call, or an inline `<use href="#sym">` of an
inline `<symbol>` (works identically in both DOM trees, including the flat clone that
lives outside the main svg id). Never hand-inline the sprite in one path only —
that is exactly how a mark silently vanishes in flat mode.

## 5. Honesty: a pictograph asserts identity the data may not have
Most of the 82 have no canonical/verifiable likeness. A per-character invented face
asserts "this is what X looks like" — a claim the pipeline cannot source (data-honesty
violation, same family as the akabab likeness gap). A single generic humanoid glyph
for all 82 is honest but is just a fancier dot — it does NOT deliver "character faces."
The gap between the owner's appetite (recognizable faces, all 82) and what the data
can truthfully assert is the core tension; surface it, don't paper over it.

## 6. Accessibility / naming-surface law is unchanged by the mark shape
The stage tooltip stays the only surface naming most of the 82 (census-conceit veto).
A sprite does not earn 82 `tabindex="0"` marks — settled law gives tabindex only to
marks with a persistent visible label/annotation; the table stays the keyboard-
canonical home. If a face visually implies a name, that implication has no keyboard/AT
path — another reason the honest mark is generic, with identity living in the tooltip.

## 7. Guard in the same commit
A sprite registry needs: one-sprite-per-character integrity, palette hygiene (no hue
outside the single-data-hue + gold budget in sprite paths), and drift-detector
extension if any sprite encodes a datum. If the sprite encodes NOTHING (pure
decoration on a dot), pin that property (absence pin) — no fake guard.
