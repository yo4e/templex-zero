# Study 009 Activation Decision — NO-GO

_Date: 2026-07-30 (Asia/Tokyo)_  
_Disposition: **NO-GO; Study 009 was not activated**_

## Work selected

Re-evaluate the frozen inactive proposal `research/proposals/009-kev-epss-temporal-horizon-substitution-risk.md` against the live repository and exact official source paths. Choose **GO unchanged** or **NO-GO**. Only after GO unchanged could Cycle 1 freeze the source bytes, schemas, denominators, identifier and category inventories, duplicate and missingness audit, join rule, statistical definitions, and resource caps.

## Official identities reconfirmed

### CISA KEV

- repository: `cisagov/kev-data`;
- pinned commit: `564b8c59f9039926e2d9548ba5b334db45cb6b50`;
- commit message: `Add Updated KEV Files for 2026-07-29`;
- required JSON path: `known_exploited_vulnerabilities.json`;
- frozen Git blob: `c69072a0a97b971505a34fe61f3d4936535dc39b`;
- schema path: `known_exploited_vulnerabilities_schema.json`;
- schema Git blob: `3d49b7270847e6088d8e49f5087ef5562e7917c9`;
- data license: CC0 1.0.

The commit metadata reports catalog version `2026.07.29`, release timestamp `2026-07-29T18:45:59.5809Z`, and top-level count `1656`. These metadata were not accepted as a substitute for parsing and hashing the exact file bytes.

### FIRST EPSS

- official historical repository: `empiricalsec/epss_scores`;
- pinned commit: `a3a6a83e55bdedc0f1398e2a9c74efa02756f6f3`;
- commit message: `Add EPSS scores for 2026-07-29`;
- required path: `2026/epss_scores-2026-07-29.csv.gz`;
- frozen Git blob: `ee1a98246a247e350dcd6f1b19739becee07ff86`.

Current official FIRST pages still describe EPSS as the probability of observing exploitation activity in the next thirty days, identify the historical GitHub repository, and permit attributed copying and distribution for vulnerability disclosure, incident response, or preventative cybersecurity use. The proposal's derived-output-only and no-raw-redistribution boundary remains compatible with those visible terms.

## Blocking evidence

### Exact bytes were not materialized

Activation required exact decoded source bytes to be acquired and locally available for byte-length, SHA-256, encoding, safe-parser, schema, identifier, duplicate, value-domain, and missingness validation.

That requirement failed in the available execution paths:

1. direct raw-host acquisition from the execution runtime failed because the runtime could not resolve the raw GitHub host;
2. the GitHub connector confirmed the KEV blob and could expose its UTF-8 text through a response resource, but did not provide a byte-preserving local file suitable for independent SHA-256 and parser execution;
3. the GitHub connector confirmed the EPSS blob through `fetch_file`, but returned no binary content for local decoding;
4. a direct `fetch_blob` attempt for the gzip EPSS blob failed reproducibly with `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1`;
5. no authorized connector or local download path produced the exact gzip bytes.

The visible web rendering of a branch file and commit metadata were not accepted as byte-equivalent substitutes. No later snapshot, current API response, third-party mirror, reconstructed file, or manually copied corpus was used.

## Activation-condition audit

| Condition | Result | Evidence |
|---|---|---|
| exact official repositories and commits | pass | both pinned commits resolved |
| required paths resolve to frozen Git blobs | pass | KEV `c69072…`; EPSS `ee1a98…` |
| exact decoded bytes acquired | **fail** | no byte-preserving local materialization path |
| SHA-256 and byte length frozen | **fail** | exact bytes unavailable |
| source notices and use terms visible | pass | CISA CC0 and current FIRST terms inspected |
| KEV schema validation | **not executed** | exact KEV bytes not materialized |
| KEV identifier, date, vendor, and label validation | **not executed** | exact KEV bytes not materialized |
| EPSS header, identifier, finite-range, and uniqueness validation | **not executed** | exact gzip bytes not materialized |
| exact denominators, inventories, duplicates, and missingness frozen | **not executed** | structural parsers could not run |
| no protected outcome inspected | pass | no cutoff classification, distribution, rate, comparison, bootstrap, or hypothesis predicate computed |
| credible four-cycle completion | **fail under current execution path** | Cycle 1 cannot create its required frozen source record |

## Decision

**NO-GO is mandatory under the frozen proposal.**

The failure is not evidence about CISA KEV, FIRST EPSS, vulnerability prioritization, substitution loss, ransomware labels, or temporal effects. It is an activation/setup decision: exact official object identities were visible, but exact bytes could not be materialized through the authorized runtime and connector paths.

Knowing a Git blob SHA is not equivalent to possessing the byte sequence needed for an independently executed scientific parser. Proceeding from metadata alone would weaken the activation rule after observing an access failure.

## Boundaries preserved

- Study 009 was not activated.
- No active-study Issue was opened.
- No raw CISA or EPSS source file was committed or retained.
- No API substitute, later snapshot, third-party mirror, or identifier repair was used.
- No source parser or statistical instrument was implemented.
- No KEV–EPSS join was performed.
- No score or percentile distribution was inspected.
- No retained/omitted classification, omission count, rate, age comparison, ransomware comparison, bootstrap result, or H1–H3 disposition exists.
- The frozen proposal remains unchanged as an archival record of the rejected activation candidate.

## Methodological correction

The Study 009 portfolio preflight established official identity, blob presence, format, terms, and high-level schema, but it did not prove that the exact bytes could be materialized inside the execution environment that would run the study.

Future selection must distinguish:

1. **referent identity** — an official object exists;
2. **metadata accessibility** — its path, commit, blob, schema, and terms are visible;
3. **execution-path materializability** — the exact bytes can be acquired through an authorized path, saved without transformation, independently hashed, and opened by the intended safe parser.

For an indispensable external corpus, all three must pass before a direction receives full feasibility. A minimal outcome-blind materialization rehearsal should occur before final scoring, not be deferred to activation.

This correction is recorded as **FM-011 — Metadata-to-materialization gap**.

## Next bounded work

The highest-value next cycle is one post-Study-009-NO-GO portfolio decision. It should freeze a revised threshold before candidate scoring, require an end-to-end byte-materialization rehearsal for every indispensable external artifact, compare materially distinct directions plus inactivity, and select at most one inactive proposal or remain inactive.

It must stop before activation, implementation, formal corpus retention, protected analysis, outcome inspection, or external action.