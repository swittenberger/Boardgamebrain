# Pattern & Exploit Hunting

A standing analytical goal of BoardGame Brain, alongside "what's the best move
now," is to answer: **are there patterns in this game worth exploiting?** Reliable
ways to win, shortcuts to the win condition, and concrete lines that close out a
game from a given position.

This lens is used everywhere, but it's *sharpened* in `/bgb-research`, where the
base strategy is tested against real-play insights and external meta.

---

## What to look for

### 1. Reliable openings / dominant lines
Sequences that are strong across many games regardless of opponents or luck. If a
particular opening or vector wins far more than its share, name it, give the exact
sequence, and note its weaknesses (every dominant line has a counter, even if rare).

### 2. Win-condition shortcuts
The fastest or most reliable route to *trigger* or *reach* the win. Do the
threshold math: "you need ~N points to win; vector A reliably yields ~X per turn,
so it caps out around T turns." Make the numbers explicit so the user can see
whether a plan even reaches the finish line in time.

### 3. Closing lines from a state (the "solver" lens)
Given a board state S with K turns/actions left, work out a concrete sequence that
reaches the win condition — back-propagating from the end. This is the
"from this specific point, here's what to do to win" analysis. State the
assumptions (what opponents must not do) and the failure points.

### 4. Multiplier / combo breakpoints
Combinations that compound rather than add — multiplicative scoring, free-action
chains, engines that feed themselves. Identify the breakpoint where the combo
becomes worth the setup cost, and how many turns it needs to pay off.

### 5. Snowball / runaway-leader setups
Positions that snowball once started. Two outputs: (a) how to *start* the snowball
yourself, and (b) how to *deny* it when an opponent is starting one (the cheapest
intervention that breaks the loop).

### 6. Dominated options and traps
Moves that look attractive but are dominated by another option, and the common
newbie traps in the game. Knowing what *not* to do (and what opponents will
wrongly do) is half the edge.

### 7. Player-count and seat effects
Lines that are strong at 2p but weak at 4p (or vice versa), and first-player /
turn-order advantages. Many "exploits" are really player-count-specific.

---

## How to hunt

1. **From the rules**: look for asymmetries, scoring multipliers, cheap repeatable
   actions, and any threshold that's easier to hit than it first appears.
2. **From external meta**: BGG forums, strategy articles, and ranked/competitive
   discussion often surface known strong lines and their counters. Cite sources.
3. **From the user's insights** (the highest-value source): real results reveal
   what actually works *for this user's group and skill level*. A line that's
   theoretically optimal but loses to the user's specific opponents isn't the
   exploit for them — and one their group never defends against might be.

Synthesize across all three. Theory + meta + lived results beats any one alone.

---

## The honesty caveat

Some exploits are degenerate or unfun: they can flatten the game, draw table-wide
retaliation, or make you the player nobody wants to invite back. **Present them
honestly anyway** — the user asked to know them — but flag the cost:
- Mark a line as "competitive / cutthroat" vs "fine at a friendly table."
- Note when a line invites kingmaking or coordinated blocking against you.
- Note when relying on it depends on opponents not knowing the counter.

The user decides how to use the information. Your job is to find it and label it
accurately, not to moralize or to hide it.

---

## Where exploits live

Record findings in the strategy file's **"Exploits & reliable lines"** section,
each with: the line, the conditions it needs, the expected payoff, the counter, and
the friendly-vs-competitive label. `/bgb-research` revises this section as
insights accumulate and the meta shifts.
