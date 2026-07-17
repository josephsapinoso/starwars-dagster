"""
Known facts about the SWAPI dataset — the single source of truth for
every expected value used by tests and asset checks.

These were verified by hand against swapi.info (the films 1-6 dataset).
They are DRIFT BASELINES, not contracts: if SWAPI adds person #83, the
pipeline should warn, not break. Exact-value assertions belong in pytest
against a frozen fixture snapshot; live asset checks compare against these
with WARN severity.
"""

# Total people records returned by /api/people/
EXPECTED_PEOPLE_COUNT = 82

# Films in the dataset (episodes 1-6; swapi.info has no sequel-trilogy films)
EXPECTED_FILM_COUNT = 6
EXPECTED_EPISODE_IDS = {1, 2, 3, 4, 5, 6}

# The only characters appearing in all six films — famously NOT just the droids
SIX_FILM_CHARACTERS = {"C-3PO", "R2-D2", "Obi-Wan Kenobi"}

# People whose mass is the literal string "unknown" in the raw data
EXPECTED_UNKNOWN_MASS_COUNT = 23

# Top homeworlds by character count
EXPECTED_NABOO_CHARACTERS = 11
EXPECTED_TATOOINE_CHARACTERS = 10

# Keys every raw people record must carry for downstream transforms to work
REQUIRED_PEOPLE_KEYS = {"name", "homeworld", "films", "mass", "gender"}

# Tables star_wars_db must create
EXPECTED_DB_TABLES = {"films", "people", "planets", "starships", "species"}
