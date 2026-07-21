"""
The resolving mark: guards for the 8-bit character faces on the census stage.

A census dot resolves into a monochrome silhouette ONLY on a beat where the
story already names that character (decision 2026-07-21-8bit-character-faces).
The honesty floor is structural: a sprite may exist ONLY for one of the six
named/emphasized marks, it must map to a real census person, and it must never
introduce a color — it inherits the four `.unit` states. The narrative floor is
the spoiler pin: the three all-six-films witnesses never resolve before their
own beat, so no earlier beat leaks the reveal through the eye.

These pins fail loudly on drift in EITHER direction — a seventh face, a missing
sprite, an early witness resolve, or a face given its own fill all trip a test.
Extending the roster requires a panel, not a commit.
"""

import json
import re
from pathlib import Path

from starwars_dagster.known_facts import (
    OLDEST_DATED_CHARACTER,
    SIX_FILM_CHARACTERS,
)

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site" / "index.html"

# The only marks the census names in copy, and therefore the only marks that
# may carry a face. A seventh entry is a design decision, not a code change.
NAMED_MARKS = {
    "Yoda",
    "Yarael Poof",
    "Jabba Desilijic Tiure",
    "C-3PO",
    "R2-D2",
    "Obi-Wan Kenobi",
}
# Beat indices into BUILDERS, pinned to the beat each character is named on.
HEIGHT_BEAT, MASS_BEAT, WITNESS_BEAT, PILOT_BEAT = 1, 2, 5, 6


def _html():
    return SITE.read_text(encoding="utf-8")


def _json_const(name, html):
    m = re.search(r"const %s = (\{.*?\});" % name, html, re.S)
    assert m, f"const {name} = {{...}} literal missing from the site"
    return json.loads(m.group(1))


def _faces(html):
    return _json_const("FACES", html)


def _face_beats(html):
    return _json_const("FACE_BEATS", html)


def _data_people_names(html):
    m = re.search(r"^const DATA = (\{.*\});$", html, re.M)
    assert m, "one-line const DATA literal missing"
    return {p["name"] for p in json.loads(m.group(1))["people"]}


def test_rosters_agree_and_are_exactly_the_named_marks():
    html = _html()
    faces, beats = _faces(html), _face_beats(html)
    assert set(faces) == set(beats), "FACES and FACE_BEATS rosters disagree"
    assert set(faces) == NAMED_MARKS, (
        "the face roster changed — a face may exist ONLY for a mark the census "
        "names in copy; a new face is a panel decision (see the 2026-07-21 log)"
    )


def test_every_sprite_maps_to_a_real_census_person():
    html = _html()
    people = _data_people_names(html)
    orphans = sorted(n for n in _faces(html) if n not in people)
    assert not orphans, f"sprites with no census record (fabricated identity): {orphans}"


def test_face_beats_match_where_each_mark_is_named():
    # every face appears exactly on the beat(s) the character is named/emphasized
    beats = _face_beats(_html())
    assert beats["Yoda"] == [HEIGHT_BEAT]
    assert beats["Yarael Poof"] == [HEIGHT_BEAT]
    assert beats["Jabba Desilijic Tiure"] == [MASS_BEAT]
    assert sorted(beats["Obi-Wan Kenobi"]) == [WITNESS_BEAT, PILOT_BEAT]


def test_beat_indices_match_the_builders_order():
    # the pinned indices above must be the ACTUAL positions in BUILDERS, or the
    # faces would resolve on the wrong beat while every assertion still passed
    html = _html()
    m = re.search(r"const BUILDERS = \[([^\]]+)\]", html)
    assert m, "BUILDERS array missing"
    order = [b.strip() for b in m.group(1).split(",")]
    assert order.index("stHeight") == HEIGHT_BEAT
    assert order.index("stMass") == MASS_BEAT
    assert order.index("stWitnesses") == WITNESS_BEAT
    assert order.index("stPilots") == PILOT_BEAT


def test_witnesses_never_resolve_before_their_reveal():
    # the spoiler pin: the three all-six-films characters (the beat-5 payoff)
    # must not show a face on any earlier beat, or the reveal leaks by eye
    beats = _face_beats(_html())
    assert SIX_FILM_CHARACTERS <= set(beats), "a witness lost its sprite schedule"
    for w in SIX_FILM_CHARACTERS:
        assert min(beats[w]) == WITNESS_BEAT, (
            f"{w} resolves on beat {min(beats[w])} < {WITNESS_BEAT} — that leaks "
            "the witnesses reveal before it is earned"
        )


def test_roster_is_anchored_to_known_facts():
    # tie the roster to the single baseline source, not a transcribed list
    faces = set(_faces(_html()))
    assert SIX_FILM_CHARACTERS <= faces, "the three witnesses must carry faces"
    assert OLDEST_DATED_CHARACTER in faces, "Yoda (height beat) must carry a face"


def test_bitmaps_are_wellformed_1bit_grids():
    for name, rows in _faces(_html()).items():
        assert rows, f"{name} has an empty sprite"
        width = len(rows[0])
        assert 1 <= width <= 16, f"{name} grid width {width} out of range"
        assert len(rows) <= 16, f"{name} grid taller than 16 rows"
        assert all(len(r) == width for r in rows), f"{name} rows are ragged"
        assert all(set(r) <= {".", "#"} for r in rows), f"{name} has non-1-bit cells"
        assert any("#" in r for r in rows), f"{name} sprite is blank"


def test_a_face_never_introduces_a_color():
    # the silhouette must inherit the four .unit states, never carry its own
    # fill — otherwise a face becomes a new color seat (breaks the one-hue law)
    html = _html()
    style = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
    for state in (
        r"\.unit circle, \.unit \.face",
        r"\.unit\.dim circle, \.unit\.dim \.face",
        r"\.unit\.faint circle, \.unit\.faint \.face",
        r"\.unit\.hot circle, \.unit\.hot \.face",
    ):
        assert re.search(state, style), (
            f"state rule {state!r} does not cover .face — the silhouette would "
            "not inherit the dot's fill/opacity state"
        )
    # the face never names its own paint: any rule that sets a fill AND touches
    # .face must be a shared `.unit` state rule (so the silhouette borrows the
    # dot's paint). A standalone `.face { fill: ... }` would be a new color seat.
    for rule in style.split("}"):
        selector, _, body = rule.partition("{")
        if ".face" in selector and "fill" in body:
            assert ".unit" in selector, (
                f"a .face fill rule ({selector.strip()!r}) is not a shared .unit "
                "state rule — that is a new color seat for the silhouette"
            )
