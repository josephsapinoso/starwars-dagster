---
name: panel-data-engineer-derived-glyph-vs-asset
description: The sourcing test for enriching data marks (dots→faces/icons/sprites) on the single-file site. Use whenever a panel proposes making a per-record visual richer than a plain shape. Decides whether the enrichment is derivable data or a new hand-authored source, and names the same-commit guard for each.
---

# Derived glyph vs. hand-authored asset — the sourcing test

When a decision proposes turning a per-record mark (a dot) into something richer (a face,
icon, portrait, sprite, badge), run this BEFORE arguing visuals. The mark IS the data
series, so its new visual carries an implied claim. Ask one question:

**Is the new visual a pure function of data we already have, or a new thing we author?**

## Model B — DERIVED GLYPH (defend this first)
The visual is `f(record)` computed at runtime from existing DATA fields (species, gender,
homeworld, counts...). Properties that make it lawful on a single-file, no-build, drift-
detected site:
- Satisfies derivable-from-inline-JSON: nothing new is stored.
- Drift-safe: change the data, the glyph changes with it — no registry to desync.
- Zero new data bytes: only generator code (write it once).
- Honest by construction: asserts only what the data asserts (an archetype), never a
  likeness/identity we can't back. Dodges the "invented identity" honesty trap.
GUARD (same commit): pytest asserts the generator is a PURE FUNCTION of DATA fields — grep
the JS for a per-name/per-id lookup map; its EXISTENCE is the failure (a hidden second
source). Glyph count == record count; no glyph for an absent record; palette = computed
tints of the sole data hue, no new hex (ride the style-hygiene guard). Extend the runtime
drift detector to cover the new claim.

## Model A — HAND-AUTHORED ASSET (survivable only under governance)
Bespoke art per record with NO producing pipeline asset. It ROTS (upstream add/drop/rename
silently desyncs) and asserts a likeness the pipeline can't verify. Only survivable shaped
like alias governance: a curated registry keyed to the known_facts roster, bidirectional
coverage + injectivity pinned to the frozen fixture, no fuzzy matching. Even then the
likeness-honesty problem stands — say so plainly; it is the panel's call, not a fait accompli.

## Cross-cutting
- No asset check — there's no producing asset; the guard is offline pytest + the runtime
  drift detector, with known_facts as the only roster home.
- Legibility floor is a fact, not a taste: effective-px = css-px × render ratio. A visual
  that needs N px to read cannot be mandated at a size below N; degrade to the plain shape.
- Status is not a series: never encode state (base/dim/faint/hot) with a new hue. Reuse the
  existing opacity/tint transforms; the display-accent color (gold) may FRAME the emphasized
  mark but never FILL it as data.
- Bloat is a budget line: state the byte cost of the chosen encoding, or prefer the encoding
  with zero data cost (procedural).
