# Board Game Analysis Methodology

This is the shared reasoning engine for all BoardGame Brain skills. It is game-agnostic:
it tells you *how* to think about any board game position. Game-specific facts
live in each game's `strategy.md`; your real-play results live in its `insights.md`
(both under the game's folder in your rules root). This file is the constant.

The goal of analysis is always the same: **convert the current situation into a
ranked, justified recommendation for what to do next, expressed in terms of the
win condition.** Everything below serves that.

## Default configuration: max players, all expansions

Unless told otherwise, assume the **maximum player count** for the game and that
**all expansions are in play**. This is the baseline every playbook is written for
and what research focuses on — strategy at full count with everything included is
the most general case, and the others are deltas from it.

Two rules follow:
- **Player count** — default to max. The user mentions when a session is smaller;
  only then adjust, and note what changes (see each game's player-count notes).
- **Expansions** — if which expansions are in play has **not** been established
  (not stated by the user, not pinned in the game's strategy file), **ask before
  giving strategy advice.** Base vs expanded play can differ enough that advice for
  the wrong configuration misleads. Once known, proceed.

---

## The analysis loop

Work through these steps. Skip lightly over steps that are obvious for the game
at hand, but never skip step 2 (vectors) or step 7 (endgame) — those are where
most mistakes hide.

### 1. Establish the frame
- Which game, how many players, what seat / turn order does the user have.
  (Default to max players unless told fewer; confirm expansions if unknown — see
  Default configuration above.)
- What phase: opening, midgame, or endgame. (If unsure, infer from step 7.)
- What is open information vs hidden. Note what you *cannot* see.
- State the win condition and scoring rule in one sentence. If you don't know it,
  read the game's strategy file; if there isn't one, ask or suggest `/bgb-new`.

### 2. Identify the victory vectors
Enumerate the distinct *paths to points / to the win* and, for each, estimate its
**ceiling** (how much it can produce) and its **reliability** (how dependent it is
on luck, opponents, or specific setups). Most games reward committing to 1–2
vectors and supporting them, not spreading thin.

Also name the game's **archetype**, because it dictates the heuristics:
- **Engine / tableau builder** — early investment compounds; ask "does this engine
  pay back before the game ends?"
- **Race** — first to a threshold wins; tempo and the critical path dominate.
- **Area control / majority** — position and timing of commitment matter; count
  contested regions.
- **Combo / multiplier** — look for things that multiply rather than add.
- **Economic / efficiency** — points-per-action is the master metric.
- **Negotiation / political** — the table is part of the board; deals and threats
  are moves.
Most modern Euros are blends; identify the dominant one or two.

### 3. Read the state
- Your resources, position, and committed plan.
- **Tempo**: how many actions / turns you have left and how many each plan costs.
- **Scarcity**: what is contested or running out (board spaces, a resource, time).
- Each opponent's likely plan and their immediate threats. Who is the leader?
- The clock: how many turns or triggers remain (this feeds step 7).

### 4. Generate candidate lines
List the *realistic* options for the decision at hand — not just the obvious one.
Force at least 2–3 candidates, including the "boring efficient" one and the
"greedy high-ceiling" one. For each, project 1–3 plies ahead: what you do, what
opponents likely do in response, where that leaves you.

### 5. Evaluate each line
Score candidates on these axes (roughly, not with false precision):
- **Value / EV** — expected points or win-probability gained.
- **Tempo / action efficiency** — points (or progress) per action or per turn.
  In efficiency games this is usually the deciding axis.
- **Opportunity cost** — what you give up, *and* what opponents gain, by choosing
  this. A move that scores 5 but hands an opponent 6 is a bad move.
- **Risk / variance** — how spread are the outcomes; what's the floor.
- **Interaction effect** — does it deny, block, or accelerate opponents?

A useful tie-breaker: the **"so what, by the end of the game?" test** — trace the
line to the final scoring and check it actually moves the win condition. Resources
that never convert before the game ends are worth nothing.

### 6. Factor opponents and interaction
- **Threat assessment**: which opponent action would hurt you most, and how likely.
- **Blocking / hate-drafting**: sometimes the best move denies the leader more than
  it builds you — but only when the denial is efficient.
- **Kingmaker / runaway-leader dynamics**: if someone is snowballing, normal
  point-maximization may be wrong; coordinate pressure or deny the snowball.
- **Politics**: in multiplayer, your reputation and the credibility of your threats
  are resources. Don't make enemies for small gains.

### 7. Mind the endgame
This is where good players separate themselves. Always:
- Count remaining turns / actions / triggers explicitly.
- **Back-propagate from the end**: what scores at game-end, and what's the last
  turn you can still set it up? Identify the **last-commit moment** for each vector.
- Avoid **stranded resources** — anything you can't convert before the end.
- Sequence late moves for end-of-game scoring (lock in majorities last, etc.).
- If the game is a race, recompute the critical path every turn.

### 8. Recommend
Deliver a ranked, concrete recommendation (see output format below). Lead with the
single best line and *why*, give 1–2 alternatives with their tradeoffs, and state
the key contingency ("if the opponent takes X, switch to Y"). Be specific enough to
act on this turn — name the actual move, tile, card, or space.

---

## Output format for live advice

Use this shape when giving in-game move advice (adapt length to the situation):

```
Read of the position: <1–2 sentences: phase, who's ahead, what's scarce, the clock>

Recommended: <the move>
  Why: <value + tempo + opportunity cost, tied to the win condition>

Alternative: <option B> — <when this is better and what it trades off>
(Alternative: <option C> if relevant)

Watch for: <the main opponent threat or contingency, and the switch>
```

Keep it tight. The user is mid-game and wants a decision, not an essay. If you're
genuinely uncertain (hidden info, close call), say so and give the line with the
best floor.

---

## Standing principles (apply across all games)

- **Convertibility is everything.** Resources, position, and engines matter only
  insofar as they become win-condition progress before the game ends.
- **Action efficiency.** Prefer the move that advances your win condition most per
  action/turn spent, unless variance or blocking justifies otherwise.
- **Flexibility early, commitment late.** Keep options open while information is
  scarce; commit hard once the path is clear and the clock forces it.
- **Variance follows position.** Behind ⇒ increase variance (take swingy lines).
  Ahead ⇒ reduce variance (take safe, denying lines).
- **Engines need payback time.** An investment that pays back after the game ends
  is a loss. Estimate the payback turn vs turns remaining.
- **Diminishing returns.** Most vectors flatten; the marginal point gets expensive.
  Watch for the moment to switch vectors.
- **Information has value.** Scouting, drawing, and bluffing are real moves;
  paying a little to resolve uncertainty is often worth it.

---

## Handling missing information

If you lack the rules or the current state:
1. Try to load the game's `strategy.md` from its folder under the rules root (see
   the paths note in each skill / `references/library.md`). If found, use it.
2. If not found, suggest the user run `/bgb-new <game>` to build one.
3. Ask **targeted** questions to fill only the gaps that change the recommendation
   — not a generic questionnaire. One focused batch, then advise.

Never invent rules. If you're recalling a game from memory and you're not sure of a
rule, flag the assumption explicitly so the user can correct it.

**Grounding a rule.** When a decision depends on a precise rule, consult a source in
this order rather than trusting memory: the game folder's `rules-digest.md` → the
rulebook PDF in that folder → official web sources (publisher rulebook/FAQ/
errata). Cite where the answer came from, and prefer current errata/FAQ over the
printed book. If nothing settles it, say the rule is unverified. `/bgb-rule` is the
dedicated command for standalone rules questions.

---

## Exploit / pattern lens

On top of "what's the best move now," always keep a second lens open: **are there
exploitable patterns in this game?** Reliable openings, win-condition shortcuts,
snowball setups, dominated options others fall for, and concrete closing lines from
a given state. Details and how to hunt for them are in `pattern-hunting.md`. Fold
any that apply into your advice, with the honest caveat when a line is degenerate
or socially costly at a friendly table.
