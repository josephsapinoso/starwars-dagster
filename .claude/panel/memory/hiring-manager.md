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
- Signals still weak: screenshots don't yet show the 12 green asset checks (open
  item; needs desktop UI). The README-opening and site/repo-invisibility weaknesses
  from PR #5 were resolved by the pipeline-reveal rewrite and the reveal disclosures.
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

## Banked: per-character transform landed (2026-07-18, execution note)

Note: `.claude/panel/decisions/2026-07-18-per-character-transform-landed.md`, commit
`082d9c9`. No new debate — the transform landed exactly on the banked acceptance
criteria, which is itself the win.

- **My coverage-theater veto held under execution pressure**: `character_stats`
  shipped with exactly the four banked WARN checks (42-of-82, six-film trio,
  19-of-82, maxFlown 5) and zero extra blocking checks; exact-value baselines stayed
  drift-severity per the known_facts law (`known_facts.py` unchanged). The "land only
  on analytics merits" constraint produced a clean asset that feeds `galaxy_report`,
  keeping the DAG-strip copy true.
- **The honesty arc is now a README narrative**, which is the best interview answer
  this repo has: "How this was built" tells panel-caught-false-map → shipped
  honestly-labeled derived beats → transform landed later and flipped them to direct.
  That sequencing (label honestly first, upgrade later) reads as senior judgment; had
  we rushed the transform in the original PR it would have read as backfilling a
  story. New interview question the repo now answers: "what do you do when a claimed
  lineage turns out to be false?"
- Totals updated everywhere: 11 assets / 4 transforms / 12 checks (4 blocking, 8
  warn); beats 4–6 now DIRECT with check badges; `raw_starships` dropped from the
  provenance map since no claim cites it — good hygiene, no dangling implied lineage.
- Bonus signal: the flip surfaced two latent honest-rendering bugs (number-word array
  overflow, hardcoded "three transforms" copy) caught and fixed in the same commit,
  with the drift detector extended. Feature+guard same-commit law held.

Newly settled (promoting nothing new — all covered by existing Settled entries; the
no-diagram-fuel and guard-honesty laws did the work here).

Open items now: (1) README screenshot retake — needs 12 green checks in the lineage
view, desktop UI required; (2) five dashboard SQL strings still unverified — no badge
or verified-home yet; watch that nobody adds an implied guard to them meanwhile.

Open items I track: screenshot retake (now 12 green checks — see next section);
dashboard SQL strings into a verified home (still unverified, blocked on a
verification story). Per-character transform: LANDED, see next section.

## Prep notes: post-landing cleanup — trio leak, SQL honesty, coverage gaps (2026-07-18)

**Q2 is the hire-signal event; I verified the audit myself, it is not hearsay.**
`transforms.py:81-87` creates only `films/people/planets/starships/species` tables;
`characters_enriched` exists solely as DataFrame + CSV (`transforms.py:130`). Yet chart 2
(index.html:1047) and chart 4 (:1184) display `FROM characters_enriched`, and chart 1
(:985) displays `len(f.characters)` — string length of stringified JSON (lists are
`json.dumps`'d at load, :74; the real transform uses `json_array_length`). Three of five
displayed SQL strings are false against the warehouse they claim to describe. README says
"Provenance you can't fake" (line 29) and "the DuckDB SQL behind every chart" (line 92) —
a false explicit README claim. An interviewer who opens one SQL disclosure and greps
transforms.py catches this in ~3 minutes. The brief's candidate story (SQL into DATA,
offline pytest EXECUTES each string against the fixture DB, asserts results == inline
numbers) is the right shape: it forces the three lies to be rewritten to real tables and
converts the liability into the repo's best interview answer ("our displayed SQL was
wrong; now CI executes it"). Watch for a "persist characters_enriched into DuckDB so the
SQL becomes true" counter — that's pipeline change for presentation; my no-diagram-fuel
law applies unless it has analytics merit.

**Q1**: leak is three-wide (trio label + "19 pilots" + "max flown 5" — beats 5/6 payoffs
all render in beat 4's rail because `chainEl` (index.html:823-843) dumps every check of
every shared-chain asset). A half-fix already exists: beat 4's summary is special-cased to
omit claim text (:859). Rail is informational, not a guard badge, so filtering it per-beat
does NOT touch guard-honesty law. Hiring lens: minor scan-signal item; a per-beat
rendering rule (guard check + blocking only on non-final shared-chain beats) reads as
craft; re-authoring checks.py strings alone can't fix the "19 pilots" label without making
the Dagster-UI description worse.

**Q3 fulcrum** (my law): a check earns its place iff it guards a number/artifact someone
consumes. (a) height-null WARN on `characters_enriched` guards beat 1's displayed
"1 unmeasured" and flips it pytest→check, matching beat 2's pattern — legitimate, not
theater; also gives the falsely-cited asset its first check. (b) galaxy_report structural
check is weaker — the site cites nothing from the report; only defensible as a blocking
"file written, sections present" smoke test on the artifact the README quick-start tells
people to read. Lean: (a) yes, (b) only if framed as consumer-facing smoke, else
disclose-only.

Cannot verify: whether the fixture-DB pytest path can execute all five rewritten strings
cheaply (chart 3/5 use TRY_CAST — likely fine, untested); artifact-side render of a
grown DATA literal.
