---
name: bgb-rule
description: Answer a specific rules question about a board game, grounded in the official rulebook. Invoke explicitly as /bgb-rule <game> — <your question>. Prefers your local rulebook PDF, falls back to official web sources, and cites the page or section. Use for "is X legal?", "how does Y resolve?", "does Z trigger at scoring?" — any rules lookup. Tabletop games only.
version: 1.1.1
metadata:
  hermes:
    tags: [board-games, tabletop, strategy]
    category: bgb
---

# /bgb-rule — grounded rules answers

> **Arguments:** the text the user typed after the slash command. If `$ARGUMENTS` below shows literally (not substituted), read the arguments from the user's invocation message instead.

Request: **$ARGUMENTS** — parse into the game and the specific rules question.

Answer the question accurately and cite where the answer comes from. Rules answers
must be **grounded in a source, never invented** — if no source settles it, say so.

## Paths
- **Resolve the rules root and the game's folder first** — see
  `references/library.md` (Glob `**/references/library.md` if
  the variable won't resolve). It reads the root from `~/.claude/bgb-games/config.json`;
  if unset, ask once and save (or point the user to `/bgb-setup`).
- Inside the game's folder: your rulebook PDF(s), the rules digest `rules-digest.md`,
  and the strategy `strategy.md` (for context).
- Digest template: `references/rules-digest-template.md`
  (Glob `**/references/rules-digest-template.md` if the variable won't resolve.)

## Source priority (your PDFs preferred, web fallback)
1. **Rules digest** — if `rules-digest.md` exists in the game's folder and covers the
   question, answer from it and report its page/section refs. Spot-check against the
   PDF if the digest is thin or the question is subtle.
2. **Rulebook PDF** — if there's no digest, or it doesn't cover the question, read the
   PDF(s) in the game's folder, answer, and **cite the page/section**. Offer to build
   or update the digest (below).
3. **Web fallback** — if there's no local PDF, search **official sources first**
   (publisher rulebook PDF, publisher site, official FAQ/errata), then reputable rules
   references (e.g. the BGG rules forum). Cite them, and tell the user that dropping the
   official PDF into the game's folder makes future answers authoritative and offline.

## Answering
- **Paraphrase in your own words** — never reproduce rulebook text verbatim. Give the
  ruling, then the citation (page/section, or source link).
- Check for **errata / official FAQ** that override the printed rulebook; if found, lead
  with the current ruling and note that it supersedes the book.
- If sources conflict or the rule is genuinely ambiguous, say so and give the most likely
  reading plus where to confirm — don't paper over uncertainty.
- Respect the configuration: if the answer differs with/without an expansion or by player
  count, say which case you're answering (default: all expansions, max players).
- Keep it tight and scannable; the user may be mid-game.

## Building / updating the digest
When asked — or when you've had to read the PDF to answer and no digest exists yet —
build `rules-digest.md` in the game's folder from the rulebook, following
`references/rules-digest-template.md`:
- Make it a **paraphrased, navigable summary with page/section refs** — an *index* to
  the rulebook in your own words, **not a copy of it**. Every entry carries a page
  pointer so it can be verified against the book.
- Cover setup, round/turn structure, the action types, scoring & win condition,
  end-game, interaction rules, common edge cases, expansion rules, and known errata/FAQ.
- Record the rulebook file it was built from and the date. This becomes the source the
  engine and future `/bgb-rule` lookups check first.

## No game / no question?
- If the game isn't clear, ask which one. If there's no rulebook and the question is
  niche, web-search official sources and answer with the caveat above.
- This system is for **tabletop / board games only.**
