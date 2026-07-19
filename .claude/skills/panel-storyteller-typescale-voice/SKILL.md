---
name: panel-storyteller-typescale-voice
description: Storyteller technique for judging typographic scale changes (consolidation, tokenization, raise-only merges) as narrative pacing decisions — which size distinctions carry voice, which are incidental, and which belong to chart geometry instead of typography. Use when a panel topic touches font-size scales, small-type hierarchies, or type tokens on a story-driven page.
---

# Type scale as voice: judging size merges narratively

The typographic hierarchy IS pacing — but size is only one of four register markers.
Judge every merge by whether the VOICE survives, not whether the pixel survives.

## Rules

1. **Voice = case + letterspacing + color tier + family, then size.** A half-pixel
   never carries a voice alone. Before opposing a merge, list the other three markers
   on both selectors; if they still separate the voices, the merge is safe. Oppose
   only merges that make two different voices identical on ALL markers.

2. **Inventory by voice pair, not by size list.** The load-bearing facts are the
   relations: aside < body, sub-head < head, quiet-badge < everything-else-on-its
   surface. Write the pairs down first; a consolidation is acceptable iff every pair
   still holds strictly after the merge map is applied.

3. **The quietest voice on a surface is a narrative asset — never level it up.**
   If a held/pause beat or a disclosure rail depends on one element being the
   quietest string present (the badge, the fine print), raising it to the floor
   flattens the very contrast the beat uses. A sanctioned sub-floor size is not
   scale debt; it is the whisper tier. One such tier, shared, is enough.

4. **In-chart lettering is geometry, not typography.** SVG axis/value/annotation
   labels sit in collision-managed layouts; changing their size reflows staggering
   that was authored to avoid overlaps. Classify them out of the typographic scale
   as an allow-list, and get the project's "collisions are fixed by staggering,
   never by shrinking" practice encoded into the guard — with a reason string per
   exemption so a future shrink fails loudly instead of silently.

5. **Raise-only interacts with hierarchy from below.** Raising a small voice
   narrows its gap to the tier above; check the pair it sits UNDER, not just the
   size it lands on. (13.5→14 under a 16 body: gap 2.5→2, whisper intact via color.
   11.5→12 under a 12 floor: gap 0, voice destroyed.)

6. **If sizes become tokens, name them by role, not pixel.** --fs-caption /
   --fs-fine / --fs-note documents the voice hierarchy in the stylesheet itself;
   --fs-12-5 documents nothing and fossilizes the number. Tokens for kept steps
   only — a token per orphan size just launders the mess.

7. **Scenery colors are not tokens.** A one-use paint inside a canvas (starfield,
   texture) that no other element will ever consume gains nothing from the token
   system, and a runtime bridge (getComputedStyle at init) adds a failure mode to
   the page's opening chord. Sanctioned literal + comment beats indirection when
   the alternative risks the hook. Reused inks on data surfaces DO belong in the
   system.
