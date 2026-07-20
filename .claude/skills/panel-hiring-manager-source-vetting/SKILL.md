---
name: panel-hiring-manager-source-vetting
description: Vet a proposed external data source through the hiring-manager lens — license, maintenance reality, provenance honesty, and whether it earns its place by answering a new interview question.
---

# Vetting a new external data source as portfolio signal

Run this checklist BEFORE debating any "add a second source" proposal. A source that
fails it is résumé-padding; a source that passes it becomes an interview answer.

## 1. The new-question test (gate)
Name the interview question the source lets the repo answer that it could not answer
before (e.g., "how do you join a second, dirtier source without fuzzy matching?").
If every question it raises is already answered by the existing pipeline, veto:
signal dilution.

## 2. License and attribution honesty
- Verify the license PRIMARY (fetch the repo, don't trust the brief).
- Name the data's true provenance in docs: official API vs fan-curated vs scraped.
  Implying a fan dataset is canonical is an interview kill.

## 3. Maintenance reality — does "drift" even apply?
- Check commit count / last activity. A static unmaintained file cannot meaningfully
  drift; the real failure mode is the HOST disappearing. Docs and check descriptions
  must match the actual risk, or the guard story reads as cargo-culted.
- Committed fixtures + a blocking shape check are the honest answer to "what if the
  source dies?" — make sure the docs say so in one clause.

## 4. Join governance reads as judgment
- Curated exception/alias maps in the single baselines module beat fuzzy matching for
  a small cast: deterministic, reviewable, testable. Demand one documented sentence
  of why-not-fuzzy — the why is the hire signal.
- Failure-mode separation: a coverage/match baseline (data moved) needs a
  data-independent companion proving the alias map itself still resolves (parser/map
  broke). Cheapest home may be pytest, not a new check — don't inflate check counts.

## 5. Ripple sweep before signing off
Counts move → sweep README numbers, architecture diagram/table, Stack attribution,
WORKSHOP count-free prose, snapshot tooling globs, AND SCREENSHOTS (retake at the new
green-check count). Briefs habitually omit screenshots; catch it in prep.

## 6. Fixture provenance stays labeled
If synthetic fixtures ship before a real snapshot, the fixtures README must say so
until the "freeze reality" commit lands, and that commit's message must name the
transition. Mixed real/synthetic fixtures with no label is a trust defect.
