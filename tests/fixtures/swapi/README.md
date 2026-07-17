# SWAPI test fixtures

**These fixtures are SYNTHETIC.** They mimic the raw shape of swapi.info responses
and deliberately include the awkward cases the pipeline must handle:

- `mass: "unknown"` (SWAPI encodes missing numbers as strings)
- a homeworld URL with no matching planet record (LEFT JOIN must keep the row)
- `crew: "30-165"` and `"342,953"` (TRY_CAST must turn these into NULL, not crash)
- exactly six films, episodes 1–6, with list-valued `characters`/`planets`/`starships`

They are intentionally small and are **not** the real dataset — tests that assert
real-world facts (82 people, 23 unknown masses, …) are skipped until a real snapshot
is present.

To replace them with a dated frozen snapshot of the real API, run:

```bash
python scripts/snapshot_fixtures.py
```

which overwrites these files and writes `SNAPSHOT.json` (the marker that activates
the banked-facts tests in `tests/test_pipeline.py`).
