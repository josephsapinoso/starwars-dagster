# Graphic Designer — Panel Memory

## Settled (do not relitigate)

- Color budget: gold #ffe81f is a display accent only — headings, marks, ceremony —
  **never** a data series. One data hue (saber blue) carries all series. (First design
  panel, PR #1/#2.)
- Single HTML file: system font stack only, no webfonts, no CDNs, no build step. The
  austerity is the brand. (First design panel.)
- Mobile stage geometry is settled: stage pinned at min(52svh, 480px) — never shrink
  it; denominator captions and annotations are at the legibility floor. (Mobile
  beat-spacing panel, PR #4.)
- Decorative fill in the gaps between story beats was rejected for cause — whitespace
  is pacing, not emptiness to decorate. (Mobile beat-spacing panel, PR #4.)

## Working knowledge

- Design tokens live in one `:root` block at the top of `site/index.html` (~lines
  6–25): colors, font stacks; everything downstream consumes the variables.
- The existing mark vocabulary: dot units (`.unit` with dim/faint/hot states), rounded
  bars (`barPathH/V`), annotation lines + labels, chip-style asset boxes in the
  dashboard lineage strip, gold ▸/▾ markers on `details` reveals. New components must
  reuse this vocabulary before inventing marks.
- The reveal pattern precedent: `details.sql` ("Show the DuckDB SQL"), styled at
  ~189–196 — mono type, gold marker, indented body. Any future disclosure should share
  these selectors rather than fork the style.

## Prep notes: pipeline-reveal (2026-07-17)

Verified in `site/index.html` for this debate:

- Disclosure vocabulary (lines 190–196): `details.sql summary` is 12px body type,
  `.06em` tracking, ink-3, with gold `▸/▾` `::before`. Any per-beat reveal MUST reuse
  this exact summary treatment (share the selector or extend it, e.g.
  `details.sql, details.reveal`) — a second disclosure style would fork the system.
- Chip vocabulary (lines 139–141): `.chip` = mono 12px, ink-2 on `--void`, 1px
  `--line` border, 5px radius; `.chip.hot` = gold text + 35%-alpha gold border, used
  ONCE (galaxy_report, line 338). Gold-as-"the one to look at" is established display
  emphasis. The mini-SVG DAG should render chips that visually match this CSS chip
  (mono 12px, rounded rect, `--line` stroke), with `.hot` gold reserved for the single
  beat-relevant asset. `.dag` scrolls horizontally (`overflow-x: auto`, line 134) —
  the mini-DAG needs the same escape hatch, not type shrinkage.
- Dashed border currently means *grouping* (`.dag-group`, line 135) — don't overload
  dashed to also mean WARN inside the same diagram family without care; if used for
  WARN it must be on the chip stroke, not a container, and paired with a text glyph.
- Palette reality: tokens define `--s2` green / `--s3` amber / `--s4` red (lines
  18–20) but the story/lineage sections use only blue + gold + inks. Check badges are
  STATUS marks, not data series — but the site is a static artifact that cannot know
  live check results, so a green "passing" badge would be a fabricated claim (data
  engineer/analyst will say the same). Position: encode checks monochrome (ink-2),
  ERROR/blocking vs WARN distinguished by weight + glyph + wording ("blocks" vs
  "warns"), not by new hues. No new color seats.
- Checks inventory (checks.py): 4 blocking — raw_people_has_required_shape,
  star_wars_db_tables_populated, films_are_exactly_the_six_episodes,
  characters_enriched_has_no_null_names; 4 WARN drift —
  raw_people_count_matches_verified_snapshot, characters_enriched_join_coverage,
  characters_enriched_unknown_mass_baseline, starship_stats_cast_sanity. Names are
  long (up to ~40 chars mono) — badges must truncate or use short display labels, or
  the mini-DAG explodes horizontally on mobile.
- Mobile (lines 105–116): `.step` uses min-height min(64svh,560px), so an open
  reveal can legitimately grow the card taller than the station — geometry survives
  as long as the stage (min(52svh,480px)) is untouched and the diagram scrolls in-x.
- Flat mode (lines 740–772) appends per-step figures inside `.step-inner`; the
  reveal must live inside `.step-inner` too so flat embeds get it for free.
- Dashboard parity instinct: the full-width lineage strip (316–340) already covers
  the 5 cards; per-card mini-DAGs there would be mark multiplication. Cheaper: badge
  the existing strip's chips once.
