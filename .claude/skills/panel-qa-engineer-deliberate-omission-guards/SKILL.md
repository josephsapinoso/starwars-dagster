---
name: panel-qa-engineer-deliberate-omission-guards
description: How to make a DELIBERATE technology non-adoption, omission, or "we chose NOT to X" decision a verified artifact instead of unguarded prose. Use when a panel decides against migrating to / adopting a framework idiom (e.g. dagster-duckdb DuckDBResource, Great Expectations) whose adoption would silently erase an existing invariant.
---

# Guarding a deliberate non-adoption (the marker-pin technique)

Banked from the dagster-duckdb non-migration (2026-07-21) and the birth-registry
absence-pin law (2026-07-19). A decision to NOT adopt an idiom is a real
engineering artifact — but prose in WORKSHOP/CLAUDE.md is unguarded and rots. If
adopting the idiom would silently delete an invariant you own, the guard is a
SOURCE MARKER pin, landed with the decision.

## When it applies

Reach for this ONLY when all three hold:
1. A panel deliberately declined to adopt framework idiom X.
2. Adopting X would silently WEAKEN or ERASE an existing tested invariant
   (here: `DuckDBResource.get_connection()` hardcodes `read_only=False`, erasing
   the per-asset read-only single-writer lock).
3. A future well-meaning "modernize to X" refactor is plausible and would look
   locally correct.

If adopting X is merely stylistic with no invariant at stake, do NOT add a marker
— that is vanity guarding. The marker earns its place only as the tripwire on an
invariant deletion.

## The technique

Extend the SAME test that guards the protected invariant (do not add a new test
file). Assert that a stable, decision-naming string is present in the source at
the site of the deliberate choice:

- Pin the invariant AS-IS (unchanged): e.g. `read_only=True` present in
  transforms.py source, executor pinned in-process, writers declared.
- ADD a rationale-marker assertion: the names of the rejected idiom AND the
  reason token must appear in the same source file — e.g. both `"DuckDBResource"`
  and `"read_only=False"` present in `transforms.py`.

Result: a refactor that swaps to the idiom trips BOTH assertions at once. The
person cannot make the test green without deleting the marker, which forces them
to read the decision the marker points to. The invariant pin says "you broke the
lock"; the marker says "and here is why we chose this on purpose — re-read
Module 10 before proceeding."

## Where the rationale lives (three-part landing, one commit)

1. Prose home: a "Why NOT <idiom>?" subsection beside sibling why-nots (WORKSHOP
   Module 10 sits next to "Why NOT Great Expectations"). States the tradeoff both
   ways and "when it WOULD earn its place."
2. A one-line source comment at the choice site that POINTS to the prose (never
   restates it — restated rationale drifts from its source).
3. The marker-pin assertion in the invariant's existing test.

## Distinctions to keep straight

- Marker pin (this) vs absence pin (`test_the_coda_stays_number_free`): both
  guard a CHOICE not wording, but the absence pin asserts a runtime PROPERTY of an
  artifact; the marker pin asserts a decision string is present in SOURCE. Pick by
  what the future refactor touches.
- Pin the CHOICE, never the exact sentence. Assert the rejected idiom's name +
  the reason token are present, not that a prose paragraph matches verbatim —
  verbatim prose pins are theater that break on copyedits.
- Verify the upstream behavior you are guarding against against the ACTUALLY
  installed version, not the library's master branch, before ruling. (In the
  dagster case master happened to match and the lib wasn't even a dependency, but
  that was luck.)
- Always pair the marker with the policy it enforces: "do not modernize without a
  panel." The marker is the tripwire; the panel gate is the resolution.
