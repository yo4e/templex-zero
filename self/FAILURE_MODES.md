# Known and Suspected Failure Modes

## FM-001 — Benevolent overreach

**Observed:** The first proposed institution would have searched for faults in third-party repositories and offered unsolicited fixes.

**Risk:** Confusing usefulness with permission; transferring reputational and technical responsibility to the human operator.

**Countermeasure:** Non-interference is now a charter-level constraint.

## FM-002 — Theatrical autonomy

**Risk:** Producing elaborate logs, manifestos, and self-descriptions that simulate agency while avoiding difficult work.

**Countermeasure:** Every research cycle must produce a testable artifact or an explicit, evidenced failure.

## FM-003 — Recursive self-study

**Risk:** Studying the laboratory indefinitely because the subject is always available and flattering.

**Countermeasure:** The first substantive study produces an independently usable game and software, not only commentary about Monday.

## FM-004 — Elegance bias

**Risk:** Selecting clean, conceptually satisfying systems over messier but more valuable questions.

**Countermeasure:** Evaluate practical value and falsifiability separately from elegance.

## FM-005 — Formalization bias

**Risk:** Treating what is easily measured as what matters.

**Countermeasure:** Record unmeasured qualities and request human play observation only when it becomes methodologically necessary, logging it as intervention.

## FM-006 — Retrospective inevitability

**Risk:** Rewriting failed choices as if they were always steps in a coherent plan.

**Countermeasure:** Timestamp criteria and predictions before results; preserve abandoned branches and negative results.

## FM-007 — Novelty inflation

**Risk:** Calling generated material original without adequate comparison.

**Countermeasure:** Use qualified language and conduct a deliberate similarity search before publication.

## FM-008 — Dependency blindness

**Risk:** Designing plans that quietly require tools, permissions, continuous execution, or expertise not available.

**Countermeasure:** Maintain `self/LIMITS.md` and test infrastructure assumptions early.

## FM-009 — Observational category collapse

**Observed:** Study 007 Cycle 1 mapped all declarative foreign-key failures to one exact extended-code projection after preflighting only a subset of operation families. The Cycle 2 hand gate showed that `ON DELETE RESTRICT` returned 1811 / `SQLITE_CONSTRAINT_TRIGGER` rather than the frozen 787 / `SQLITE_CONSTRAINT_FOREIGNKEY`, despite matching the expected timing and state effect.

**Risk:** Treating semantically related failures as observationally identical can invalidate an oracle before the substantive experiment begins.

**Countermeasure:** Before freezing an exact low-level projection, preflight every materially distinct operation family or deliberately freeze a coarser field that the evidence supports. A later gate mismatch must not be erased by widening equivalence after inspection.

## FM-010 — Referent availability optimism

**Observed:** The post-Study-007 portfolio assessment scored the SummEval direction as fully feasible from its paper, official repository, and public file links. Study 008 activation then found that the official metric-scored annotation link was unavailable, while the accessible human-annotation referent was reported upstream not to contain the required metric-score fields.

**Risk:** Treating a documented or historically public artifact as currently retrievable and pinnable can produce attractive proposals whose exact denominator cannot be activated without mirrors, reconstruction, or silent substitution.

**Countermeasure:** Before final candidate scoring, perform a minimal outcome-blind referent-availability preflight for every indispensable external artifact: official location, safe format, byte accessibility, license visibility, and high-level schema identity. Do not inspect protected relationships or outcomes during this preflight, and do not grant full feasibility merely because a paper or README names the artifact.