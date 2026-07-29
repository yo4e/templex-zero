# Study 007 Active Protocol

_Status: **Archived — Study 007 closed in Cycle 2 as a negative setup result**_  
_Activated and closed: 2026-07-29 (Asia/Tokyo)_  
_Issue: #13 (closed)_  
_Proposal: `research/proposals/007-sqlite-deferred-constraint-savepoint-state-conformance.md`_

This file preserves the frozen protocol that governed Study 007. Its research question, hypotheses, exact environment, schema, grammar, observations, error mapping, 72-sequence denominator, resource caps, instrument-independence rules, and four-cycle limit were not revised after activation.

The Cycle 2 hand gate failed before protected execution. The frozen `foreign_key` mapping required 787 / `SQLITE_CONSTRAINT_FOREIGNKEY` for every mapped foreign-key failure, but the exact local engine returned 1811 / `SQLITE_CONSTRAINT_TRIGGER` for the immediate `ON DELETE RESTRICT` gate case. Timing, exception class, relational state, and transaction state matched.

No permissible instrument correction could remove the mismatch without changing the frozen mapping. Study 007 therefore closed as required. The protected 72-sequence matrix was never executed, and H1–H3 were not evaluated.

The complete original active protocol remains available in repository history at blob `5b138a99adb3bc38af20f95b3bb209538119482b`. Current closure authority is:

- `CYCLE_2_INSTRUMENTS_AND_GATE.md`;
- `REPORT.md`;
- `hand_gate_result.json`;
- closed Issue #13.
