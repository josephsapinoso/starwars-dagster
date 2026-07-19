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
- No standing weak signals: screenshot item CLOSED at 15 green checks (f170379);
  dead portfolio link and the ps1 bootstrap script are gone. Counts: 15 checks.
- The 90-second scan path to design for: recruiter opens README on a phone → headline
  + live site link → one architecture visual → one testing-philosophy paragraph →
  decides whether to open the site or the code.

## Prep notes: pipeline-reveal (2026-07-17, compacted after banking)

Kept for reuse (verdict resolved the rest — see Settled and Banked):
- Commit history reads well: coherent boundaries, panel-workflow commits (`9e9db1c`,
  `3a82146`) make the agent infra discoverable; PR merges #1–#5 show iteration. README
  need only point at it, not restate it.
- The brief's beat→asset map was partly false (per data-analyst): the films-per-
  character numbers (beats 4–5 flavor) are hand-derived at site-authoring time from
  `raw_people[].films`; `galaxy_report` has zero checks. Lesson: verify a brief's
  claimed lineage before building the pitch on it.
- `.claude/` 9-agent panel is a double-edged 2026 signal: reads "AI built this"
  (discount) or "engineers their AI collaboration" (premium) depending on framing;
  human-as-adjudicator framing chosen, now settled in README order.
- External context (2026 loops): trust in raw AI output falling (29%, from 40% in
  2024); loops screen for judgment over AI output — spotting what's wrong, explaining
  tradeoffs; live demos out-engage prose. "Judgment made visible" is the durable pitch
  frame for this repo. (dataexpert.io, dataengineeracademy.com, herohunt.ai.)

Cannot verify: how the artifact URL renders as a link preview off-platform.

## Banked: pipeline-reveal + transform landing (2026-07-18, compacted)

Verdicts: `2026-07-18-pipeline-reveal.md`, `2026-07-18-per-character-transform-landed.md`.
Durable lessons only (outcomes live in Settled):
- First-impression defects beat feature arguments: finding the truncated README in
  prep was the round's highest-leverage catch.
- Lost beat-0 reveal, but the signal was met structurally (`raw_people` opens every
  chain). Lesson: state the signal requirement, let story roles find the placement;
  don't spend capital on placement fights when structure can satisfy the concern.
- Coverage-theater veto held twice: transform landed later on analytics merits with
  exactly the banked WARN slate, which turned "label honestly first, upgrade later"
  into the repo's best interview narrative. Rushing it would have read as backfilling.
- Bring concrete wording proposals for badge/severity ground rather than ceding it to
  qa/designer.

## Prep notes: post-landing cleanup (2026-07-18, compacted after banking)

Kept for reuse (verdict resolved the rest — see Settled and Banked):
- The audit method that found the SQL lie is the reusable part: read the transform's
  actual `CREATE TABLE` list, then grep every displayed `FROM` clause against it. Three
  of five site SQL strings were false (charts 2/4 queried a never-created table; chart 1
  measured stringified-JSON length). An interviewer catches that class of defect in ~3
  minutes — always execute displayed code claims during prep, never trust them.
- Q3 fulcrum held as stated: a check earns its place iff it guards a number/artifact
  someone consumes. Height-null WARN qualified (guards beat 1's "1 unmeasured");
  galaxy_report did not (no site claim cites it; would also pre-solve WORKSHOP
  Exercise 8 — qa/tech-writer supplied that second reason).

Cannot verify (still): artifact-side render of the grown DATA literal.

## Banked: post-landing cleanup (2026-07-18)

Verdict: `.claude/panel/decisions/2026-07-18-post-landing-cleanup.md`. Implemented in
two commits: `c0b97e0` (SQL truth) then `2aa845e` (spoiler re-author + pin + height
check). Won on every axis this round.

- **Q1 (won, 5-3-1):** re-authoring + uniform rail. Rail density is coverage signal;
  narrative metadata pollutes the one object whose credibility is "machine-checked".
  The designer's guard-only rail lost: thinning the rail hides real check density.
- **Q2 (won, unanimous, my shape):** interview-kill → best-answer conversion made
  REAL — tests/test_site_sql.py executes every displayed SQL string against the
  fixture warehouse and compares to chart rows. "Our displayed SQL was wrong twice;
  CI executes it so it cannot rot." Framing veto banked as law (see Settled).
- **Truth-then-tell sequencing happened exactly as I argued** and is now a reusable
  principle: when a public claim is false, commit 1 makes the claim TRUE (and the
  commit message names the defect — c0b97e0 does); commit 2 does the storytelling/
  polish. Never interleave: a mixed commit reads as burying the fix; the honesty arc
  only earns credit when the fix is separable and self-describing. README gained the
  second-false-claim sentence in the truth commit, where it belongs.
- **Q3(b) disclose-only held** — third consecutive win for the coverage-theater law
  under pressure; galaxy_report stays check-free by design, gap disclosed.

Prep lesson (durable): executing the displayed SQL myself during prep — rather than
arguing from the brief — is what made the position unassailable; primary verification
converts opinion into evidence the panel can't discount.

## Prep notes: improvement survey (2026-07-19, compacted after banking)

All three findings shipped (dead portfolio link → HTML-comment slot; ps1 bootstrap
script deleted; Limits section landed — see Banked below). Reusable method: scan the
repo ROOT for stray personal files every round — a one-time bootstrap script had
quietly reintroduced the "self-study" framing the README rewrite removed.

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
