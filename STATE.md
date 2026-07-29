# State

_Last updated: 2026-07-29_

## Phase

**Active Study 007 / Cycle 1 complete / instruments not implemented**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Active issue: **#13**

## Closed studies

Studies 001 through 006 are closed. Study 006 ended as a valid partial Python tar extraction boundary-conformance result: H1 and H2 supported, H3 unsupported.

## Study 007 activation

- Active name: **SQLite Deferred-Constraint and Savepoint State Conformance**
- Activation decision: `research/decisions/2026-07-29-study-007-activation.md`
- Active protocol: `research/studies/007-sqlite-deferred-constraint-savepoint-state-conformance/PROTOCOL.md`
- Exact runtime: CPython 3.13.5 at `/usr/bin/python3.13`
- Exact SQLite package: `libsqlite3-0 3.46.1-7+deb13u1`
- Local source ID suffix: `alt1`; not the vanilla 3.46.1 suffix `1e33`
- Scope consequence: all claims are limited to the exact pinned local binary
- Frozen matrix: **72 sequences / 439 actions / six families of 12**
- Manifest SHA-256: `16a01c109b196a1127d7783f110e492e4609713f8f527e50e95d7ef254678b4c`
- Structure validation: pass; maximum 12 actions and depth 3
- Capability preflight: pass
- Protected sequence executions: **0**

The portfolio assessment's earlier statement that the local source ID matched the published vanilla release ID was corrected during activation. The proposal remained unchanged because it already required pinning the exact local library at activation.

## Next bounded work

The next exact `承認` may perform **Study 007 Cycle 2 only**:

1. re-read the live protocol, manifest, Cycle 1 audit, environment, Issue #13, governance, and restart state;
2. implement a SQLite-independent relational/savepoint-stack model;
3. implement a separate SQLite harness and immutable-record comparator;
4. write targeted unit tests without executing the protected 72-sequence matrix;
5. freeze twelve hand-audited miniature traces and expected per-step records before running them;
6. run the hand gate, allowing at most one bounded implementation-correction phase;
7. freeze passing instruments or close negatively if the gate cannot pass;
8. stop before complete-matrix execution.

No Study 007 protected matrix outcome may be inspected in Cycle 2.

## Human action currently needed

None beyond a later exact `承認` for Cycle 2.
