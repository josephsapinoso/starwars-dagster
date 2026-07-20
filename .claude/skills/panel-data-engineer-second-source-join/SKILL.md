---
name: panel-data-engineer-second-source-join
description: Checklist for adding a second external data source to a pinned-string,
  provenance-tested Dagster+DuckDB pipeline without widening the blast radius —
  URL-shape honesty, universal-key contracts, unit/sign convention traps, alias
  governance, writer registration, and dual-gated snapshot fixtures.
---

# Adding a second data source to a provenance-pinned pipeline

Run this checklist BEFORE writing the resource. Every item is a place the
starwars-dagster akabab prep (2026-07-20) found a real trap.

## 1. Characterize the source yourself — do not trust the survey
- Fetch the live payload. Count records by listing IDs; check contiguity
  (akabab: 87 records, ids 1..88, id 17 absent — id is an opaque key, never
  an ordinal, never a contiguity check).
- Enumerate fields ACROSS record kinds: schemas are often polymorphic
  (akabab droids carry dateCreated/creator instead of born/died). The
  blocking shape check asserts only the universal keys ({id, name}), nothing
  kind-specific.
- Confirm the license on the source repo, not the survey doc.

## 2. Resource honesty
- New URL shape = new ConfigurableResource. Do not subclass the existing
  resource just to inherit fields when fetch() semantics differ
  ({base}/{endpoint}/ vs {base}/{endpoint}.json) — a subclass claims
  substitutability it doesn't have.

## 3. Convention collisions (the silent killers)
- Units: same field name, different units across sources (SWAPI cm/kg
  strings vs akabab meters/kg numbers) → exclude or convert with a tested
  path; never let both spellings into the warehouse.
- Signs/epochs: one convention per warehouse. If the house column is
  BBY-positive and the source is ABY-positive, normalize at transform time
  with a synthetics-tested sign flip, or name the column so the convention
  is in the name. A bare ambiguous column is a future lie.
- Prose contamination: list fields may embed commentary
  ("Ben Solo (along with a dozen apprentices)") — store as JSON string +
  count; never treat as join keys.

## 4. Join governance
- Exact-name LEFT JOIN from the anchor table; keep all anchor rows.
- Misses go in a curated alias dict in the single facts module (one home),
  seeded only with verified pairs. No fuzzy matching.
- Add a dead-alias pytest: every alias source exists in the new source's
  fixture, every target in the anchor fixture (gated on real snapshots).
- Blocking grain check on the joined asset: rows == anchor count, key
  unique — duplicate source names must never fan out.

## 5. Blast radius of pinned strings and hardcoded rosters
Grep before designing, and prefer the design that leaves pinned files
byte-identical. Standing roster homes to check:
- provenance tests that pin LISTED assets' check sets exactly (attach new
  checks only to UNLISTED assets until the site panel rules);
- totals math (group membership decides the transforms count);
- warehouse access-policy test (a new CREATE OR REPLACE TABLE writer must
  join its hardcoded writer list AND the returned-frame parity loop, same
  commit);
- README/WORKSHOP prose-encoded counts; spoiler-pin vocabulary (write new
  check descriptions number/roster-free even if currently unscanned).

## 6. Fixtures and snapshot plumbing
- Synthetic fixture in the REAL shape, using anchor-source real names so the
  offline join hits; README notes synthetic status + license attribution.
- Each source gets its OWN SNAPSHOT.json marker — existing tests may pin the
  first marker's shape by substring; never merge markers.
- Dual-gate banked tests: source-only facts gate on that source's marker;
  cross-source facts (match counts) gate on BOTH.
- Widen the snapshot workflow's `git add` path and the snapshot script's
  endpoint list; the workflow's post-fetch `pytest -v` remains the CI for
  refreshed fixtures.
