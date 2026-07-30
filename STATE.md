# State

_Last updated: 2026-07-31_

## Phase

**No active study / portfolio remains inactive / execution-path audit complete**

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
- Study 010 proposal: **None**.

## Non-study execution-path capability audit

- Audit: `operations/execution-path-capability-audit-2026-07-31.md`
- Machine-readable matrix: `operations/execution-path-capability-audit-2026-07-31.json`
- Probe-matrix freeze commit: `56f01b116ae92c9785a2a0e69cd5f19c3f0dc901`
- Result: **2 PASS, 2 PARTIAL, 4 FAIL**

Complete materialization passed only for tested existing local UTF-8 text and local binary files. Both paths supported byte-for-byte copies, local size and SHA-256, bounded safe-parser opening, and repeated identical results.

Tested official HTTPS paths did not create local files:

- RFC Editor text and IANA gzip downloads failed through `container.download`;
- bounded curl failed DNS resolution for `www.rfc-editor.org` and `data.iana.org`.

GitHub connector paths remained partial:

- pinned UTF-8 text returned repeatable blob identity and complete response content but no mounted local file;
- pinned binary returned blob identity and a base64 response resource but no mounted local file;
- direct binary `fetch_blob` failed with `UnicodeDecodeError`.

Connector response resources were not visible as execution-filesystem paths. No manual reconstruction or reserialization was accepted as byte-preserving materialization.

All temporary audit files were deleted. No formal corpus, research instrument, scientific outcome, proposal, active study, or active Issue was created.

`self/LIMITS.md` now records the sharper distinction between local materialization, public HTTPS failure, connector content inspection, and filesystem handoff. FM-010 and FM-011 remain sufficient; no new failure mode was added.

## Next bounded work

The next exact `承認` may perform **one non-study inactivity re-entry gate only**:

1. re-read the live capability audit, portfolio decision, limits, failure modes, governance, state, issues, and recent commits;
2. freeze objective conditions that justify reopening portfolio candidate research rather than repeating search without changed evidence;
3. distinguish capability change, a materially new externally governed local referent, an authorized human-evidence opportunity, and mere availability or activity pressure;
4. classify the current state against those conditions;
5. update the restart state and stop;
6. do not research or score candidates, freeze a proposal, activate a study, retain a corpus, inspect protected outcomes, or take external action.

## Human action currently needed

None beyond a later exact `承認` for the bounded inactivity re-entry gate.
