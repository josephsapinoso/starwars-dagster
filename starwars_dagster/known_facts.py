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

# People whose height is the literal string "unknown" (Arvel Crynyd)
EXPECTED_UNKNOWN_HEIGHT_COUNT = 1

# People appearing in exactly one film — most of the census are one-scene wonders
EXPECTED_ONE_FILM_COUNT = 42

# People listed at the controls of at least one starship
EXPECTED_PILOT_COUNT = 19

# Most starships flown by a single character (Obi-Wan Kenobi)
EXPECTED_MAX_STARSHIPS_FLOWN = 5

# Top homeworlds by character count
EXPECTED_NABOO_CHARACTERS = 11
EXPECTED_TATOOINE_CHARACTERS = 10

# The birth registry: people whose birth_year is the literal string "unknown",
# and the oldest dated record (all dated records are BBY in this snapshot)
EXPECTED_UNDATED_BIRTH_COUNT = 39
EXPECTED_DATED_BIRTH_COUNT = 43
EXPECTED_OLDEST_BIRTH_BBY = 896.0
OLDEST_DATED_CHARACTER = "Yoda"

# Keys every raw people record must carry for downstream transforms to work
REQUIRED_PEOPLE_KEYS = {"name", "homeworld", "films", "mass", "gender"}

# Tables star_wars_db must create
EXPECTED_DB_TABLES = {"films", "people", "planets", "starships", "species"}
