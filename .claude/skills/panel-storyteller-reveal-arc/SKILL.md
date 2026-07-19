---
name: panel-storyteller-reveal-arc
description: Storyteller technique for layering an opt-in "second arc" (provenance, methodology, making-of reveals) under a primary narrative without leaking payoffs or stalling the spine, and for closing the frame (codas, quoted-testimony audits of external claims). Use when a panel topic adds expandable/aside content to an existing beat sheet or closing copy after the final data surface.
---

# The second arc: opt-in reveals under a primary spine

A provenance/making-of reveal is not decoration and not documentation — it is a second
narrative arc the reader opts into. Judge it as story.

## Rules

1. **Audit for leaks first, at the source.** Read the actual labels the reveal will
   surface (asset names, check names, SQL, captions) — not the summaries. A payoff can
   leak through a check description as easily as through copy. A reveal *inside* the
   payoff beat, below its copy in reading order, may name the payoff freely.

2. **Each reveal must be a micro-story, not a diagram.** Shape: claim → machinery →
   guard ("this number, made by these steps, defended by this check"). A bare chain with
   no rationale is furniture. One line of rationale per guard, maximum.

3. **Labels: specific and in-voice.** Generic labels ("Open the pipeline") waste the
   click; out-of-voice labels break the conceit. Restate the beat's own number in the
   story's register ("Check the paperwork — where 23 of 82 comes from"). Restating the
   beat's own number can never leak — it is already on screen.

4. **Protect the hook and the pause.** No new affordance on the opening beat (the hook
   must stay a single clean chord). On a held/pause beat, the affordance must be the
   quietest in the set — the pause exists to set up the payoff, not to host a detour.

5. **The closing beat gets the callback, not another reveal.** If the finale already
   gestures at the machinery, a tally callback ("you've now opened six pipelines") is an
   earned rhyme. Count only what the reader could actually have opened.

6. **Don't retell the gag in the epilogue.** If a later section has an establishing shot
   of the whole system (e.g. a full lineage strip), per-item mini-reveals there repeat
   the joke past its welcome. One arc, told once, closed once.

7. **Opt-in preserves reader pacing by definition** — but only if opening a reveal never
   moves the stage, advances a beat, or changes what unopened readers see. Corollary
   (adjudicated 2026-07-19): where a browser lacks scroll anchoring, a centered
   disclosure opening moves the reader ~180px at the exact opt-in moment — the PLATFORM
   violates this rule, not a fix for it. The sanctioned repair is anchoring restoration:
   capture the summary's viewport top on activation, scroll by the MEASURED delta on
   toggle, synchronous and instant — so where the browser already anchors the delta is
   0 and the fix no-ops. Measured-delta or nothing; animated or assumed-delta variants
   are scroll-jacking. When ruling on this, hold your conditions AND draw the verdict
   they imply: if you can name the exact shape that would flip you, that shape is your
   proposal — "accept unless someone builds it right" forfeits authorship of the gate.

8. **Blast-radius rule for shared machinery.** When reveals render metadata from a
   shared source (a lineage chain, a check registry, a glossary), a string's blast
   radius is every beat that cites its container — not the beat it was written for.
   Audit procedure: for each beat, list every string its reveal can surface (labels,
   hovers, tooltips), then mark any that state a LATER beat's number, name, or
   punchline. A one-off audit decays — encode it as a standing automated guard so new
   strings are screened at birth.

9. **Fix leaks in the strings, not the renderer.** (Adjudicated 2026-07-18: the
   storyteller's placement-filter proposal lost, correctly.) Separate a string's
   *operational meaning* from its *rendered phrasing*: a label can name the
   invariant's subject without stating its payoff — "all-six set", not "six-film
   trio"; "flight record", not "max flown = 5". Before claiming re-authoring cannot
   work, DRAFT the number-free, name-free label; if the subject can be named without
   the payoff, re-authoring works. Placement filtering fails when its key (a beat
   index on machine-verified metadata) would be hand-authored narrative attribution
   the test surface cannot check — never buy spoiler safety with an unverifiable
   field. Companion rule for check/guard prose: descriptions state the invariant and
   its stakes; run metadata carries the particulars; no check string may quote
   another beat's caption or punchline; rosters and payoff numbers live only in the
   single facts module.

10. **The spoiler pin.** The durable form of rule 8's guard: an offline test that
    DERIVES the payoff term sets — names AND payoff numbers, phrase-anchored — from
    the project's single source-of-truth facts module, and asserts no metadata string
    renders on a beat earlier than its claim's reveal. Two disciplines: the pin must
    be seen to fail (plant a leak, watch it catch, revert) before it counts as a
    guard; and every new metadata string passes the pin before landing. Names-only
    pins are half a pin — a bare payoff count ("19", "5") leaks as loudly as a name.
    When a new payoff ships, extending the pin's term sets is part of the payoff's
    landing, not a follow-up.

11. **Close the frame with a coda, not a summary.** (Adjudicated 2026-07-19.) After
    the last data surface, one short in-voice paragraph plus a re-read affordance
    that loops to the story's top ("Take the census again ↑" → #story). The coda
    states the story's epistemic promise ("nothing here is sealed") — it recaps no
    numbers and repeats no payoffs, because a coda that restates figures is a
    summary, and a summary is a second ending. That number/name/payoff-free property
    is what exempts it from the project's drift detector, so the exemption gets an
    **absence pin**: a test asserting the property (digit-free), never the wording.
    Pinning the wording is theater; the premise is what's load-bearing. Placement:
    inside the main content, after the final grid — the footer stays footer, and the
    frame closes exactly once (resist all future appended closing prose).

12. **Quoted testimony: auditing external claims in copy.** When canon/dialogue
    offers a number the data cannot derive but can corroborate, do not exclude it
    and do not fake it as data — AUDIT it in the story's own register ("filed at
    896 BBY — his own count, nine hundred years, checks out"). Mechanics, all
    mandatory: (a) the quoted figure is never rendered as site-derived data —
    derived numbers come only from the data literal; (b) the line renders
    data-conditionally on the exact facts it audits (name AND value), so if the
    record drifts the line disappears rather than lies; (c) no derived twin of the
    quoted figure exists anywhere (~900 computed from 896 would launder testimony
    into data); (d) the motif is rationed — an audit-the-canon aside is a motif at
    two uses and a tic at three. Prep discipline: when the deliverable is words,
    draft the FINAL copy before debate; verbatim adoption is only possible if the
    exact text is on the table.

13. **Deixis tooltips: tap-to-pin, reader-owned dismissal.** (Shipped 2026-07-19,
    fdd3178.) A hover tooltip that names data marks is deixis, not delivery — the
    spine must survive its absence (prose/captions carry every payoff). But when it
    is the ONLY surface naming most of a story's cast, the conceit is load-bearing
    and no input modality may be cut off from it: suppress-for-touch is the wrong
    fix. Shape: a touch tap (which fires pointermove per spec) shows AND pins;
    touch pointerleave does not hide; dismissal is the reader's own next tap
    (hit-test miss) or their own scroll — never a timer, because a timer is the
    page taking back what the reader asked for. One grammar across story stage and
    dashboards, no forked layer. Companion norms from the same round: an accepted
    limitation enters the log WITH its reopening tripwire (a shrug is not a
    verdict); decisions resting on unreachable hardware label measured facts and
    inferences separately; and exposure changes reach, not content — widening a
    verified string's audience renders the same string verbatim from its one home.
