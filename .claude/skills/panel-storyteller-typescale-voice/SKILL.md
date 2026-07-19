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

7. **The whisper clause — pin exceptions, don't hole them (SHIPPED shape, a30a5bc).**
   Every sanctioned exception to the scale is an exact (selector-fragment, exact-px,
   reason) tuple in the structural guard, asserted to exist at exactly that value:
   a raise OR a shrink fails the test and prints the reason. This converts "allow-list"
   (which rots silently) into "law" (which fails loudly), and it answers the
   allow-lists-rot objection outright — a drifted pin is a red test, not a stale
   comment. As shipped in tests/test_site_style_hygiene.py: `SANCTIONED_SCALE`
   {11,12,13,14,16,17,18,42} plus `EXEMPT_SELECTORS` pinning the geometry tier
   (.axis-t/.val-t/.anno-t 11.5, .cat-t 12.5, .seg-pct 11.5 with its w>46 gate) and
   the whisper tier (.prov-check 11.5, reason citing the held pause). Put the STORY
   rationale in the reason string — the pin then argues for itself at failure time.
   Corollary: bring the drafted pin table to the debate, not just the pin idea.

8. **Raise-only grants permission, not obligation.** A raise-only consolidation never
   obliges pinned geometry to move: standing still needs no evidence; moving
   collision-managed lettering does (clipping, gates, stagger reflow). Use this to
   refuse "while we're at it" raises smuggled into hygiene passes.

9. **The registry is the test, not a token set.** The sanctioned scale's one
   machine-readable home is the executable structural test — it fails when the file
   drifts, unlike prose ledgers or CSS variables minted only to feed a checker.
   Rule 6's role-named tokens apply only IF tokens are wanted for authoring reasons;
   never mint tokens purely to give a guard something to read.

10. **Fixed-viewBox raises are geometry moves — do the unit math first.** In a
   fixed-viewBox SVG, font-size is authored in viewBox units and renders at
   `viewBox-px × (rendered-width / viewBox-width)`; a "css bump" therefore scales
   INSIDE the collision-managed layout, not around it. Before granting any raise:
   (a) compute the needed viewBox px from the target effective size at the
   smallest rendered width; (b) check that number against every authored spacing
   the labels sit in (stacked annotation offsets, gate thresholds like `w > 46`,
   axis tick gaps). If needed-px ≥ authored-spacing, the raise is a stagger
   rework, not a typography change — and if the colliding labels are a payoff
   beat's names, the naive fix breaks the exact moment it meant to save. Bring
   this math to the debate; "raise-only" grants permission only to moves that
   survive it. (Vindicated 2026-07-19: the stage-type raise was accepted
   unanimously on exactly this math plus a channel-redundancy audit — "prose and
   captions are the payoff carriers; annos are deixis." The strongest acceptance
   warrant is redundancy proven by audit, not resignation; pair the collision
   math with a per-claim readable-twin inventory.)

11. **Scenery colors are not tokens.** A one-use paint inside a canvas (starfield,
   texture) that no other element will ever consume gains nothing from the token
   system, and a runtime bridge (getComputedStyle at init) adds a failure mode to
   the page's opening chord. Sanctioned literal + comment beats indirection when
   the alternative risks the hook. Reused inks on data surfaces DO belong in the
   system.
