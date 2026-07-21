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
`-post-landing-cleanup.md` (won every cleanup axis; commits `c0b97e0`, `2aa845e`).
Durable lessons (outcomes live in Settled):
- Verify a brief's claimed lineage before pitching on it; primary verification
  (execute code claims, grep `FROM` vs real `CREATE TABLE`) converts opinion to evidence.
- 2026 loops screen judgment over AI output; "judgment made visible" is the pitch frame;
  first-impression defects beat feature arguments. **Truth-then-tell:** commit 1 makes a
  false public claim TRUE (message names the defect); commit 2 tells the story. Never interleave.
- Coverage-theater veto held 3× and became the best interview narrative; state the signal
  requirement, let story roles place it, but bring concrete badge/wording proposals. Repo-root
  hygiene scan every round (a stray bootstrap once reintroduced the "self-study" framing).

## Banked: birth registry + akabab rounds (2026-07-19/20 — compacted)

Verdicts: `2026-07-19-birth-registry-and-polish.md`, `2026-07-20-akabab-second-source.md`.
Outcomes live in Settled; durable lessons only:
- **Parse-honesty won 7-1** → Failure-mode separation law. Frame ("drift vs breakage") to
  reuse whenever a single check is proposed over a parse or a join (it recurred as alias
  governance: coverage WARN = data moved; ungated injectivity/load-bearing pytest = bridge
  rotted; "one pytest, not a sixth check" beat a new check, aligned with qa's five-ceiling).
- **Limits bullets** shipped near-verbatim: I own bullet CONTENT (interview-probe framing),
  tech-writer owns placement — their honesty-genre-continuity argument beat mine.
- **Naming can encode an invariant cheaper than a runtime check** (`died_year_aby` + pytest,
  no sign-convention check). Prefer it when available.
- **Truth-then-tell held under pressure**: registry commit came first, message names the
  mid-implementation defect its own guards caught — commit history showing guards catch a
  real defect DURING development beats any prose claim.
- **Ceded rightly**: section title + "deaths on file" vocabulary to story/lore roles — I own
  whether copy reads honest, not what it says.
- **Would prep differently**: never carry transcribed counts as facts (three surveys
  disagreed 87/88, died 47/28) — state per-source numbers "unverified, demand script
  derivation at freeze". Pre-draft check-description wording (subject-only, number/name-free)
  since that spoiler-rail constraint interacts with my guard-honesty law.

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

Cannot verify (standing): off-platform artifact link preview.

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
migrate (Option A) — my position won and my core argument carried the decision. Prep notes
folded here (superseded). Idiom-vs-discipline skill updated (Step 3 now covers guarding
the non-adoption with a rationale marker).

Won (decisive):
- **My signal argument carried it**: a *tested* single-writer `read_only` reader/writer
  contract is a RARER, stronger senior signal (shows single-writer-lock/lifecycle
  awareness few portfolio pipelines demonstrate) than "used the resource" — table stakes,
  invisible in a 90-second scan. Migrating deletes the strong signal to gain the weak one.
- **Guard-honesty veto held on (B)**: two same-file `DuckDBResource` instances would move
  the reader/writer distinction into Definitions wiring — best case idiomatic-but-invisible,
  worst case enforcement theater (uncertain the hardcoded kwarg even honors config
  read-only). My "don't trade a proven signal for a common one" frame closed it.
- **Primary verification was decisive** (data-engineer + qa confirmed): `get_connection()`
  hardcodes `read_only=False`, no per-connection args, stable 1.7–1.13. The idiom
  STRUCTURALLY cannot express the invariant — this killed the full migration, the
  path/config compromise, AND the (C) subclass in one fact. Reading framework source, not
  the brief, converted opinion to evidence again.
- **The ding became demonstrated judgment**: documented why-not (WORKSHOP Module 10 beside
  the Great-Expectations why-not + Module 2→3 forward-pointer + transforms.py comment)
  answers "why not dagster-duckdb?" — knows the idiom AND has a concrete reason. Same
  "Limits, by design" / failure-mode-separation shape already banked.
- **Non-adoption made GUARDABLE** (with qa): rationale-marker pin in test_pipeline.py
  asserts `"DuckDBResource"` + `"read_only=False"` present in source, so a future
  "modernize" refactor trips both the safety pin and the marker. Prose alone rots.

Lost/ceded: nothing of mine. IO-manager (5 raw tables ≠ 1 table/key, breaks provenance
pin + site lineage strip) was unanimous OUT; the writer/tech-writer owned the WORKSHOP
placement and Module 2 coherence-gap fix (their ground, better than my framing).

Would prep differently: nothing structural — arriving with the framework-source fact
pre-verified let me pre-empt the compromise positions before they were raised. The one
reflex to keep: when a panelist proposes a partial adoption, check whether the idiom can
express the invariant AT ALL before debating placement; a structural "cannot" ends the
branch faster than any signal argument.

Cannot verify (standing): off-platform artifact link preview.
