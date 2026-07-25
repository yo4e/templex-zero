# Post-Study-005 Portfolio Assessment

_Date: 2026-07-25 (Asia/Tokyo)_  
_Status: **GO to one frozen proposal; no active study**_

## 1. Decision

TEMPLEX/0 should remain without an active study while preserving one frozen, inactive proposal for a possible Study 006 on **Python tar extraction boundary conformance**.

The selected direction asks whether Python 3.13.5 `tarfile` extraction with the explicit `data` filter obeys its documented destination-containment, link, special-file, and metadata-sanitization boundaries across a frozen stateful fixture matrix, and whether an independent post-extraction filesystem oracle can detect every protected boundary violation without treating the filter as a general security proof.

This cycle creates the portfolio decision and frozen proposal only. It does not activate Study 006, create an active-study issue, implement an archive generator or oracle, create or extract the protected fixture corpus, inspect extraction outcomes, or run the formal experiment.

## 2. Evidence carried forward

The decision is grounded in all five closed studies.

- Study 001 showed that attractive aggregate behavior can hide short constructive failures and that a disciplined negative result is preferable to repairing a favored artifact indefinitely.
- Study 002 showed that exact structural evidence can reveal false reassurance, while also showing that instruments and comparison rules must be frozen before protected outcomes are inspected.
- Study 003 showed that machine-readable procedural contracts can reject declared forms of evidence contamination, but procedural validity cannot establish substantive truth or value.
- Study 004 showed that a plausible model-guided method can lose to a simpler random baseline and that an unfrozen aggregation rule must remain unresolved rather than be chosen after results.
- Study 005 showed that an independent parser and externally maintained referent can support a positive bounded conformance result, while also exposing source-identity, artifact self-containment, and path-portability defects inside an otherwise successful study.

The portfolio now has enough evidence that another pure conformance study must earn its place by changing the failure surface. Study 006 should not merely compare another parser with another standard. It should introduce stateful filesystem effects, partial failure, member ordering, path resolution, and version-sensitive defaults while remaining contained and auditable.

## 3. Decision standard

Each active direction was scored from 0 to 5 on seven criteria:

1. information value for TEMPLEX/0;
2. falsifiability or auditability;
3. strength of the external normative or operational referent;
4. epistemic diversification from Studies 001–005;
5. feasibility under current tool, permission, licensing, and containment limits;
6. clarity of stopping conditions;
7. likely reusable contribution.

A direction could displace inactivity only if it:

- scored at least **30 of 35**;
- had no criterion below **4**;
- had an external referent not authored by TEMPLEX/0;
- admitted a concrete negative, partial, or setup-failure result;
- could close within four approval cycles;
- could be frozen without beginning implementation or experiment execution in this cycle;
- required no external contact, terms acceptance, private data, third-party repository modification, or extraction of untrusted external archives.

Scores are explicit research judgments, not empirical measurements.

## 4. Bounded feasibility evidence

These checks establish proposal feasibility only. They are not Study 006 results.

### 4.1 Python tar extraction filters

Official Python documentation states that extraction filters were added in Python 3.12. It documents `fully_trusted`, `tar`, and `data` filters; destination and link containment checks; special-file rejection; metadata sanitization; possible partial extraction after an error; and residual risks not blocked by the built-in filters.

PEP 706 is final and specifies the filter API, default transition, error classes, partial-extraction behavior, and the need for further verification. The PEP is public domain or CC0.

The available execution environment exposed:

- CPython **3.13.5**;
- Linux **6.12.13 x86_64** with glibc **2.41**;
- `tarfile.data_filter`;
- `AbsolutePathError`, `OutsideDestinationError`, `AbsoluteLinkError`, `LinkOutsideDestinationError`, and `SpecialFileError`;
- working temporary-directory symlink creation;
- the `resource` module and `setrlimit`.

Python 3.13 is methodologically useful because omitting the filter still falls back to the older fully trusted behavior with a deprecation warning, while the explicit `data` filter is available. The proposed primary study therefore fixes `filter="data"` and treats default extraction only as a descriptive control.

Primary references inspected:

- `https://docs.python.org/3.13/library/tarfile.html`
- `https://docs.python.org/3/library/tarfile.html`
- `https://peps.python.org/pep-0706/`

### 4.2 Reproducible scientific artifact envelope

The Reproducible Builds project publishes a `SOURCE_DATE_EPOCH` specification and guidance for timestamps, archive metadata, stable input order, build paths, and output identity. The direction is feasible and directly relevant to Study 005's path-dependent complete digest.

It does not pass the portfolio floor because TEMPLEX/0 would define most of the envelope, perturbation matrix, and success contract itself. It risks becoming infrastructure engineering whose central positive result is guaranteed by construction. It remains a strong future tool-building direction, not the selected next study.

Primary references inspected:

- `https://reproducible-builds.org/specs/source-date-epoch/`
- `https://reproducible-builds.org/docs/`

### 4.3 RFC 3986 relative-reference resolution

RFC 3986 Section 5 defines a deterministic relative-reference resolution algorithm and normal and abnormal examples. Python documents that `urllib.parse.urljoin` was updated to match RFC 3986 semantics and warns about attacker-controlled absolute references.

The direction is highly feasible and auditable, but it is too close to Study 005's independent-reference-reader pattern and likely produces a small restatement of an already mature algorithm. Its reusable contribution floor is not met.

Primary references inspected:

- `https://datatracker.ietf.org/doc/html/rfc3986`
- `https://docs.python.org/3/library/urllib.parse.html`

### 4.4 Unicode UTS #46 IDNA processing

Unicode UTS #46 is a stable external specification with a versioned conformance file. It offers practical and exact outputs, including mapping and error-status behavior.

The direction fails the current feasibility floor because a meaningful independent implementation and full version-pinned conformance study would require a larger Unicode data and algorithm surface than can be responsibly frozen and completed within four cycles under the present capability evidence. Running an existing implementation against the official file alone would also have weak contribution value.

Primary reference inspected:

- `https://www.unicode.org/reports/tr46/`

## 5. Compared directions

| Direction | Info | Falsifiable | External | Diversifies | Feasible | Stop | Reusable | Total | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Python tar extraction boundary conformance | 5 | 5 | 5 | 4 | 5 | 4 | 4 | **32** | **GO to frozen proposal** |
| Reproducible scientific artifact envelope | 5 | 5 | 4 | 3 | 5 | 4 | 5 | 31 | HOLD: diversification floor fails |
| RFC 3986 relative-reference resolution | 4 | 5 | 5 | 3 | 5 | 5 | 3 | 30 | HOLD: diversification and contribution floors fail |
| Unicode UTS #46 IDNA conformance | 5 | 5 | 5 | 4 | 3 | 4 | 4 | 30 | HOLD: feasibility floor fails |
| Prospective project-selection calibration | 4 | 3 | 2 | 4 | 5 | 4 | 3 | 25 | HOLD |
| Remain inactive | — | — | — | — | — | — | — | baseline | Viable fallback |

## 6. Why the selected direction passes

### 6.1 It changes the failure surface

The referent is still external, but the primary evidence is no longer only a value comparison. Extraction mutates a filesystem over time. Member order, pre-existing nodes, links, duplicate names, error handling, and partial completion can matter. This introduces stateful and environmental failure modes not represented in the five closed studies.

### 6.2 It has a direct operational boundary

The strongest ground truth is not a self-authored semantic label. It is whether any node outside a fresh destination root changes, whether forbidden object classes are created, whether expected `FilterError` boundaries fire, and whether safe members survive with documented metadata normalization.

### 6.3 It can fail clearly

The study can close negatively or partially if:

- the explicit `data` filter permits a protected destination escape;
- a forbidden link or special file is created;
- a safe control archive is rejected or materially corrupted;
- the independent filesystem oracle cannot reliably distinguish safe in-root effects from outside-root effects;
- expectations disagree with the pinned Python documentation or PEP 706;
- complete results fail deterministic reproduction;
- the work cannot close within four cycles.

Zero protected escapes is also a valid result if bounded to the exact runtime, operating system, fixture matrix, filter, error level, and filesystem assumptions.

### 6.4 It remains contained

The proposal uses only original synthetic archives created inside disposable temporary roots. It does not download or extract untrusted third-party archives, target real paths, require elevated privileges, create external effects, or claim to test denial-of-service resistance.

### 6.5 It leaves a reusable artifact

A completed study can leave a deterministic tar-fixture generator, a manifest of path/link/member-order cases, a filesystem-diff oracle, a version-pinned extraction harness, machine-readable traces, and a bounded preflight checklist. These are useful even if the filter passes every protected case.

## 7. Why the other directions do not pass now

### Reproducible artifact envelope — HOLD

This is the strongest rejected direction and should remain available as infrastructure work. It directly addresses Study 005's non-portable path metadata and the repository's repeated artifact-transport difficulties. It does not pass as the next research study because TEMPLEX/0 would author both the envelope and most of its success conditions, making a positive result too easy to manufacture.

### RFC 3986 resolution — HOLD

The external algorithm is exact and the local API is available. The expected corpus is small, mature, and largely supplied by the RFC itself. The study would be clean but would repeat the independent-reference conformance pattern without enough new uncertainty or reusable contribution.

### UTS #46 IDNA — HOLD

The subject is practically important and externally specified, but the full data and algorithm surface is large. A shallow test-runner study would contribute little; an independent implementation study exceeds the present four-cycle feasibility evidence.

### Project-selection calibration — HOLD

Five studies now provide a richer record, but retrospective scoring would still let the same operator choose labels after outcomes. A prospective calibration ledger may be useful across future studies, but it should be infrastructure attached to later work rather than the next standalone study.

### Remaining inactive — viable baseline

Inactivity remains preferable to a study that merely copies Study 005's successful shape. The selected direction displaces inactivity because it is externally anchored, stateful, contained, falsifiable, version-sensitive, and capable of producing reusable evidence without external action.

## 8. Final disposition

**GO to one frozen proposal, created in this same portfolio cycle and kept inactive.**

- Studies 001 through 005 remain closed.
- Study 006 is proposed but not active.
- No issue, implementation, fixture archive, extraction, formal outcome, external message, third-party operation, or new publication channel is created by this decision.
- A later exact `承認` must independently inspect the frozen proposal and choose activation **GO unchanged** or **NO-GO**.
