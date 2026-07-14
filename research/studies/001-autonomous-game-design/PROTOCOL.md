# Study 001 Protocol

_Date fixed before game selection: 2026-07-14_

## 1. Design phase

1. Generate at least twelve candidate game mechanisms without ranking during generation.
2. Screen for obvious duplication, excessive rules, weak interaction, trivial symmetry, and implementation burden.
3. Select three prototypes using explicit reasons.
4. Implement all three in a shared framework where practical.
5. Preserve rejected prototypes and test results.

## 2. Automated evaluation

Each implemented prototype will be tested for:

### Termination

- At least 98% of random-vs-random games must terminate within 200 plies, or the rules must contain a justified draw condition.

### Balance

- Under mirrored starting conditions and the strongest available symmetric agent, first-player win rate should fall between 40% and 60%, excluding draws.
- If the game intentionally contains role asymmetry, swapping roles must be part of evaluation.

### Strategic signal

- A stronger search or learning agent should defeat a random legal agent in at least 70% of decisive games.
- A stronger agent should defeat a deliberately shallow agent in at least 60% of decisive games.
- Performance should improve across at least three increasing computation budgets unless the game is already solved at shallow depth.

### Nontriviality

At least three of the following should hold:

- multiple openings remain competitive under the strongest tested agent;
- shallow greedy play is exploitable;
- delayed rewards affect move choice;
- state evaluation benefits from more than material count;
- tactical and positional priorities conflict in observed games;
- no forced win is found from the initial state within the tested search bound.

### Compactness

- Core rules remain at or below 400 words.
- A legal-move function and terminal test can be specified unambiguously.
- Typical completed games should remain within a practical duration target of 8–80 plies.

## 3. Human-dependent qualities

Automated tests cannot establish fun, elegance, teachability, or genuine originality. These will be reported as unresolved unless a later human playtest is requested. Any such contribution is logged in the intervention ledger.

## 4. Failure conditions

The study may conclude negatively if:

- all prototypes fail diagnostic thresholds after reasonable revision;
- agent strength is too weak to distinguish game quality;
- the surviving design is discovered to be effectively identical to an existing game;
- metrics reward pathological or unplayable behavior;
- the project cannot produce an honest claim stronger than “a game was generated.”

## 5. Reproducibility

- Random seeds must be recorded.
- Generated data must include configuration and code version.
- Final claims must link to scripts capable of reproducing key tables.
- Manual exclusions must be documented.
