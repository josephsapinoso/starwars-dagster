---
name: panel-lore-fanatic-source-scope-audit
description: Lore Fanatic technique for vetting a NEW external Star Wars data source before it joins the pipeline - scope audit (in-saga vs beyond-saga vs Legends), spelling provenance (whose typo is it), and the "as filed" attribution rule. Use when a second source, enrichment API, or join is proposed.
---

# Second-source scope audit

When a new source enriches the six-film census, audit it on three axes BEFORE
debating schema or naming. Run each axis against the actual payload, not the README.

## 1. Scope: which universe frame does each field live in?

Sort every enrichment field into: **in-saga** (events within Episodes I–VI, e.g.
Obi-Wan died 0, "death star, alderaan system"), **beyond-saga canon** (sequel/
anthology facts, e.g. Luke died 34 ABY on Ahch-To), **Legends** (check for known
tells: Chewbacca with a death record = Vector Prime contamination), and **stale**
(canon events the source predates, e.g. no Leia death = pre-TROS vintage).

Consequence: an aggregate over a mixed-frame field ("deceased count") is neither
saga-scoped nor canon-complete. The honest noun is **"on file"** — deaths on file,
allegiances on file — with the frame disclosed wherever the number renders. The
settled "claims must not imply more than the six-episode saga" law is satisfied by
disclosure, not by silently filtering the source (that would be correcting the
record — forbidden).

## 2. Spelling provenance: whose typo is it?

For every join miss, determine which side holds the canon spelling (Wookieepedia
check). A curated alias map is legitimate ONLY as a join device onto the census's
as-filed names; the alias entry must carry a comment naming the canon spelling and
which source misfiled it. The rendered name stays the census's own ("record the
error, never silently correct"). Corollary: if the new source reproduces the old
source's known typos verbatim (akabab: "Ayla Secura", "Beru Whitesun lars"), it is
DERIVED from it — expect near-perfect joins and inherit-not-independent errors.

## 3. Attribution: the source is testimony, not canon

Enrichment values (birth years, affiliations) may disagree with current canon
(akabab Han born -29 vs canon ~32 BBY). The pipeline republishes what the source
filed; copy attributes claims to the profiles, never to "canon." This is the
quoted-testimony rule extended to whole datasets: audit against canon where a gem
depends on it, but render only what's on file.

## Bonus check: does new data upgrade an old gem?

A field arriving in a second source can turn quoted testimony into derivable data
(akabab `died: 4` for Yoda makes 896+4=900 computable). Flag every such upgrade for
the surfacing panel — the gem's render condition changes from "while the quote still
agrees with DATA" to a genuine derived claim with its own guard.
