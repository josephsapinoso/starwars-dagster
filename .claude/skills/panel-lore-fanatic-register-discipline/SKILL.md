---
name: panel-lore-fanatic-register-discipline
description: Lore Fanatic technique for judging Star Wars copy on this project - the two-register rule separating in-universe story voice from out-of-universe machinery voice. Use when evaluating labels, reveal summaries, badges, or README copy for authenticity vs kitsch.
---

# Register discipline: the two-voice rule

The site earns its fandom by keeping two registers strictly apart. Apply this test to
any proposed label, badge, or copy before debating aesthetics.

## The registers

1. **In-universe (the census audit).** The story beats speak as a Republic/Empire
   records office: "The measuring", "The weighing", "the census", "paperwork
   problems". Star Wars facts live here and must be canon-precise (the six-film
   trio is C-3PO, R2-D2, AND Obi-Wan).
2. **Out-of-universe (the machine shop).** Anything about how the page was built —
   SQL reveals, lineage diagrams, asset checks, README — speaks plain engineering:
   "Show the DuckDB SQL", "The pipeline that made this page". No Star Wars dressing
   here at all; the restraint IS the signal.

## The test

For any proposed copy, ask which register the element belongs to:

- Is it narrating the DATA (characters, films, planets)? → in-universe allowed,
  canon-checked, load-bearing only.
- Is it exposing the MACHINERY (assets, checks, SQL, CI)? → engineering register.
  A single bridge word from the audit conceit ("paper trail", "the record behind
  this number") is permitted because the census conceit is the story's spine —
  but never a joke, quote, or icon from the films.

## Automatic vetoes (kitsch)

- Aurebesh or film iconography decorating diagrams or badges.
- Status/severity encoded as allegiance or lightsaber colors; crawl gold (#ffe81f)
  as any status or data color — gold is display ceremony only.
- Quote-jokes in machinery copy ("these aren't the rows you're looking for").
- Yoda-speak, misattributed lines, "just the droids".

## Corollary: one home per fact — precision lives in the reference

(Rewritten after the post-landing-cleanup decision, 2026-07-18, which overruled the
earlier "sequence the quotation" version of this corollary.)

The primary source for a canon roster or payoff number is `known_facts.py`, NOT any
prose that mentions it. A check description that hand-lists a roster (e.g. naming the
six-film trio) is a SECOND home — a drift bug that can make the Dagster UI lie if the
snapshot changes. "Matches known_facts.SIX_FILM_CHARACTERS" is more precise than the
prose list, not vaguer: fidelity can live in a derived reference; verbatimness is not
the only form of fidelity. The particulars still surface truthfully at runtime via
check metadata computed from known_facts.

Settled shape: descriptions state the invariant and its stakes; metadata carries the
particulars; the rail renders uniformly (all checks of the chain assets) and spoiler
safety lives in the strings, enforced by the spoiler pin test whose term sets are
DERIVED from known_facts — never hand-listed. This is not bowdlerizing: nothing canon
was scrubbed from the system, only de-duplicated into its single verifiable home.

Audit tips that survive from the old corollary: on shared chains, every upstream beat
inherits every downstream claim's check strings — audit ALL forward leaks, not just
the loudest one. And never add hand-authored narrative fields (beat indexes, story
attribution) to provenance; if pytest can't verify it against the real definitions,
it doesn't belong on the machine-checked object.

## Corollary: quoted testimony, not derived data (banked 2026-07-19)

External claims — film dialogue, canon numbers — may be *audited* in site copy but
never rendered as if the pipeline derived them. Derived numbers come only from DATA;
a canon number enters as testimony the census checks against its records. The model:
the registry's Yoda line — "filed at 896 BBY — his own count, nine hundred years,
checks out" — where 900 is Yoda's RotJ self-report (896 BBY + 4 ABY death = 900) and
the line renders ONLY while DATA still shows 896 as the oldest. If the record moves,
the audit line vanishes rather than lie.

Practical rule: for any canon number proposed for the page, arrive with three things —
the fact, the source quote verified, and the RENDER CONDITION (when it appears, when
it must disappear). Data-conditional copy is what separates an earned canon gem from
decoration. Related laws this rides with: the gold ring asserts "extreme" only
(non-extremes get labels, never rings); annotations are capped at the load-bearing
few; a unit native to the dataset (BBY) is used as-is, positive, with its gloss
printed — never converted into a frame (ABY) the data doesn't contain.

## Why it works

Mixing registers reads as a theme park; separating them reads as an archivist who
loves the source material. Restraint is the deeper fandom.
