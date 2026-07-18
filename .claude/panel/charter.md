# Design Panel Charter

The panel is a set of nine persistent role agents (`.claude/agents/panel-*.md`) that debate
significant design, UX, storytelling, pipeline, and portfolio decisions for this project.
Each panelist keeps its own memory file and may author its own skills; the panel therefore
*learns* — settled arguments are never re-fought, and each debate starts smarter than the last.

Main-session Claude orchestrates (subagents cannot spawn subagents) and is the **final
decision maker**.

## Roles and scoping

| Agent | Mandate | Memory file |
|---|---|---|
| panel-lore-fanatic | authenticity; what's earned vs. kitsch | `.claude/panel/memory/lore-fanatic.md` |
| panel-data-engineer | lineage, reproducibility, data honesty, no build-step creep | `.claude/panel/memory/data-engineer.md` |
| panel-data-analyst | which claims the data actually supports; denominators and nulls | `.claude/panel/memory/data-analyst.md` |
| panel-graphic-designer | typography, color budget, one coherent mark system | `.claude/panel/memory/graphic-designer.md` |
| panel-ux-designer | user control, accessibility, mobile, embeds; never gate content | `.claude/panel/memory/ux-designer.md` |
| panel-storyteller | narrative spine, hook, beat sheet, pacing | `.claude/panel/memory/storyteller.md` |
| panel-hiring-manager | the 90-second portfolio scan; what signal each choice sends | `.claude/panel/memory/hiring-manager.md` |
| panel-qa-engineer | tests, asset checks, schema/null validation, failure modes | `.claude/panel/memory/qa-engineer.md` |
| panel-technical-writer | docs as the landing page; explain the why, not just the how | `.claude/panel/memory/technical-writer.md` |

**Scoping rule** (unchanged from the original workflow): pure visual/site decisions are carried
by the first six roles; pipeline, repo, or portfolio-presentation decisions must include the
last three (hiring-manager, qa-engineer, technical-writer). Convene all nine only when the
decision genuinely spans both.

## Protocol: prep → debate → synthesis → bank

1. **Brief.** The orchestrator composes ONE factual brief — current state with `file:line`
   references, constraints, and the concrete decision questions — and gives the *same text*
   to every scoped role.

2. **Prep pass** (the learning phase). Spawn every scoped role in parallel with the brief and
   `MODE: PREP`. Each panelist reviews the brief, reads its own memory end-to-end, inventories
   its own skills, identifies what the question requires that it doesn't have banked, fills the
   gaps (reading repo files named in the brief; external research only for things outside the
   repo), then writes what it learned into its own memory — and, if it learned a reusable
   technique, into a new or updated skill under `.claude/skills/panel-<role>-<topic>/SKILL.md`.
   Each returns a ≤150-word readiness note: what it knew, what it learned, what it still
   cannot verify.

3. **Debate pass.** Spawn every scoped role in parallel again with the brief, `MODE: DEBATE`,
   and the collected one-line readiness notes (so each role knows what the others researched).
   Each returns, in ≤500 opinionated words: a verdict, ONE concrete proposal, its top 3
   must-haves, and its top 3 objections to what the other roles will likely propose.

4. **Synthesis.** The orchestrator adjudicates conflicts explicitly — who won each argument
   and why — and produces ONE synthesized plan, not a menu. It writes the decision log to
   `.claude/panel/decisions/<YYYY-MM-DD>-<topic>.md`: the brief, one-line per-role verdicts,
   the adjudication, the final plan, and any newly settled constraints.

5. **Bank pass.** Spawn each scoped role with `MODE: BANK` and the synthesis. Each panelist
   appends a dated "Banked" section to its own memory in its own voice: which of its arguments
   won or lost and why, new settled constraints it must not relitigate, and what it would prep
   differently next time. Panelists keep their memories compact (~200 lines) by folding
   superseded prep notes into the settled sections.

6. **CLAUDE.md upkeep.** Only genuinely global, code-touching constraints earn a one-line
   addition to the hard-constraints digest in `CLAUDE.md`. Everything else lives in role
   memories and the decision log.

## Write-scope law

During any panel mode, a role agent may write ONLY:
- its own memory file (`.claude/panel/memory/<role>.md`), and
- its own skill directories (`.claude/skills/panel-<role>-*`).

It must never write CLAUDE.md, source code, the site, other roles' files, or the decisions
log. This is what makes nine parallel writers safe. The orchestrator alone writes the
decision log and any code.

## Memory file format

```
# <Role> — Panel Memory
## Settled (do not relitigate)   ← constraints this role enforces, cited to the PR/decision that banked them
## Working knowledge             ← repo facts this role has verified itself
## Prep notes: <topic> (<date>)  ← appended during PREP, compacted after banking
## Banked: <topic> (<date>)      ← appended during BANK
```

Anything under "Settled" is law for that role — it defends it in debate rather than
re-arguing it.
