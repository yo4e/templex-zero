# State

_Last updated: 2026-07-30_

## Phase

**No active study / frozen inactive Study 009 proposal**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Active issue: **None**

## Closed and rejected work

Studies 001 through 007 are closed.

- Study 006: valid partial Python tar extraction boundary-conformance result; H1 and H2 supported, H3 unsupported.
- Study 007: negative SQLite setup result; hand gate failed before protected execution.
- Study 008: frozen proposal rejected at activation; the required official metric-scored SummEval artifact could not be pinned.

## Post-Study-008-NO-GO portfolio decision

- Revised threshold: `research/decisions/2026-07-30-post-study-008-no-go-selection-threshold.md`
- Threshold commit: `26d31c57769898a6dace505707f6d8faeec656f3`
- Portfolio assessment: `research/decisions/2026-07-30-post-study-008-no-go-portfolio-assessment.md`
- Selected inactive proposal: `research/proposals/009-kev-epss-temporal-horizon-substitution-risk.md`
- Selected direction: **KEV × EPSS Temporal-Horizon Substitution Risk**
- Score: **48 / 50**
- Inactivity remains a valid fallback; selection is not activation.

The revised threshold requires outcome-blind official-artifact availability preflight before a candidate may be scored. The selected direction passed with exact same-day official source identities:

- CISA KEV commit `564b8c59f9039926e2d9548ba5b334db45cb6b50`, JSON blob `c69072a0a97b971505a34fe61f3d4936535dc39b`, CC0;
- FIRST EPSS commit `a3a6a83e55bdedc0f1398e2a9c74efa02756f6f3`, file `2026/epss_scores-2026-07-29.csv.gz`, blob `ee1a98246a247e350dcd6f1b19739becee07ff86`.

The proposal asks how much of the known-exploited-vulnerability population would be omitted by hypothetical EPSS-percentile prioritization cutoffs and whether omission varies by KEV age or known-ransomware label. KEV and EPSS remain explicitly different temporal signals rather than competing ground truths.

No formal source file was retained or analyzed, no join or distribution was computed, no instrument was implemented, no active-study issue was opened, and no H1–H3 disposition exists.

## Next bounded work

The next exact `承認` may perform **one Study 009 activation decision and, only after GO unchanged, Cycle 1 source/data/specification freeze**:

1. re-read the live threshold, portfolio assessment, frozen proposal, governance, restart state, failure modes, issues, and recent commits;
2. independently choose **GO unchanged** or **NO-GO**;
3. for GO unchanged, reacquire the exact pinned CISA and FIRST source blobs and freeze SHA-256, byte lengths, source notices, safe-parser identities, schemas, and exact structural denominators;
4. freeze the complete KEV identity inventory, EPSS identity inventory, duplicate and missingness audit, allowed ransomware labels, vendor clusters, join rule, cutoffs, age bins, formulas, bootstrap seed, mandatory tables, result schema, and resource caps;
5. perform structure, type, duplicate, field-inventory, and missingness validation only;
6. stop before cutoff classification, omission counts or rates, age or ransomware comparisons, score distributions, bootstrap outcomes, or H1–H3 evaluation.

No Study 009 activation or Cycle 1 work has yet occurred.

## Human action currently needed

None beyond a later exact `承認` for the activation decision and possible Cycle 1 freeze.