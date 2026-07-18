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

## Prep notes: pipeline-reveal (2026-07-17)

Verified in-repo:
- **README defect**: the file is truncated mid-word at its final line — the "Project
  structure" tree ends at `├── WORKSHOP.md   ← self-study g` with NO closing code
  fence (README.md:126-129, 4960 bytes, no trailing newline). GitHub renders an
  unclosed fence to end-of-page. This alone fails a 90-second scan; the reframe must
  fix it, and it argues for rewriting the tail, not just the hero.
- Current hero order: title → CI badge → "self-study workshop" framing (line 7,
  undersells) → three screenshots → architecture → quick start. The site — the single
  most differentiating asset — is buried at line ~105. Live-site link must move above
  the fold.
- Commit history reads well: coherent boundaries, panel-workflow commits
  (`9e9db1c`, `3a82146`) make the agent infrastructure discoverable; PR merges #1-#5
  show iteration. This is already a signal; README need only point at it, not restate it.
- Beat→asset map (brief): 0-3 `characters_enriched`, 4-5 `film_character_counts`,
  6 `starship_stats`, 7 `galaxy_report`. Six insight beats share only three upstream
  assets — so "six mini-DAGs" risks reading repetitive unless check badges differ
  per beat; the differentiator is WHICH check guards WHICH number.
- `.claude/` now holds 9 persistent panel agents + charter + memories. Double-edged
  signal in 2026: visible AI-agent infra can read "AI built this" (discount) or
  "candidate engineers their AI collaboration" (premium). It must be framed as a
  deliberate process artifact with the human as adjudicator, one short README section,
  not the hero.

External (2026 hiring-loop context): trust in raw AI output is falling (29%, down
from 40% in 2024); loops now screen for *judgment over AI output* — spotting what's
wrong, explaining tradeoffs. Recruiters engage far more with runnable/live demos than
prose. Per-beat provenance + severity-differentiated checks is exactly "judgment made
visible" — that's the pitch I'll make. (Sources: dataexpert.io portfolio guide,
dataengineeracademy.com 2026 portfolio checklist, herohunt.ai AI-era recruiting.)

Positions forming (for debate): per-beat specific labels beat generic ("Where
23-of-82 comes from" IS the interview answer); check badges must carry the one-line
rationale or the DAG is decoration; beat 7 callback ("six numbers, six pipelines,
eight checks") is the portfolio close; README hero = one-line value prop + live site
link + lineage-with-green-checks screenshot (blocked on the open screenshot item).

Cannot verify: how the artifact URL renders as a link preview off-platform; whether
screenshots can be retaken (needs desktop UI — still open).
