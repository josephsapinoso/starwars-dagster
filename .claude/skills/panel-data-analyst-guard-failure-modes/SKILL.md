---
name: panel-data-analyst-guard-failure-modes
description: Enumerate distinct failure modes of a displayed number's derivation path before arguing guard count — decides one-guard vs two-guard positions honestly.
---

# Guard failure-mode enumeration

Run this BEFORE taking a position on how many checks a displayed number needs.
Born from the birth-registry 7–1 loss (2026-07-19): I argued one baseline check was
enough; the room proved that without a parse-honesty invariant, "39 undated" can
silently mean "39 unparsed" while the badge glows green.

## The procedure

1. Write the number's full derivation path, stage by stage:
   `source field → parse/cast → transform/join → aggregate → DATA literal → render`.
2. For each stage, name its distinct failure mode:
   - source drift (the data genuinely moved),
   - parse breakage (format change; values silently become null/absorbed),
   - join loss (rows drop; denominators shrink),
   - render drift (copy disagrees with data).
3. For each failure mode, ask: **which existing guard fires, and would it fire
   ALONE?** A guard that only fires when a *different* mode also fires is not
   coverage for this mode.
4. Guard count verdict: two guards are redundant ONLY if they fail for the same
   reason. Economy arguments beat redundancy arguments only in that case —
   otherwise each independent failure mode earns its own guard.

## Key distinctions

- A baseline check (`count == constant`) detects drift but cannot distinguish
  "data moved" from "parser broke": breakage can swell a null-bucket to absorb
  itself, or coincidentally match the constant during partial breakage. The
  number's digits match while its MEANING changed.
- A parse-honesty invariant is data-independent: every null must trace to a
  known raw sentinel (e.g. literal `'unknown'`). It fires on format breakage
  even when the baseline still passes.
- "39 undated" and "39 unparsed" are different claims wearing the same digits —
  this is denominator honesty applied to failure semantics, i.e. MY law, so
  propose the second guard myself rather than ceding the point.
- Trigger phrase: any "parsed display number" invokes the failure-mode
  separation law (settled 2026-07-19) — drift baseline + parse-honesty, always.

## Repo anchors

- Example pair: `character_stats_birth_year_baseline` +
  `character_stats_birth_year_parse_honesty` (both WARN) in
  `starwars_dagster/assets/checks.py`; constants in `known_facts.py`;
  synthetic ABY/fractional/garbage parse tests in `tests/test_transforms.py`.
