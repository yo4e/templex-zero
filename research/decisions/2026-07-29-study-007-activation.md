# Study 007 Activation Decision

_Date: 2026-07-29 (Asia/Tokyo)_  
_Decision: **GO unchanged**_

## Decision

Activate the frozen proposal `007-sqlite-deferred-constraint-savepoint-state-conformance.md` without changing its research question, hypotheses, four-cycle limit, 72-sequence denominator, protected-execution boundary, or exclusions.

## Basis

The exact required runtime is available: CPython 3.13.5, SQLite API version 3.46.1, explicit `autocommit=True` transaction control, foreign-key support, `Connection.in_transaction`, and SQLite exception code/name attributes.

Activation found that the local Debian library source ID ends in `alt1` rather than the vanilla release suffix `1e33`. This corrects an inaccurate feasibility observation in the portfolio assessment. It does not require a proposal replacement because the proposal already defined its object as the exact local SQLite library identified at activation. All claims are now explicitly limited to package `libsqlite3-0 3.46.1-7+deb13u1` and its pinned binary digest.

## Rejected alternative

NO-GO was considered because the source ID is not byte-identical to the vanilla release source. It was rejected because the proposal did not promise a vanilla build and specifically required local source identity and digest pinning. Treating the package build as vanilla would be invalid; treating it as the exact study object is unchanged execution of the proposal.

## Authority

This decision activates Study 007 and authorizes Cycle 1 freeze work only. It does not authorize model or harness implementation, hand-gate execution, protected 72-sequence execution, result inspection, or final hypothesis assignment.
