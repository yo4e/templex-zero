# Study 004 Cycle 3 — Oracle Fixture Freeze

_Date: 2026-07-23 (Asia/Tokyo)_

## Protected order

This record and `data/oracle_fixtures_v1.json` were committed before implementation or execution of the exact paired-state oracle and before any frozen-corpus equivalence classification.

No Cycle 1 corpus mutant was inspected while these expected results were written.

## Frozen fixture set

- fixture count: **10**;
- equivalent cases: **2**;
- distinguishable cases: **8**;
- shortest expected trace lengths: 1, 2, 3, and 4 actions;
- one explicit equal-length lexicographic tie case;
- one hidden-state divergence case where the first action output agrees;
- file: `data/oracle_fixtures_v1.json`;
- file SHA-256: `c3dbd66b2260918f1f3b0071d39655d00f4734f3ef427dd2dd0796c4d4e3281e`;
- fixture commit: `2a32a84d80b9eb30afdcceb52031a8250a88f604`.

## Hand-audit rule

Each fixture contains a prose reason for its expected equivalence result or exact shortest distinguishing trace. Expectations were determined by direct inspection of the hand-authored transition tables under the frozen action order `a0 < a1 < a2`.

The fixture freeze does not validate the future oracle. The oracle passes its correctness gate only if it reproduces every frozen expected result without changing this file or the fixture data.

## Correction allowance

The protocol permits at most one bounded oracle correction cycle after a failed gate. It does not permit changing fixture expectations to match an implementation result. Any fixture error discovered after execution must remain visible and must be dispositioned as a fixture or gate failure rather than silently rewritten.
