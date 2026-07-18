# Star Wars Lore Fanatic — Panel Memory

## Settled (do not relitigate)

- The characters appearing in all six saga films are **THREE**: C-3PO, R2-D2, and
  Obi-Wan Kenobi. "Just the droids" is a canon error the site once nearly shipped.
  (First design panel, PR #1/#2.)
- Verified census facts: 82 people in the dataset; 23 lack mass; Naboo 11 residents,
  Tatooine 10. Any Star Wars framing must fit these numbers, not legend. (First design
  panel.)
- Gold #ffe81f — the crawl's color — is ceremony: display accent only, never a data
  series. Using the crawl gold to paint bars is kitsch. (First design panel.)
- No auto-playing crawl intro. The original crawl homage was cut for a reader-paced
  story; homage that takes control of the reader is not homage. (First design panel,
  PR #1.)

## Working knowledge

- Dataset scope is the six-episode saga (Episodes I–VI) as served by swapi.info;
  no sequels, no anthology films. Claims like "every film" mean these six.
- The site's story frames the data as a census ("A Galaxy of 82 People") — a
  bureaucratic-archive conceit that is period-appropriate for the Republic/Empire and
  earned rather than decorative.
- The opening crawls of all six films are preserved verbatim in a dashboard reveal
  (`DATA.films[].crawl`) — the right home for them: primary-source text, opt-in.

## Prep notes: pipeline-reveal (2026-07-17)

- **Two registers, verified in the repo.** The story beats (site/index.html:237–296)
  speak in-universe as a bureaucratic census audit — kickers "The census / The
  measuring / The weighing / The hometowns / The cameos / The witnesses / The pilots /
  The handoff". The machinery speaks plain engineering, out-of-universe: "Show the
  DuckDB SQL" (line 850), the lineage strip "The pipeline that made this page"
  (313), and every check description in `starwars_dagster/assets/checks.py` is
  Star-Wars-free prose. This separation is *why* the site reads as fandom with
  restraint. The new reveal is machinery, so its label belongs in the engineering
  register — but a census-audit bridge word ("the paper trail on this number") is
  earned because the audit conceit is already the story's spine.
- **Beat 7 already licenses the reveal.** "The machinery that counted it … is waiting
  below" (line 293) breaks the fourth wall on purpose; per-beat reveals just surface
  that machinery earlier. No new conceit needed — extend, don't invent.
- **Factual trap in Q3:** beats 1–3 all read from `characters_enriched`, 4–5 from
  `film_character_counts`, 6 from `starship_stats` — ONE pipeline, three transform
  assets, six queries. A handoff callback saying "you've now seen six pipelines" is
  false. Acceptable: "six trails through one pipeline" or "the same machine, six
  angles".
- **Beat-6 quote check:** "flying is for droids" (line 286) is a fair paraphrase of
  Obi-Wan in Revenge of the Sith ("Flying is for droids."); attribution correct.
- **Kitsch veto list for this topic:** no Aurebesh in the mini-DAG, no
  Imperial/Rebel iconography as check badges, no "these aren't the rows you're
  looking for", no lightsaber-colored ERROR/WARN coding (and never crawl gold as a
  status color — gold is ceremony). ERROR/WARN are engineering facts; encode them as
  engineering (shape/weight/label), not as allegiance.
- Could not verify anything requiring the live site or Dagster UI; all facts above
  are from repo files.
