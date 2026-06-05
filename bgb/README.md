# BoardGame Brain (`/bgb`) — a board game analysis plugin for Claude Code

A Claude Code plugin that turns Claude into a board-game strategist: live move
advice, a growing per-game playbook library, rules answers grounded in your
rulebooks, a post-game debrief loop, and a deep research pass that hunts for
exploitable patterns and reliable win lines.

You point bgb at **one folder** — your rules root — and it keeps one subfolder per
game inside it. Each game's folder holds your rulebook PDF(s) and the files bgb
generates (strategy, insights, rules digest). Set or change the root with
`/bgb:setup`.

For **tabletop / board games** (not video games). The plugin's identifier is `bgb`,
which is why every command is namespaced under `/bgb:`.

## Commands

| Command | What it does |
|---|---|
| `/bgb:setup [path]` | Point bgb at your **rules root** (the folder holding one subfolder per game). Run it first, or whenever you move that folder. |
| `/bgb:move <position>` | The analysis engine. Also **auto-activates** when you describe a position in plain language. Gives ranked, justified move advice. |
| `/bgb:new <game>` | Researches a game (on by default) and writes a reusable strategy playbook + seeds an insights log. |
| `/bgb:help <game>` | Fast briefing on a game you've already added — read-only, good at the table. |
| `/bgb:insights <game>` | Interviews you after a session and logs the results so future advice improves. |
| `/bgb:research <game>` | Reconciles the base strategy with your real-play insights, refreshes the meta, hunts exploits, and updates the playbook. |
| `/bgb:rule <game> — <question>` | Answers a specific rules question, grounded in the rulebook PDF in the game's folder (web fallback), citing the page/section. Builds a rules digest. |

The shared engine — the analysis methodology, exploit-hunting playbook, and templates
— lives in `references/` and is used by all the skills.

### The loop

```
/bgb:setup →  point bgb at your rules root (once)
   ↓
/bgb:new   →  builds  <Game>/strategy.md  +  <Game>/insights.md  (empty log)
   ↓
 play; ask /bgb:move (or just describe the position); /bgb:help to refresh; /bgb:rule for rules
   ↓
/bgb:insights  →  appends your results to <Game>/insights.md
   ↓
/bgb:research  →  compares strategy vs insights, hunts exploits, updates <Game>/strategy.md
   ↑______________________ repeat; the playbook keeps sharpening ___________________|
```

Each game is one subfolder under your rules root (`<rulesRoot>/<Game>/`), holding:
- `strategy.md` — the **strategy** (theory + meta + exploits).
- `insights.md` — your **real-play feedback** (the highest-value input).
- `rules-digest.md` — a **rules digest** built from the rulebook (page-referenced), if you've added one.
- your **official rulebook PDF(s)** — drop them in the folder; `/bgb:rule` grounds answers in them.

## Install

### Recommended (permanent, no marketplace)

Drop the `bgb/` folder into your personal skills directory. A plugin placed there
auto-loads as `bgb@skills-dir` on the next session — no install step.

```bash
cp -r bgb ~/.claude/skills/        # → ~/.claude/skills/bgb/
```

Restart Claude Code, type `/`, and you should see `/bgb:setup`, `/bgb:new`,
`/bgb:help`, `/bgb:insights`, `/bgb:research`, `/bgb:rule`, and `/bgb:move`.
(Requires a recent Claude Code with `/plugin` support; if `/plugin` is missing,
update Claude Code.) Run `/bgb:setup` once to point bgb at your rules folder — bgb
also asks for it automatically the first time a command needs it.

### For testing / iterating

Load the plugin for a single session without copying it anywhere (also accepts a
`.zip`):

```bash
claude --plugin-dir ./bgb
# or:  claude --plugin-dir ./bgb.zip
```

Run `/reload-plugins` to pick up edits without restarting.

### Paths
- **Plugin:** `~/.claude/skills/bgb/` (skills resolve bundled files via `${CLAUDE_PLUGIN_ROOT}`).
- **Rules root (your data):** a folder *you* choose, set via `/bgb:setup`. Each game
  is one subfolder under it (`<rulesRoot>/<Game>/`) holding your rulebook PDF(s) plus
  the generated `strategy.md`, `insights.md`, and `rules-digest.md`. Kept entirely
  outside the plugin, so updates never touch your data — and you can point it at a
  synced/versioned folder (Dropbox, a git repo, etc.).
- **Config:** `~/.claude/bgb-games/config.json` — the one small file bgb keeps under
  `~/.claude/`, storing `{ "rulesRoot": "<your folder>" }`. `/bgb:setup` writes it.

## Try it

```
/bgb:setup D:\Games\BoardGameRules   # point bgb at your rules folder (once)
/bgb:new Messina 1347        # research + build the playbook
/bgb:help Messina 1347       # quick briefing before you play
# … play a game …
/bgb:insights Messina 1347   # debrief; logs how it went
/bgb:research Messina 1347   # reconcile + hunt exploits + update the playbook
/bgb:rule Messina 1347 — does the plague spread before or after scoring?
```

Add a rulebook: drop the official PDF into that game's folder
(`<rulesRoot>/Messina 1347/`), then `/bgb:rule` answers from it (citing pages) and
builds a `rules-digest.md` alongside it.

Mid-game, just ask — `/bgb:move` auto-fires:
> "I'm 3rd, two rounds left, I have 4 cubes and the plague track is filling. Push points or block the leader?"

## Structure

```
bgb/
├── .claude-plugin/
│   └── plugin.json            # manifest (name "bgb" → /bgb:* namespace)
├── skills/
│   ├── setup/SKILL.md         # configure the rules root (/bgb:setup)
│   ├── move/SKILL.md          # analysis engine (auto-fires + /bgb:move)
│   ├── new/SKILL.md
│   ├── help/SKILL.md
│   ├── insights/SKILL.md
│   ├── research/SKILL.md
│   └── rule/SKILL.md          # grounded rules answers (/bgb:rule)
├── references/                # shared engine (read via ${CLAUDE_PLUGIN_ROOT})
│   ├── methodology.md
│   ├── pattern-hunting.md
│   ├── library.md             # rules-root config + per-game folder convention
│   ├── strategy-template.md
│   ├── insights-template.md
│   └── rules-digest-template.md
└── README.md
```

## Notes

- **Board games only.** `/bgb:new` stops on a video/PC game (and offers a tabletop
  adaptation if one exists).
- **Name vs command.** The plugin identifier is `bgb` (Claude Code derives the `/bgb:`
  namespace from it, and it can't contain spaces). "BoardGame Brain" is the
  human-readable title.
- **Sharing it.** To distribute to others, publish via a Claude Code plugin
  marketplace — the structure here is already marketplace-ready.
- **Tuning.** The skill-creator workflow can run test games against these skills and
  iterate on triggering/output quality later if you want.
