# Decision: pipeline-reveal (per-beat provenance) + portfolio reframing

Date: 2026-07-18 (prep pass ran 2026-07-17) · Scope: all nine roles · Orchestrator: Claude

## Brief (summary)

Repurpose the project as a portfolio showcase. Each insight beat of the scroll story gets
an opt-in expandable reveal showing the specific pipeline behind that number as a mini
lineage diagram with relevant asset checks marked; README reframed portfolio-first.
Full brief text was shared identically with all nine roles (see git history of this run).

## Prep-pass findings that changed the spec

- **The brief's beat→asset map was partly false** (data-analyst): beats 0–3 ←
  `characters_enriched` is true, but the 42-one-film and six-film-trio numbers are
  films-per-CHARACTER — computed by no asset (hand-derived from `raw_people[].films` at
  site-authoring time); beat 6's per-person pilot counts are not in per-ship
  `starship_stats`; `galaxy_report` has zero checks. Only beats 0, 2, 3 have checks that
  assert the displayed number.
- **WARN severity is runtime-only in Dagster; `spec.blocking` is static** (data-engineer,
  qa-engineer): provenance must encode `blocking` and derive badge wording from it.
- **README.md is truncated mid-word with an unclosed code fence** (hiring-manager).
- **Desktop steps are center-anchored flex** (ux-designer): an opening reveal shifts the
  clicked summary unless growth is bottom-anchored.

## Per-role verdicts (one line each)

- lore-fanatic: ship 1–6 only; engineering register with one bridge word ("paper trail");
  "six pipelines" callback is false; no misattributed guards.
- data-engineer: ship only if honest; one asset-keyed provenance object with
  `relation: direct|derived` and `guard: check|pytest|none`; badges from `blocking`.
- data-analyst: the map is partly false — either add a per-character transform to make
  all beats DIRECT, or render honest "derived at authoring time" attribution.
- graphic-designer: reuse exercise, zero new marks; shared details selector; chips match
  `.chip`; monochrome ◆ blocks / ◇ warns; fix the 28px hit-area precedent once.
- ux-designer: 1–6 only; bottom-of-card summary; vertical chain within 260px; static at
  init inside `.step-inner`; reader-owned state; never color-only status.
- storyteller: claim → machinery → guard micro-story; honest third act; beat 0 clean;
  beat-7 callback reworded, kept; beat 4 quietest label.
- hiring-manager: honesty about coverage IS the hire signal; README tail rewrite + link
  above the fold; keep a reveal on beat 0; no coverage theater.
- qa-engineer: single test file asserting topology, check ownership, blocking-derived
  badges, verbatim rationale projection, exact coverage set, honest guard typing.
- technical-writer: all reveal strings generated/projected from provenance; checks.py
  `description=` is the single rationale source; honesty line per guard type.

## Adjudication

1. **Coverage — storyteller/lore/ux/designer win over hiring-manager; beats 1–6 only.**
   Beat 0 stays a clean hook and beat 7 gets a callback line, not a reveal. The
   hiring-manager's concern (the 82-count is our best-guarded number and must be
   scannable) is satisfied structurally: `raw_people` — carrying the shape (blocking)
   and 82-count (warn) checks — is the first node of EVERY chain, so the claim→guard
   story for the census appears in all six reveals without touching the hook.
2. **Honest labeling wins over adding a per-character transform — data-engineer and
   hiring-manager over data-analyst (for now).** Adding an asset primarily so a diagram
   can point at it is presentation-driven pipeline design, and the hiring-manager calls
   the hasty-check variant coverage theater. `relation: "derived"` beats render the
   truth: computed from `raw_people[].films` at authoring time, guarded offline by
   pytest against `known_facts.py`. The analyst's transform is logged as an open
   candidate (below) on its real merits — grain-correct analytics — not as diagram fuel.
3. **Vertical chain wins over horizontal — ux-designer over graphic-designer.** At the
   ~260px mobile budget a horizontal chain needs an overflow escape that hides the
   terminal node; a vertical stack shows every node with no scrolling. All of the
   designer's chip specs (mono, rounded rect, `--line` stroke, single gold `.hot` seat,
   ◆/◇ monochrome badges) carry over unchanged.
4. **HTML chips instead of a hand-built SVG.** The chains are ≤4 nodes of labeled boxes;
   rendering them as real `.chip` elements reuses the existing CSS verbatim (the
   designer's own must-have), keeps the text accessible without aria re-plumbing, and
   avoids SVG text-measurement hazards at small widths. The plan's "inline-SVG diagram"
   phrasing was a technology guess; the decided deliverable — a mini lineage diagram of
   the specific chain with checks marked — is unchanged.
5. **Beat-7 callback: storyteller wins over lore-fanatic's cut, with lore's wording
   law.** The line is computed from provenance so it is drift-detectable and
   arithmetically true: "One pipeline, three transforms, eight checks — the full record
   is below."
6. **No dashboard per-card mini-DAGs (unanimous minus a conditional).** The lineage
   strip is the establishing shot. Migrating the five hand-written SQL strings into
   provenance (data-engineer's stretch) is deferred — it grows this change's surface
   without a verification story for SQL text.
7. **Labels: one template, generated.** "The paper trail — where {claim} comes from"
   (lore's sanctioned bridge word); beat 4 (the held pause) renders the quietest
   variant, "The paper trail." — identical placement/size everywhere (ux's law).

## Final plan (implemented in the same PR)

- `DATA.provenance` (inside the one-line strict-JSON literal): `assets` keyed by id
  (`deps`, `checks[{name, label, blocking, why}]` with `why` projected verbatim from
  checks.py `description=`) + `claims[]` per beat 1–6 (`beat`, `chain`, `hot`,
  `relation: direct|derived`, `guard: {kind: check|pytest|none, ref}`, `label`).
- Reveal: `details.prov` sharing the details.sql summary treatment (selector extended;
  hit area raised to ≥44px for both), built statically at init at the bottom of each
  `.step-inner` for beats 1–6; body = vertical chip chain (`.chip` reuse, one `.hot`
  gold seat on the beat-relevant asset, ↓ connectors) + check rail per chip (◆ blocks /
  ◇ warns + short label) + one honesty line per guard type. No auto-open/close; no
  animation; works unchanged in flat mode; `aria-label` generated from the same data.
- Beat 7: plain-text callback line computed from provenance counts. Beat 0: untouched.
- Drift detector: extend with internal-consistency checks (claims cover exactly beats
  1–6, every chain id resolves in `provenance.assets`, badge values derive from
  `blocking`, callback counts match the object).
- `tests/test_site_provenance.py` (same commit): extract the one-line DATA JSON (loud
  failure if the format changes) → assert vs `defs.resolve_asset_graph()` and
  `check_specs`: assets/edges real; checks belong to their assets; `blocking` matches;
  `why` matches checks.py descriptions verbatim; coverage set is exactly beats 1–6;
  derived/none guards never render a check badge as asserting the number;
  `guard.kind=pytest` refs name real tests.
- README: full rewrite including the broken tail. Order: identity sentence (replacing
  "self-study workshop") → live-site link → screenshot (current one; retake stays an
  open item) → testing-philosophy paragraph incl. the provenance sentence ("every
  number on the site names its asset and its guard — including which numbers are
  guarded offline only") → architecture + quick start → `.claude/` panel as one short
  process section (human as adjudicator) → WORKSHOP.md as linked teaching appendix →
  personal-site link slot.

## Newly settled constraints (banked law)

- Every provenance/severity string on the site derives from `DATA.provenance`, which is
  pytest-verified against the real Dagster definitions; badge severity derives from
  `spec.blocking`; check rationales are verbatim projections of checks.py descriptions.
- Guard honesty: a check badge may only appear where the check asserts the displayed
  number (or its denominator/structure, labeled as such); derived/unguarded claims say
  so in plain words. No fabricated or implied live status, ever.
- Reveals exist on beats 1–6 only; beat 0 stays clean; beat 7 carries the
  provenance-computed callback. One disclosure style, shared with details.sql.
- The one-line strict-JSON format of `const DATA` is load-bearing (tests parse it).

## Open items

- Per-character-grain transform (films-per-character, starships-flown-per-person) with
  checks asserting 42-of-82, the trio, 19-of-82, maxFlown 5 — a real analytics
  improvement to consider on its own merits; would upgrade beats 4–6 to DIRECT.
- Migrating the five hand-written dashboard SQL strings into a verified home.
- README screenshots retake with 8 green checks (needs desktop UI) — unchanged.
