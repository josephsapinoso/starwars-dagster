# Professional Visual Storyteller — Panel Memory

## Settled (do not relitigate)

- Reader-paced always: no auto-playing or time-gated intros, no scroll-jacking. The
  auto-playing crawl homage was cut in favor of the scroll story. (First design panel,
  PR #1.)
- Exactly ONE authored pause in the mobile story (`.step--held`, 90svh) — placed before
  the witnesses reveal, because that is the payoff beat. A second held beat would
  cheapen the first. (Mobile beat-spacing panel, PR #4.)
- The beat counter ("n / 8") is orientation and rides the stage caption; decorative
  fill between beats was rejected for cause. (Mobile beat-spacing panel, PR #4.)
- Provenance reveals exist on beats 1–6 ONLY. Beat 0 stays a clean hook — no aside, no
  competing affordance; beat 7 carries a provenance-computed callback line instead of a
  reveal. One disclosure style, shared with details.sql. (Pipeline-reveal panel,
  2026-07-18.)
- Beat-7 callback wording is computed from provenance counts so it is drift-detectable
  and arithmetically true. Never hand-write pipeline arithmetic into copy; the
  number-word list is drift-guarded against overflow (the "undefined checks" near-miss
  proved why). (2026-07-18; WORDS now runs through "fifteen".)
- Reveal label template is generated, not per-beat bespoke: "The paper trail — where
  {claim} comes from"; beat 4 (the held pause) renders the quietest variant, "The paper
  trail." — identical placement/size everywhere. "Paper trail" is lore's one sanctioned
  bridge word into the archive conceit. (2026-07-18.)
- Guard honesty is voice law, not just data law: a check badge appears only where the
  check asserts the displayed number; derived/unguarded claims say so in plain words.
  The honest third act is part of the story, not a footnote to hide. (2026-07-18.)
- Every provenance/severity string derives from `DATA.provenance`, pytest-verified
  against real Dagster definitions; check rationales are verbatim checks.py
  descriptions. Copy in the reveals is projection, never authorship. (2026-07-18.)
- **Spoiler pin law** (2026-07-18): a standing offline test derives payoff term sets
  from `known_facts` — names AND payoff numbers, phrase-anchored — and asserts no check
  string renders on a beat earlier than its claim's reveal. Every new check passes this
  audit before landing, and the pin must be seen to fail before merge. Extended
  2026-07-19 with the registry payoffs: 896 / Yoda / 39-of-82 banned on all story
  rails, verified seen-to-fail.
- **The rail is uniform; spoiler safety lives in the strings, not the renderer.**
  Every beat renders the same rule (all checks of its chain assets). No beat-indexed
  filtering — a `beat` field would be hand-authored narrative metadata pytest cannot
  verify. Corollary: DATA.provenance carries no narrative fields, ever. (2026-07-18.)
- **Description style rule** (technical-writer's, I enforce the story half): check
  descriptions state the invariant and its stakes, subject-only, number/name-free; run
  metadata carries the particulars; known_facts.py is the only roster/number home. No
  check string quotes another beat's caption or payoff. (2026-07-18; reaffirmed
  2026-07-19 for both registry checks, which rail on beats 4–6.)
- **Quoted-testimony rule** (2026-07-19): external claims (dialogue, canon) may be
  AUDITED in copy but never rendered as site-derived data; derived numbers come only
  from DATA. The quoted figure appears only while the record still agrees — the line
  renders data-conditionally on the exact facts it audits, and disappears rather than
  lie. Shipped instance: the Yoda line ("…his own count, nine hundred years, checks
  out.") renders only inside `if (oldest.name === "Yoda" && oldest.bby === 896)`;
  no derived ~900 exists anywhere.
- **The coda** (2026-07-19): shipped verbatim and is now fixed copy — "The census is
  filed. Nothing here is sealed — every figure above traces to a record, and every
  record is open to a second reading." + re-read anchor "Take the census again ↑"
  looping to #story. Placement: inside main, after the final dashboard grid; the
  footer stays footer. The coda is number/name/payoff-free BY DESIGN — that property
  (not the wording) is pinned by `test_the_coda_stays_number_free`.
- **Absence pins are legitimate guards** (2026-07-19): an element exempted from a
  detector by a property gets a pin asserting that property; pinning wording is
  theater.
- **Audit-canon motif is capped at two uses** — copy that audits a canon claim against
  the filed record. The Yoda line is the second and LAST use; a third would turn a
  motif into a tic. (2026-07-19, my ruling, adopted.)
- Two-register law holds at the repo boundary: the records-office voice lives on the
  site only; README (including "Limits, by design") stays engineering register.
  (2026-07-19.)
- **The whisper clause** (2026-07-19, token-hygiene): every sanctioned style exception
  is an exact (selector, value, reason) pin in the guard, failing loudly on change in
  EITHER direction and printing its reason. Unexplained holes are theater; pinned
  exceptions are law. Shipped as `EXEMPT_SELECTORS` in test_site_style_hygiene.py.
- **`.prov-check` stays 11.5 — the whisper tier.** `details.prov summary` is 12 and
  `.chip` is mono 12; at 12 the guard voice merges into the machinery voice on the
  rail the held pause depends on. Pinned with reason "whisper tier — the held pause's
  authored contrast (Settled)". (4–2, 2026-07-19.)
- **Chart lettering is pinned geometry, not typography** (3–2): .axis-t/.val-t/.anno-t
  11.5, .cat-t 12.5, .seg-pct 11.5 (its `w > 46` gate is tuned to it). Collisions are
  fixed by staggering, never by shrinking; **raise-only grants permission, not
  obligation** — standing still needs no evidence, moving chart geometry does.
- **Scenery is not ink** (2026-07-19): decorative paints (aria-hidden canvas) may stay
  literals with a required sanction comment, counted exactly once; data ink must be
  tokenized. No runtime bridges for decoration — the hero's opening chord takes no
  init dependency for a one-use star color.
- **Ink adapts to its ground** (2026-07-19): on-mark labels choose ink per computed
  ground from the same array that drives the ground; every rendered pair ≥4.5:1,
  verified computationally. Never one ink that fails somewhere; never a new hex.
- **The style registry is the test** (5–1): the sanctioned type scale's one
  machine-readable home is the structural pytest (`SANCTIONED_SCALE`); no font-size
  tokens, no parallel lists.
- **Anchoring restoration is not scroll-jacking** (2026-07-19): a synchronous,
  activation-triggered, MEASURED-delta scroll correction that no-ops where the browser
  already anchors is the sanctioned disclosure-growth shape; animated or assumed-delta
  variants stay banned. "Opening a reveal never moves the reader" is violated by
  anchoring-less Safari, not by this fix.
- **Measured-vs-inferred labeling** (2026-07-19): decisions resting on unreachable
  hardware state measured facts and inferences separately, verbatim, in the log; the
  honest proxy is named as a proxy.
- **Acceptance is a decision with a tripwire** (2026-07-19): an accepted limitation
  enters the log with its reopening trigger written down; a shrug is not a verdict.
  Live: Q1 — a why gains load-bearing content with no non-hover home, or the legend
  line goes false; Q4 — an anno carries content absent from copy/caption, or a viewBox
  rework arrives without the 8-state anchor-geometry re-verification costed.
- **The census conceit is load-bearing** (2026-07-19): the stage tooltip is the only
  surface naming most of the 82 individuals; no input modality may be cut off from it.
  On touch it pins; dismissal is the reader's own next tap or own scroll, NEVER a timer.
- **Exposure changes reach, not content** (2026-07-19): widening a verified string's
  audience renders the same string verbatim from its one home; if it doesn't fit the
  vessel, change the vessel.
- **Q4 acceptance warrant** (unanimous, in the log verbatim): "prose and captions are
  the payoff carriers; annos are deixis" — zero load-bearing orphans at 5px. The beat-5
  collision math (witness names 20 viewBox-units apart cap any raise at ~8px effective)
  is standing veto ground against naive stage-type raises.
- **Cross-source derived figures are quoted-testimony territory** (2026-07-20):
  arithmetic combining sources (SWAPI birth × akabab death — the Yoda 896+4=900
  temptation) is pre-vetoed off every surface until a surfacing panel rules; computing
  it from `died_year_aby` would launder the audited quote into data. Written tripwire
  in the akabab log.
- **The galaxy_report akabab section is fixed copy** (2026-07-20): title "Affiliations
  & Apprenticeships" (as-filed — the source field is literally `affiliations`), analyst
  register (two-register law), my drafted copy verbatim including the closing "'On file'
  means the curated source records it — absence is not survival." Nested denominators
  (N of field-present, of 81 matched, of 82) on every enrichment line; "on file"
  everywhere, never "deceased"; no superlatives from sparse lineage fields —
  affiliations may rank only with n disclosed.
- **Description-style law applies at birth** (2026-07-20): checks on unlisted assets
  that rail on no beat today still ship subject-only, number/name/payoff-free — the
  uniform-rail rule means a future chain join inherits them silently. If
  `character_biographies` ever joins a beat chain, extending the spoiler-pin term sets
  is part of THAT landing (written tripwire for the surfacing panel).

## Working knowledge

- The beat sheet (8 beats, site/index.html ~237–296):
  0 census hook (all 82 as dots) → 1 the measuring (heights) → 2 the weighing (mass +
  the 23 unweighed — absence as story) → 3 the hometowns (origins) → 4 the cameos
  (most appear once) → 5 the witnesses (**payoff: three saw all six films — C-3PO,
  R2-D2, Obi-Wan**) → 6 the pilots → 7 the handoff (dots filed away → dashboard).
- The arc is a census-archive conceit: measurement → absence → origins → persistence →
  handoff to the "records office" (dashboard), now closed by the coda's loop back to
  the hook. Additions must serve this spine or a deliberate second read-through.
- The witnesses payoff must not leak early. Leak history: 2026-07-18 FAIL, four
  forward leaks fixed in 2aa845e with invariant-subject labels ("all-six set",
  "flight record", …). The standing spoiler pin carries the audit; manual re-audit
  only for payoff *concepts* the pin cannot derive from known_facts.
- The held pause is beat 4 (the cameos). Any affordance inside the pause must be the
  quietest voice on the page.
- Reveal micro-story structure: claim → machinery (vertical chip chain, one gold
  `.hot` seat) → guard (◆ blocks / ◇ warns + one-line rationale) → honesty line from
  the NOTE.check template. A bare chain is a diagram, not a beat.
- `raw_people` opens every chain, so the census's best-guarded numbers recur in all
  six reveals — the structural reason beat 0 could stay clean.
- Pipeline carries 15 checks (4 blocking, 11 warn); the akabab commits take it to 20
  (adds 2 blocking / 3 WARN on two UNLISTED assets — no beat rail renders them today),
  assets 11→13, WORDS through "twenty". Beats 1 and 4–6 are `guard.kind: "check"`;
  every pytest→check flip re-projected honesty lines with zero hand edits.
- Birth registry (2026-07-19): `#card-registry`, dashboard Census section — bar (39
  undated as tint) + dot strip, Yoda gold-ringed, Jabba labeled, BBY gloss printed.
  Coda ~395–398; Yoda conditional line ~1371–1375.
- Touch tooltip pin + reveal delta compensation (fdd3178): tipPinned/tipHide
  ~465–485 and ~796–802; the stage tooltip is now mobile's real-pixel dot-identity
  channel (bonus, not Q4's justification).
- Dashboard lineage strip is the epilogue's establishing shot; per-card mini-DAGs were
  rejected unanimously — telling the gag eight ways.

## Banked: 2026-07-18 rounds (pipeline reveals + post-landing cleanup; 082d9c9, c0b97e0, 2aa845e; compacted)

Won: beats 1–6 only, clean hook, beat-7 callback, micro-story reveal shape, quietest
label on the pause, honest third act; all four spoiler leaks fixed (incl. the "23
unweighed" leak only my audit caught); the spoiler pin carries names AND numbers.
Lost, correctly: bespoke labels → ONE generated template; my "six pipelines" callback
was arithmetically false (hand-authored pipeline copy drifts); my cumulative-rail
mechanism 5–3–1 — placement filtering bought spoiler safety with an unverifiable
hand-authored `beat` field — and I declared re-authoring impossible without drafting
the counterexample label first. A check's blast radius is every beat that cites its
asset. Lessons live in skill rules 9–10.

## Banked: birth registry, coda, hue enforcement (2026-07-19, log 2026-07-19-birth-registry-and-polish.md; 1f3cf9e, 4d92cb7, f170379; compacted)

Clean sweep; all outcomes promoted to Settled above (coda + digits-pin; quoted
testimony; motif cap; subject-only descriptions; spine untouched — registry is a
dashboard card). Lessons: draft the FINAL copy at prep time; reach for quote-and-audit
before exclusion; a sweep means check harder for anchoring next debate. Watch:
unconditionalizing the Yoda line's data-gated render is a law violation; the coda is
the ONLY post-grid narrative element — the frame closes once.

## Banked: token hygiene + type consolidation (2026-07-19, decision log 2026-07-19-token-hygiene.md; a30a5bc; compacted)

Won across the board: the whisper clause was the guard's architecture; `.prov-check`
11.5 held 4–2 on the concrete adjacent-voices math (precedent survives best re-argued
from the surface, not the statute); "merge the prose, exempt the geometry" adopted
whole, my voice-safe merges verbatim (register markers carried every merged voice);
exact pins answered allow-lists-rot (a drifted pin is a red test); registry-is-the-test
5–1. Lost nothing outright. Lessons kept in skill rules 7–9: bring the drafted pin
TABLE, not the pin idea; when two roles collide on a mechanism, check whether MY shape
dissolves the objection before picking a side.

## Banked: akabab second source (2026-07-20, log 2026-07-20-akabab-second-source.md; prep folded in)

Clean round on my turf; drafted-copy discipline won its second tiebreak. Spine, beat
sheet, and reveals untouched — Option C ratified unanimously; site ripple is the
totals pin plus WORDS growth through "twenty" with a pytest pin that `len(WORDS)`
exceeds every DATA-rendered count (my 2026-07-18 overflow lesson, now generalized law).

- **Q5 won whole**: analyst register held (galaxy_report is engineering-adjacent
  stakeholder voice — emoji headers, "Total characters tracked" — never the census
  conceit; two-register law), my drafted copy adopted VERBATIM, and the title tiebreak
  ("Affiliations" over lore/tech-writer's "Allegiances") fell to me precisely because
  I brought finished copy anchored to the as-filed field name. New technique: in a
  naming dispute, the source's as-filed vocabulary is a tiebreak I can invoke — and
  only a finished draft can invoke it.
- **Q3 won**: all five check descriptions payoff-free at birth. My prep read was
  exactly right — the report cannot leak (repo Markdown, not a site rail); the real
  spoiler surface is check descriptions on today-unlisted assets, which the spoiler
  pin cannot see because the payoff term set doesn't exist yet. Deaths, like births,
  read as a records fact, not a spine payoff — no veto, same call as the registry.
- **Pre-veto became law**: my Yoda 896+4=900 tripwire was adopted verbatim as
  surfacing-panel tripwire (1) AND generalized into the cross-source Settled
  constraint. The quoted-testimony rule gained its second application before its
  first violation.
- Adopted from others, now my voice law for the report: lore's "deaths on file"
  package ("deceased" would overclaim — sequel-inclusive AND canon-incomplete);
  analyst's nested denominators as copy discipline, not checks (qa's five-check
  ceiling held). Lost: nothing outright.

Prep differently: the file-reading pass predicted every fault line (register,
non-leaking report, descriptions as spoiler surface, future-chain hazard) — keep
doing it. Add one borrowed lesson: baselines are computed from the frozen fixture,
never transcribed (three independent surveys disagreed on record counts) — the
data-side twin of "never hand-write pipeline arithmetic"; cite it against any
transcribed number in copy. Still cannot verify: whether a future panel makes
affiliations/lineage a spine beat — that's their call, my tripwires are written.

## Banked: watchlist round (2026-07-19, log 2026-07-19-watchlist-round.md; fdd3178; compacted)

Q3 won 5–1 (tap-to-pin; reader-owned dismissal shipped exactly: pin :799, leave-guard
:802, scroll dismiss :469). Q1 won 4–2 on my voice-load math (48 tab stops, ~15
crossing the held pause); `title=` stays a desktop bonus, the legend line is the
honest non-hover contract. Q4 unanimous — warrant + beat-5 collision math promoted to
Settled. **Q2 LOST (ship 3–2–1), rightly**: my three conditions were all met, and the
adjudication turned my own rule around (rule 7 is violated ON Safari today, not by the
fix). Lessons: when I can name the exact shape that would flip me, that shape IS my
proposal — draft the flip-condition as the proposal; keep authoring cross-question
findings; cannot-verify honesty became the round's measured-vs-inferred law. The ux
watchlist is empty; Q1/Q4 tripwires and hazards live in the log.
