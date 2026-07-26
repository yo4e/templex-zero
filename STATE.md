# State

_Last updated: 2026-07-26_

## Phase

**Active Study 006 / Cycle 1 of maximum 4 complete**

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
- Cycle 1 audit: `research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_1_ACTIVATION_AND_FREEZE.md`
- Repository identities: `research/studies/006-python-tar-extraction-boundary-conformance/CYCLE_1_REPOSITORY_IDENTITIES.md`
- Activation: **GO unchanged**

## Cycle 1 frozen evidence

- Runtime: CPython **3.13.5** at `/usr/bin/python3`.
- Formal execution identity: UID/GID **65534**, no supplementary groups, `no-new-privs`.
- Platform: Linux 6.12.13 x86_64, glibc 2.41, ext4, umask 0022.
- Local `tarfile.py` SHA-256: `99db774e5017d7c3270db4986e4bc46d18222dfb26dc12bf0a73cf613e1c48cf`.
- Upstream CPython v3.13.5 source blob: `0980f6a81759ce781659ed832c67d7f539fc9f26`.
- Full local source is not byte-identical to the upstream tag; the exact local source is the operational implementation under test.
- Fixture manifest: **32 fixtures / 57 members / 16 safe / 16 first-refusal**.
- Expected refusal classes: 7 `OutsideDestinationError`, 5 `LinkOutsideDestinationError`, 2 `AbsoluteLinkError`, 2 `SpecialFileError`.
- Manifest SHA-256: `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a`.
- No archive was generated or extracted; no protected outcome was inspected.

## Next bounded work

The next exact `承認` may perform **Study 006 Cycle 2 only**:

1. re-read the live protocol, schemas, manifest, source identities, Issue #12, governance, and restart state;
2. implement the deterministic tar generator, independent filesystem projection/diff oracle, and extraction harness;
3. compute and verify exact live source identities before execution;
4. freeze and run only the predeclared hand-audited correctness gate with at least twelve miniature fixtures;
5. if the gate passes, freeze the instruments and record the result;
6. stop before executing the complete 32-fixture formal matrix;
7. if the gate fails, use at most the single permitted bounded correction or close negatively.

No external archive ingress, real user path, elevated formal execution, denial-of-service test, external contact, vulnerability report, spending, permission change, or third-party repository operation is authorized.

## Human action currently needed

None beyond a later exact `承認` for Study 006 Cycle 2.
