# Decision: 8-bit character faces as the census mark

Date: 2026-07-21 · Scope: pure visual/site · Panelists: the first six
(lore-fanatic, data-engineer, data-analyst, graphic-designer, ux-designer, storyteller).
Orchestrator/final decision: Claude (main session).

## Brief

The owner asked to replace the census story's dots with 8-bit character faces, "a lot
more fun." Stated appetite (chosen explicitly): **ALL 82 marks become faces, every beat**
— the maximal form. Current state: the census scroll story renders 82 `.unit` circles,
one per tracked character — the sole data-series mark — repositioned/re-classed across 8
beats (`site/index.html:766,774-808`). Mark states (`:89-92`): base saber-blue `--s1`;
`.dim` ink-3; `.faint` .18 opacity; `.hot` gold. Gold = "the one to look at," always
direct-labeled. Stage tooltip is the sole surface naming most of the 82 (banked census
conceit). Banked laws bearing on this: one HTML file / no external assets; saber-blue is
the sole data hue, gold is display-accent-only, no per-item hue; mark legibility floor;
every mark derivable from inline JSON; reduced-motion + mobile + flat-embed parity; a
feature and its guard land in the same commit. Full brief in the session scratchpad.

The pipeline holds **zero portrait data** — SWAPI has no image field; akabab's `image`
URL is a banned external asset surfaced nowhere. Every face is authored-from-nothing.

## Per-role verdicts (one line each)

- **lore-fanatic**: VETO maximal — all-82 forces invented portraits (~60 obscure
  characters have no canonical face) or species-archetype stamps (distinct people drawn
  identically, inherits clerical errors like R4-P17-filed-Human). Faces only where a
  canonical silhouette EXISTS and the mark is already named; else a labeled dot. Saber-blue
  monochrome only; color-IS-identity so no amendment.
- **data-engineer**: VETO maximal — a face is a likeness the JSON can't derive; an all-82
  sprite registry is "a second data file in disguise" that rots against SWAPI drift and no
  asset check can assert. Even a procedural glyph f(species) is a per-item channel; back the
  resolve, constrain the target to a bounded, guarded set — not likeness for all 82.
- **data-analyst**: VETO maximal — each beat's mark state encodes THREE facts (missing-data
  via opacity, group via base/faint, superlative via gold); a face's internal luminance at
  .18/~3px breaks the missing-data signal; ~60 fabricated identities have no possible
  correctness guard (guard-shaped hole = the tell). No per-item hue, no species glyph.
- **graphic-designer**: VETO maximal — full-color = double veto (new color seats + a
  likeness claim). A face carries base/dim/faint/hot for free ONLY as a SINGLE-fill path
  (outline/two-tone breaks dim/faint). Pixels = compact 1-bit bitmap on the subset only,
  decoded to one `<path>`, one shared builder. Sprite registry needs a same-commit guard.
- **ux-designer**: VETO maximal — geometrically impossible: a face at dot footprint is
  ~3–6px (mud); a readable 8-bit face needs ~24–32px and 82 overlap catastrophically. The
  graceful, legible form is faces only on the featured/named marks at their emphasis size;
  one shared builder (sticky + flat); resolve is a static state, never a tween.
- **storyteller**: VETO maximal — turns a census into a cast poster, kills the gold pointing
  gesture, and leaks the beat-5 witnesses reveal through the eye. The mark should RESOLVE
  into a face at the instant it goes hot/named — delight as a reveal mechanic, not wallpaper;
  beat 5 (three anonymous dots → C-3PO, R2-D2, Obi-Wan) becomes the best beat on the site.

## Adjudication

**Unanimous, on four independent grounds** — honesty (no portrait source for ~60 of 82),
legibility (illegible at mark footprint; recognizable faces overlap), color law (per-item
hue is a forbidden series), narrative (destroys the census conceit and leaks the payoff).
Literal all-82 distinct faces has no honest form; a *shared* all-82 face-shape that
degrades to a blob is, as the storyteller put it, "the dot with extra nodes" — no delight.
So the maximal ask is not delivered as asked.

**Two sub-fights resolved:**
1. *All-82 shared silhouette (UX/GD framing) vs. resolve-on-named (storyteller).*
   Storyteller wins: a generic face-shape identical for 82 asserts nothing and reads as a
   dot; a per-character all-82 is impossible. Base marks stay uniform dots.
2. *Procedural glyph f(species) (data-engineer) vs. curated sprite (analyst/GD/lore).*
   Analyst/lore win the honesty point: species ≠ face, species is sparse, and a
   field-varying glyph is a per-item channel that cross-talks with the beat encoding
   (beat 3 already groups by homeworld). Engineer's underlying value — no rotting
   unguardable second source — is honored by making the sprite set *tiny and 1:1 guarded*,
   not by making it procedural.

## Final plan — "The Resolving Mark"

1. **Base mark unchanged.** All 82 stay uniform saber-blue `.unit` dots at rest, every
   beat. The census conceit and the missing-data opacity ladder are untouched.
2. **A mark resolves into a monochrome 8-bit silhouette exactly on the beats where it is
   directly named in an annotation** — i.e. the mark already asserts that identity in copy.
   The full named set across all 8 beats is **six characters**: Yoda + Yarael Poof (height
   labels, base/blue), Jabba (mass, hot/gold), C-3PO + R2-D2 + Obi-Wan (witnesses, hot/gold;
   Obi-Wan again on pilots, hot/gold). No other mark ever resolves.
3. **Single fill.** The silhouette is one `<path>` swapped in for the `<circle>`, so all
   four states ride the existing CSS for free: a hot named mark is a **gold-filled
   silhouette** (the face IS the one emphasis seat — no gold-among-81 problem); a base named
   mark (Yoda, Poof) is a **saber-blue silhouette**. No outline, no second tone, no skin
   tone, zero new color seats.
4. **Pixels live** as a compact 1-bit bitmap string on a curated registry keyed to
   `known_facts` canonical names — six entries — decoded once to a single path, cached,
   emitted by ONE shared builder that both `applyState` (sticky) and `enterFlat` (flat) call.
   Not on the 82. Not procedural. Faces degrade to a blob (= the dot) if ever rendered small.
5. **Reduced-motion / a11y / tooltip.** Resolve is a static state class, no morph/tween. No
   new tabindex (label-only rule preserved). The stage tooltip stays the sole naming surface
   for all 82. Scatter (`:1227`) and birth-strip (`:1385`) stay dots — different legibility
   regime, held out of v1.
6. **Same-commit guard (offline pytest):** sprite-registry integrity — (a) a sprite exists
   ONLY for a character that is named/annotated on some beat and is in `known_facts` (a
   sprite for an anonymous mark = ERROR); (b) injective (one sprite per character); (c)
   palette hygiene: sprite fill comes only from the state classes/tokens, no hex, no skin
   tone; (d) decode is a pure deterministic function → single path; (e) drift detector gains
   an entry: a named-iconic mark that lost its sprite, or a sprite whose character is no
   longer named on any beat, trips it; (f) the beat-5 spoiler pin extends to the three
   witness sprites — no earlier beat may resolve a witness mark. Feature + guard, one commit.

## Newly settled constraints (candidates to bank)

- **The census population is anonymous dots; identity is earned, not default.** A mark may
  gain a face ONLY on a beat where the story already names it in copy. Faces are a reveal
  mechanic, never a population reskin. (Kills any future "faces for all 82.")
- **Faces are single-fill monochrome silhouettes** that inherit the four mark states; no
  outline, no second tone, no per-item hue, no skin tone; a hot face is gold (the one
  emphasis seat). Sourcing is a tiny curated 1:1-guarded registry, never procedural-by-field
  and never an external image.
- **A sprite asserts only what the adjacent name already asserts.** No sprite for an
  unnamed/anonymous mark; ~60 obscure characters stay dots. The registry lands with its
  integrity guard in the same commit.
