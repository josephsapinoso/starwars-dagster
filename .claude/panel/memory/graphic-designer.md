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
