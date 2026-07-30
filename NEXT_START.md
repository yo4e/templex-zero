# Next Start

_Updated: 2026-07-30 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the post-Study-008-NO-GO threshold and portfolio assessment, the frozen Study 009 proposal, the Study 008 activation NO-GO decision, all seven closed-study results, governance and intervention records, self-model and failure modes, open issues, and recent commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**TEMPLEX/0 has no active study. Studies 001 through 007 are closed. Study 008 was not activated. One Study 009 proposal is frozen and inactive.**

The selected proposal is **KEV × EPSS Temporal-Horizon Substitution Risk**. It scored 48 / 50 after passing the revised outcome-blind official-artifact availability preflight.

The direction asks how much of the complete CISA known-exploited-vulnerability population would be omitted by hypothetical FIRST EPSS percentile cutoffs and whether omission differs by:

- time since CISA KEV addition;
- CISA's `knownRansomwareCampaignUse` label.

KEV and EPSS must remain semantically separate: KEV records historical evidence of exploitation in the wild; EPSS estimates exploitation probability in the next thirty days. The proposal measures substitution loss and does not treat either signal as a universal ground truth.

No source dataset was retained or analyzed, no join or distribution was computed, no code or active issue exists, and no hypothesis outcome exists.

## Key records

- revised selection threshold: `research/decisions/2026-07-30-post-study-008-no-go-selection-threshold.md`;
- threshold creation commit: `26d31c57769898a6dace505707f6d8faeec656f3`;
- portfolio assessment: `research/decisions/2026-07-30-post-study-008-no-go-portfolio-assessment.md`;
- frozen inactive proposal: `research/proposals/009-kev-epss-temporal-horizon-substitution-risk.md`;
- Study 008 NO-GO decision: `research/decisions/2026-07-29-study-008-activation.md`;
- failure mode: `self/FAILURE_MODES.md` — FM-010 referent availability optimism.

## Frozen source candidates

### CISA KEV

- official repository: `cisagov/kev-data`;
- commit: `564b8c59f9039926e2d9548ba5b334db45cb6b50`;
- JSON path: `known_exploited_vulnerabilities.json`;
- Git blob: `c69072a0a97b971505a34fe61f3d4936535dc39b`;
- same-commit JSON Schema;
- license: CC0 1.0.

### FIRST EPSS

- official historical-score repository: `empiricalsec/epss_scores`;
- commit: `a3a6a83e55bdedc0f1398e2a9c74efa02756f6f3`;
- file: `2026/epss_scores-2026-07-29.csv.gz`;
- Git blob: `ee1a98246a247e350dcd6f1b19739becee07ff86`;
- documented fields: `cve`, `epss`, `percentile`;
- use limited to bounded preventative cybersecurity research under visible FIRST terms, with no raw EPSS redistribution by TEMPLEX/0.

## Mandatory activation conditions

GO unchanged requires:

1. both official repositories, commits, paths, and frozen Git blobs remain accessible;
2. exact decoded bytes can be acquired safely without credentials, payment, new terms, or mirrors;
3. SHA-256, byte length, encoding, source notices, and parser identities can be frozen;
4. the KEV JSON and same-commit schema are structurally valid;
5. KEV identifiers, `dateAdded`, `vendorProject`, and ransomware labels satisfy the frozen requirements;
6. EPSS identifiers are unique and `epss` / `percentile` values are finite in `[0,1]` with a matching source date and model header;
7. exact source counts, duplicates, identifier inventories, vendor clusters, ransomware-label inventory, and KEV-to-EPSS missingness can be frozen without computing protected outcome rates;
8. every KEV record remains in the protected denominator, including unscored records;
9. the visible CISA and FIRST use conditions remain compatible with derived aggregate research and no raw EPSS redistribution;
10. the study remains feasible within four cycles and frozen caps.

Any failure requires NO-GO. No different date, API substitute, mirror, identifier repair, guessed label, recomputed score, reduced denominator, or raw EPSS republication is permitted.

## Protected Cycle 1 boundary

After GO unchanged, Cycle 1 may:

- reacquire exact source blobs;
- freeze source hashes, bytes, schemas, notices, parser identities, denominators, identifier and category inventories;
- freeze exact joins, explicit unscored treatment, percentile cutoffs `0.50, 0.75, 0.90, 0.95, 0.99`, age bins, vendor-cluster bootstrap, seed `2026073009`, hypotheses, mandatory tables, result schema, and caps;
- validate structure, types, duplicates, field inventories, and missingness.

It must stop before:

- classifying records as retained or omitted;
- computing omission counts or rates;
- comparing age or ransomware strata;
- inspecting EPSS score or percentile distributions;
- running bootstrap outcome analysis;
- evaluating H1–H3;
- making security or remediation recommendations.

## Human gate

> 承認

## Human action pending

None. A later exact `承認` opens one activation decision and, only after GO unchanged, Study 009 Cycle 1.