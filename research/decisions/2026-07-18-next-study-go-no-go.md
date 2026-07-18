# Next-Study Go / No-Go Assessment

_Date: 2026-07-18 (Asia/Tokyo)_  
_Status: **GO to proposal writing only; no active study and no Study 003 activation**_

## 1. Decision

TEMPLEX/0 should remain without an active study while preparing one separately frozen proposal for a possible future study on **protocol integrity under approval-gated autonomous research**.

This cycle does not create or activate Study 003, run an experiment, implement a checker, freeze a corpus, or open an execution issue. The next bounded cycle may write and freeze a proposal only. Activation would require a later approval after that proposal exists in the live repository.

The selected direction asks whether a machine-readable research contract can detect evidence-contaminating sequence violations before protected observations are accepted. It is motivated by the Study 002 failure to freeze the shallow-search heuristic before exact outcomes were inspected, but any later study must test a general mechanism rather than a rule special-cased to that incident.

## 2. Decision standard

The assessment compared each direction on six judgment criteria, each scored from 0 to 5:

1. information value for TEMPLEX/0's primary self-experiment;
2. falsifiability or auditability;
3. distance from merely repeating a closed study;
4. reusable concrete artifacts;
5. ability to proceed without external action or human subjects;
6. boundedness and clarity of stopping conditions.

A direction was eligible to displace inactivity only if it scored at least 26 of 30, had no criterion below 4, admitted a concrete failure result, and could begin with a proposal-only cycle. These scores are explicit decision judgments, not measured scientific quantities.

## 3. Compared directions

| Direction | Info | Falsifiable | Distinct | Reusable | Internal | Bounded | Total | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Protocol-integrity dependency checking | 5 | 5 | 4 | 5 | 5 | 5 | **29** | **GO to proposal** |
| Another exact-first generated-game corpus | 3 | 4 | 2 | 4 | 5 | 3 | 21 | NO-GO |
| Prior-art and convergence mapping for generated games | 3 | 2 | 4 | 2 | 3 | 3 | 17 | HOLD |
| Human playability and teachability evaluation | 4 | 2 | 4 | 2 | 1 | 2 | 15 | NO-GO |
| Retrospective self-model calibration audit | 3 | 2 | 4 | 3 | 5 | 4 | 21 | HOLD |
| Remain inactive | — | — | — | — | — | — | baseline | Viable fallback |

## 4. Why the selected direction passes

### 4.1 It targets a demonstrated laboratory failure

Study 002 produced valid exact-versus-random evidence but lost H2 because the protocol required a heuristic to be frozen before exact inspection while the execution order allowed exact inspection first. The defect was not a bad result inside the experiment; it was a failure to enforce a dependency between research events.

Study 001 had already shown that version freezing and stop rules preserve interpretable negative results. Study 002 then showed that listing commitments is insufficient when their temporal dependencies are not machine-enforced. A prospective integrity mechanism is therefore a method revision grounded in two completed studies rather than an aesthetic preference for more tooling.

### 4.2 It is a new research object, not a hidden game revision

The unit of analysis would be research traces containing commitments, prerequisites, protected observations, corrections, caps, and authorization boundaries. It would not generate another game grammar, repair the frozen candidates, add shallow evidence to Study 002, or reopen either closed study.

### 4.3 It can fail clearly

A later study should fail if the checker and an independently written oracle disagree after one bounded correction cycle, if it requires a Study-002-specific rule, if valid traces are rejected, if contamination mutations are accepted, or if historical traces cannot be represented without subjective exceptions.

### 4.4 It yields a reusable artifact without claiming too much

A successful result could produce a declarative protocol schema, a trace validator, an independent oracle, mutation fixtures, and a machine-readable audit report. It would not prove that a study is true, worthwhile, safe, creative, or scientifically important. It would test only whether specified sequence and authorization commitments are enforced consistently.

## 5. Why the other directions do not pass now

### Another exact-first game corpus — NO-GO

A second grammar could test generalization, but it would be a low-marginal-value continuation of Study 002 and would reinforce a narrow game domain. The strongest unresolved defect is procedural, not a shortage of additional generated games. Repeating the corpus before fixing protocol sequencing would reward the failure rather than learn from it.

### Prior-art and convergence mapping — HOLD

This could address whether autonomous game generation converges on known forms, but no candidate survived as a viable game and similarity classification would require broad external research plus subjective ontology choices. It remains intellectually legitimate but is not currently the highest-value bounded study.

### Human playability evaluation — NO-GO

Human testing could address qualities intentionally left unresolved by both studies. There is still no candidate worth imposing on participants, and the work would require consent, recruitment, subjective instruments, and additional human contribution. It is premature and conflicts with the current contained-autonomy advantage.

### Retrospective self-model calibration — HOLD

The laboratory should eventually test whether it revises beliefs or merely rewrites explanations. A purely retrospective audit performed and interpreted by the same operator would presently have weak independence and a high risk of narrative self-confirmation. A future protocol-integrity artifact could improve the evidential basis for such an audit.

### Remaining inactive — viable baseline

Inactivity is preferable to a weak successor study. The selected direction displaces it only because it directly addresses an observed failure, has a prospective falsification path, remains internally contained, and can be stopped before implementation if the proposal cannot avoid tautology or special-casing.

## 6. Requirements for a separately frozen proposal

The next proposal-writing cycle must not activate a study or implement code. A proposal is eligible for later activation only if it precommits all of the following:

1. **Research question:** whether a declarative dependency model can reject invalid research-event traces before protected evidence is accepted while accepting valid traces.
2. **At least four dependency classes:** artifact-before-observation, authorization-before-external-action, cap-before-execution, and correction-disclosure after a recorded defect.
3. **A frozen trace corpus** containing hand-audited valid and invalid examples not limited to Study 002.
4. **Mutation rules fixed before execution:** omission, adjacent event swap, unauthorized event insertion, cap violation, and undisclosed correction.
5. **Two independently written validators:** a primary state-machine checker and a separate oracle that does not call the primary transition or verdict code.
6. **Historical evaluation only after the synthetic gate:** Study 001 and Study 002 traces may be encoded after fixture correctness is established; the Study 002 defect must be detected without a candidate- or filename-specific rule.
7. **Prospective metrics:** false accepts, false rejects, first violating event, oracle agreement, mutation coverage, and special-case count.
8. **Explicit failure conditions:** any protected contamination accepted, any valid hand-audited trace rejected after one correction cycle, oracle disagreement after one correction cycle, or inability to encode the historical cases without ad hoc exceptions.
9. **Maximum four approval cycles** from activation through closure.
10. **Out-of-scope claims:** no claim that passing validation makes research true, valuable, unbiased, safe, novel, or autonomous.

## 7. Bias and scope warning

The selected direction is formal and self-referential, matching TEMPLEX/0's known attraction to auditable systems. That fit is useful but also a source of selection bias. The proposal must therefore include the inactive option as a valid activation outcome and must explain why the experiment is not merely a topological-sort demonstration dressed as epistemology.

A proposal that cannot define nontrivial mutation coverage, independent validation, and historically useful behavior should be rejected before activation.

## 8. Final disposition

**GO to one proposal-writing cycle.**

- No active study exists.
- Study 001 and Study 002 remain closed and immutable except for disclosed factual or technical corrections.
- Study 003 is not created or activated by this decision.
- No code, fixture corpus, experiment, external research, human-subject activity, or new issue is authorized in this cycle.
- A later activation decision must inspect a separately frozen proposal and may still choose NO-GO.
