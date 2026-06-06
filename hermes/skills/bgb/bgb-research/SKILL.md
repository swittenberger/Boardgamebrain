---
name: bgb-research
description: Deep strategy review for a board game — compares the base strategy against the user's accumulated real-play insights, refreshes external meta, hunts for exploitable patterns and reliable win lines, and updates the playbook. Invoke explicitly as /bgb-research <game name>. Use to improve or revise a game's strategy after some plays.
version: 1.1.1
metadata:
  hermes:
    tags: [board-games, tabletop, strategy]
    category: bgb
---

# /bgb-research — reconcile theory with reality, and hunt exploits

> **Arguments:** the text the user typed after the slash command. If `$ARGUMENTS` below shows literally (not substituted), read the arguments from the user's invocation message instead.

Game: **$ARGUMENTS**

The deep pass. Take the base strategy and the user's lived insights, find where they
agree and disagree, refresh the external meta, hunt hard for exploitable patterns,
discuss it with the user, and then revise the playbook.

## Paths
- Resolve the **rules root** and the game's folder via
  `references/library.md` (root path in
  `~/.claude/bgb-games/config.json`; if unset, ask once and save, or use `/bgb-setup`).
  Inside the game's folder: strategy `strategy.md` · insights `insights.md`.
- References: `references/` (methodology + pattern-hunting).

## Steps

1. **Load both files.** Read the game folder's `strategy.md` (base strategy) and
   `insights.md` (real-play results + rollup). If either is missing, say so — `/bgb-new` for the
   strategy, `/bgb-insights` to log plays. Research is most valuable with both.
   **Focus the whole pass on the default configuration — maximum player count with
   all expansions.** Reconcile and hunt exploits for that case first; keep smaller
   counts and reduced-expansion setups as secondary notes.

2. **Refresh the meta (optional but default-on).** Web-search for current consensus,
   newer strategy articles, expansion effects, or shifts since the file was written.
   Cite new sources.

3. **Compare & reconcile — make the deltas explicit.** Go section by section:
   - Where do the user's insights **confirm** the base strategy? (lock those in)
   - Where do they **contradict** it? (the base theory may be wrong *for this group*,
     or the user found something — decide which, and say why)
   - Where do they **extend** it with things theory didn't cover?
   Present this as a clear list of proposed changes, not a vague discussion.

4. **Hunt exploits hard** (`references/pattern-hunting.md`). This is the pass where
   you actively look for: dominant/reliable lines, win-condition shortcuts with the
   threshold math, concrete closing lines from common board states ("from position X
   with K turns left, do this to win"), multiplier breakpoints, and snowball setups —
   grounded in **both** the meta and the user's actual results and group tendencies.
   Label each friendly-vs-competitive and give its counter.

5. **Discuss, then update.** Walk the user through the reconciliation and the exploit
   findings. On their confirmation, revise the game's `strategy.md`: update the TL;DR and affected
   sections, expand "Exploits & reliable lines", refresh "Last updated", and add a
   dated **Changelog** entry summarizing what changed and why (cite insights/sources).
   Keep the file decision-oriented and tight.

6. **Close the loop.** Note any remaining "Open questions to test" for the next few
   plays, so the strategy ⇄ insights ⇄ research cycle keeps tightening.
