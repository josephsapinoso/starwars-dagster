---
name: panel-data-analyst-provenance-audit
description: Audit technique for verifying that a claimed number→asset→check provenance map is true before it is displayed. Use whenever the site or docs propose to attribute a displayed number to a pipeline asset or asset check.
---

# Provenance truth audit

Before any UI element attributes a number to a pipeline asset or check, build a
three-column table and verify each row against source, not against the briefing
document:

| Displayed claim | Computing asset (file:line of the actual SQL/code) | Guarding check (exact assertion) |

Classification per row:
- **DIRECT** — the asset's own query computes the quantity, and a check asserts it
  (or its denominator). Safe to badge.
- **FRAME-ONLY** — a check guards a precondition (e.g. "exactly 6 films") but not
  the displayed number itself. Badge the precondition only, labeled as such.
- **ORPHAN** — no asset computes the quantity (it was hand-derived at authoring
  time from raw data). The diagram must attribute it to the raw asset + an
  "authored derivation" step, or a real transform must be added first. Never point
  the arrow at a transform that computes something else with a similar name.

Traps learned in this repo:
- Name similarity lies: `film_character_counts` is characters-per-film, but the
  site's claims are films-per-character. Grain mismatch = false lineage.
- Per-entity vs. per-person grain: `starship_stats.known_pilots` (per ship) cannot
  source "19 of 82 people flew" (per person).
- A terminal asset (`galaxy_report`) may have zero checks — a badge slot there
  renders empty; design for that case rather than inventing coverage.
- Cross-check tests must assert the asset computes the claimed COLUMN/grain, not
  merely that an asset with that name exists in Definitions.
