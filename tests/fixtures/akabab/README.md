# akabab test fixtures

**These fixtures are SYNTHETIC.** They mimic the raw shape of
[akabab/starwars-api](https://github.com/akabab/starwars-api) (`/all.json` — MIT
licensed, fan-curated, SWAPI-derived) and deliberately include the awkward cases
the join must handle:

- real SWAPI character names, so the offline LEFT JOIN against the swapi fixtures
  actually matches ("Luke Skywalker" — a full record with affiliations, masters,
  apprentices, and a death on file)
- a case-variant name ("Beru Whitesun Lars" vs SWAPI's as-filed
  "Beru Whitesun lars") — normalization must bridge it
- "Ratts Tyerell": akabab holds the canon spelling, SWAPI holds the typo
  ("Ratts Tyerel") — the curated alias map must bridge it
- a minimal record carrying only `id` + `name` ("Greedo") — every other field is
  optional; the schema is polymorphic
- a droid with empty list fields and no born/died ("C-3PO")
- a sequel-era record with no SWAPI counterpart ("Rey") — the join must count it
  as unmatched, never invent a row
- non-contiguous ids (the real dataset skips ids too — never assert contiguity)
- prose inside `apprentices` ("Ben Solo (along with a dozen other Jedi
  apprentices)") — lineage strings are display-only, never join keys

They are intentionally small and are **not** the real dataset — tests that assert
real-world facts (profile count, join coverage, deaths on file) are skipped until
a real snapshot is present.

To replace them with a dated frozen snapshot of the real API, run:

```bash
python scripts/snapshot_fixtures.py
```

which overwrites `all.json` and writes `SNAPSHOT.json` (the marker that activates
the akabab banked-facts tests; cross-source baselines need BOTH this marker and
the swapi one).
