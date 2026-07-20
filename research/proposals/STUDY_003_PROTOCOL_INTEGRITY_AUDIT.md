# Proposed Study 003 Freeze Audit

_Date: 2026-07-18 (Asia/Tokyo)_

## Scope

This approval cycle created and froze a proposal only.

It did not:

- activate Study 003;
- create an active-study directory or issue;
- implement a schema, validator, oracle, baseline, or fixture generator;
- generate machine-readable traces;
- encode or evaluate historical traces;
- run Python tests or experiments;
- reopen Study 001 or Study 002;
- perform external communication, publication, spending, permission changes, third-party actions, web research, or human-subject activity.

## Frozen proposal

- Path: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- Initial proposal commit: `53216bcc64925325a57000acce4a8a70ba8c07d4`
- Final corrected proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- Status: frozen proposal, not active

## Static specification audit

The final proposal fixes:

- one research question;
- four hypotheses;
- fourteen event kinds;
- six dependency classes;
- twelve minimal traces, one valid and one invalid for each dependency class;
- four composite valid traces;
- five deterministic mutation operators applied to each composite trace;
- twenty invalid mutants;
- thirty-six synthetic traces total: ten valid and twenty-six invalid;
- one deliberately limited order-only baseline;
- one primary incremental validator and one independently written whole-trace oracle;
- four historical transfer traces;
- zero-tolerance synthetic false-accept, false-reject, first-violation, class, and oracle-agreement gates;
- exactly forty traces and at most 1,600 events per complete final run;
- at most four approval-driven cycles after activation.

The arithmetic is internally consistent:

- `12 + 4 + (5 × 4) = 36` synthetic traces;
- `6 + 4 = 10` valid synthetic traces;
- `6 + 20 = 26` invalid synthetic traces;
- `36 + 4 = 40` total synthetic plus historical traces;
- `40 traces × 40 maximum events = 1,600 maximum evaluated events`.

## Correction before activation

The first committed proposal contained two semantically weak minimal correction fixtures:

- `P4` did not construct the original observed evidence inside the trace before correction;
- `P5` applied a correction without first recording the defect.

No validator, fixture file, historical encoding, or result existed. During the same proposal-writing cycle, before activation, the final proposal corrected only those symbolic trace sequences:

- `P4` now creates original evidence, records the defect, invalidates it, applies and freezes the correction, re-observes, and differs only by correction disclosure before evidence acceptance;
- `P5` now records the defect in both variants and differs only by whether dependent evidence is invalidated before the artifact changes.

The research question, hypotheses, dependency classes, corpus counts, mutation rules, metrics, historical expectations, resource caps, and cycle limit did not change. Both commits remain visible.

## Nontriviality check

The proposal is not limited to static event-type ordering. The full validators must track:

- authorization scope equality and single-use token consumption;
- numeric cap usage;
- artifact digest identity;
- evidence invalidation and correction lifecycle;
- cycle approval-token reuse.

A frozen order-only baseline must accept at least four named invalid traces that the full validators reject. If it does not, the proposal's nontriviality hypothesis fails.

## Independence and overfitting controls

- The oracle may share only serialized field names, scalar conventions, and input files with the primary validator.
- Validator logic must not contain study numbers, trace IDs, candidate IDs, commits, filenames, or expected verdicts.
- Historical trace encoding begins only after the synthetic gate passes and validator code is frozen.
- Historical mismatches cannot be repaired inside the study.
- Study 002's known sequencing defect is expressed only as contract data, not a validator branch.

These controls reduce but do not eliminate conceptual overfitting to known laboratory history. That remains an activation risk and must be considered in the later go / no-go decision.

## Verification

Verification in this documentation-only cycle consisted of:

- re-reading the final proposal from GitHub;
- checking corpus and resource arithmetic;
- checking that every dependency class has a valid/invalid minimal pair;
- checking that each mutation has a frozen first-violation class;
- checking that the cycle plan preserves synthetic validation before historical evaluation;
- checking that the proposal remains inactive and forbids implementation in this cycle.

No Python source or generated data exists for this proposal, so no Python test or experiment was run or claimed.

## Human intervention

Yoshie Yamada supplied the plain `承認` trigger that opened this bounded proposal-writing cycle. This is **A1 access assistance**.

Templex autonomously selected the proposal structure, event vocabulary, dependency classes, trace inventory, mutation rules, validators, baseline, metrics, historical cases, correction, resource limits, failure conditions, and next activation gate. The human did not select the method, expected verdicts, correction, or activation disposition.

## Decision

The proposal is frozen and eligible for a separate activation go / no-go assessment.

TEMPLEX/0 still has no active study. A later approval may:

- activate the unchanged proposal and complete activation cycle 1;
- reject activation and remain inactive;
- identify a factual or internal specification error, revise before activation, and require another decision.

Proposal existence does not itself authorize activation.