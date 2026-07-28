# Proposed Study 007 — SQLite Deferred-Constraint and Savepoint State Conformance

_Date: 2026-07-28 (Asia/Tokyo)_  
_Status: **Frozen inactive proposal — not activated**_

## 1. Go / no-go status

**GO to a separately gated activation decision.**

This proposal does not activate Study 007, create an active-study issue, implement a model or harness, generate the protected 72-sequence manifest, execute a protected SQL sequence, inspect a protected outcome, or assign a hypothesis disposition. TEMPLEX/0 remains without an active study.

A later exact project-chat `承認` must re-read the live repository and choose activation **GO unchanged** or **NO-GO**. If activated unchanged, the study may perform Cycle 1 only.

The proposal follows `research/decisions/2026-07-28-post-study-006-portfolio-assessment.md` and its separately committed pre-selection threshold.

## 2. Research question

> On the pinned SQLite 3.46.1 engine exposed through CPython 3.13.5, do explicit SQL transactions, nested and duplicate-named savepoints, deferred and immediate foreign-key constraints, failed commit or outer-release boundaries, and subsequent recovery operations produce the documented error timing, transaction-stack effects, relational state, and constraint state across a frozen finite sequence matrix, as judged by an independently implemented relational and savepoint-state model?

The unit of analysis is one original declarative statement sequence, one fresh in-memory SQLite database, one frozen schema and connection configuration, and one complete step-by-step logical-state trace.

The study evaluates one SQLite version, one CPython wrapper version, one compile configuration, explicit SQL transaction control, a small relational schema, and a frozen sequence grammar. It does not certify SQLite generally and does not test durability, crash recovery, concurrency, locking, WAL behavior, performance, SQL injection, hostile database files, extension loading, arbitrary SQL, or other database engines.

## 3. External referents

The normative and operational referents are fixed as:

- SQLite savepoint documentation: `https://www.sqlite.org/lang_savepoint.html`;
- SQLite foreign-key documentation: `https://www.sqlite.org/foreignkeys.html`;
- SQLite 3.46.1 release record: `https://sqlite.org/releaselog/3_46_1.html`;
- Python 3.13 `sqlite3` documentation: `https://docs.python.org/3.13/library/sqlite3.html`;
- the exact local SQLite library and CPython `sqlite3` wrapper available at activation, whose version, source ID, compile options, module paths, and digests must be recorded.

Activation must confirm:

- CPython is exactly 3.13.5 at the selected executable;
- `sqlite3.sqlite_version` is exactly 3.46.1;
- `SELECT sqlite_source_id()` matches the recorded engine build;
- foreign-key support is compiled in and can be explicitly enabled;
- the Python connection supports the explicit `autocommit` parameter;
- `Connection.in_transaction`, `sqlite_errorcode`, and `sqlite_errorname` are available for the frozen observation schema;
- in-memory databases and all required SQL statements work without extensions or external files.

A runtime or engine change closes activation as NO-GO unless this proposal is replaced in a separate portfolio cycle. The study must not silently migrate to a newer Python or SQLite version.

## 4. Frozen hypotheses

### H1 — savepoint-stack and rollback semantics

For every H1 sequence:

1. `SAVEPOINT` pushes a named mark and permits duplicate names;
2. `ROLLBACK TO name` restores rows to the state immediately after the most recent matching mark, cancels intervening marks, and leaves the matched mark active;
3. `RELEASE name` removes marks back through the most recent matching name and merges their work into the remaining parent;
4. inner `RELEASE` does not make work immune to a later outer rollback;
5. outermost `RELEASE`, plain `COMMIT`, and plain `ROLLBACK` empty the transaction stack with the documented commit or rollback effect;
6. missing-name, nested-`BEGIN`, and other frozen invalid operations return the expected error category without an unrecorded row-state change.

**Support criterion:** zero mismatch in statement disposition, `in_transaction`, final and intermediate ordered rows, foreign-key-check rows, and frozen probe results across all H1 sequences.

### H2 — immediate and deferred foreign-key timing

For every H2 sequence:

1. immediate constraints reject the violating statement and revert that statement's relational effect;
2. deferred constraints may remain violated inside an explicit transaction;
3. a deferred violation causes `COMMIT` or outer transaction-savepoint `RELEASE` to fail;
4. nested savepoints may be released while a deferred violation exists;
5. a `RESTRICT` action fires at the documented immediate boundary even when attached to a deferred constraint;
6. repairing the relational violation before the governing outer boundary permits the boundary to succeed.

**Support criterion:** zero mismatch in error timing and code, relational state, foreign-key-check output, transaction state, and final committed state across all H2 sequences.

### H3 — failed-boundary recovery and reproducibility

For every H3 sequence:

1. a failed deferred-constraint `COMMIT` leaves the transaction open;
2. nested savepoints that should survive a failed outer boundary remain operable under frozen follow-up probes;
3. a failed outer transaction-savepoint `RELEASE` preserves the documented recoverable state;
4. subsequent repair, rollback, rollback-to, release, commit, or full rollback produces the independently modeled result;
5. the complete portable step trace reproduces byte-identically in one clean final execution from verified committed inputs and instruments.

**Support criterion:** zero recovery-state mismatch across all H3 sequences and byte-identical complete portable scientific payloads between the original and clean reproduction.

No hypothesis, denominator, sequence, error expectation, or threshold may be changed after protected sequence outcomes are inspected.

## 5. Frozen behavioral domain

### 5.1 Connection configuration

The primary connection must use:

- database: `:memory:`;
- Python `sqlite3.connect(..., autocommit=True)` so transaction boundaries are expressed only by explicit SQL in the sequence;
- `PRAGMA foreign_keys = ON` before schema creation;
- no adapters, converters, row factories, user functions, collations, extensions, authorizers, progress handlers, or trace callbacks that can alter engine behavior;
- one connection and one thread;
- deterministic text and integer values only.

Activation must verify the exact wrapper semantics before freezing the active protocol. If `autocommit=True` cannot provide direct explicit-SQL transaction control under the pinned wrapper, activation is NO-GO.

### 5.2 Schema family

The protected schema family must remain small and original. It may use only:

- one parent table with an integer primary key;
- one or two child tables with integer primary keys and parent references;
- one immediate foreign key;
- one `DEFERRABLE INITIALLY DEFERRED` foreign key;
- one separately frozen deferred foreign key with `ON DELETE RESTRICT` for timing controls;
- no triggers other than SQLite's internal foreign-key machinery;
- no generated columns, virtual tables, attached databases, recursive CTEs, views, or schema mutation during a protected sequence.

Every schema statement and initial row must be frozen before protected execution.

### 5.3 Declarative action grammar

The protected grammar may contain only declarative actions translated by the harness into fixed SQL templates:

- `begin`;
- `savepoint(name)`;
- `release(name)`;
- `rollback`;
- `rollback_to(name)`;
- `commit`;
- insert parent;
- delete parent;
- insert immediate child;
- insert deferred child;
- delete immediate or deferred child;
- frozen read-only state probes.

Arbitrary SQL strings are not permitted in the manifest. Names and values must come from frozen bounded alphabets.

### 5.4 Exact sequence matrix

Cycle 1, if activated, must freeze exactly **72 sequences** before protected execution:

| Family | Sequences | Primary tag |
|---|---:|---|
| basic savepoint stack and rollback | 12 | H1 |
| duplicate and missing savepoint names | 12 | H1 |
| immediate versus deferred constraint timing | 12 | H2 |
| failed commit and repair or rollback | 12 | H2/H3 |
| nested versus transaction savepoint under violation | 12 | H2/H3 |
| failed-boundary survival and `RESTRICT` timing | 12 | H3 |

The matrix must include at minimum:

1. outer savepoint commit by `RELEASE`;
2. inner release followed by outer rollback;
3. rollback-to with the matched mark retained;
4. duplicate names with release to the most recent match;
5. duplicate names with rollback to the most recent match;
6. missing-name release and rollback-to errors;
7. `BEGIN` attempted with a nonempty transaction stack;
8. immediate violating insert;
9. deferred violating insert repaired before commit;
10. deferred violating insert followed by failed commit, repair, and successful commit;
11. deferred violation with nested savepoint release;
12. deferred violation with outer transaction-savepoint release failure;
13. nested savepoints remaining usable after failed commit;
14. full rollback after failed commit;
15. `RESTRICT` action producing immediate failure under a deferred declaration;
16. matched nonviolating controls for every protected error family.

No sequence may be added, removed, reordered, repaired, retagged, or have its expected result changed after the first protected execution begins.

### 5.5 Resource caps

Cycle 1 must freeze caps no weaker than:

- exact sequences: 72;
- maximum actions per sequence: 24;
- maximum active savepoint depth: 6;
- maximum distinct savepoint names: 4;
- maximum rows per table: 16;
- maximum total inserted logical rows per sequence: 32;
- maximum output records per sequence: 32;
- maximum wall time per sequence: 2 seconds;
- maximum complete-matrix wall time: 120 seconds;
- no subprocess from the sequence runner;
- no network, extension loading, filesystem database, attached database, or external input.

A cap failure is evidence and may produce an operationally incomplete result. Caps may not be raised after protected execution begins.

## 6. Independent state model and oracle

The primary oracle must be a finite state model that does not call SQLite, execute SQL, import the harness's verdict helpers, or infer expected behavior from observed outcomes.

It must independently represent:

- ordered parent and child row sets;
- immediate and deferred constraint validity;
- a transaction/savepoint stack with duplicate names;
- the relational snapshot associated with each mark;
- whether an outer transaction exists;
- statement success or expected error category;
- commit, release, rollback, and rollback-to effects;
- the state retained after a failed boundary.

The SQLite harness must independently observe:

- per-step success or Python exception class;
- SQLite error code and error name where available;
- `Connection.in_transaction` after every step;
- ordered table rows after every step;
- `PRAGMA foreign_key_check` output after every step;
- results of frozen follow-up probes used to establish surviving savepoint behavior.

The comparison layer may compare model and observed records but may not alter either instrument's state transitions.

Raw database pages, rowids not declared by the schema, timing, memory addresses, exception prose, and absolute paths must be excluded from the portable scientific payload.

## 7. Hand-audited correctness gate

Before the complete 72-sequence matrix is executed, Cycle 2 must freeze and run at least twelve miniature sequences with manually stated step-by-step model states and expected SQLite observations.

The gate must cover:

- basic savepoint and release;
- inner release followed by outer rollback;
- rollback-to with retained mark;
- duplicate names;
- missing savepoint name;
- nested `BEGIN` error;
- immediate foreign-key failure;
- deferred violation repaired before commit;
- failed commit with open transaction;
- nested release during deferred violation;
- outer transaction-savepoint release failure;
- immediate `RESTRICT` timing.

The independent model and SQLite observation must match every frozen gate expectation. At most one bounded instrument-correction phase is permitted before the complete matrix. A correction may fix implementation defects but may not change the proposal hypotheses, complete-matrix denominator, or already inspected gate expectations merely to obtain a pass.

## 8. Protected sequence and cycle plan

The study has a maximum of four approval cycles from activation through closure.

1. **Cycle 1 — activation and freeze:** reverify exact environment and source identities; freeze active protocol, documentation referents, schema, action grammar, projection, error mapping, resource caps, exact 72-sequence manifest, and Issue. Perform structure-only validation and capability preflight, but no protected sequence execution.
2. **Cycle 2 — instruments and gate:** implement the independent model, SQLite harness, comparison layer, and targeted tests; freeze and pass the hand-audited gate; freeze instruments.
3. **Cycle 3 — formal matrix:** execute the complete 72-sequence matrix exactly once; preserve complete results, mismatches, operational metadata, and source identities; do not assign final hypothesis dispositions.
4. **Cycle 4 — reproduction and closure:** reconstruct exact committed inputs and original result; execute one clean reproduction; compare portable payloads; analyze without expectation revision; assign H1–H3; report; close Issue and study.

No fifth cycle is permitted.

## 9. Required artifacts and metrics

The final report must include:

- CPython, SQLite, source ID, compile options, wrapper paths, and documentation identities;
- exact schema, grammar, sequence count, action count, and family inventory;
- expected and observed success/error counts by operation family;
- error-class, SQLite-code, and error-boundary accuracy;
- per-step `in_transaction` accuracy;
- ordered relational-state accuracy;
- foreign-key-check accuracy;
- savepoint-survival probe accuracy;
- failed-commit and failed-release recovery outcomes;
- immediate versus deferred and `RESTRICT` timing outcomes;
- complete scientific payload digests for original and reproduction;
- H1–H3 dispositions without threshold revision.

Required reusable artifacts are:

- frozen proposal and active protocol;
- schema and declarative 72-sequence manifest;
- independent finite state model;
- SQLite execution harness;
- hand-audited gate cases;
- targeted tests;
- complete machine-readable results and mismatch records;
- source/result identity ledgers;
- cycle audits and final report.

## 10. Disposition rules

### Full bounded success

All of the following must hold:

- activation and capability preflight pass;
- the hand-audited correctness gate passes within its one permitted correction opportunity;
- the complete matrix and clean reproduction are operationally complete;
- H1, H2, and H3 are supported;
- complete portable scientific results reproduce byte-identically;
- the study closes within four approval cycles.

### Partial result

The study is partial if setup and the gate pass and the complete matrix is valid, but one or more hypotheses are unsupported or unresolved without invalidating the remaining evidence.

### Negative setup result

The study closes before formal execution if:

- the pinned runtime or SQLite version is unavailable;
- the required wrapper or foreign-key capability is absent;
- exact explicit transaction control cannot be isolated from wrapper-generated behavior;
- the independent model cannot be made reliable;
- the hand-audited gate fails after the single permitted correction opportunity;
- safe bounded execution cannot be maintained.

### Operationally incomplete result

The study closes as incomplete if the complete matrix or reproduction cannot finish within frozen caps, source identities cannot be established, or evidence is contaminated and cannot be replaced within the four-cycle limit.

## 11. Boundaries and exclusions

The proposal does not authorize:

- activation without a later exact approval;
- a fifth cycle;
- changing expectations after protected outcomes;
- concurrency, multiple connections, locking, WAL, shared cache, busy handlers, or race experiments;
- crash, power-loss, durability, corruption, or recovery testing;
- performance or resource-exhaustion testing;
- hostile SQL, external database files, downloaded corpora, extensions, or arbitrary user input;
- filesystem or security certification;
- claims about PostgreSQL, MySQL, SQL standards generally, or SQLite versions other than the pinned engine;
- external contact, vulnerability disclosure, spending, permission changes, or third-party repository operations.

If an unexpected result suggests a security or corruption issue, preserve it internally and stop for separate human review before any external action.

## 12. Final proposal status

**Frozen and inactive.**

The next exact `承認` may perform one activation decision and, only if the live repository and environment support **GO unchanged**, Study 007 Cycle 1. Activation must stop before model implementation or protected SQL-sequence execution.
