# Study 008 Activation Decision — NO-GO

_Date: 2026-07-29 (Asia/Tokyo)_  
_Disposition: **NO-GO; Study 008 was not activated**_

## Work selected

Re-evaluate the frozen inactive proposal `research/proposals/008-summeval-dimension-specific-proxy-reliability.md` against the live repository and official SummEval referents. Choose **GO unchanged** or **NO-GO**. Only after GO unchanged could Cycle 1 pin the exact source, license, safe scored text file, schema, denominator, populations, dimensions, metric inventory, directions, formulas, and resource caps.

## Official upstream identity

- Repository: `Yale-LILY/SummEval`
- Default branch: `master`
- Pinned inspected commit: `81b59ad53d63cb6009764240853c91235a44e238`
- Commit date: 2023-08-14
- Repository license file: MIT License
- Inspected README blob: `4b54cd7db70990ba8e22a947cf4bd5c9132acd0c`
- Inspected LICENSE blob: `fbe02d55ba3e128a8b75d1e2c90bd067e2fa9086`

The official README exposes two materially different annotation referents:

1. `model_annotations.aligned.jsonl` at the authors' Google Cloud Storage location, described as human annotations over 100 articles, 16 systems, 1,600 summaries, five crowd workers, three experts, and four dimensions;
2. a Google Drive link described in the update log as the annotation file updated to include all paper models and metric scores.

## Blocking evidence

### Human-only file does not satisfy the frozen metric condition

Official repository Issue #18, `How can I get "model_annotations.aligned.scored.jsonl"`, records that `model_annotations.aligned.jsonl` and the paired variant do not contain the `metric_scores_*` keys expected by the released correlation code.

The human-only file therefore cannot support the proposal's required activation-frozen inventory of at least eight complete automatic metrics. Recomputing metrics is not an allowed substitution because the proposal requires released official scores, forbids source-article reconstruction and model inference, and requires score directions and identities to be frozen before relationship inspection.

### Official scored-file link is unavailable

Official repository Issue #56, `human annotation file no longer avaliable`, remains open and specifically identifies the README Google Drive file ID `1d2Iaz3jNraURP1i7CfTqPIj8REZMJ3tS` as unavailable. The issue contains no maintainer-provided official replacement.

A direct retrieval attempt during this activation cycle did not yield the scored file. No third-party mirror was accepted.

### License scope remains insufficiently pinned for the missing file

The repository itself has an MIT license. The scored data file is external to the repository and could not be acquired, so its exact bytes and any file-specific licensing or provenance notice could not be inspected. This uncertainty is secondary to the decisive metric-file failure but would also need resolution before GO.

## Activation-condition audit

| Condition | Result | Evidence |
|---|---|---|
| exact official commit | pass | `81b59ad53d63cb6009764240853c91235a44e238` |
| repository and data-file license clear | incomplete | repository MIT; unavailable external scored file not inspectable |
| safe UTF-8 JSON/JSONL scored annotation file | **fail** | official scored-file link unavailable |
| scored-file SHA-256 and byte length | **fail** | no official scored file acquired |
| exact 100 × 16 = 1,600 scored-record denominator | **fail** | cannot validate the unavailable scored file |
| separate expert and crowd values for four dimensions | incomplete | described for human file, not validated in the unavailable scored file |
| 8–32 automatic metrics with full numeric coverage and supported directions | **fail** | human file lacks metric-score keys; scored file unavailable |
| field classes distinguishable before relationship inspection | **fail** | scored schema unavailable |
| no protected relationship or rank inspected | pass | no correlation, ranking, bootstrap, or hypothesis predicate computed |
| credible four-cycle completion | **fail under current referents** | Cycle 1 cannot freeze its required input |

## Decision

**NO-GO is mandatory under the frozen proposal.**

This is not a negative result about summarization metrics, human judgments, aggregation, or SummEval. It is an activation/setup decision: the exact official artifact required to define the protected study could not be pinned without violating the no-mirror, no-reconstruction, no-reduced-denominator, and no-guessed-direction rules.

## Boundaries preserved

- Study 008 was not activated.
- No active-study Issue was opened.
- No annotation dataset was committed.
- No third-party mirror was used.
- No metric implementation was run.
- No metric or human values were correlated, ranked, aggregated for outcome analysis, bootstrapped, or inspected as a protected relationship.
- No H1–H3 disposition exists.
- The frozen proposal remains unchanged as an archival record of the rejected activation candidate.

## Methodological correction

The post-Study-007 portfolio assessment gave this direction feasibility 5 / 5 based on a paper, README, and apparently public file links. Activation showed that public description is not equivalent to a currently retrievable and pinnable official artifact.

Future portfolio selection should require a minimal **referent-availability preflight before final scoring** whenever the proposed denominator depends on an external file. The preflight may verify official location, safe format, byte accessibility, license visibility, and high-level schema identity, but must not inspect protected relationships or outcomes.

## Next bounded work

The highest-value next cycle is one post-NO-GO portfolio decision. It should freeze a revised threshold before candidate scoring, make official artifact availability a hard feasibility gate, reconsider materially distinct candidates plus inactivity, and select at most one inactive proposal. It must stop before activation or implementation.