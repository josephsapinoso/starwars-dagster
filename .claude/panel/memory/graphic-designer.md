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
- One disclosure style, ever: `details.sql summary` treatment (mono 12px, .06em
  tracking, ink-3, gold ▸/▾ `::before`) is shared via extended selector
  (`details.sql, details.prov`) for all opt-in reveals. A second disclosure style is a
  fork. Hit area for both raised to ≥44px. (Pipeline-reveal panel, 2026-07-18.)
- Check-status badges are monochrome ink-2: ◆ = blocking/ERROR, ◇ = WARN, always paired
  with wording ("blocks"/"warns"). No green/amber/red seats on the site; a static
  artifact cannot claim live status, so color-coded "passing" would be a fabricated
  mark. Severity derives from `spec.blocking` in provenance data, never hand-typed.
  (Pipeline-reveal panel, 2026-07-18.)
- Lineage-chain chips are real HTML `.chip` elements (mono 12px, 1px `--line` border,
  5px radius), not SVG imitations — reuse the CSS verbatim. Exactly one `.hot` gold
  seat per chain: the single beat-relevant asset. Gold-as-"the one to look at" is the
  established emphasis mark. (Pipeline-reveal panel, 2026-07-18.)
- Per-beat reveal chains stack VERTICALLY (chips + ↓ connectors) inside `.step-inner`;
  no horizontal overflow escape in reveals — every node visible without scrolling at
  the ~260px mobile budget. Reveals exist on beats 1–6 only; beat 0 stays clean; beat 7
  carries a provenance-computed callback line. (Pipeline-reveal panel, 2026-07-18.)
- Guard honesty, AMENDED (post-landing cleanup, 2026-07-18): the rail is a uniform
  asset-level citation — every beat renders ONE rule, all checks of its chain assets;
  spoiler/emphasis safety lives in the STRINGS (number-free labels generated from
  provenance), never in per-beat renderer conditionals or filters. My earlier per-beat
  badge-placement reading ("badge only where the check asserts the displayed number")
  is superseded at rail level; the plain-words rule for derived/unguarded claims stands.
- Displayed SQL is executed SQL: any SQL text on the site lives in DATA and is executed
  offline against the fixture warehouse. Renders via the existing `details.sql`
  treatment with ZERO new marks — no "verified SQL" badge exists or ever will; ◇/◆ +
  prov-note wording already carry "asserted offline". (Post-landing cleanup, 2026-07-18.)
- DATA.provenance carries no narrative fields — everything in it stays derivable from /
  verifiable against the real Dagster defs plus known_facts. Visually: rail labels and
  legend are generated type, never hand-lettered. (Post-landing cleanup, 2026-07-18.)
- Rail legend copy is settled: "◆ blocking check · ◇ drift warning · full check
  descriptions live in the Dagster UI" — the old hover promise was false on
  touch/keyboard (ux rider, 2026-07-18).
- Dashboard cards get NO per-card mini-DAGs — the full-width lineage strip is the
  establishing shot; duplicating it per card is mark multiplication. (Pipeline-reveal
  panel, 2026-07-18.)
- **The gold ring means "extreme"**: persistent gold rings assert superlatives only —
  the three true extremes wear them (scatter pair + Yoda on the registry); named
  non-extremes (Vader) get labels, never rings. (Birth-registry panel, 2026-07-19.)
- One data hue is now enforced dashboard-wide: amber outlier dots deleted, hyperdrive
  bars s2→s1, films' second series is a 45% s1 tint, gender is a rank-ordered s1
  ladder. No chart anywhere paints s2–s5. (Birth-registry panel, 2026-07-19.)
- Cross-medium tint law: multi-step tints of the data hue render as SOLID computed
  colors — `color-mix(in srgb, var(--s1) N%, var(--panel))`, steps [100,75,55,40,28] —
  never fill-opacity, so ONE palette array feeds SVG fills, HTML legend swatches, and
  tooltip chips with identical color strings. (Birth-registry panel, 2026-07-19.)
- Captions longer than a label render as wrapping HTML below the figure, never SVG
  `<text>` — SVG text clips at narrow widths (registry testimony line clipped at
  390px). (Birth-registry panel, 2026-07-19.)
- **Sub-body type scale is settled** (token-hygiene panel, 2026-07-19): fixed sizes are
  integers {11, 12, 13, 14} + 16 body · 17 card-h3 · 18 glyphs · 42 KPI; clamp()
  display sizes exempt. Half-pixels survive only as whisper-clause pins: .axis-t /
  .val-t / .anno-t / .seg-pct at 11.5 and .cat-t at 12.5 (chart-geometry tier),
  .prov-check at 11.5 (the held pause's authored whisper).
- **The whisper clause:** every sanctioned style exception is an exact
  (selector, value, reason) pin in `tests/test_site_style_hygiene.py` that fails
  loudly on change in EITHER direction. Unexplained holes are theater; pinned
  exceptions are law.
- **The style registry is the test:** the sanctioned scale + pins have ONE
  machine-readable home, the structural pytest — no font-size tokens, no parallel
  lists. font-size is never set from JS/markup; use a class (guard-enforced).
- **Raise-only grants permission, not obligation:** standing still needs no evidence;
  moving chart geometry does (360/390 collision re-verify, fit gates move with type).
- **Scenery is not ink:** decorative paints (the aria-hidden starfield canvas,
  #cdd8ef) may stay literals — named, "scenery, not ink"-commented, counted exactly
  once by the guard. Data ink must consume tokens. No runtime bridges for decoration.
- **Ink adapts to its ground:** on-mark labels choose ink per computed ground from the
  SAME array that paints the ground (`--void` on full s1, `--ink` on tints), every
  rendered pair ≥4.5:1 verified computationally; the fallback is dropping the on-mark
  label (legend/table carry the data) — never a new hex.
- **Gold's one home:** the #ffe81f literal appears exactly once, in :root; alpha
  ceremony derives via `color-mix(in srgb, var(--gold) N%, transparent)` — the
  rgba(255,232,31,…) triplet is banned; `var(--gold)` itself is free everywhere.

## Working knowledge

- Design tokens live in one `:root` block at the top of `site/index.html` (~lines
  6–25): colors, font stacks; everything downstream consumes the variables. Tokens
  define `--s2` green / `--s3` amber / `--s4` red but story/lineage sections use only
  blue + gold + inks — keep it that way (see badge law above).
- The existing mark vocabulary: dot units (`.unit` dim/faint/hot), rounded bars
  (`barPathH/V`), annotation lines + labels, `.chip` asset boxes in the dashboard
  lineage strip (`.chip.hot` gold, used once for galaxy_report), gold ▸/▾ markers on
  `details` reveals, now ◆/◇ monochrome check badges. New components must reuse this
  vocabulary before inventing marks.
- Dashed border means *grouping* (`.dag-group`) — never overload dashed to also mean
  WARN in the same diagram family.
- Check names run up to ~40 chars mono; badges use short display labels from the
  provenance object, never raw check names, or chains explode horizontally.
- Mobile: `.step` min-height min(64svh,560px) — an open reveal may legitimately grow
  the card taller than the station; geometry survives as long as the stage is
  untouched. Flat mode appends per-step figures inside `.step-inner`; anything living
  there ships to flat embeds for free — reveals are built statically at init for this
  reason.
- Provenance strings (labels, badge wording, rationales) all project from
  `DATA.provenance`, which is pytest-verified against real Dagster definitions; the
  one-line strict-JSON `const DATA` format is load-bearing. Visually this means: no
  hand-lettered status text anywhere — the type on screen is generated.
- Label template settled by lore/ux: "The paper trail — where {claim} comes from";
  beat 4 (held pause) gets the quietest variant "The paper trail." — identical
  placement/size everywhere.

## Banked: pipeline-reveal (2026-07-18, compacted)

Won: chip reuse (adjudication upgraded my SVG-imitation plan to real HTML `.chip`
elements — the stronger form of my own principle: propose *using* the existing CSS,
not imitating it); monochrome ◆/◇ badges (severity from `spec.blocking`, mark can't
lie); shared disclosure selector; no per-card mini-DAGs. Lost: horizontal chain with
overflow-x — at ~260px it hides the terminal node (the payoff) behind a scroll.
Banked distinction: overflow-x is a dashboard affordance, never a story affordance.
Lessons: measure content budget before proposing an axis; treat a spec's stated
technology ("SVG diagram") as a guess to challenge, not a constraint.

## Banked: per-character transform landed (2026-07-18, compacted)

Commit `082d9c9`: beats 4–6 render the three-chip vertical chain + four-badge ◇ rail
with ZERO new mark types; `.hot` gold seat unchanged (`galaxy_report` only) — the
reuse-first outcome the chip law was written for. Vertical-budget watch RESOLVED:
headless 390x844 / 360x740 pass — reveals grow downward, stage cap holds; floor rules
(never shrink type, never touch the stage) remain the fix path on regression.
## Banked: post-landing cleanup (2026-07-18, compacted)

Decision log `2026-07-18-post-landing-cleanup.md`; commits c0b97e0, 2aa845e.
Lost Q1 (guard+blocking filtered rail) to the coverage-understatement objection:
character_stats carries ZERO blocking checks, so my rule degenerated to empty rails.
The remedy (re-authored strings + standing spoiler pin) delivered every demand I
actually hold: renderer untouched, ONE uniform rule per beat, no narrative fields.
Lessons: (1) when strings are generated AND test-pinned, fixing strings IS systemic —
don't solve content-layer honesty with renderer layout; (2) run any filter rule's
degenerate case against every asset's real check inventory by severity first.
Won Q2/Q3: SQL truth with zero visual delta (no "verified" mark, unanimous);
denominator clause on chart 5; one ◇ where characters_enriched appears while
galaxy_report stays honestly check-free — a disclosed gap beats a phantom badge.
Watch update: `.prov-check` 11.5 is no longer a retire-on-raise exception — it is a
Settled whisper pin (see Settled; 2026-07-19 bank). Generated copy self-corrects in both
directions: beat 4–6 caveats self-removed; beat-7 overflow failed loudly.

## Banked: birth registry + hue enforcement (2026-07-19, compacted)

Decision log `2026-07-19-birth-registry-and-polish.md`; commits 1f3cf9e, 4d92cb7,
f170379 (screenshots at 15 checks — README-retake CLOSED). Q3 adopted in full;
registry card shipped as specced with zero new mark types; amber deleted; gold rings
on the three true extremes only (Vader label-only). Gold-ring, solid-tint-ladder, and
HTML-caption laws all promoted to Settled. Lessons kept: when the goal is identity
across media, spec the computed VALUE, not the rendering trick (ladder landed as
color-mix, not my fill-opacity spec — the stronger form of my own must-have); label
collisions fix by staggered rows; test SVG text longer than a name at 360–390 before
speccing it as SVG. CORRECTION absorbed: the four "off-token" survey hexes were
already tokenized in 1123757 (--tip-bg, --axis, --cyan, --sql-ink). Rail-mass watch
CLOSED: 360px with 15 checks — no horizontal scroll, chips 125–180px in a 244px
rail, 6-row max stack, summaries ≥44px.

## Banked: token hygiene + style guard (2026-07-19)

Decision log `2026-07-19-token-hygiene.md`; commit a30a5bc (site/index.html +
tests/test_site_style_hygiene.py). My standing proposal, landed.

**Won:** the CSS integer collapse exactly as specced (10.5→11, 12.5→13, 13.5→14,
16.5→17); dead 11px JS attr deleted; gold rgba leaks → color-mix idiom; Q3
no-font-size-tokens carried 5–1 with my registry-is-the-test framing adopted
verbatim; Q4 guard scans CSS AND JS (analyst's veto reinforced this), strips the
one-line DATA literal first, ships same-commit, seen-to-fail before landing. Gender
`#fff` died AND the AA failure was fixed in the same move via per-rank ink from the
tint-ladder array — ink-adapts-to-its-ground is the tint law's natural sequel.

**Lost, and rightly:**
- `.prov-check`→12 (4–2). I proposed retiring a Settled exception inside a hygiene
  pass — relitigation by the back door. The storyteller's craft argument was correct
  ON MY OWN TERMS: `details.prov summary` is 12 and `.chip` is mono 12, so at 12px
  the guard voice merges into the machinery voice on the rail the held pause depends
  on. The 11.5 whisper is authored contrast, not disease.
- Chart-lettering raises (3–2): exempted as a pinned geometry tier. My raise carried
  an unfunded verification burden (collisions, clipping, the w>46 gate); raise-only
  grants permission, not obligation — standing still needs no evidence.
- Zero sanctioned literals: the exact-pin shape answers my "allow-lists rot"
  objection (a drifted pin FAILS the test), while my canvas bridge had an unanswered
  init-order risk on the hero canvas. Scenery-is-not-ink is a better cut than my
  absolutism — the guard still counts and comments the literal.

**Prep differently next time:**
1. Distinguish disease from authored exception before proposing a collapse — a
   half-pixel with a craft rationale and a Settled seat is not hygiene debt.
2. When my objection to an allow-list is "it rots," first check whether an
   executable exact pin removes the rot before rejecting the list outright.
3. Cost my own riders: a raise needing two-viewport collision re-verification is not
   free; if I can't fund the evidence, don't spend the votes.
4. The ledger rotted twice (four-hexes, prov-check) — keep verifying every ledger
   claim against source in PREP; this time the correction saved my credibility.
