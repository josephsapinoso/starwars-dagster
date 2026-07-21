# Decision: demonstrate a production pattern (partitions / incremental / SCD)?

Date: 2026-07-21 · Scope: pipeline + portfolio-presentation · Panelists: data-engineer,
data-analyst, qa-engineer, technical-writer, hiring-manager. Orchestrator/final decision:
Claude (main session), with the owner making the final call on a balanced split.

## Brief
Portfolio assessment rec #3: the pipeline is full-refresh on a small static dataset, so a senior
reviewer can't see whether the author can build partitioned / incremental / SCD assets. Proposal:
add ONE such asset. This REOPENS the banked "Limits, by design" copy that documents those absences
as deliberate. Full brief in the session scratchpad. Central tension: the #2 panel (same day) just
banked that *a documented why-not can beat adopting machinery* — and "Limits, by design" is exactly
such a why-not.

## Per-role verdicts (one line each)
- **hiring-manager**: SCD2/incremental-merge — the harder pattern that survives the interviewer
  probe; a partition "answers no question the data poses." Distinction: #2's why-not PROTECTED a
  real capability (read_only), "no partitions" EXCUSES an absent one. (Wanted to headline the
  87→88 drift.)
- **data-engineer**: SCD2 dated-snapshot dimension; partitions are honest-but-HOLLOW (6 rows /
  disjoint endpoints); the real change signal is refresh-to-refresh drift, not the daily cron.
- **data-analyst**: endpoint StaticPartition; VETO SCD2 — on frozen fixtures it can only say
  "0 of N changed" (hollow), and the 87→88 is un-baselineable SURVEY NOISE (banked: survey numbers
  never become displayed numbers). `episode_id` is a denominator trap (many-to-many ≠ 82).
- **technical-writer**: endpoint partition — docs-honest, reopens only ONE limits bullet (keeps
  "Full refresh, no history" literally true); SCD forces the hollow "0 changes" sentence and
  reopens two. WORKSHOP Module 10 already teaches partitions aspirationally → shipping pre-solves
  the reader's own exercise unless endpoints (which diverge from the episode_id snippet) are used.
- **qa-engineer**: endpoint partition; decisive site-ripple reading — totals (L261-269) + DAG-strip
  (L242-258) are EQUALITY pins, per-asset blob (L76-101) is SUBSET; so ANY new asset key or
  `@asset_check` ripples the site in the same commit. SCD2 adds both → not site-free + breaks
  write-back parity. Partition's CDC-risk is zero by construction.

## Adjudication
The panel split 3–2 for the endpoint partition (analyst, writer, qa) over SCD2 (engineer,
hiring-manager). But the partition majority rested on a **containment premise that the code shape
falsifies**: the raw ingestion is FIVE separate assets (`raw_films` … `raw_species`), so an
"endpoint partition" is not a contained tweak — it means collapsing five clean SDAs into one
partitioned `raw_swapi`, which drops the asset count (13→9), rewrites the WORKSHOP Layer-1 "five
SDAs, one per endpoint" lesson, changes `star_wars_db`'s signature, and DOES ripple the site
totals/DAG-strip. So both forms ripple, and **each is contrived on a static, heterogeneous, 82-row
snapshot** — the data genuinely lacks the dimension every candidate pattern needs (no time axis;
episodes many-to-many; endpoints heterogeneous; SCD on a frozen source detects nothing).

When every demonstration is contrived because the data lacks the dimension, the #2-banked principle
governs: a documented why-not beats bolted-on machinery. Crucially, the panel surfaced the ONE
non-contrived weakness — `schedules.py` literally CLAIMED an incremental/streaming payoff it never
delivers ("simulates streaming"; "the API would return new records each run"). That over-claim, not
"no partitions," was the real soft spot.

Owner's call (presented three paths): **stand pat + fix the over-claim.**

## Final decision
- **Do NOT** add a partitioned / incremental / SCD asset. Both forms are contrived on this dataset
  and ripple the site; the honest documented limit is the stronger signal (per #2).
- **Fix the real defect**: rewrite `schedules.py`'s docstring + the daily schedule description to
  state honestly that it demonstrates cron-driven orchestration and does a FULL REFRESH on a static
  source — no incremental/streaming/CDC — and point to "Limits, by design."
- **Sharpen "Limits, by design"**: a lead-in making explicit that naming the ceiling AND its
  forcing-trigger is the engineering judgment, and that a scale technique bolted onto an 82-row
  static snapshot signals less than knowing not to. Every bullet stays literally true; nothing
  deleted. Pure copy/comment honesty — no code behavior change, no new asset/check, no site ripple,
  99 tests still green.

## Newly settled constraints (candidates to bank)
- **No production-pattern-for-show.** A partition / incremental / SCD / backfill asset is NOT added
  merely to signal scale. On a static, small, heterogeneous source that lacks the pattern's
  dimension, the documented "Limits, by design" why-not is the stronger senior signal (extends the
  #2 principle from framework idioms to architectural patterns). Revisit only if the source gains a
  real time axis or grows past re-pull scale.
- **Docs must not claim a capability the code lacks.** `schedules.py` may not imply
  incremental/streaming; a scheduler on a static source is a full refresh, and the copy says so.
- The 87→88 akabab drift is survey noise — never a displayed number, baseline, or "detected change"
  headline (reaffirms the data-analyst frozen-baseline law).
