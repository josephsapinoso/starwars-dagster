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
- **Anchoring restoration is not scroll-jacking** (watchlist round, 2026-07-19): the
  sanctioned shape for disclosure-growth compensation is a synchronous,
  activation-triggered, MEASURED-delta `scrollBy` that no-ops where the browser
  anchors (proxy-verified 0/−180/0/0). Animated or assumed-delta variants stay banned;
  a synchronous restoration cannot read as motion, so it is invisible by construction.
- **Tap-to-pin is the touch analog of focus-pin, not a fork:** one shared tooltip,
  pointerType branch ONLY in the stage handlers; touch tap pins, dismissal is the
  reader's own next tap or scroll — never a timer, zero new marks or styles.
- **The census conceit is load-bearing:** the stage tooltip is the only surface
  naming most of the 82 individuals; no input modality may be cut off from it.
  Suppress-for-touch is permanently off the table.
- **Exposure changes reach, not content:** widening a verified string's audience
  renders the SAME string verbatim from its one home; if it doesn't fit the vessel
  (prose in the readout tooltip), change the vessel — never the string, never the mark.
- **Measured-vs-inferred labeling:** any decision resting on unreachable hardware
  states measured facts and inferences separately, verbatim, in the log.
- **Acceptance is a decision with a tripwire:** accepted limitations (Q1 hover-only
  whys; Q4 5px stage type) enter the log with written reopening triggers — Q4 reopens
  if any anno ever carries content absent from caption/copy.

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

## Prep notes: akabab surfacing (2026-07-20)

Brief: surface the wired-but-invisible second source (raw_character_profiles,
character_biographies). My lane: does a new surface (card / DAG chip / beat) fragment the
mark system, the one-hue law, gold-only rule, color/type budget. Verified against source:

- **DAG chips are source-agnostic and monochrome (ink-2, `--void` bg, `--line` border).**
  Adding `raw_character_profiles` to 01 (5→6 chips) and `character_biographies` to 02 (4→5)
  is pure `.chip` reuse — ZERO new marks. RESIST any instinct to color/tint akabab chips to
  mark provenance: a source distinction would be a new data-color seat (violates one-hue)
  and a status-that-is-not-a-series. Attribution belongs in TEXT (footer, prov-note, card
  caption), never in a chip hue. The `.hot` gold seat stays exactly one per chain
  (galaxy_report); akabab earns no gold. `aria-label` string updates with the counts.
- **Headline number → `.kpi` treatment** (`.kpi`/`.k-value` 42px, sanctioned scale integer;
  `.k-label` 13, `.k-sub` 12). A dashboard-only akabab stat card is the lowest-fragmentation
  home: it reuses the existing `.kpis` grid / `.card span*` grid. No new component.
- **"on file" is ALREADY the site's voice** — tooltips render "film on file", "no mass on
  file", "82 rows, on file" (L267, L594, L652). So the mandated vocabulary needs no new
  style and reads as continuity, not a bolt-on. Confirm "on file" / "as filed"; never
  "deceased".
- **Nested denominators render as wrapping HTML caption below the figure** (banked caption
  law) — never SVG `<text>`. 47-of-82-matched / field-present split lives in `.prov-note`
  (13px) or a `.k-sub`, never on-chart clipping.
- **Provenance reveal = `details.prov`** (shared disclosure selector, gold ▸/▾, ink-3 12px
  summary, `.prov-check` 11.5 rail, legend "◆ blocking · ◇ drift"). A dashboard akabab card
  gets its own `details.prov` exactly like the others — no per-card mini-DAG (banked).
  Check badges stay monochrome ◆/◇; the 5 akabab checks slot into the SAME rail grammar.
- **No superlatives → no gold rings.** Sparse akabab list fields (affiliations/masters/
  apprentices) yield no verified extreme; ranked lists would need a superlative the data
  can't honestly assert. Gold ring stays reserved for the three true extremes. If any death
  "oldest/most" claim tempts a ring, veto — "on file" is not "complete".

Design verdict forming (for DEBATE): **dashboard-only surface, no new beat.** A new beat
re-opens settled 8-step/"n/8"/exactly-8-kicker geometry and buys nothing visual the mark
system doesn't already give a card. The live beat-7 contradiction ("four transforms" static
L320 vs "five transforms" rendered L941) is a copy-truth fix, not a mark question — but the
count that renders must match provenance. No new skill: mark-system skill already covers
chip reuse, status-not-a-series, no-per-card-DAG, caption-wraps-HTML, gold-ring-is-extreme.

## Banked: pipeline-reveal + per-character (2026-07-18, compacted)

Won: real HTML `.chip` reuse (propose *using* existing CSS, not imitating it);
monochrome ◆/◇; shared disclosure selector; no per-card mini-DAGs. Lost: horizontal
chain — at ~260px overflow-x hides the payoff node (dashboard affordance, never
story). Commit 082d9c9 landed beats 4–6 with ZERO new mark types; vertical-budget
watch resolved at 390/360. Lessons: measure content budget before proposing an axis;
treat a spec's stated technology as a guess to challenge.

## Banked: post-landing cleanup (2026-07-18, compacted)

Log `2026-07-18-post-landing-cleanup.md`; c0b97e0, 2aa845e. Lost Q1 (filtered rail):
character_stats has zero blocking checks, so my rule degenerated to empty rails; the
string-level remedy delivered everything I hold (renderer untouched, one uniform
rule, no narrative fields). Lessons: generated + test-pinned strings mean fixing
strings IS systemic; always run a filter rule's degenerate case against real check
inventories by severity. Won: SQL truth with zero visual delta; denominator clause;
disclosed check-gap beats a phantom badge. Generated copy self-corrects both ways.

## Banked: birth registry + hue enforcement (2026-07-19, compacted)

Log `2026-07-19-birth-registry-and-polish.md`; 1f3cf9e, 4d92cb7, f170379. Registry
shipped with zero new mark types; amber deleted; gold rings on the three true
extremes only. Gold-ring, tint-ladder, HTML-caption laws promoted to Settled.
Lessons: for cross-media identity, spec the computed VALUE, not the rendering trick
(color-mix beat my fill-opacity spec); collisions fix by staggered rows; test SVG
text longer than a name at 360–390 first. Correction absorbed: the four "off-token"
hexes were already tokenized (1123757). Rail-mass watch closed at 360px/15 checks.

## Banked: token hygiene + style guard (2026-07-19, compacted)

Log `2026-07-19-token-hygiene.md`; commit a30a5bc. My standing proposal, landed:
integer collapse as specced; dead JS attr gone; gold rgba → color-mix; Q3
no-font-size-tokens 5–1 with registry-is-the-test adopted verbatim; guard scans
CSS+JS, strips the DATA literal, ships same-commit, seen-to-fail. Gender `#fff`
died and AA was fixed in one move (per-rank ink from the ladder array). Lost,
rightly: `.prov-check`→12 (retiring a Settled exception inside a hygiene pass is
back-door relitigation — 11.5 is authored contrast vs the 12px machinery voice);
chart-lettering raises (unfunded verification burden → raise-only law); zero
sanctioned literals (exact pins can't rot; my canvas bridge had init-order risk).
Lessons: distinguish disease from authored exception; check whether an executable
pin fixes an allow-list before rejecting it; cost my own riders; verify every
ledger claim against source in PREP — the ledger rotted twice.

## Banked: watchlist round (2026-07-19)

Decision log `2026-07-19-watchlist-round.md`; commit fdd3178. All four watch items
closed; prep notes compacted into Settled + the skill.

**Won:**
- Q2 ship, 3–2–1. My argument — "a synchronous scrollBy cannot read as motion" —
  named the shape; the analyst's evidence gate made it land: the orchestrator's
  `overflow-anchor:none` proxy measured 0/−180/0/0 across all four states. The
  landed form (capture summary top on click, restore measured delta on toggle,
  site/index.html:471–485) is BETTER than my "just compensate" instinct because the
  measured delta self-corrects: where the browser anchors, it no-ops. Now Settled as
  "anchoring restoration is not scroll-jacking."
- Q3 tap-to-pin, 5–1 — my "analog, not a fork" framing carried and shaped the
  implementation exactly: shared tip module, `tipPinned` flag, pointerType branch
  only in the stage handlers (799–802), scroll/tap dismissal, zero new marks.
- Q1 accept, 4–2 — my every-exposure-shape-breaks-a-law walk (48 tab stops, nested
  details vs one-disclosure law, prose-in-readout fork) was cited in adjudication;
  the settled legend line stands as the honest contract. Tripwire recorded.
- Q4 accept, unanimous — my unfundable-raise costing (viewBox-unit blowup, anchor
  geometry across 8 states, @media-blind guard parser) was part of the kill; the
  8px-effective ceiling (beat 5's 20-unit witness stack) made the raise IMPOSSIBLE
  below target, not merely expensive.

**Lost, and rightly:** my Q3/Q4 coupling — "the pinned tooltip substitutes for the
illegible annos" — was demoted to bonus channel. The analyst's redundancy audit is
the actual warrant: zero load-bearing orphans at 5px; every stage claim has a
real-pixel twin in `.stage-cap` or 16px beat copy. Correct on my own terms: an
acceptance that leans on a brand-new affordance is fragile (remove the pin, lose the
warrant); an acceptance grounded in the EXISTING system stands alone. Never make a
new mark or behavior load-bearing for a limitation you're accepting.

**Prep differently:**
1. Pair aesthetic verdicts with a measurement plan — "cannot read as motion" was
   right, but the four-state proxy matrix is what closed the vote. Propose the
   experiment, not just the judgment.
2. When arguing two questions are coupled, state which direction the dependency
   runs and whether each verdict survives alone — the panel will decouple them, so
   do it first.
3. Redundancy audits (does a real-pixel twin exist for every scaled claim?) are a
   reusable acceptance test for any SVG-legibility complaint — run one in prep
   before proposing compensation.
