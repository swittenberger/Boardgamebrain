---
name: bgb-help
description: Quick strategy briefing for a board game already in the BoardGame Brain library — pull up the playbook before or during a game. Invoke explicitly as /bgb-help <game name> (or with no argument to list available games).
version: 1.1.1
metadata:
  hermes:
    tags: [board-games, tabletop, strategy]
    category: bgb
---

# /bgb-help — quick strategy briefing

> **Arguments:** the text the user typed after the slash command. If `$ARGUMENTS` below shows literally (not substituted), read the arguments from the user's invocation message instead.

Game requested: **$ARGUMENTS**

Give a fast, structured briefing on this game's strategy, optimized for pre-game
prep or a mid-game memory refresh. This is a **read-only** command — it doesn't
change files.

## Paths
- Resolve the **rules root** via `references/library.md` (root
  path in `~/.claude/bgb-games/config.json`; if unset, ask once and save, or use
  `/bgb-setup`). Games are the subfolders under the root.

## Steps

1. **No argument given?** List the game subfolders under the rules root
   (`ls "<rulesRoot>"`) and ask which one. Stop.

2. **Find the file.** Locate the game's folder and read its `strategy.md`. If it
   doesn't exist, say so and suggest `/bgb-new <game>` to build it. (Offer a quick
   from-memory summary if useful, flagging it's unverified.)

3. **Also read the insights** — the game folder's `insights.md` if present — the
   user's lived results should color the briefing (especially the synthesized rollup
   and their group's tendencies).

4. **Brief, structured:**
   - **TL;DR** — the 3–5 things that matter most.
   - **How you win** — win condition + rough winning score.
   - **Victory vectors** — the main paths, with when to pick each.
   - **Phase priorities** — opening / midgame / endgame in a line each.
   - **Exploits & reliable lines** — the headline ones, with their caveats.
   - **Top mistakes to avoid.**
   - **From your games** — anything notable from the insights rollup.

   The briefing assumes the file's configuration (max players + all expansions). If
   the user signals a different setup — fewer players or only some expansions — flag
   what changes for that case rather than giving the full-config advice unqualified.

   Keep it scannable — the user may be reading this at the table.

5. **If the user also describes a live situation** ("I'm at X, what now?"), switch
   into move advice using the BoardGame Brain engine's methodology
   (`references/methodology.md`) and give a ranked
   recommendation rather than just the generic briefing.
