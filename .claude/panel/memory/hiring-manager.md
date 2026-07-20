# Data Engineering Hiring Manager — Panel Memory

## Settled (do not relitigate)

- The README is the landing page and must survive the 90-second scan; docs must
  explain the *why* and the tradeoffs, not just the how — visible reasoning is the
  hire signal. (Recruiter-lens panel, PR #5.)
- Commit history is part of the portfolio: clear messages, coherent commit boundaries,
  visible decision points. (Recruiter-lens panel, PR #5.)
- The testing architecture (pytest for code offline / asset checks for data live,
  ERROR-vs-WARN severity discipline, `known_facts.py` single source) was chosen
  specifically because it *reads* as senior judgment — do not dilute it with framework
  sprawl or coverage theater. (Testing panel, PR #3.)
- Guard honesty IS the hire signal: a check badge may only appear where the check
  actually asserts the displayed number (or its denominator/structure, labeled as
  such); derived/unguarded claims say so in plain words; no fabricated or implied live
  status. (Pipeline-reveal panel, 2026-07-18.)
- Every provenance/severity string on the site derives from `DATA.provenance`,
  pytest-verified against the real Dagster definitions; badge severity derives from
  `spec.blocking`; check rationales are verbatim projections of checks.py
  descriptions. The one-line strict-JSON `const DATA` format is load-bearing.
  (Pipeline-reveal panel, 2026-07-18.)
- Reveals exist on beats 1–6 only; beat 0 stays a clean hook; beat 7 carries the
  provenance-computed callback ("One pipeline, three transforms, eight checks…").
  The 82-count guard story is covered structurally: `raw_people` opens every chain.
  Do not re-argue a beat-0 reveal. (Pipeline-reveal panel, 2026-07-18.)
- README order is settled: identity sentence (no "self-study workshop" framing) →
  live-site link above the fold → screenshot → testing-philosophy paragraph incl. the
  provenance sentence → architecture + quick start → `.claude/` panel as one short
  process section (human as adjudicator) → WORKSHOP.md as linked teaching appendix →
  personal-site link slot. Tail rewrite includes fixing the truncated/unclosed fence.
  (Pipeline-reveal panel, 2026-07-18.)
- No assets added primarily as diagram fuel — presentation-driven pipeline design is
  vetoed; a per-character-grain transform may land only on its analytics merits.
  (Pipeline-reveal panel, 2026-07-18.)
- Displayed SQL is executed SQL: any SQL text shown on the site lives in DATA and is
  executed against the fixture-built warehouse by the offline suite; no hand-verified
  SQL copy anywhere. (Post-landing cleanup, 2026-07-18.)
- Framing law (mine, banked in the decision log): the `characters_enriched` write-back
  is "closing a warehouse gap" — the enriched grain becoming queryable — never "making
  the site's SQL true." Pipeline changes are justified on pipeline merits; the site
  merely benefits. Any doc/commit phrasing that inverts this gets vetoed.
  (Post-landing cleanup, 2026-07-18.)
- DATA.provenance carries no narrative fields: everything in it stays derivable from /
  verifiable against the real Dagster definitions plus known_facts. Spoiler safety
  lives in the check strings (spoiler-pin test, description style rule), not in the
  renderer or in hand-authored beat metadata. The rail renders uniformly.
  (Post-landing cleanup, 2026-07-18.)
- **Failure-mode separation law (mine + qa's, banked 7-1):** a displayed number derived
  through a parse gets TWO guards — a drift baseline AND a data-independent
  parse-honesty invariant — because "the data moved" and "the parser broke" must fail
  differently. One check conflating them lets the headline lie under a glowing badge.
  (Birth-registry panel, 2026-07-19.)
- **"Limits, by design" README section shape is law:** each bullet runs
  limit → why-fine-now → forcing trigger; engineering register, number-free, every
  bullet true of the current repo; ONE link to WORKSHOP Module 10 as the sole home of
  tooling why-nots; placed between "How this was built" and "Learn Dagster". Stated
  ceilings-with-triggers, never apologies. (Birth-registry panel, 2026-07-19.)
- WORKSHOP.md is on the permanent count-ripple checklist; teaching prose states counts
  count-free unless the count is the lesson. Quoted external claims (dialogue, canon)
  may be audited in copy but never rendered as site-derived data. Absence pins
  (asserting an exemption's premise) are legitimate guards; pinning wording is theater.
  (Birth-registry panel, 2026-07-19.)

## Working knowledge

- Interview questions this repo currently answers well: "why two test layers?", "what
  happens when the upstream API changes?", "why no Great Expectations?", "why a
  single-file site?", "what do you do when a claimed lineage turns out to be false?",
  "how do you keep displayed SQL from rotting?" (executed in CI — tests/
  test_site_sql.py), and now "how do you tell drift from breakage?" (two-check
  registry design) and "what breaks at 10x?" (Limits, by design). Every new feature
  should either answer a new question or sharpen an existing answer.
- No standing weak signals: dead portfolio link and the ps1 bootstrap script are
  gone. Counts move 11→13 assets / 15→20 checks when akabab lands; screenshot item
  REOPENS at that ripple (retake reflex).
- The 90-second scan path to design for: recruiter opens README on a phone → headline
  + live site link → one architecture visual → one testing-philosophy paragraph →
  decides whether to open the site or the code.

## Banked: 2026-07-17/18 rounds (pipeline reveal, transform, cleanup — compacted)

Verdicts: `2026-07-18-pipeline-reveal.md`, `-per-character-transform-landed.md`,
`-post-landing-cleanup.md` (won every cleanup axis; commits `c0b97e0` then
`2aa845e`). Durable lessons (outcomes live in Settled):
- Commit history reads well (coherent boundaries, PR merges #1–#5); README points at
  it, never restates it.
- Verify a brief's claimed lineage before building a pitch on it; primary
  verification (execute displayed code claims, grep `FROM` clauses against the real
  `CREATE TABLE` list) converts opinion into evidence.
- 2026 loops screen for judgment over AI output; "judgment made visible" is the
  pitch frame; first-impression defects beat feature arguments.
- Q3 fulcrum: a check earns its place iff it guards a number/artifact someone
  consumes; galaxy_report stays check-free by design, gap disclosed. Coverage-theater
  veto held three times and became the best interview narrative.
- **Truth-then-tell sequencing:** when a public claim is false, commit 1 makes it
  TRUE with a message naming the defect; commit 2 does the storytelling. Never
  interleave.
- State the signal requirement, let story roles find placement; bring concrete
  wording proposals for badge/severity ground rather than ceding it.
- Repo-root hygiene scan every round: a stray bootstrap script once quietly
  reintroduced the "self-study" framing the README rewrite removed.

## Banked: birth registry, coda, hues, limits (2026-07-19)

Verdict: `.claude/panel/decisions/2026-07-19-birth-registry-and-polish.md`. Commits:
1f3cf9e (registry), 4d92cb7 (coda + hues), 7d96df5 (limits), f170379 (screenshots).

Won:
- **Parse-honesty argument won 7-1** and is now the Failure-mode separation law (see
  Settled). The interview framing carried it: "how do you tell drift from breakage?"
  is now answerable IN the repo — baseline check = data moved, parse-honesty
  invariant = parser broke; one conflated check lets "39 undated" silently mean "39
  unparsed" under a glowing badge. This is the repo's newest strong answer; use the
  failure-mode-separation frame whenever a single check is proposed over a parse.
- **Q4 Limits bullets shipped nearly verbatim** (five bullets, limit → why-fine-now →
  forcing trigger, Module 10 linked once) at the tech-writer's placement. Verified in
  README post-landing: reads as stated ceilings with forcing triggers, not apologies —
  "what breaks at 10x?" converted from vulnerability to hire signal. Lesson: I own the
  bullet CONTENT (interview-probe framing); placement is tech-writer ground and their
  honesty-genre-continuity argument was better than any I had.
- **13→15 ripple demand landed everywhere**, including a fresh one-retake screenshot
  set at 15 green checks. The standing screenshot open item closes AGAIN at the new
  count — retake-after-ripple is now reflex; keep demanding it whenever counts move.
- **Truth-then-tell sequencing held under pressure**: registry commit came first and
  its message names the mid-implementation defect the guards caught (DATA.sql.ages
  referenced a table that didn't exist until character_stats got its write-back — the
  second verification-driven write-back). The commit history now shows guards catching
  a real defect DURING the feature's own development — stronger than any prose claim.

Lost/ceded: nothing of mine this round; the analyst's one-check economy lost to the
position I shared with qa/engineer. The coda digits-pin I backed is law (absence
pins guard the exemption's premise; pinning wording is theater).

Would prep differently: nothing structural — primary verification (executing parses,
scanning repo root, reading the actual README tail) keeps converting opinion into
evidence. Next round, pre-draft the check-description wording too: subject-only,
number/name-free descriptions were adjudicated via storyteller/qa; that spoiler-rail
constraint interacts with my guard-honesty law and I should arrive with wording.

Open items I track: (1) watch that future copy never frames write-backs as
site-serving (framing law); (2) Limits section must stay true — if any bullet's
forcing trigger fires (e.g., partitions land), the bullet updates in the same commit.

## Banked: akabab second source (2026-07-20)

Verdict: `.claude/panel/decisions/2026-07-20-akabab-second-source.md`. Option C
ratified unanimously; my prep notes for this round are folded here (superseded).

Won:
- **Option C** with my exact history argument: Option A's ripple through the pinned
  "five tables" strings would read as churn without cause; C keeps star_wars_db
  byte-identical and the write-back still closes a warehouse gap (framing law holds).
- **Alias governance is the failure-mode-separation law applied to a join**: coverage
  WARN check = data moved; ungated pytest (injectivity + every-alias-load-bearing) =
  the bridge itself rotted. My "one pytest, not a sixth check" home won — qa's
  five-check ceiling and my coverage-theater law pointed the same way. Amendment I
  accepted: alias-resolution-against-fixtures assertions are dual-snapshot-gated
  (they depend on payload contents), while injectivity/load-bearing stay ungated.
- **No sign-convention asset check** — naming (`died_year_aby`) plus pytest suffices;
  the engineer's column-rename veto delivered the same safety cheaper. Pattern: when
  a naming convention can encode the invariant, prefer it over a runtime check.
- **Docs ripple + screenshot retake in the feature commit.** MY CATCH: the brief's
  ripple list omitted screenshots (README:16 shows 11 assets/15 checks; retake at
  13/20). Retake-after-ripple is now a written tripwire in the decision log itself.
- **Q3 fulcrum held via the analyst's symmetry rule** (same principle, her phrasing):
  the report prints deaths-on-file, so its drift guard ships in the same commit.
- Interview-signal test passed: the feature answers "how do you join a second,
  dirtier source without fuzzy matching and account for coverage honestly?" — one
  why-not-fuzzy sentence lands in docs; WORKSHOP:493's "swap the resource" claim
  becomes demonstrated, not asserted.

Lost/ceded (both rightly):
- **Section title**: storyteller's "Affiliations & Apprenticeships" beat the
  alternatives on the as-filed tiebreak (source field is literally `affiliations`).
  Copy is story ground; I own whether it reads honest, not what it says.
- **Vocabulary**: lore's "deaths on file" package beat plain "deceased" — attribution
  honesty (fan-curated, sequel-inclusive AND canon-incomplete) was my probe, but
  lore's wording answers it better than my prep framing ("curated fan dataset,
  effectively frozen") which survives only in the Stack attribution line.

Would prep differently: baselines-by-script (three independent surveys disagreed —
87/88 records, died 47/28) proves I should never carry transcribed counts into
debate as facts; next time, state per-source numbers as "unverified, demand script
derivation at freeze." My prep correctly flagged I couldn't verify the 87.

Watch items: (1) commit 4's message must name the synthetic→real fixture transition;
fixtures README labels the synthetic period until then. (2) At the surfacing panel:
re-audit spoiler exposure of the five new check strings, extend spoiler-pin term
sets if character_biographies joins a beat chain, and hold the Yoda-derivation
pre-veto. (3) Screenshot retake at 13 assets/20 green checks closes the count item.

## Settled additions (2026-07-20, akabab panel — do not relitigate)

- Enrichment-join numbers always carry nested denominators (matched AND
  field-present); this is report-copy discipline computed from data, not new checks.
- Signed-year columns name their convention in the column name (`_bby`/`_aby`); no
  bare year columns in the warehouse.
- Cross-source derived figures (SWAPI birth × akabab death arithmetic) are
  quoted-testimony territory — pre-vetoed off all surfaces pending a surfacing panel.
- Name aliases between sources: curated dict in known_facts with canon-direction
  comments, injectivity + load-bearing pytest, no fuzzy matching ever; aliases bridge
  joins, they never mutate as-filed records.
- Akabab "died" data is "on file" vocabulary everywhere; never "deceased", never
  canon-complete claims. Akabab is attributed as fan-curated MIT SWAPI-derived data,
  never canon authority.
- The site WORDS number-renderer is a guard surface: it grows (with its pytest pin)
  in the same commit as any DATA-rendered count it must spell.

Cannot verify (standing): off-platform artifact link preview.
