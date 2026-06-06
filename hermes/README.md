# BoardGame Brain — Hermes Agent export

Generated from the Claude Code plugin in `../bgb/` by `tools/export_hermes.py`.
**Do not edit these files directly** — edit the source skills and re-run the script.

Seven skills in the [agentskills.io](https://agentskills.io) SKILL.md format used by
[Hermes Agent](https://github.com/NousResearch/hermes-agent) (Nous Research). Each
skill folder is self-contained (shared references are embedded per skill).

| Skill | What it does |
|---|---|
| `/bgb-setup` | Point bgb at your rules folder (one subfolder per game) |
| `/bgb-new` | Research a game and build its strategy playbook + insights log |
| `/bgb-help` | Quick strategy briefing before/during a game |
| `/bgb-move` | Live move advice engine (also reachable via natural conversation) |
| `/bgb-rule` | Rules questions grounded in your rulebook PDFs, with page cites |
| `/bgb-insights` | Post-game debrief logged to the game's insights file |
| `/bgb-research` | Deep pass: reconcile theory vs. real plays, hunt exploits, revise |

## Install on the Hermes host

Option A — install all seven through the Hermes installer (one line; keeps
Skills Guard scanning and `hermes skills check`/`update` tracking):

```bash
for s in setup new help move rule insights research; do hermes skills install swittenberger/Boardgamebrain/hermes/skills/bgb-$s; done
```

Option A′ — plain file copy (one line, no CLI; bypasses Skills Guard and
update tracking):

```bash
git clone --depth 1 https://github.com/swittenberger/Boardgamebrain /tmp/bgb && cp -r /tmp/bgb/hermes/skills/* ~/.hermes/skills/ && rm -rf /tmp/bgb
```

Option B — clone and point `external_dirs` at it (gets updates via `git pull`):

```yaml
# ~/.hermes/config.yaml
skills:
  external_dirs:
    - /path/to/clone/hermes/skills
```

Option C — copy the `skills/bgb-*` folders into `~/.hermes/skills/`.

> For `hermes skills tap add <owner>/<repo>` support, publish the contents of
> `hermes/skills/` as the `skills/` directory of a dedicated repo.

## After installing

1. Run `/bgb-setup <path>` once on the Hermes host to set the **rules root** —
   the folder holding one subfolder per game (rulebook PDFs + generated
   `strategy.md` / `insights.md` / `rules-digest.md`). Config is stored at
   `~/.claude/bgb-games/config.json` (shared deliberately, so Claude Code and
   Hermes use the same library on the same machine).
2. The web-research skills (`bgb-new`, `bgb-research`, `bgb-rule`, `bgb-move`)
   want web search/fetch and shell access; grant the corresponding toolsets.
3. Rulebook PDFs: text extraction drops icons and value tables — when building
   rules digests, render suspect pages to images and read them visually
   (see `references/rules-digest-template.md` notes in each skill).
