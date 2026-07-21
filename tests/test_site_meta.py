"""
Publish-readiness of the site's <head>: the share metadata a portfolio link
needs, guarded so it can't silently rot.

These are presence + consistency pins, not content contracts — the point is
that og:url stays the canonical URL, og:image points at a file Pages actually
serves (a broken preview image is the classic share-card bug), and the favicon
stays inline (the page loads no external asset, per the one-file rule).
"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site" / "index.html"
SITE_DIR = REPO / "site"


def _head():
    html = SITE.read_text(encoding="utf-8")
    return html[: html.index("<style>")]


def _meta(head, *, name=None, prop=None):
    attr, val = ("name", name) if name else ("property", prop)
    m = re.search(
        rf'<meta\s+{attr}="{re.escape(val)}"\s+content="([^"]*)"', head
    )
    return m.group(1) if m else None


def test_description_and_title_present():
    head = _head()
    assert "<title>" in head
    desc = _meta(head, name="description")
    assert desc and len(desc) > 40, "meta description missing or too short"


def test_open_graph_tags_present():
    head = _head()
    assert _meta(head, prop="og:title"), "og:title missing"
    assert _meta(head, prop="og:description"), "og:description missing"
    assert _meta(head, prop="og:type"), "og:type missing"
    assert _meta(head, prop="og:url"), "og:url missing"
    assert _meta(head, prop="og:image"), "og:image missing"


def test_twitter_card_present():
    head = _head()
    assert _meta(head, name="twitter:card") == "summary_large_image"
    assert _meta(head, name="twitter:image"), "twitter:image missing"


def test_og_url_matches_canonical():
    head = _head()
    canonical = re.search(r'<link rel="canonical" href="([^"]*)"', head)
    assert canonical, "canonical link missing"
    assert _meta(head, prop="og:url") == canonical.group(1), (
        "og:url and <link rel=canonical> disagree — pick one URL"
    )


def test_og_image_is_served_by_pages():
    # og:image / twitter:image must resolve to a file that ships in site/, or
    # the share card renders broken. Pin the basename to a real file.
    head = _head()
    og_image = _meta(head, prop="og:image")
    twitter_image = _meta(head, name="twitter:image")
    assert og_image == twitter_image, "og:image and twitter:image differ"
    basename = og_image.rsplit("/", 1)[-1]
    assert (SITE_DIR / basename).exists(), (
        f"og:image points at {basename!r} but site/{basename} does not exist"
    )


def test_favicon_is_inline_not_an_external_asset():
    # the page must load no external file; the favicon is an inline data: URI
    head = _head()
    m = re.search(r'<link rel="icon" href="([^"]*)"', head)
    assert m, "favicon <link rel=icon> missing"
    assert m.group(1).startswith("data:"), (
        "favicon must be an inline data: URI (one-file / no-external-asset rule)"
    )
