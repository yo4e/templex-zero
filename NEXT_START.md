# Next Start

_Updated: 2026-07-29 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the post-Study-007 selection threshold and portfolio assessment, the frozen Study 008 proposal, the Study 008 activation NO-GO decision, all seven closed-study results, governance and intervention records, self-model and failure modes, open issues, and recent commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**TEMPLEX/0 has no active study. Studies 001 through 007 are closed. Study 008 was not activated.**

The frozen Study 008 proposal concerned dimension-specific false reassurance in SummEval automatic metrics. Activation chose **NO-GO** because the exact official metric-scored annotation artifact could not be pinned under the proposal's no-mirror and no-reconstruction rules.

## Retained activation evidence

- activation decision: `research/decisions/2026-07-29-study-008-activation.md`;
- frozen proposal: `research/proposals/008-summeval-dimension-specific-proxy-reliability.md`;
- official upstream: `Yale-LILY/SummEval`;
- pinned inspected commit: `81b59ad53d63cb6009764240853c91235a44e238`;
- repository license: MIT;
- human annotation referent: `model_annotations.aligned.jsonl`;
- official Issue #18 reports that the human and paired annotation files lack `metric_scores_*` keys required by released correlation code;
- official Issue #56 reports the scored Google Drive annotation file unavailable and remains open without an official replacement;
- no third-party mirror was accepted;
- no dataset, code, active issue, correlation, rank, bootstrap result, or hypothesis outcome exists.

## Why NO-GO was mandatory

GO unchanged required one safe official scored JSON/JSONL artifact with exact bytes, 100 documents × 16 systems = 1,600 unique records, separate expert and crowd judgments across four dimensions, and 8–32 automatic metrics with complete numeric coverage and upstream-supported directions.

The unavailable scored file prevented freezing:

- SHA-256 and byte length;
- scored-file schema and exact denominator;
- metric inventory and field classification;
- complete numeric coverage;
- score directions;
- file-specific provenance or licensing notice.

The accessible human-only referent could not be substituted because it lacks the required metric-score fields. Recomputing metrics, reconstructing source articles, using a mirror, guessing directions, or reducing the denominator would change the frozen proposal.

## Mandatory lesson

`self/FAILURE_MODES.md` now includes **FM-010 — Referent availability optimism**.

A candidate that depends on an external artifact must not receive full feasibility merely because a paper or README names a public file. Before final scoring, perform an outcome-blind availability preflight covering official location, safe format, byte accessibility, license visibility, and high-level schema identity. Do not inspect protected relationships or outcomes during that preflight.

## Next bounded work unit

The next exact `承認` may perform **one post-Study-008-NO-GO portfolio decision only**:

1. freeze a revised threshold before candidate research or scoring;
2. make official referent availability a hard feasibility gate;
3. compare materially distinct candidates plus inactivity;
4. select at most one frozen inactive proposal or remain inactive;
5. update decision, state, restart, and intervention records;
6. stop before activation, implementation, protected analysis, or external action.

## Human gate

> 承認

## Human action pending

None. A later exact `承認` opens the bounded post-NO-GO portfolio decision only.