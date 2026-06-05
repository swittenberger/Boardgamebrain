---
description: Configure BoardGame Brain — set or change the rules root, the single folder that holds one subfolder per game (your rulebook PDFs plus the generated strategy, insights, and rules digest). Invoke explicitly as /bgb:setup (optionally with a folder path). Run this first, or whenever you move your rules folder.
disable-model-invocation: true
argument-hint: "[path to your rules folder]"
allowed-tools: Read, Write, Glob, Bash
---

# /bgb:setup — point bgb at your rules folder

Requested: **$ARGUMENTS** (a folder path, or empty)

Set or change the **rules root** — the one folder that holds all your games. Under
it, each game is a subfolder containing your rulebook PDF(s) and the files bgb
generates (`strategy.md`, `insights.md`, `rules-digest.md`). The full convention is
in `${CLAUDE_PLUGIN_ROOT}/references/library.md` (Glob `**/references/library.md` if
the variable won't resolve).

Config file: `~/.claude/bgb-games/config.json` → `{ "rulesRoot": "<path>" }`.
Use Bash so `~` expands; on Windows it's `%USERPROFILE%\.claude\bgb-games\config.json`.

## Steps

1. **Show current config.** Read `config.json` if it exists and report the current
   `rulesRoot` and whether that folder still exists on disk. If there's no config
   yet, say bgb isn't configured.

2. **Get the new path.**
   - If `$ARGUMENTS` is a path, use it.
   - Otherwise ask: "Where's your board-game rules folder?" — the folder that holds
     (or will hold) one subfolder per game.

3. **Validate.** Check the path exists (`ls "<path>"` via Bash). If it doesn't,
   tell the user and offer to create it (`mkdir -p "<path>"`) or to re-enter. Don't
   save a path that doesn't exist unless the user confirms creating it.

4. **Save.** Write `~/.claude/bgb-games/config.json` with `{ "rulesRoot": "<path>" }`
   (create `~/.claude/bgb-games/` first if missing). Preserve any other keys already
   in the config. Store an absolute path.

5. **Confirm & list.** Re-read the config to confirm it saved, then list the game
   subfolders under the new root (`ls "<rulesRoot>"`). Report how many games were
   found and name a few. An empty or brand-new root is fine — say that `/bgb:new
   <game>` will create the first game folder. If the root holds loose PDF files but
   no per-game subfolders, mention the expected layout (one subfolder per game, the
   PDF inside it) and offer to reorganize.
