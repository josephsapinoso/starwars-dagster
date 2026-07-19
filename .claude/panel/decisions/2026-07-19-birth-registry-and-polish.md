# Decision: the birth registry, the coda, hue enforcement, limits-by-design

Date: 2026-07-19 · Scope: all nine roles · Orchestrator: Claude
Prep: the 2026-07-19 improvement survey served as this debate's PREP pass (all nine
seats researched these exact proposals and banked prep notes; the survey returns were
circulated as the readiness notes).

## Brief (summary)

Four debate-worthy survey items: (Q1) the age census — birthYear 100% unused, 39 of 82
undated, verified oldest Yoda 896BBY / Jabba 600BBY, all 43 dated values BBY, zero ABY;
(Q2) a coda + re-read affordance; (Q3) dashboard hue enforcement under the one-data-hue
law; (Q4) a "Limits, by design" README section. Full brief and returns in git history.

## Per-role verdicts (one line each)

- lore-fanatic: Q1(a) — BBY is the dataset's own unit, two-register safe; the canon gem: 896 + 4 = 900, matching Yoda's own RotJ count; annotations capped at Yoda + Jabba; no ABY implied anywhere.
- data-engineer: Q1(a) firmly; one column `birth_year_bby DOUBLE`, sign-safe parse, raw string stays in `people`; parse-honesty + baseline checks; ABY branch pytest-tested with synthetics or it's dead code; Q4 add the no-history bullet, drop "unpinned env".
- data-analyst: Q1(a); card display lines with denominators everywhere; ONE check (lost, see adjudication); gender segments must stay named and sum to 82; Vader is not an extreme.
- graphic-designer: zero new mark types anywhere — the registry card reuses the part-to-whole bar (undated as faint tint) and the dot strip with two annotations, Yoda alone gold-ringed; Q3 spec: amber deleted, persistent gold rings on the three true extremes, hyper s2→s1, gender opacity ladder [1,.75,.55,.4,.28] with the legend CONVERTING not dying, films tint.
- ux-designer: coda mechanics (block anchor ≥44px, `tabindex="-1"` on #story, aria-hidden glyph, no JS); no content in title tooltips — the BBY gloss prints; 360px sliver proof before legend conversion; labeled marks get keyboard parity.
- storyteller: the coda drafted verbatim (number/name/payoff-free, after the last grid, never the footer); the Yoda annotation earns its place as the audit-canon motif's second and last use — 900 only as quoted testimony, never derived; check descriptions subject-only (they rail on the held pause).
- hiring-manager: parse-honesty EARNS its keep — drift vs breakage is the interview answer; Q4 bullets drafted (limit → why fine now → forcing trigger); truth-then-tell sequencing; recruiter-screenshot rationale for Q3.
- qa-engineer: TWO checks, different failure modes on different layers — without parse-honesty, "39 undated" can silently mean "39 unparsed" while the badge glows; ripple is 13→15; the coda digits-pin STANDS as an absence assertion (don't pin wording); full guard slate specced; render-only is a review fact, not a fakeable test.
- technical-writer: Q4 placement between "How this was built" and "Learn Dagster" (honesty-genre continuity, Module-10 handoff adjacency); WORKSHOP:705's "thirteen checks" is a live count-drift surface — retire it count-free; only (a) is coherent for Q1.

## Adjudication

**Q1 — unanimous (a), engineer's column, TWO checks (7–1 with one abstention).** The
analyst's one-check economy loses to the failure-mode argument (qa/hiring-manager/
engineer): the baseline detects data drift, parse-honesty detects format breakage, and
conflating them lets the headline number lie under a glowing badge. The analyst's card
shape, denominators, and Vader ruling all win. Lore's annotation cap and typography
("896 BBY", positive, as filed) win; the storyteller's framing governs the Yoda line —
900 appears only as quoted testimony being audited. Checks' descriptions are subject-only
and number/name-free (they render on beats 4–6 rails); 39/43/896/Yoda live in
known_facts only. Ripple is 13→15 everywhere, screenshots retaken once, after.

**Q2 — adopt the storyteller's coda verbatim with ux mechanics; the digits-pin stands
(5–3).** QA's ruling frames it: the pin guards the exemption's premise, not the content —
theater would be pinning the wording, which no one does. Placement after the final grid
inside main; the footer stays footer.

**Q3 — adopt the designer's spec in full.** Amber dies; the gold ring means "extreme"
or it means nothing (Vader: label only); hyper goes saber blue; the gender bar takes the
opacity ladder with the legend converting to matching swatches (names + counts summing
to 82 stay visible, solving the sliver problem without leaders); films keeps its real
second series as a tint. Render-only is verified at review by the DATA literal's
byte-identity — no fake mechanical test. New persistent labels compute from DATA and
get keyboard parity.

**Q4 — adopt: hiring-manager's bullets, technical-writer's placement and closing link.**
Engineering register only, number-free, every bullet true of the current repo, one link
to WORKSHOP Module 10 as the sole home of the tooling why-nots. WORKSHOP:705's
hardcoded "thirteen checks" is retired count-free in the same commit, and WORKSHOP joins
the permanent count-ripple checklist.

## Final plan

1. **Commit 1 — the birth registry (pipeline + site + guards, one commit because
   provenance totals couple them):** `birth_year_bby` column; known_facts constants
   (UNDATED=39, DATED=43, OLDEST_BBY=896.0, Yoda's name); two WARN checks with green
   assertions; ABY/fractional/garbage parse pytest on synthetics; the registry card
   (#card-registry, Census section, span12) with bar + dot strip, two annotations, BBY
   gloss printed, table toggle; DATA.sql.ages + compare test; drift-detector claims;
   provenance totals 15; WORDS "fourteen"/"fifteen"; spoiler terms extended; README/
   WORKSHOP count ripples.
2. **Commit 2 — coda + hue enforcement:** storyteller's lines + ux mechanics + digits
   pin; designer's four chart changes; headless 360px verification.
3. **Commit 3 — Limits, by design** in the README per the adopted shape.
4. Screenshots retaken once at 15 green checks; artifacts republished; BANK pass.

## Newly settled constraints (banked)

- **Failure-mode separation law:** a displayed number derived through a parse gets two
  guards — a drift baseline and a data-independent parse-honesty invariant — because
  "the data moved" and "the parser broke" must fail differently.
- **Quoted-testimony rule:** external claims (dialogue, canon) may be audited in copy but
  never rendered as site-derived data; derived numbers come only from DATA.
- **Absence pins are legitimate guards:** an element exempted from a detector by a
  property (number-free, spoiler-free) gets a pin asserting that property; pinning
  wording is theater.
- **The gold ring means "extreme":** persistent gold emphasis marks assert superlatives
  only; named non-extremes get labels, never rings.
- **WORKSHOP.md is on the count-ripple checklist**; teaching prose states counts
  count-free unless the count is the lesson.
