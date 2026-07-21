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

Cannot verify (standing): off-platform artifact link preview.

## Prep notes: production pattern (partition/SCD) vs "Limits, by design" (2026-07-21)

Knew: "Limits, by design" (README L124-144) is settled honest copy — each bullet is
limit → why-fine-now → forcing trigger, incl. "Full refresh, no history" and "No
partitions." The #2 why-not principle (don't trade a rare signal for table stakes).

Learned (crux — the ASYMMETRY that separates this from #2): in the dagster-duckdb case
the strong signal (the tested `read_only` single-writer contract) was ALREADY REAL in
the code; the why-not merely declined a DIFFERENT idiom. Here, "no history / no
partitions" documents patterns that appear NOWHERE in the repo — the why-not EXCUSES an
absent capability rather than PROTECTING a demonstrated one. That is materially weaker:
a reviewer probing rec #3's "can you actually build incremental/SCD/partitions?" finds
prose, not proof. A why-not naming a mechanism you've never shown < a why-not for a
mechanism the repo proves elsewhere. So the #2 principle does NOT automatically save the
limit here; the two why-nots are different species.
- schedules.py: `daily_refresh_schedule` re-pulls ALL endpoints; docstring already says
  "swap in a live API, schedule logic stays identical" — the cadence is real, the
  incremental payoff is asserted but never demonstrated. Latent probe: "you run daily but
  full-refresh a static snapshot — so what does the schedule prove?"
- Real keys that EXIST: `episode_id` (6 films), the 5 endpoints, homeworld. NO time/date
  key in source — a time-partitioned incremental would be FAKED (the cargo-cult tell).
- Contrivance ranking: (a) static partitions over `episode_id`/endpoint = least dishonest
  (real key, honest backfill/reprocess semantics, no faked change) but tiny; (b) daily-
  snapshot SCD2/MERGE = stronger senior pattern BUT "hollow if never changes" — needs a
  simulated delta, the exact tell the honesty signal guards against.
- Leaning: the honest limit out-signals bolt-on machinery ONLY if we keep excusing an
  absence; the sharper move is ONE genuinely non-contrived demonstration over a REAL key
  (lean (a) episode_id partitions) + guard (partition/backfill test) in the same commit,
  with "Limits" REWRITTEN to "partitioning demonstrated over episode_id; time-partitioned
  incremental still absent because the source is static." Keep pipeline-only for v1 (no
  site/provenance touch); asset/check counts ripple (count-ripple law, tech-writer owns).
  Verdict is NOT a default yes and NOT a default no — it turns on whether the chosen form
  is non-contrived AND the copy stays honest about what is/ISN'T demonstrated.

Can't verify: whether a per-film/per-endpoint reprocess serves any real analytics
consumer (if not, (a) is still decoration); the final asset/check count delta (freeze).

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
