"""
Style hygiene: every color literal lives in :root, and every font-size
resolves to the sanctioned scale or a pinned exception.

The registry IS this test (token-hygiene decision, 2026-07-19): the
sanctioned type scale and the whisper-clause exemptions below are the
single machine-readable home of the style law — no CSS variable layer, no
parallel list. Each exemption is an exact (selector, value, reason) pin
that fails loudly if the value moves in EITHER direction, so a sanctioned
exception can neither erode nor silently spread.

The scan covers CSS *and* JS: all four literal residues this guard was
built against lived in script, not <style> — a style-only scraper would
be coverage theater. The one-line `const DATA` literal is stripped before
any regex; it is load-bearing and never regex-mangled.
"""

import re
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site" / "index.html"

# integer scale (px) for fixed font sizes; clamp() display sizes are exempt
# by pattern. 16 is body prose, 18 glyph arrows, 42 the KPI figure.
SANCTIONED_SCALE = {11, 12, 13, 14, 16, 17, 18, 42}

# whisper clause: (selector fragment, exact px, reason). Exact-value pins —
# a raise OR a shrink of any entry fails this test and prints the reason.
EXEMPT_SELECTORS = [
    (".axis-t", 11.5, "data-ink stratum — chart geometry, stagger never shrink"),
    (".val-t", 11.5, "data-ink stratum — value labels sit at x+7, raise risks clipping"),
    (".anno-t", 11.5, "data-ink stratum — annotation rows are collision-staggered"),
    (".cat-t", 12.5, "chart geometry — SVG category labels"),
    (".seg-pct", 11.5, "chart geometry — the gender fit gate (w > 46) is tuned to it"),
    (".prov-check", 11.5, "whisper tier — the held pause's authored contrast (Settled)"),
]

# sanctioned off-token color literals: (literal, required marker comment).
# Scenery is not ink: decorative paints may stay literals, but only named,
# commented, and counted — exactly one occurrence each.
SANCTIONED_LITERALS = [
    ("#cdd8ef", "scenery, not ink"),
]

HEX_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b")


@pytest.fixture(scope="module")
def doc():
    html = SITE.read_text(encoding="utf-8")
    lines = html.split("\n")
    body = "\n".join(l for l in lines if not l.startswith("const DATA = "))
    assert len(body) < len(html), "const DATA line not found — exclusion is load-bearing"
    m = re.search(r"<style>(.*?)</style>", body, re.S)
    assert m, "style block missing"
    style = m.group(1)
    root = re.search(r":root\s*\{(.*?)\}", style, re.S)
    assert root, ":root token block missing"
    return {"body": body, "style": style, "root": root.group(1),
            "nonstyle": body.replace(style, "")}


def test_every_hex_literal_lives_in_root(doc):
    outside = [h for h in HEX_RE.findall(doc["body"])
               if h not in HEX_RE.findall(doc["root"])]
    sanctioned = {lit for lit, _ in SANCTIONED_LITERALS}
    strays = [h for h in outside if h not in sanctioned]
    assert not strays, f"hex literals outside :root (mint a token): {strays}"


def test_sanctioned_literals_are_pinned_and_commented(doc):
    for lit, marker in SANCTIONED_LITERALS:
        sites = [l for l in doc["body"].split("\n") if lit in l]
        assert len(sites) == 1, f"{lit} must appear exactly once, found {len(sites)}"
        assert marker in sites[0], (
            f"{lit}'s sanction comment ({marker!r}) is missing — an uncommented "
            "hole is coverage theater"
        )


def test_gold_has_exactly_one_home(doc):
    # the literal lives in :root alone; var(--gold) and color-mix derivations
    # are free — the pin is on the byte pattern, never on ceremony.
    assert doc["body"].count("#ffe81f") == 1, "gold literal must appear exactly once"
    assert "#ffe81f" in doc["root"], "gold's one home is :root"
    assert "255,232,31" not in doc["body"], (
        "gold rgba() leak — derive with color-mix(in srgb, var(--gold) ...) instead"
    )


def test_css_font_sizes_resolve_to_scale_or_pins(doc):
    exempt_px = {}
    for rule in doc["style"].split("}"):
        if "{" not in rule:
            continue
        selector, _, decls = rule.partition("{")
        for m in re.finditer(r"font-size:\s*([\d.]+)px", decls):
            px = float(m.group(1))
            pin = next((e for e in EXEMPT_SELECTORS if e[0] in selector), None)
            if pin is not None and px == pin[1]:
                exempt_px.setdefault(pin[0], px)
                continue
            assert px in SANCTIONED_SCALE, (
                f"{px}px in {selector.strip()!r} is outside the sanctioned scale "
                f"{sorted(SANCTIONED_SCALE)} and matches no exemption pin"
            )
    for sel, px, reason in EXEMPT_SELECTORS:
        assert exempt_px.get(sel) == px, (
            f"exemption pin broken: {sel} must be exactly {px}px ({reason})"
        )


def test_no_style_literals_outside_the_style_block(doc):
    js = "\n".join(
        l for l in doc["nonstyle"].split("\n")
        if not any(lit in l for lit, _ in SANCTIONED_LITERALS)
    )
    assert not re.search(r"font-size", js, re.I), (
        "font-size set from JS/markup — style lives in <style>; use a class"
    )
    assert not re.search(r"(fillStyle|fill)\s*[:=]\s*[\"']#", js), (
        "hex fill in JS — data ink must consume tokens (var(--...)); "
        "scenery literals are individually sanctioned above"
    )
