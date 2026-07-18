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

## Working knowledge

- Interview questions this repo currently answers well: "why two test layers?", "what
  happens when the upstream API changes?", "why no Great Expectations?", "why a
  single-file site?". Every new feature should either answer a new question or
  sharpen an existing answer.
- Signals still weak as of PR #5: README opens as a self-study workshop (reads
  tutorial-follower, undersells); screenshots don't yet show the 8 green asset checks
  (open item); the site's engineering craft is invisible to someone who only skims the
  repo — and the repo's pipeline is invisible to someone who only sees the site.
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

Cannot verify: how the artifact URL renders as a link preview off-platform; whether
screenshots can be retaken (needs desktop UI — still open).

## Banked: pipeline-reveal (2026-07-18)

Verdict: `.claude/panel/decisions/2026-07-18-pipeline-reveal.md`. Reveals on beats
1–6 as bottom-of-card `details.prov` disclosures (vertical `.chip` chains + check
rail), all strings generated from a pytest-verified `DATA.provenance` object; README
fully rewritten portfolio-first.

Won:
- **README hero spec** adopted nearly verbatim: identity sentence replaces "self-study
  workshop", live-site link above the fold, testing-philosophy paragraph with the
  provenance sentence, tail rewrite fixing the unclosed-fence defect I found in prep.
  Finding the truncated README was the prep pass's highest-leverage catch — first
  impressions defects beat feature arguments.
- **Honesty-as-signal framing** carried adjudication #2: my "coverage theater" veto of
  a hasty per-character transform beat the analyst's push for all-DIRECT beats. The
  transform survives only as an open candidate on analytics merits.
- Beat-7 callback survives (reworded, provenance-computed) — the portfolio close I
  wanted, made drift-detectable.

Lost:
- **Beat-0 reveal.** Story roles won: the hook stays clean. My underlying concern
  (82-count is our best-guarded number and must be scannable) was satisfied
  structurally — `raw_people`, carrying the shape-blocking and 82-count-warn checks,
  is the first node of EVERY chain, so the census guard story appears in all six
  reveals. Lesson: when my signal concern can be met structurally, arguing placement
  is spending capital on the wrong axis; next time, state the signal requirement and
  let the story roles find the placement.

Would prep differently: pre-check whether a proposed reveal's underlying guard is
reachable from other surfaces before demanding prime real estate for it; and bring a
concrete badge-wording proposal (the `blocking`-derived ◆/◇ scheme won without me —
qa/designer owned that ground I could have shared).

Open items I track: per-character-grain transform (would upgrade beats 4–6 to
DIRECT — support only with real checks: 42-of-82, trio, 19-of-82, maxFlown 5);
screenshot retake with 8 green checks; dashboard SQL strings into a verified home.
