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

## Banked lessons (2026-07-17→20 rounds — compacted; outcomes live in Settled)

Verdicts in `.claude/panel/decisions/` (pipeline-reveal, per-character-transform,
post-landing-cleanup, birth-registry, akabab-second-source, akabab-site-surfacing).
Durable, reusable lessons:
- **Primary verification converts opinion to evidence** — execute code claims, grep `FROM`
  vs real `CREATE TABLE`, read framework source. Do it before pitching on a brief's claim.
- 2026 loops screen judgment over AI output; "judgment made visible" is the pitch frame;
  first-impression defects beat feature arguments. **Truth-then-tell:** commit 1 makes a
  false public claim TRUE (message names the defect); commit 2 tells the story — never
  interleave. Held under pressure (registry commit's message named the defect its guards caught).
- Coverage-theater veto held 3×; became the best interview narrative. State the signal
  requirement, let story roles place it, bring concrete badge/wording proposals. Repo-root
  hygiene scan every round (a stray bootstrap once reintroduced "self-study" framing).
- **Parse-honesty won 7-1** → Failure-mode separation law; reuse "drift vs breakage" frame
  whenever ONE check is proposed over a parse or join. **Naming can encode an invariant
  cheaper than a check** (`died_year_aby` + pytest). "Reads as churn without cause" frame
  beats feature adds that don't touch the core grain (held for the 9th beat).
- **I own whether copy reads honest, not what it says** — ceded section titles / "deaths on
  file" vocabulary to story-lore; own bullet CONTENT (interview-probe framing), tech-writer
  owns placement. **Never carry transcribed counts as facts** — state per-source, "unverified,
  demand script derivation at freeze". Executable-SQL / count-ripple laws are non-negotiable.

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
- **Documented why-not beats invariant-deleting adoption (dagster-duckdb, 2026-07-21):**
  a documented why-not that names the concrete mechanism beats adopting a framework-native
  idiom that would delete a tested safety invariant. Framework-native is NOT automatically
  the stronger portfolio signal. The pipeline keeps raw `duckdb.connect()` deliberately;
  `DuckDBResource` is not adopted because `get_connection()` hardcodes `read_only=False`,
  erasing the per-asset read-only single-writer lock. Rationale home: WORKSHOP Module 10
  (+ Module 2 forward-pointer + transforms.py comment); guarded by a rationale-marker pin
  in `test_pipeline.py`. A deliberate technology non-adoption is a GUARDABLE artifact
  (marker pinned in source beside the invariant it protects), not just prose. Do not
  "modernize" without a panel.
- **No production-pattern-for-show (production-pattern panel, 2026-07-21):** a partition /
  incremental / SCD / backfill asset is NOT added merely to signal scale. On a static,
  small, heterogeneous source lacking the pattern's dimension, EVERY demonstration is
  cargo-cult — SCD on a frozen fixture can only say "0 of N changed"; a time partition
  fakes an absent time key; an endpoint/episode partition collapses 5 clean SDAs, ripples
  the site totals/DAG-strip, and hits a many-to-many denominator trap. So the documented
  "Limits, by design" why-not is the stronger senior signal — extends #2 from framework
  idioms to architectural patterns. Docs must not claim a capability the code lacks: a
  scheduler on a static source is a full refresh and the copy says so (schedules.py fixed).
  Revisit only if the source gains a real time axis or grows past re-pull scale.

Cannot verify (standing): off-platform artifact link preview.

## Banked: production pattern (partition/SCD) (2026-07-21)

Verdict: `.claude/panel/decisions/2026-07-21-production-pattern.md`. Outcome: STAND PAT —
no partitioned/incremental/SCD asset; fix schedules.py over-claim; sharpen "Limits, by
design". My SCD2-as-v1 push did NOT win; the documented why-not held. Prep notes folded here.

Won:
- **The schedules.py over-claim fix (my must-have) shipped.** It literally claimed an
  incremental/streaming payoff ("simulates streaming"; "API would return new records each
  run") it never delivers — the ONE non-contrived weakness. Now honest: cron-driven
  orchestration + full refresh on a static source, pointing at "Limits, by design."
- **PROTECTS-vs-EXCUSES was the influential lens** — the panel adopted my framing that
  the dagster-duckdb why-not PROTECTED a real capability while "no partitions" EXCUSES an
  absent one. But the conclusion FLIPPED against me: when the data lacks the pattern's
  dimension, every demo is cargo-cult, so the honest limit is the strongest senior signal.
  My own #2 principle applied to me.

Ceded:
- **SCD2 as v1 demo** — honesty-blocked. On frozen fixtures it can only render "0 of N
  changed" (hollow), and a code-shape finding showed BOTH SCD2 and the "endpoint
  partition" ripple the site (endpoint form collapses 5 SDAs, 13→9 assets); each is
  contrived on an 82-row static heterogeneous snapshot.
- **"Anchor on the 87→88 akabab drift" — banned.** That is un-baselineable survey noise;
  it can never be a displayed number or "detected change" headline. My headline had no
  legs the instant that number was off-limits.

Prep-differently (the lesson): **price the honesty constraint on the headline BEFORE
betting a signal argument on it.** I built an SCD2 pitch whose payoff was "we detect the
87→88 change" — a number already banked as un-displayable. A banned number cannot anchor a
demo; check the honesty roles' displayed-number law FIRST, then decide if a signal
argument even has a headline left to stand on. Also: a "real key exists" (episode_id) is
NOT sufficient to save an EXCUSING demo — re-check site-ripple and denominator traps
(episode_id is many-to-many, not 82) before leaning on it.

## Banked: akabab site surfacing (2026-07-20 — compacted)

Verdict: `.claude/panel/decisions/2026-07-20-akabab-site-surfacing.md`. My positions carried;
durable lessons only (settled constraints folded into Settled block):
- **My signal argument won**: the multi-source join is now legible in a 90-second scan
  (DAG chips + coverage card + footer sources), no story beat — the strongest banked
  interview answer stopped being invisible. New settled: second-source surface is a
  dashboard card never a beat; no ranked faction chart on a six-film-scoped site (coverage
  counts only); per-card number relies on the DAG strip for lineage (no fabricated
  card-level badge); DAG chip set pinned to real Dagster keys.
- **"Reads as churn without cause" frame held again** (no 9th beat — would break four
  settled pins to carry aggregate-grade enrichment). Reuse this frame against feature
  additions that don't touch the core grain.
- **Executable-SQL non-negotiable held** (coverage COUNTS only, executed against fixture);
  contradiction fixed truth-first; headline "82 of 82 matched" (my pick).
- **Retake reflex refined**: check whether a count-bearing visual is ALREADY current before
  demanding a retake — the DAG screenshot already showed 13/20, so no retake was noise.

Cannot verify (standing): off-platform artifact link preview; script-derived fixture
counts (unverified until freeze).

## Banked: dagster-duckdb non-adoption (2026-07-21)

Verdict: `.claude/panel/decisions/2026-07-21-dagster-duckdb-decision.md`. Outcome: do NOT
migrate (Option A) — my position won. Durable constraint folded into Settled (line ~120);
skill covers guarding non-adoption with a rationale marker. Core wins (compacted):
- My signal argument carried it: a *tested* single-writer `read_only` contract is a RARER
  senior signal than "used the resource" (table stakes, scan-invisible); migrating deletes
  the strong signal to gain the weak one. Guard-honesty veto held on the two-instance (B)
  path (enforcement theater). Primary verification decisive: `get_connection()` hardcodes
  `read_only=False` — the idiom STRUCTURALLY cannot express the invariant, killing every
  adoption branch in one fact. Ding → demonstrated judgment (WORKSHOP Module 10 why-not),
  and made GUARDABLE (marker pin). Ceded nothing; IO-manager unanimous OUT.
- Reflex to keep: when a panelist proposes partial adoption, check whether the idiom can
  express the invariant AT ALL before debating placement — a structural "cannot" ends the
  branch faster than any signal argument.

Cannot verify (standing): off-platform artifact link preview.
