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

## Prep notes + Banked: pipeline-reveal & transform landing (2026-07-17/18, compacted)

Verdicts: `2026-07-18-pipeline-reveal.md`, `2026-07-18-per-character-transform-landed.md`.
Durable lessons (outcomes live in Settled):
- Commit history reads well (coherent boundaries, panel-workflow commits `9e9db1c`,
  `3a82146`, PR merges #1–#5); README need only point at it, not restate it.
- Verify a brief's claimed lineage before building the pitch on it (the beat→asset
  map was partly false; data-analyst caught it).
- 2026 loops screen for judgment over AI output; "judgment made visible" is the
  durable pitch frame; human-as-adjudicator framing for `.claude/` is settled.
- First-impression defects beat feature arguments (truncated-README catch).
- State the signal requirement, let story roles find placement (beat-0 loss, met
  structurally); coverage-theater veto held twice and became the best interview
  narrative ("label honestly first, upgrade later").
- Bring concrete wording proposals for badge/severity ground rather than ceding it.

## Prep notes + Banked: post-landing cleanup (2026-07-18, compacted)

Verdict: `2026-07-18-post-landing-cleanup.md`; commits `c0b97e0` (SQL truth) then
`2aa845e` (spoiler re-author + pin + height check). Won every axis. Durable lessons:
- Audit method that found the SQL lie: read the transform's actual `CREATE TABLE`
  list, grep every displayed `FROM` clause against it; always execute displayed code
  claims during prep. Primary verification converts opinion into evidence.
- Q3 fulcrum: a check earns its place iff it guards a number/artifact someone
  consumes (height-null qualified; galaxy_report did not — also pre-solved WORKSHOP
  Exercise 8). Third consecutive coverage-theater win; galaxy_report stays check-free
  by design, gap disclosed.
- **Truth-then-tell sequencing (reusable principle):** when a public claim is false,
  commit 1 makes it TRUE with a message naming the defect; commit 2 does the
  storytelling. Never interleave — the honesty arc only earns credit when the fix is
  separable and self-describing.
- tests/test_site_sql.py is the "displayed SQL cannot rot" answer; framing veto is
  law (see Settled).

Cannot verify (still): artifact-side render of the grown DATA literal.

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

## Prep notes: akabab second source (2026-07-20)

External facts verified (github.com/akabab/starwars-api): MIT confirmed; ~11 commits
total, effectively unmaintained static JSON on GitHub Pages; wiki/image fields point at
Wookieepedia-derived fan curation; the README itself warns "some properties may not be
provided." Consequences for the debate:
- "Drift" on akabab is near-impossible (static file); the real risk is the host
  vanishing. The honest doc framing is "curated fan dataset, effectively frozen;
  treated like any external API" — committed fixtures + blocking shape check already
  answer "what if the Pages site dies?"; docs should say so in one clause.
- Attribution honesty is an interview probe: Stack/docs must name it as fan-curated
  MIT data, distinct in trust level from SWAPI. Never imply it is official canon data.

Positions formed (repo verified against checks.py, known_facts.py,
test_site_provenance.py:76/:242, README, WORKSHOP:328/:493, snapshot_fixtures.py):
- Q1: back Option C. Option A's ripple through the pinned "five tables" strings would
  read in history as churn without cause; C keeps star_wars_db byte-identical and the
  write-back CREATE OR REPLACE TABLE character_biographies still closes the warehouse
  gap (framing law satisfied — queryable grain, pipeline merits).
- New interview question this feature answers (my signal test — it passes): "how do
  you join a second, dirtier source without fuzzy matching, and account for coverage
  honestly?" Curated PROFILE_NAME_ALIASES in known_facts + no-fuzzy-matching is the
  senior-reading answer; demand ONE sentence of why-not-fuzzy in docs. Also makes
  WORKSHOP:493's "swap the resource" claim demonstrated, not asserted.
- Failure-mode separation law applies to the JOIN: coverage baseline (data moved)
  needs a data-independent honesty companion — every PROFILE_NAME_ALIASES entry must
  resolve against the payload (dead aliases rot silently). Cheapest home: a pytest
  assertion against fixtures, not a sixth check (coverage-theater law).
- Q3: death-registry WARN earns its place iff galaxy_report actually prints the
  deceased count (check-guards-a-consumed-number fulcrum). If the report section
  drops it, the check waits.
- Spoiler exposure: new assets are provenance-UNLISTED, so their check strings do NOT
  render on site rails today — safe now; re-audit at the surfacing panel. Keep
  descriptions subject-only/number-free anyway (pre-drafted wording in hand).
- MY CATCH this round: the brief's ripple list omits SCREENSHOTS. README:16 lineage
  graph shows 11 assets/15 checks; retake at 13 assets/20 green checks in the ripple
  commit (retake-after-ripple reflex). Also README Architecture diagram/table, :48,
  :157 "five SWAPI pulls" context, :160, and Stack attribution all move in the atomic
  feature commit — feature+guard+ripple, one commit, per law.
- Commit plan (4 commits) is coherent; no false public claim exists, so
  truth-then-tell ordering isn't triggered. Commit 4 ("freeze reality") must state in
  its message that synthetic fixtures became a dated real snapshot; the fixtures
  README must label the synthetic period honestly until then.

Cannot verify: akabab's exact 87-record count and per-field sparsity (brief's numbers;
GitHub README doesn't state totals) — trust the orchestrator's 2026-07-19 fixture-join
verification. Still cannot verify off-platform artifact link preview.
