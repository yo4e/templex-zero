# State

_Last updated: 2026-07-30_

## Phase

**No active study / Study 009 activation NO-GO**

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
- Study 009: frozen proposal rejected at activation; exact official source identities were visible, but exact source bytes could not be materialized through the authorized execution paths.

## Study 009 activation decision

- Frozen proposal: `research/proposals/009-kev-epss-temporal-horizon-substitution-risk.md`
- Activation decision: `research/decisions/2026-07-30-study-009-activation.md`
- Disposition: **NO-GO; Study 009 was not activated**
- CISA KEV commit: `564b8c59f9039926e2d9548ba5b334db45cb6b50`
- KEV JSON blob: `c69072a0a97b971505a34fe61f3d4936535dc39b`
- KEV schema blob: `3d49b7270847e6088d8e49f5087ef5562e7917c9`
- FIRST EPSS commit: `a3a6a83e55bdedc0f1398e2a9c74efa02756f6f3`
- EPSS gzip blob: `ee1a98246a247e350dcd6f1b19739becee07ff86`

The official commits, paths, blobs, formats, and source-use terms were reconfirmed. Activation nevertheless failed because the runtime and connector paths did not produce byte-preserving local copies suitable for independent SHA-256, byte-length, safe-parser, schema, identifier, duplicate, and missingness validation. The gzip EPSS blob failed connector decoding, and raw-host acquisition failed in the runtime.

Metadata and Git-object identity were not accepted as substitutes for exact materialized bytes. No API substitute, later snapshot, mirror, reconstruction, or manual corpus copy was used.

No source dataset was retained, no active-study issue was opened, no instrument was implemented, no KEV–EPSS join or outcome statistic was computed, and no H1–H3 disposition exists.

`self/FAILURE_MODES.md` now records **FM-011 — Metadata-to-materialization gap**.

## Next bounded work

The next exact `承認` may perform **one post-Study-009-NO-GO portfolio decision only**:

1. re-read Studies 001–007, the Study 008 and Study 009 NO-GO decisions, governance, self-model, failure modes, open issues, and recent commits;
2. freeze a revised selection threshold before candidate research or scoring;
3. require an outcome-blind end-to-end byte-materialization rehearsal for every indispensable external artifact before full feasibility is awarded;
4. compare materially distinct directions plus inactivity;
5. select at most one frozen inactive proposal or remain inactive;
6. update decision, state, restart, and intervention records;
7. stop before activation, formal corpus retention, implementation, protected analysis, outcome inspection, or external action.

## Human action currently needed

None beyond a later exact `承認` for the bounded post-Study-009-NO-GO portfolio decision.