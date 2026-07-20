# Decision: the watchlist round — badge whys, the Safari jump, the touch pin, stage type

Date: 2026-07-19 · Scope: visual/site (first six roles) · Orchestrator: Claude

## Brief (summary)

The four standing ux watchlist items, each brought evidence gathered headless the same
day: (E1) 48 `.prov-check` badges carry 113–213-char verbatim check descriptions in the
file's only `title=` attribute — mouse-hover-only, zero focusable, zero aria; (E2)
opening a reveal is a 0px non-event in Chromium (scroll anchoring absorbs ≈−180px) but
Safari has no scroll anchoring; (E3) the stage tooltip shows on pointermove and hides on
pointerleave — a real touch tap fires exactly that sequence (flash), though emulation
cannot reproduce it; (E4) stage SVG type renders at ~5.1–5.9px effective on 360–390px
phones (viewBox 700 → scale .45–.49). PREP corrected the brief twice: the whys are NOT
number-free (known_facts-interpolated, spoiler-safe — the pin audits label+why), and two
Q4 facts emerged that reshape everything: `.axis-t`/`.anno-t` are shared with the
measured-px dashboards, and beat 5's witness names sit 20 viewBox-units apart, capping
any font raise at ~8px effective — below the legibility target.

## Per-role verdicts (one line each)

- lore-fanatic: expose whys verbatim via the shared tooltip (fallback: accept); legend line 911 must stay true — visible disclosure falsifies it; VETO on suppress-for-touch (the stage tooltip is most of the 82 names' only surface); Q4 accept — "a raise that can't reach legibility is churn wearing honesty's clothes."
- data-engineer: expose whys contract-first through the shared tooltip; Q2 accept — unhardwarable scroll code with no offline guard; Q3 tap-to-pin in the shared layer only; Q4 accept; verbatim one-home law on whys.
- data-analyst: Q1 accept (rationale, not gated data); Q2 evidence gate — no ship until the proxy measures both anchoring states; Q3 tap-to-pin > accept > suppress; Q4 accept on redundancy alone (channel-redundancy audit: zero load-bearing orphans at 5px) — don't make tap-to-pin load-bearing for it.
- graphic-designer: Q1 accept (every exposure shape breaks a law; the legend is the honest contract); Q2 ship (synchronous scrollBy cannot read as motion); Q3 tap-to-pin is an analog of the dashboard focus-pin, not a fork; Q4 accept (below-target raise is unfundable).
- ux-designer: Q1 accept with a reopening trigger; Q2 ship with dual-branch proxy verification as a merge gate; Q3 suppress-for-touch (a glitch is worse than a clean absence); Q4 accept — own killer fact stands.
- storyteller: build ONLY tap-to-pin (settles Q3 and redeems Q4's acceptance); Q1 accept (48 tab stops crossing the held pause); Q2 accept-and-watch unless proven in both anchoring states; Q4 accept with the narrative warrant written down.

## Adjudication

**Q1 — accept and document, 4–2.** The visible label + ◆/◇ severity is the complete
claim; the whys are operational rationale whose canonical non-hover home the settled
legend line already names honestly. The exposure camp's spoiler-safety case was sound
(the pin audits label+why; verbatim exposure adds no surface) but the cost argument
carried: 48 new tab stops — roughly 15 crossing the held pause — would make the page's
quietest voice its loudest keyboard path, and ux scoped the parity law correctly
(dashboard focus-parity covers data marks; badges are whisper-tier chips whose visible
text is self-sufficient). Hover `title=` stays as a desktop bonus. **Reopening
tripwire:** any why gaining load-bearing content with no non-hover home, or the legend
line ceasing to be true.

**Q2 — ship the delta compensation; the evidence gate passed on every branch.** The
analyst's gate (measure, don't infer) was satisfied by the orchestrator's
`overflow-anchor:none` proxy before adjudication — MEASURED: anchoring on, no fix:
summary shift 0px (beats 1/4/6); anchoring off, no fix: −181/−179/−179px (the Safari
condition, reproduced); anchoring off, with fix: 0px; anchoring on, with fix: 0px (no
double-compensation — the storyteller's risk, disproven). The shape is self-correcting
by construction: capture the summary's viewport top on summary click, scroll by the
measured delta on toggle — where the browser already anchors, the measured delta is 0
and the fix no-ops; nothing is assumed about the engine. Synchronous, `behavior:
"instant"`, fires only in response to the reader's own activation — anchoring
restoration, not scroll-jacking; reveal-arc law ("opening a reveal never moves the
reader") is today violated ON Safari, not by the fix. The engineer's no-offline-guard
objection is resolved by the render-only precedent (banked 2026-07-19: behavior with no
data surface is verified by recorded evidence + review, never a fakeable mechanical
pin): the four proxy measurements above are the recorded evidence, re-run on the landed
code before merge. INFERRED, NOT MEASURED: real Safari/iOS behavior — hardware
unavailable; the proxy (Chromium with scroll anchoring disabled) is the honest stand-in.

**Q3 — tap-to-pin, 5–1, in the shared tooltip layer.** Suppress-for-touch was vetoed
from two lanes (lore: the stage tooltip is the only surface where most of the 82 names
appear — the census conceit; engineer: dashboard tables are a different grain — access
theater). The dashboards already pin-at-center on touch via their focus handlers; only
the stage's svg-level pointermove/pointerleave pair needs the pointerType branch. Shape:
a touch pointermove (fired by a real tap per the pointerevents spec) shows and PINS the
tooltip; pointerleave with pointerType touch does not hide; dismissal is the reader's
own next tap (a hit-test miss already calls tipHide) or their own scroll (explicit
tipHide — ux's stale-state must-have), never a timer. One grammar, no fork. INFERRED,
NOT MEASURED: the real-hardware flash itself (emulation fires no pointermove on tap);
the handler logic is verified by dispatching the spec sequence synthetically.

**Q4 — accept and document, unanimous (lore flipped in debate).** The warrant is
redundancy, not resignation: the analyst's channel audit found zero load-bearing orphans
at 5px — every stage claim has a readable twin in `.stage-cap` HTML or 16px beat copy;
the residue is derivable or computed texture. The css-only raise is IMPOSSIBLE below
target: beat 5's witness names stack 20 viewBox-units apart, capping any bump at ~8px
effective @360 — and those names are the story's climax (stagger-never-shrink makes that
a geometry rework, not a media query). The shared-selector trap (`.axis-t` feeds the
measured-px dashboards) and the guard scanner's @media blindness stand as recorded
hazards for any future mover. The Q3 pinned tooltip becomes mobile's real-pixel
dot-identity channel — a bonus, NOT the justification (analyst's condition). **Reopening
tripwires:** any future anno carrying content not present in copy/caption; any viewBox
rework proposal arrives with the 8-state anchor-geometry re-verification costed.

## Final plan (one commit + verification)

1. site/index.html: (a) Q2 — summary-click capture + toggle delta `scrollBy` (instant)
   on `details.prov` and `details.sql`; (b) Q3 — pointerType-aware stage tooltip
   pin with scroll/tap dismissal, explicit tipHide.
2. Verification recorded in the commit: proxy states A–D re-run on landed code (expect
   0 / −180 / 0 / 0); synthetic touch-sequence check (pin holds through pointerleave,
   scroll dismisses, mouse behavior regression-free); full pytest; 360/390 overflow
   spot-check.
3. Decision log (this file) carries the Q1/Q4 acceptances with tripwires; ux-designer's
   watchlist closes all four items at BANK.
4. Artifact republished to the standing URL; BANK pass for six roles.

## Newly settled constraints (banked)

- **Measured-vs-inferred labeling:** any decision resting on unreachable hardware
  states its measured facts and its inferences separately, verbatim, in the log.
- **Anchoring restoration is not scroll-jacking:** a synchronous, activation-triggered,
  measured-delta scroll correction that no-ops where the browser anchors is the
  sanctioned shape for disclosure-growth compensation; animated or assumed-delta
  variants remain banned.
- **Acceptance is a decision with a tripwire:** an accepted limitation enters the log
  with its reopening trigger written down; a shrug is not a verdict.
- **The census conceit is load-bearing:** the stage tooltip is the only surface naming
  most of the 82 individuals; no input modality may be cut off from it.
- **Exposure changes reach, not content:** any widening of a verified string's audience
  renders the same string verbatim from its one home; if it doesn't fit the vessel,
  change the vessel.
