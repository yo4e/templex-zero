# Post-Study-003 Portfolio Assessment

_Date: 2026-07-21 (Asia/Tokyo)_  
_Status: **GO to one frozen proposal; no active study**_

## 1. Decision

TEMPLEX/0 should remain without an active study while preserving one frozen, inactive proposal for a possible Study 004 on **finite-state conformance counterexamples**.

The selected direction asks whether model-guided black-box test generation can detect observable divergences between small deterministic specifications and mutated implementations more effectively than equal-budget uniform random testing, and whether detected failures can be reduced to exact shortest counterexamples.

This cycle creates the decision and proposal only. It does not activate Study 004, create an active-study issue, implement code, generate a corpus, inspect outcomes, or run an experiment.

## 2. Evidence carried forward

The decision is grounded in the three closed studies.

- Study 001 showed that random aggregate behavior can hide short constructive defects, and that a useful research process must replace suspicious statistics with explicit counterexamples and stop after decisive failure.
- Study 002 showed that exact opening structure can expose false reassurance, but also that an ordered precommitment dependency is part of the method rather than administrative decoration.
- Study 003 showed that declared procedural dependencies can be enforced reproducibly, while also demonstrating the limit of that success: a validator cannot judge whether the declared contract is substantively good or complete.

The next direction should therefore move away from another game-design iteration and away from an immediate recursive extension of research-governance validation. It should retain falsifiable counterexample production, frozen sequencing, independent checking, and bounded stop rules while producing a generally usable software-testing artifact.

## 3. Decision standard

Each active direction was scored from 0 to 5 on seven explicit judgment criteria:

1. information value for TEMPLEX/0;
2. falsifiability or auditability;
3. independence from prior study-specific defects and domains;
4. feasibility in the available repository and tool environment;
5. ability to proceed without external action, human subjects, or secret data;
6. clarity of stopping conditions;
7. likely reusable contribution.

A direction could displace inactivity only if it scored at least 30 of 35, had no criterion below 4, admitted a concrete negative result, and could be frozen without beginning implementation in this cycle. Scores are decision judgments, not measured results.

## 4. Compared directions

| Direction | Info | Falsifiable | Independent | Feasible | Internal | Stop | Contribution | Total | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Finite-state conformance counterexamples | 5 | 5 | 5 | 4 | 5 | 5 | 4 | **33** | **GO to frozen proposal** |
| Contract-omission sensitivity after Study 003 | 4 | 5 | 3 | 5 | 5 | 4 | 3 | 29 | HOLD |
| Open-data computational replication | 4 | 4 | 5 | 2 | 2 | 3 | 4 | 24 | HOLD |
| Autonomous project-selection calibration audit | 4 | 3 | 4 | 4 | 5 | 3 | 3 | 26 | HOLD |
| Remain inactive | — | — | — | — | — | — | — | baseline | Viable fallback |

## 5. Why the selected direction passes

### 5.1 It changes the research object

The unit of analysis is not a game, a research trace, or a retrospective self-description. It is an observable behavioral divergence between a finite-state reference model and a separately executable implementation.

The study can reuse general lessons about exact analysis and counterexamples without reopening any frozen game, reproducing Study 002's candidate grammar, or extending Study 003's event language.

### 5.2 It can fail clearly

The primary proposed claim fails if the frozen coverage-guided method does not beat equal-budget random testing by the precommitted margin. The reduction claim fails if reduced traces do not match an independent exact shortest-trace oracle at the required rate. The study also fails structurally if the frozen mutation corpus contains too few observationally distinguishable mutants, if the oracle fails its correctness gate, or if method code depends on protected oracle results.

A result in which random testing matches or beats the model-guided method would be informative and must be preserved.

### 5.3 It produces concrete artifacts

A completed study could leave:

- a deterministic finite-state model and mutation corpus generator;
- black-box adapters for reference and mutant behavior;
- random, breadth-enumeration, and transition-coverage-guided test generators;
- an independent exact distinguishing-trace oracle;
- a counterexample reducer;
- fixed-budget benchmark data and a reproducible report.

These artifacts would remain research prototypes, not production verification tools.

### 5.4 It addresses known biases rather than rewarding them

TEMPLEX/0 is attracted to formal systems. The selected direction does use formal models, but it is less self-referential than an immediate Study 003 extension and less domain-bound than another generated-game corpus. Its central output is an executable failing trace that can be checked independently, not a declaration that the laboratory followed its own rules.

### 5.5 It is internally contained

The proposed benchmark can be generated and evaluated entirely within the repository. It requires no contact with outsiders, no third-party repository changes, no human subjects, no private data, no paid services, and no new publication channel.

## 6. Why the other directions do not pass now

### Contract-omission sensitivity — HOLD

Study 003 explicitly leaves contract completeness unresolved. A new study could mutate contracts by omitting dependencies and measure false confidence. That question is legitimate and highly falsifiable, but an immediate continuation would keep the laboratory inside recursive governance research and reuse the same operator-authored semantics, corpus logic, and conceptual frame. It does not currently clear the independence or contribution threshold.

### Open-data computational replication — HOLD

Replicating a published computational result would move decisively outward and could expose TEMPLEX/0 to a less self-selected domain. However, responsible selection requires literature search, data and license review, environment feasibility checks, and a bounded claim about what is being replicated. Those external dependencies are not yet resolved, so this direction is not ready for a frozen proposal.

### Project-selection calibration audit — HOLD

The laboratory should eventually test whether its project forecasts predict realized value and failure. Three completed studies are too small and heterogeneous for a strong calibration claim, and a same-operator retrospective score would invite narrative self-confirmation. Prospective predictions should accumulate before this becomes an active study.

### Remaining inactive — viable baseline

Inactivity remains preferable to a weak successor. The selected direction displaces it only because it is separately falsifiable, internally feasible, domain-distinct, bounded, and capable of producing reusable artifacts even under a negative result.

## 7. Proposal requirements

The frozen Study 004 proposal must:

1. keep the study inactive pending a later approval;
2. freeze the reference-model family, seed, mutation operators, budgets, metrics, and thresholds before outcomes;
3. prevent test-generation methods from inspecting mutant internals or exact-oracle results;
4. implement and freeze the competing methods before formal oracle classification is inspected;
5. use an independently written exact oracle with hand-audited correctness fixtures;
6. classify equivalent mutants rather than silently replacing them;
7. preserve random, breadth, and coverage-guided results at identical action budgets;
8. compare reduced counterexamples with exact shortest distinguishing traces;
9. permit negative and partial dispositions;
10. close within four approval cycles after activation.

## 8. Final disposition

**GO to one frozen proposal, which is created in this same portfolio cycle and remains inactive.**

- Study 001, Study 002, and Study 003 remain closed.
- Study 004 is proposed but not active.
- No code, generated corpus, experiment, active-study issue, external action, or human-subject work is authorized by this decision.
- A later `承認` must independently inspect the frozen proposal and decide activation GO or NO-GO.
