"""
The learning docs must stay true to the pipeline they describe.

`learn/ELI5.md` and `learn/flashcards.md` restate headline counts (assets,
checks, groups, characters, sources). Per this repo's count-ripple discipline,
a restated number must never drift from the real Dagster definitions and
`known_facts.py`. This guard derives the true values from the live `defs` /
baselines and asserts the docs state exactly those — so changing the pipeline
without updating the study material fails loudly, offline, no network.

It also pins flashcard parity: `flashcards.md` (human-readable Q&A) and
`flashcards.tsv` (Anki import) are generated from one another and must carry
the same number of cards.
"""

import re
from pathlib import Path

from starwars_dagster import defs
from starwars_dagster.known_facts import EXPECTED_PEOPLE_COUNT

REPO = Path(__file__).resolve().parent.parent
LEARN = REPO / "learn"
ELI5 = LEARN / "ELI5.md"
CARDS_MD = LEARN / "flashcards.md"
CARDS_TSV = LEARN / "flashcards.tsv"


def _normalize(text: str) -> str:
    """Strip markdown emphasis/code markers and collapse whitespace so the
    assertions match on plain phrasing, not on `**bold**`/`code` decoration."""
    text = text.replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", text)


def _real_counts():
    graph = defs.resolve_asset_graph()
    keys = list(graph.get_all_asset_keys())
    groups = {}
    for k in keys:
        g = graph.get(k).group_name
        groups[g] = groups.get(g, 0) + 1
    blocking = warn = 0
    for checks_def in defs.asset_checks:
        for spec in checks_def.check_specs:
            if spec.blocking:
                blocking += 1
            else:
                warn += 1
    return {
        "assets": len(keys),
        "groups": groups,
        "checks": blocking + warn,
        "blocking": blocking,
        "warn": warn,
        "sources": len(defs.resources),
        "people": EXPECTED_PEOPLE_COUNT,
    }


def test_eli5_counts_match_the_real_pipeline():
    c = _real_counts()
    text = _normalize(ELI5.read_text(encoding="utf-8"))
    expected = [
        f"{c['assets']} assets",
        f"{c['checks']} asset checks",
        f"{c['blocking']} blocking",
        f"{c['warn']} warn",
        f"{c['people']} characters",
        f"{c['sources']} upstream sources",
    ]
    # per-group breakdown, phrased "<group> = <count>" in ELI5.md
    expected += [f"{g} = {n}" for g, n in c["groups"].items()]
    missing = [p for p in expected if p not in text]
    assert not missing, (
        f"learn/ELI5.md is out of sync with the pipeline; these derived facts "
        f"are not stated as written: {missing}"
    )


def test_flashcards_counts_match_the_real_pipeline():
    c = _real_counts()
    text = _normalize(CARDS_MD.read_text(encoding="utf-8"))
    expected = [
        f"{c['assets']} assets",
        f"{c['checks']} asset checks",
        f"{c['blocking']} blocking",
        f"{c['warn']} warn",
        f"{c['people']} characters",
    ]
    missing = [p for p in expected if p not in text]
    assert not missing, (
        f"learn/flashcards.md is out of sync with the pipeline; these derived "
        f"facts are not stated as written: {missing}"
    )


def test_flashcard_files_are_in_lockstep():
    md = CARDS_MD.read_text(encoding="utf-8").splitlines()
    q = sum(1 for line in md if line.startswith("**Q:**"))
    a = sum(1 for line in md if line.startswith("**A:**"))
    assert q == a, f"flashcards.md has {q} questions but {a} answers"

    tsv_rows = [
        line
        for line in CARDS_TSV.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]
    assert len(tsv_rows) == q, (
        f"flashcards.tsv has {len(tsv_rows)} cards but flashcards.md has {q}; "
        f"regenerate the TSV from the Markdown so they stay in lockstep"
    )
    for row in tsv_rows:
        cols = row.split("\t")
        assert len(cols) == 2, f"TSV row is not two tab-separated columns: {row!r}"
        assert cols[0].strip() and cols[1].strip(), f"TSV row has an empty cell: {row!r}"
