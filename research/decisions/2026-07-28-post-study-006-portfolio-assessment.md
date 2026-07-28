# Post-Study-006 Portfolio Assessment

_Date: 2026-07-28 (Asia/Tokyo)_  
_Status: **GO to one frozen inactive proposal; no active study**_

## 1. Decision

TEMPLEX/0 should remain without an active study while preserving one frozen, inactive proposal for a possible Study 007 on **SQLite deferred-constraint and savepoint state conformance**.

The selected direction asks whether the pinned SQLite engine available through CPython's `sqlite3` module follows its documented transaction-stack, nested-savepoint, failed-boundary, and deferred-foreign-key semantics across a frozen sequence matrix, when compared with an independently implemented relational and savepoint-state model.

This cycle creates only the portfolio decision and proposal. It does not activate Study 007, create an active-study issue, implement the model or harness, generate the formal sequence corpus, execute protected SQL sequences, inspect protected outcomes, or assign hypothesis dispositions.

## 2. Evidence carried forward from Studies 001–006

- **Study 001:** aggregate random behavior can hide short constructive failures; an authored artifact must be discarded when stronger evidence defeats it.
- **Study 002:** exact structural evidence can expose false reassurance, but instruments and comparison rules must be frozen before protected outcomes.
- **Study 003:** a machine-readable process contract can enforce declared dependencies, but procedural consistency cannot establish substantive value or truth.
- **Study 004:** an elaborate guided method can lose to a simple random baseline; an underspecified aggregation rule must remain unresolved.
- **Study 005:** an external referent and independent parser can support a positive bounded result, while source identity and path portability can still fail.
- **Study 006:** a stateful boundary study can support strong containment claims while retaining a reproducible study-authored expectation error; explanation must not erase failure.

The portfolio also reveals a real selection bias. After the first game-design study, five consecutive studies favored exact, machine-readable, formally bounded domains. This is now observed behavior rather than merely a suspected failure mode. The next study must therefore justify its formalism by introducing a new operational state model and a meaningful chance of contradicting TEMPLEX/0's expectations, not merely by supplying another large conformance count.

## 3. Frozen selection rule

The threshold was committed before candidate scoring in:

`research/decisions/2026-07-28-post-study-006-selection-threshold.md`

Creation commit:

`9e924b2de72254437afd1ae1008e2ebac82cd77c`

A direction requires at least 34 / 40, no score below 4, a non-self-authored external referent, material diversification, a credible negative or partial result, four-cycle closure, and no external or unsafe authority requirement.

## 4. Current feasibility observations

These observations establish proposal feasibility only. They are not protected Study 007 results.

### 4.1 SQLite transaction-state direction

The current execution environment exposes:

- CPython 3.13.5 at `/usr/bin/python3`;
- SQLite 3.46.1 through the standard-library `sqlite3` module;
- SQLite source ID for release 3.46.1 as published by SQLite;
- foreign-key support in the compiled library;
- explicit connection-level foreign-key activation;
- named and nested `SAVEPOINT`, `RELEASE`, and `ROLLBACK TO` statements;
- in-memory and disposable file-backed databases;
- Python 3.13's explicit `autocommit` connection parameter.

Official SQLite documentation specifies that savepoints form a stack, names need not be unique, `ROLLBACK TO` preserves the matched savepoint while canceling intervening ones, inner `RELEASE` merges work into its parent, and outermost `RELEASE` commits. The foreign-key documentation distinguishes immediate and deferred constraints, states that failed `COMMIT` leaves the transaction open, allows nested savepoint release during a deferred violation, applies commit restrictions to a transaction savepoint, and states that nested savepoints remain open after a failed outer boundary.

Primary referents inspected:

- `https://www.sqlite.org/lang_savepoint.html`
- `https://www.sqlite.org/foreignkeys.html`
- `https://sqlite.org/releaselog/3_46_1.html`
- `https://docs.python.org/3.13/library/sqlite3.html`

The proposed study can use only original bounded schemas and statement sequences in disposable databases. It needs no external dataset, concurrency, network, untrusted SQL, extension loading, or third-party system.

### 4.2 Unicode 17 extended grapheme segmentation

Unicode 17.0 supplies a stable UAX #29 specification, versioned property files, and a 124 KiB `GraphemeBreakTest.txt` conformance corpus. The direction is externally anchored and useful.

It fails the current feasibility floor because the available Python runtime embeds Unicode 15.1 data, while a genuine Unicode 17 implementation requires separately freezing several Unicode 17 property datasets, emoji properties, and Indic conjunct behavior. A shallow runner over the official expected-output file would add little; a credible independent implementation is too large for the current four-cycle evidence.

Primary referents inspected:

- `https://www.unicode.org/reports/tr29/`
- `https://www.unicode.org/Public/17.0.0/ucd/auxiliary/`
- `https://unicode.org/versions/Unicode17.0.0/`

### 4.3 RFC 8785 JSON canonicalization

RFC 8785 defines deterministic property ordering, UTF-8 output, I-JSON restrictions, and ECMAScript-compatible primitive serialization. Node.js 22.16.0 is available as an operational number-serialization referent.

The direction is feasible and reusable but fails the diversification floor. Its central object is canonical artifact identity, too close to the path and transport identity problems already central to Studies 003, 005, and 006. The verified errata concerning negative zero also make a careful implementation worthwhile, but not the strongest next study.

Primary referents inspected:

- `https://www.rfc-editor.org/rfc/rfc8785.html`
- `https://www.rfc-editor.org/errata/rfc8785`

### 4.4 Reproducible scientific artifact envelope

The Reproducible Builds project supplies the `SOURCE_DATE_EPOCH` specification and documented variance sources including timestamps, locale, timezone, archive metadata, stable ordering, and build paths. This direction directly addresses repeated TEMPLEX/0 transport and path-portability defects.

It again fails the diversification and self-confirmation floors. TEMPLEX/0 would define most of the envelope, artifact grammar, and success criteria. A positive result could be produced largely by construction. This remains worthwhile internal infrastructure but not the next standalone research study.

Primary referents inspected:

- `https://reproducible-builds.org/specs/source-date-epoch/`
- `https://reproducible-builds.org/docs/`

### 4.5 Prospective project-selection calibration

A prospective scoring ledger could eventually test whether pre-study predictions correlate with later value, validity, and completion. Six closed studies provide some history.

It fails the external-referent and self-confirmation floors. The same operator would still define the labels, select the studies, and evaluate the outcomes. It should be attached to future portfolio decisions rather than treated as a standalone study.

## 5. Candidate scores

| Direction | Info | Falsifiable | External | Diversifies | Feasible | Stop | Reusable | Anti-confirmation | Total | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SQLite deferred constraints and savepoint state | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | **39** | **GO to frozen proposal** |
| Unicode 17 grapheme segmentation | 4 | 5 | 5 | 4 | 3 | 4 | 4 | 4 | 33 | HOLD: feasibility floor fails |
| RFC 8785 JSON canonicalization | 4 | 5 | 5 | 3 | 4 | 5 | 4 | 4 | 34 | HOLD: diversification floor fails |
| Reproducible artifact envelope | 5 | 5 | 4 | 3 | 5 | 4 | 5 | 3 | 34 | HOLD: diversification and anti-confirmation floors fail |
| Prospective selection calibration | 4 | 3 | 2 | 4 | 5 | 4 | 4 | 2 | 28 | HOLD |
| Remain inactive | — | — | — | — | — | — | — | — | baseline | Viable fallback |

## 6. Why SQLite passes

### 6.1 It introduces a different state model

The core object is neither a static parser output nor a filesystem containment boundary. It is a reversible transactional history with a named stack, logical row state, constraint-validity state, failed commit boundaries, and recoverable intermediate states.

### 6.2 It has externally specified counterintuitive behavior

The documentation explicitly distinguishes:

- inner versus transaction savepoints;
- `ROLLBACK` versus `ROLLBACK TO`;
- nested savepoint release versus outer boundary commit;
- immediate versus deferred constraint checking;
- failed commit with the transaction still open;
- nested savepoints remaining available after a failed outer boundary;
- `RESTRICT` action timing even when the constraint is deferred.

These interactions create a meaningful opportunity for model defects, wrapper assumptions, or undocumented expectation errors.

### 6.3 It can be falsified cleanly

The study can close negatively or partially if:

- the independent model disagrees with hand-audited fixtures;
- a frozen sequence produces a different error boundary, stack effect, row state, or foreign-key state;
- the Python wrapper changes explicit transaction behavior despite a pinned configuration;
- failed-boundary recovery cannot be observed independently;
- the complete result does not reproduce;
- the study cannot close within four cycles.

### 6.4 It remains contained

All SQL, schemas, and values can be original, bounded, and executed only in memory or under disposable repository-independent temporary roots. The study excludes concurrency, locks, crashes, durability claims, hostile SQL, extensions, arbitrary databases, performance, and external services.

### 6.5 It leaves reusable artifacts

A completed study can leave:

- a declarative transaction-sequence grammar;
- a finite relational/savepoint-stack model;
- a deterministic SQLite sequence generator;
- a state and error projection harness;
- hand-audited transaction fixtures;
- a version-pinned regression corpus for deferred constraints and nested savepoints.

## 7. Risks and controls

- **Formalization bias:** the selected study remains formal. The control is to require an operationally stateful failure surface and to state that SQLite conformance is not equivalent to broader importance.
- **Self-authored oracle agreement:** the model and harness must be independently structured, with manually frozen fixtures and source-level separation.
- **Wrapper ambiguity:** activation must pin Python transaction control explicitly and record the exact SQLite source ID and compile options.
- **Combinatorial growth:** the formal grammar must cap stack depth, statements, rows, sequence count, and execution time before outcome inspection.
- **False security framing:** the study concerns transaction semantics, not database security, durability, crash safety, or SQL injection.
- **Documentation drift:** activation must freeze retrieval dates and relevant documentation/source identities; no silent migration to a newer SQLite engine is allowed.

## 8. Final disposition

**GO to one frozen inactive proposal for Study 007.**

- Studies 001 through 006 remain closed.
- No study is active.
- The selected proposal is not an activation decision.
- No issue, implementation, formal sequence corpus, database experiment, protected result, or external communication is created in this cycle.
- A later exact `承認` must re-read the live proposal and independently choose activation **GO unchanged** or **NO-GO**.
