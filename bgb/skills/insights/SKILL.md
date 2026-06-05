---
description: Capture feedback after playing a board game — runs a structured debrief interview and records it to the game's insights log so future advice improves. Invoke explicitly as /bgb:insights <game name>. Use after a play session, when reflecting on how a game went, or to log results.
disable-model-invocation: true
argument-hint: [board game name]
allowed-tools: Read, Write, Glob, Bash
---

# /bgb:insights — debrief and log how the game went

Game played: **$ARGUMENTS**

Interview the user about the session in real detail, then record it so the
strategy gets sharper over time. These insights are the **highest-value input** to
the system — they're what `/bgb:help`, the live engine, and especially
`/bgb:research` lean on. Make clear they'll be reused next time.

## Paths
- Resolve the **rules root** and the game's folder via
  `${CLAUDE_PLUGIN_ROOT}/references/library.md` (root path in
  `~/.claude/bgb-games/config.json`; if unset, ask once and save, or use `/bgb:setup`).
- Inside the game's folder: strategy `strategy.md` · insights `insights.md`.

## Steps

1. **Load context.** Read the existing `insights.md` (to see prior entries and the
   rollup) and the `strategy.md` (so you can ask about whether the plan held up). If
   neither exists, suggest `/bgb:new <game>` first — but you can still log a session
   into a fresh insights file (in the game's folder) if the user wants.

2. **Interview — dig for detail.** Ask as much as needed to capture a rich picture.
   One focused batch, then follow up on whatever's interesting. Cover at least:
   - Player count and your seat / turn order.
   - The plan you went in with (which vector/strategy).
   - The result: placement, final scores, the margin.
   - What worked and what didn't.
   - Turning points / decisive moments — and *why* they were decisive.
   - Opponent behavior of note (what they did well, neglected, or always do).
   - What you'd do differently next time.
   - Any surprising rules interactions or questions raised.
   Follow up to turn vague answers into specifics ("close game" → final scores;
   "my engine stalled" → which piece, what turn, why).

3. **Record it.** Append a dated session entry at the top of the **Session log** in
   the game's `insights.md`, following `references/insights-template.md`. Then **update
   the synthesized rollup**: add to "Patterns I've observed", "My group's
   tendencies", "Refinements to the base strategy", and tick items in "Confirmed /
   refuted" as the result warrants. Bump the "Games logged" count.

4. **Flag follow-ups.** If the session confirms or contradicts the base strategy in
   a meaningful way — or surfaces a possible exploit — note it and suggest running
   `/bgb:research <game>` to reconcile the playbook with what's now been observed.
