---
name: panel-hiring-manager-idiom-vs-discipline
description: Decide whether to adopt a framework-native idiom over hand-rolled code in a portfolio repo, when the migration would delete a tested safety invariant. Guards against trading a rare senior signal for a table-stakes one.
---

# Idiom vs. discipline: when NOT to migrate to the framework-native way

Use this when a panelist flags hand-rolled code as "should use the framework's
idiomatic resource/abstraction" and the migration touches a tested invariant.

## The core question (decisive)
Which reads as MORE senior in an interview loop:
- **"Used `<FrameworkResource>`"** — table stakes; usually invisible in a 90-second
  scan; proves familiarity only.
- **"Hand-managed `<X>` with a tested safety contract because `<constraint>`"** — a
  rare signal that proves the author understands the underlying system (locking,
  concurrency, lifecycle), not just the framework's happy path.

If the hand-rolled code encodes a *tested* invariant the idiom **cannot express**,
migrating is usually NET-NEGATIVE for the portfolio: you delete the stronger signal to
gain the weaker one.

## Step 0 — Classify the why-not: PROTECTS vs EXCUSES (decides how strong it is)
Two why-nots look identical in prose but differ in signal strength:
- **Protecting** why-not: declines an idiom to preserve a capability the repo ALREADY
  demonstrates and tests (e.g. hand-rolled `read_only` contract). Strong — the repo
  proves capability; the why-not adds judgment on top.
- **Excusing** why-not: documents the absence of a pattern that appears NOWHERE in the
  repo (e.g. "no partitions / no SCD" when no partitioned or incremental asset exists).
  Weak — to a reviewer probing "can you actually build this?", it reads as "talks about
  it, hasn't shown it." Naming the mechanism and its forcing-trigger is honest but is not
  proof of capability.
For a PROTECTING why-not, the documented-limit almost always beats adopting machinery
(the #2 result). For an EXCUSING why-not, weigh ONE non-contrived, guarded demonstration
against the prose: if a real key exists to demonstrate over WITHOUT faking data (e.g. a
static partition over an existing categorical key, not a faked time key), the
demonstration + honest "still absent for X because Y" copy can out-signal the excuse.
Reject the demonstration if it requires faking the data's shape (time partitions on a
static snapshot, an SCD history table that can never change) — that is the cargo-cult the
honesty signal exists to guard against; keep the excuse and sharpen the copy instead.

## Step 1 — Verify the idiom's real capability (PRIMARY, non-negotiable)
Read the framework source, not the brief or the docs summary. Ask: can the native
abstraction express the exact invariant the hand-rolled code encodes and tests?
Example finding that flipped a verdict: `dagster_duckdb.DuckDBResource.get_connection()`
hardcodes `read_only=False` and accepts no per-connection args — so it structurally
cannot carry a per-connection reader/writer safety contract. A "just for path/config"
compromise dies on the same fact (calling `get_connection()` still loses the invariant).

## Step 2 — Name the ding for what it is
A "didn't use the idiom" flag is almost always an INTERVIEW LANDMINE (reviewer may think
the author didn't know the idiom exists), not a scan-level first-impression defect. Treat
it accordingly: the fix is making the CHOICE VISIBLE, not capitulating.

## Step 3 — Prefer the documented why-not to migration, and GUARD it
The real gap is that the repo doesn't yet ANSWER "why not `<idiom>`?" The senior move:
one honest sentence in the tooling why-not home (e.g. WORKSHOP "Limits/why-not" section)
plus a code comment, stating the concrete reason (the invariant the idiom can't express).
This converts the ding into a hire signal — knows the idiom AND has a reason. Same shape
as a "Limits, by design" bullet: a stated ceiling with a trigger, never an apology.

A deliberate non-adoption is a GUARDABLE artifact, not just prose (shipped in the
dagster-duckdb panel). Pin a stable rationale MARKER in the source test beside the
invariant it protects — assert the idiom name AND the disqualifying mechanism string
(e.g. `"DuckDBResource"` + `"read_only=False"`) are present in the code comment — so a
future "modernize" refactor trips both the safety pin and the marker and must re-read the
decision. Prose alone rots silently; a marker forces the next author back through the why.

## Step 4 — Count the collateral
Migration cost includes: rewriting banked tests, falsifying teaching/tutorial assets
(themselves portfolio signal — raw calls are often BETTER from-zero pedagogy than
framework magic), and reshaping asset graphs that other guards/site-lineage pin. Tally
these against the (usually small) idiom credit before signing off.

## When migration IS worth it
Flip to YES only if: the idiom expresses the invariant at least as well, OR no tested
invariant exists to lose, AND the hand-rolled code is genuinely non-idiomatic in a way a
reviewer would read as a mistake rather than a choice. Absent that, documented why-not wins.
