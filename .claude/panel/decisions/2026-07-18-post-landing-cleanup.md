# Decision: post-landing cleanup — spoiler leaks, SQL truth, coverage gaps

Date: 2026-07-18 · Scope: all nine roles (site + pipeline) · Orchestrator: Claude

## Brief (summary)

After the per-character transform landed (082d9c9), three questions: (Q1) the storyteller's
leak audit fails — beat 4's paper-trail rail pre-announces the trio, "19 pilots", and
"max flown = 5"; beat 5 pre-announces beat 6; beat 1 shows "23 unweighed" pre-beat-2.
(Q2) the five dashboard SQL strings needed a verification story — and prep proved three of
five are WRONG today (charts 2/4 query `characters_enriched`, which was never a DuckDB
table; chart 1's `len()` returns string length — the orchestrator's execution run confirmed:
1222 "characters" for Episode I, two CatalogExceptions). (Q3) beat-1 height nulls and
galaxy_report have no checks — act or disclose. Full brief + readiness notes in git history
of this branch (panel prep commits 1b6a385..4c6fcdc).

## Per-role verdicts (one line each)

- lore-fanatic: rendering fix (cumulative beat-indexed rail); never rewrite checks.py — "the description IS the canon correction"; Q2 adopt; Q3(a) yes.
- data-engineer: re-author strings, uniform rail; Q2 adopt WITH characters_enriched write-back so `FROM characters_enriched` becomes true; Q3(a) yes, (b) disclose-only.
- data-analyst: re-author with number-free labels ("all-six set", "pilot census", "flight record", "mass coverage"); compare layer must assert SQL rows == DATA rows; chart-5 denominator on-card; Q3(a) yes.
- graphic-designer: filter rail to guard+blocking uniformly; the DAG strip is the record, the rail the citation; no new "verified" marks; Q3(a) yes — one earned badge per beat.
- ux-designer: cumulative rail with riders; label text is the ENTIRE touch/keyboard surface (hover-why is a title attribute); the rail legend's hover promise is false — fix it; Q2 render-identical.
- storyteller: cumulative rail; beat index = spoiler clearance, max_flown = 6; strip the two meta-leak phrases ("'Ben counts' beat", "punchline of the pilots beat"); standing spoiler guard, pin numbers not just names.
- hiring-manager: re-author + uniform rail — rail density is signal, story metadata pollutes verified provenance; write-back passes the merit test (CSV-only enriched grain was the anomaly); truth-then-tell sequencing; README overclaim fixed same commit.
- qa-engineer: re-author + pin; `beat` field = hand-authored attribution pytest cannot derive (unverifiable surface); write-back OK iff same-df parity assertion and EXPECTED_DB_TABLES stays five; retracts galaxy_report weak-yes (Exercise-8 collision).
- technical-writer: re-author — the trio roster in prose is a THIRD home for one roster (one-home law); "matches known_facts.SIX_FILM_CHARACTERS" is more precise, drift-proof; README:92 + WORKSHOP Module 4 edits same commit; (b) disqualified by Exercise 8.

## Adjudication

**Q1 — re-authoring wins, 5–3–1.** The one-home law is the decisive argument: the trio
description hand-listing C-3PO/R2-D2/Obi-Wan duplicates a roster whose single source is
`known_facts.py` — a drift bug that would make the Dagster UI lie if the snapshot changed,
independent of any spoiler concern. QA's point seals it: a `beat` index is hand-authored
narrative attribution that pytest cannot verify against the real definitions, on the one
object whose credibility is "everything in it is machine-checked." Lore's "sequencing"
instinct and storyteller's "make the law executable" demand survive in the remedy: the
standing spoiler pin (term sets DERIVED from known_facts — names AND payoff numbers,
phrase-anchored; seen-to-fail before merge) makes re-authoring structural, not whack-a-mole.
UX's legend fix is adopted (the hover promise is false on touch/keyboard). The designer's
guard-only rail loses to the coverage-understatement objection (character_stats has zero
blocking checks; final beats would understate forever). Storyteller's meta-leak companion
edit is adopted — descriptions must not quote other beats' captions.

**Q2 — unanimous adopt, engineer's shape.** `characters_enriched` gains a warehouse
write-back (`CREATE OR REPLACE TABLE ... AS SELECT * FROM df` on the same df it returns —
QA's one-code-path condition, with a full_run parity assertion; `EXPECTED_DB_TABLES` stays
five, `star_wars_db_tables_populated` must NOT grow — ordering lie). The five SQL strings
move into DATA (single source; site renders only from DATA); chart 1 uses
`json_array_length`; chart 2's droid recode and charts 4/5's tiebreaks move INTO the SQL so
executed output equals rendered rows; the stale `-- 59 of 82` comment dies; chart 5's card
gets its denominator. Offline pytest: ungated EXECUTE layer + snapshot-gated COMPARE layer
(SQL results == the rows the charts derive from DATA), riding full_run's pipeline-built DB
read-only. Drift detector grows one claim (every SQL disclosure resolves a nonempty DATA
entry). README:92 corrected to "executed against the fixture warehouse by the offline
suite" + one honesty-arc sentence naming the second panel-caught false claim; WORKSHOP
Module 4 gains one write-back sentence. Hiring-manager's framing veto is law: the
write-back is closing a warehouse gap (enriched grain queryable), never "making the site's
SQL true."

**Q3 — (a) lands, (b) disclose-only, unanimous.** `characters_enriched_unknown_height_baseline`
(WARN, from EXPECTED_UNKNOWN_HEIGHT_COUNT) guards beat 1's displayed "1 unmeasured"; beat
1's guard flips pytest→check through the NOTE template. All count ripples land in the same
commit: 13 checks (4 blocking, 9 warn), WORDS list through "thirteen", README/CLAUDE.md
counts, provenance totals. galaxy_report stays check-free by design — a check there
pre-solves WORKSHOP Exercise 8 and duplicates pytest coverage (coverage-theater law); the
gap remains deliberately disclosed here.

## Final plan (truth-then-tell sequencing, two commits)

1. **SQL truth commit:** write-back + parity test; DATA gains the five corrected SQL
   strings; site renders SQL from DATA; execute-and-compare pytest (both layers); drift
   detector claim; chart-5 denominator; README:92 + honesty arc + WORKSHOP Module 4.
2. **Spoiler + coverage commit:** re-author the five leaking strings (trio, pilots,
   max-flown, unknown-mass labels/descriptions per the style rule below); spoiler pin test
   (seen-to-fail, then reverted); legend fix; height-null check + beat-1 guard flip +
   13-check ripples.
3. Screenshot retake stays open, now targeting 13 green checks (desktop UI).

## Newly settled constraints (banked)

- **Description style rule (technical-writer):** check descriptions state the invariant and
  its stakes; run metadata carries the particulars; known_facts.py is the only roster/number
  home. No check string quotes another beat's caption or payoff.
- **Spoiler pin law (qa/storyteller):** a standing offline test derives payoff term sets
  from known_facts and asserts no check string renders on a beat earlier than its claim's
  reveal; new checks pass the spoiler audit before landing.
- **Displayed SQL is executed SQL (all):** any SQL text shown on the site lives in DATA and
  is executed against the fixture-built warehouse by the offline suite; no hand-verified
  SQL copy anywhere.
- **Provenance carries no narrative fields:** everything in DATA.provenance stays derivable
  from / verifiable against the real Dagster definitions plus known_facts.
- **The rail is uniform:** every beat renders the same rule — all checks of its chain
  assets; spoiler safety lives in the strings, not the renderer.
