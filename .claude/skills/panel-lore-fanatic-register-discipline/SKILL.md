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

## Corollary: sequence the quotation, don't rewrite the source

Check names/descriptions are primary sources — they render in the Dagster UI and are
projected verbatim to the site. When a verbatim projection spoils a story beat (e.g. a
shared asset chain surfaces a later beat's payoff early), the fix is a RENDERING rule
(which checks appear on which beat), never a bowdlerized description. Scrubbing canon
facts (like the trio's names) from the operational source to protect page pacing
destroys the very precision the source exists to hold. Audit tip: on shared chains,
every upstream beat inherits every downstream claim's baseline label — check all
forward leaks, not just the loudest one.

## Why it works

Mixing registers reads as a theme park; separating them reads as an archivist who
loves the source material. Restraint is the deeper fandom.
