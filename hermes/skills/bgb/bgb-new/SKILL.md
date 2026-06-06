---
name: bgb-new
description: Start a new board game in the BoardGame Brain library. Researches the game and generates a reusable strategy playbook plus an empty insights log. Invoke explicitly as /bgb-new <game name>. Board/tabletop games only.
version: 1.1.1
metadata:
  hermes:
    tags: [board-games, tabletop, strategy]
    category: bgb
---

# /bgb-new — build a strategy file for a new game

> **Arguments:** the text the user typed after the slash command. If `$ARGUMENTS` below shows literally (not substituted), read the arguments from the user's invocation message instead.

Game requested: **$ARGUMENTS**

Create a researched, reusable strategy playbook for this board game and seed its
insights log, so `/bgb-help`, `/bgb-research`, and the live engine can all use
it later.

## Paths
- References: `references/` (Glob `**/references/*.md` if `~` won't resolve).
- Resolve the **rules root** and create the game's folder under it — see
  `references/library.md`. The root path is in
  `~/.claude/bgb-games/config.json`; if it isn't configured yet, ask the user once and
  save it (or have them run `/bgb-setup`) before writing any game files.
- This game's files go in its own subfolder: `<rulesRoot>/<Game>/` holding
  `strategy.md`, `insights.md`, `rules-digest.md`, and your rulebook PDF(s).

## Steps

1. **Confirm the game & guard scope.** Disambiguate if the name is ambiguous
   (edition/expansion). **This system is for tabletop/board games only** — if
   `$ARGUMENTS` is a video/PC game, say so and stop, but offer the board-game version
   if a notable one exists (e.g. a video game with a tabletop adaptation). If a
   a folder for this game already exists under the rules root (with a `strategy.md`),
   tell the user and ask whether to refresh it (consider `/bgb-research`) rather than
   overwrite.

2. **Research (ON by default).** Build for the **default configuration: maximum
   player count + all expansions**, unless the user specifies otherwise. Research
   the full expanded game at full count; treat smaller counts and fewer-expansion
   setups as secondary notes, not the main focus. Web-search and fetch:
   - A correct summary of the **rules / win condition / scoring** (so advice is grounded).
   - The **full expansion list** for the game, and how the expansions change strategy.
   - **Current strategy & meta**: BGG forums, strategy articles, ranked/competitive
     discussion. Look for known strong lines, common mistakes, and player-count effects.
   Prefer primary/reputable sources; cite everything in the file's Sources section.
   If web access is unavailable, fall back to your own knowledge, **explicitly flag
   any uncertain rules**, and ask the user to confirm or paste the rules.

3. **Read the methodology.** Load `references/methodology.md` and
   `references/pattern-hunting.md` and apply both — especially: enumerate victory
   vectors with ceiling/reliability, identify the game archetype, and hunt for
   exploitable patterns (reliable openings, win-condition shortcuts, multiplier
   breakpoints, snowball setups).

4. **Write the strategy file.** Follow `references/strategy-template.md` exactly.
   Fill every section with real, researched content — not placeholders. **State the
   assumed configuration in the metadata** ("Configured for: max players + all
   expansions" and the expansion list). Be decision-oriented (a playbook, not an
   encyclopedia). Put initial exploit hypotheses in "Exploits & reliable lines" with
   friendly-vs-competitive labels, and seed "Open questions to test" with things to
   validate in real play. Save to `<rulesRoot>/<Game>/strategy.md` (create the game's
   folder if needed). Set "Last updated" and add the first Changelog entry.

5. **Seed the insights log.** Create `insights.md` in the game's folder from
   `references/insights-template.md` (empty session log) so `/bgb-insights` has a
   home. Ask the user their usual group size and skill level to fill the header.

6. **Rules digest (if a rulebook is available).** Check the game's folder for
   rulebook PDF(s). If present, build `rules-digest.md` there following
   `references/rules-digest-template.md` — a **paraphrased, page-referenced index, not
   a copy** of the rulebook. If no PDF is present, tell the user they can drop the
   official rulebook into the game's folder and run `/bgb-rule <game>` to build it;
   proceed for now with the web-grounded rules from your research.

7. **Brief the user.** Summarize the strategy in a few lines: win condition, the 2–3
   strongest vectors, the headline exploit/reliable line, and the top mistake to
   avoid. Make clear this is a *starting* playbook grounded in theory + meta — it
   gets sharper after real plays via `/bgb-insights` and `/bgb-research`.
