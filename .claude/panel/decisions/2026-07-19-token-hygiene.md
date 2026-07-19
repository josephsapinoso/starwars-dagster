# Decision: token hygiene, raise-only type consolidation, and the style guard

Date: 2026-07-19 · Scope: visual/site (first six roles) · Orchestrator: Claude

## Brief (summary)

The graphic-designer's standing proposal. Verified state: the four survey hexes were
already tokenized in 1123757 (the ledger was stale); the remaining literals are JS-only —
`#cdd8ef` canvas starfield fill (~489) and `#fff` gender %-label fill (~1131) — plus two
gold `rgba(255,232,31,…)` leaks (53, 152) found in PREP. Sub-body scale: eight sizes
(10.5–14) plus a 16.5 oddball. New PREP facts: the 11px JS attr (747) is dead code; the
gender labels fail AA (~3.6:1 white on --s1); SVG `fill` takes `var()` directly, canvas
needs a bridge; a JS-blind guard would miss all four literal residues.

## Per-role verdicts (one line each)

- lore-fanatic: split the literals (tokenize data ink, sanction scenery — no bridge for decoration); gold single-home pin shaped "literal exactly once in :root, var() free"; crawl register 12/13/14 untouchable; named allow-list entries, no silent holes.
- data-engineer: tokenize both, no fallback hex; convert all three JS font-size sites to classes; derive the sanctioned scale from `--fs-*` tokens so the guard has zero lists; exclude the DATA line; re-derive the `w > 46` gate with any 11.5 change.
- data-analyst: guard scans JS or it's coverage theater (hard veto); 11.5 is the data-ink stratum — keep it, evidence before any raise; tokenize gender ink, allow-list starfield with a required comment; no font-size tokens; gold exactly once.
- graphic-designer: full integer collapse incl. 11.5→12 retiring the badge exception; zero sanctioned literals anywhere; no font-size tokens (the pytest constant is the registry); geometry riders ship with raises.
- ux-designer: pure raises to {11,12,13,14}; dead attr deleted; the AA fix ships THIS pass (dark ink, else drop in-segment %; "white at 12px is not on the menu"); guard must scan JS; headless re-verify before merge.
- storyteller: merge the prose, exempt the geometry; `.prov-check` 11.5 is the held pause's authored contrast (at 12 the badge merges with summary and chip voice); the whisper clause — exemptions as (selector, exact px, reason) pins that fail loudly in either direction.

## Adjudication

**Q1 — split, 6/6 on the gender ink, 3–3 on the starfield broken toward no-bridge.**
Gender `#fff` becomes a tokenized class AND the AA failure is fixed in the same move
(ux's must-have; the designer's own remedy list included dark ink). Orchestrator's
contrast math: no single ink passes both labeled segments — `--void` on full-strength
`--s1` ≈5.5:1 but ≈3.7:1 on the 75% step; `--ink` ≈4.8:1 on the 75% step but fails on
full s1. Adopted: per-rank ink from the same ladder index that drives segment color
(`--void` on rank 1, `--ink` on tinted ranks), every rendered pair verified ≥4.5:1
computationally at implementation; if any fails, the pre-authorized fallback is dropping
in-segment % (legend + table already carry the data). The starfield stays a literal:
the engineer's allow-lists-rot argument is answered by the storyteller's exact-pin shape
(a pinned entry that drifts FAILS the test), while the bridge's init-order risk on the
hero canvas has no answer — lore/analyst/storyteller carry it. Gold: unanimous — the two
rgba leaks become `color-mix(in srgb, var(--gold) N%, transparent)` (line-1093 idiom) and
the guard pins the gold byte-patterns to exactly once, in :root, with `var(--gold)`
explicitly free (never "no gold in JS" — line 693's tooltip ceremony is settled).

**Q2 — merge the prose, exempt the geometry (storyteller's shape, 4–2 on .prov-check,
3–2 on chart lettering).** CSS raises adopted unanimously: 10.5→11, 12.5→13, 13.5→14,
16.5→17; dead 11px attr (747) deleted; JS sites 1132/1374 converted to classes.
`.prov-check` stays 11.5: the exception is Settled law, four roles hold it, and the
craft argument is decisive — `details.prov summary` is 12 and `.chip` is mono 12, so a
12px badge merges the guard voice into the machinery voice on the rail the held pause
depends on. Chart SVG lettering (.axis-t/.val-t/.anno-t 11.5, .cat-t 12.5, seg-% 11.5
with its `w > 46` gate) is exempted as a pinned geometry tier: raise-only grants
permission, not obligation; the collision/clipping/gate evidence burden is real
(analyst) and unfunded, and nothing regresses by standing still. Ux's fixed-viewBox
stage-legibility observation is noted as a possible future proposal requiring its own
evidence — not smuggled into a hygiene pass.

**Q3 — no font-size tokens, 5–1.** The engineer's rot objection is answered structurally:
the registry lives in an EXECUTABLE test (it fails when the file drifts), unlike the
prose ledgers that rotted. Minting CSS variables to feed a test is the tail wagging the
stylesheet (analyst/storyteller/designer/ux/lore).

**Q4 — one structural pytest, the whisper-clause shape, same commit, seen to fail.**
`test_site_style_hygiene` in the existing suite: (1) strip the one-line `const DATA`
literal before any regex — never mangle it; (2) every hex literal (CSS and JS) lives in
:root, except pinned entries asserted to exist exactly once with their required comment;
(3) gold byte-patterns exactly once; (4) every font-size occurrence — CSS px, JS attrs,
cssText, bare SVG numbers — resolves to the sanctioned integer scale or a pinned
(selector, exact-px, reason) exemption; clamp() exempt by pattern; (5) exemption pins
fail loudly on change in EITHER direction, printing the reason. Seen-to-fail before
landing (planted violation, then reverted).

## Final plan (one commit + verification)

1. site/index.html: gold rgba→color-mix (53, 152); starfield literal gains its
   sanction comment; gender %-labels become class `.seg-pct` (11.5px, per-rank ink
   `--void`/`--ink`) after computational contrast verification; JS caption 1374 becomes
   a class; dead attr 747 deleted; CSS raises 10.5→11, 12.5→13, 13.5→14, 16.5→17.
2. tests/test_site_style_hygiene.py: the guard as specced, same commit.
3. Headless 360/390 pass (raises touch prose only; zero horizontal overflow bar);
   full pytest; seen-to-fail note in the commit message.
4. Republish the artifact to the same URL; BANK pass.

## Newly settled constraints (banked)

- **The whisper clause:** every sanctioned style exception is an exact
  (selector, value, reason) pin in the guard — it fails loudly on change in either
  direction. Unexplained holes are theater; pinned exceptions are law.
- **Scenery is not ink:** decorative paints (aria-hidden canvas) may stay literals with
  a required sanction comment; data ink must be tokenized. No runtime bridges for
  decoration.
- **Ink adapts to its ground:** on-mark labels choose ink per computed ground
  (from the same array that drives the ground), every rendered pair ≥4.5:1, verified
  computationally — never a single ink that fails somewhere, never a new hex.
- **The style registry is the test:** the sanctioned type scale has one machine-readable
  home, the structural pytest — no font-size tokens, no parallel lists.
- **Raise-only grants permission, not obligation:** standing still needs no evidence;
  moving chart geometry does.
