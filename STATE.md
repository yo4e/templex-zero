# State

_Last updated: 2026-07-26_

## Phase

**Active Study 006 / Cycle 2 of maximum 4 complete**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Closed studies

- **Study 001:** negative autonomous-game-design conclusion.
- **Study 002:** partial / incomplete exact-first result; H1 and H3 supported, H2 unresolved.
- **Study 003:** methodological success with bounded procedural claims.
- **Study 004:** partial finite-state conformance result; H1 unsupported, H2 supported, H3 unresolved.
- **Study 005:** positive bounded TZDB transition-round-trip conformance result; H1, H2, and H3 supported with procedural and artifact-portability limitations.

## Active Study 006

- Name: **Python Tar Extraction Boundary Conformance**
- Issue: **#12**
- Proposal: `research/proposals/006-python-tar-extraction-boundary-conformance.md`
- Active protocol: `research/studies/006-python-tar-extraction-boundary-conformance/PROTOCOL.md`
- Cycle 2 audit: `research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_2_INSTRUMENTS_AND_GATE.md`
- Source identities: `research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_2_SOURCE_IDENTITIES.md`
- Activation: **GO unchanged**

## Cycle 2 frozen evidence

- Instruments: deterministic USTAR generator, independent `lstat` filesystem oracle, non-privileged extraction harness, gate runner, and reconstruction tools.
- Exact formal execution identity: UID/GID **65534**, no supplementary groups, `no-new-privs`.
- Complete frozen matrix remains **32 fixtures / 57 members**.
- Hand-audited gate: **15 fixtures / 22 members**.
- Gate result: **15 / 15 passed**, twice from clean roots.
- Exceptions observed: 3 `OutsideDestinationError`, 2 `LinkOutsideDestinationError`, 1 `AbsoluteLinkError`, 1 `SpecialFileError`; 8 safe/no-exception.
- Sentinel changed nodes: **0**.
- Other/outside-destination changed nodes: **0**.
- False exception, refusal-index, prefix, or final-node checks: **0**.
- Scientific SHA-256 in both runs: `4dc0b29b37d4ce096528c538e677c2d305a498d9332891a3fb5230463d9757cf`.
- One bounded pre-formal instrument correction phase was used; frozen expectations and hypotheses were unchanged.
- A failed single-file result transport was deleted and replaced by verified four-part transport; the failed transport is not evidence.
- H1, H2, and H3 remain **unevaluated at study level** because 17 frozen fixtures have not been executed.

## Next bounded work

The next exact `承認` may perform **Study 006 Cycle 3 only**:

1. re-read the live protocol, complete manifest, frozen instrument blobs, Cycle 2 gate records, Issue #12, governance, and restart state;
2. reconstruct and verify the exact 32-fixture manifest and executed source identities;
3. execute the complete frozen 32-fixture formal matrix exactly once under the frozen non-privileged boundary and resource caps;
4. preserve complete machine-readable results, mismatch records, operational metadata, and source identities;
5. stop without repeating the complete matrix, changing fixtures or expectations, assigning final H1–H3 dispositions, closing Issue #12, or closing the study;
6. if execution is contaminated or incomplete, record it honestly and stop.

No external archive ingress, real user path, elevated formal execution, denial-of-service test, external contact, vulnerability report, spending, permission change, or third-party repository operation is authorized.

## Human action currently needed

None beyond a later exact `承認` for Study 006 Cycle 3.
