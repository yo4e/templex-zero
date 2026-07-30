# Proposed Study 009 — KEV × EPSS Temporal-Horizon Substitution Risk

_Date: 2026-07-30 (Asia/Tokyo)_  
_Status: **Frozen and inactive**_

## 1. Research question

Within exact same-day official CISA KEV and FIRST EPSS snapshots, how much of the known-exploited-vulnerability population would be omitted by hypothetical EPSS-percentile prioritization cutoffs, and does that omission vary by time since KEV addition or by the catalog's known-ransomware label?

The study does not ask whether CISA KEV or FIRST EPSS is correct. KEV records historical evidence of exploitation in the wild. EPSS estimates the probability of exploitation in the next thirty days. The study tests the loss created when a prospective probability signal is used as a substitute for a historical confirmed-exploitation signal.

It does not provide remediation advice, exploit instructions, organization-specific prioritization, or a claim that any vulnerability is safe to ignore.

## 2. Why this study

Studies 001 and 002 showed that reassuring aggregates can hide important local failures. Studies 004–007 accumulated substantial exact-conformance evidence and also exposed aggregation, expectation, and observation-boundary defects. The rejected Study 008 activation showed that external-artifact availability must be verified before feasibility is trusted.

This proposal changes the evidence and decision object. Its primary evidence consists of two independently governed public cybersecurity signals with different temporal meanings. The analysis remains quantitative and auditable, but it is about substitution, tradeoffs, uncertainty, and population stratification rather than implementation conformance.

## 3. Frozen external referents

### 3.1 CISA Known Exploited Vulnerabilities catalog

- official repository: `cisagov/kev-data`;
- pinned commit: `564b8c59f9039926e2d9548ba5b334db45cb6b50`;
- commit message: `Add Updated KEV Files for 2026-07-29`;
- required path: `known_exploited_vulnerabilities.json`;
- Git blob: `c69072a0a97b971505a34fe61f3d4936535dc39b`;
- schema path: `known_exploited_vulnerabilities_schema.json` at the same commit;
- license: CC0 1.0;
- snapshot date: 2026-07-29.

### 3.2 FIRST Exploit Prediction Scoring System

- official historical-score repository named by FIRST: `empiricalsec/epss_scores`;
- pinned commit: `a3a6a83e55bdedc0f1398e2a9c74efa02756f6f3`;
- commit message: `Add EPSS scores for 2026-07-29`;
- required path: `2026/epss_scores-2026-07-29.csv.gz`;
- Git blob: `ee1a98246a247e350dcd6f1b19739becee07ff86`;
- format: gzip-compressed CSV;
- documented fields: `cve`, `epss`, and `percentile`;
- snapshot date: 2026-07-29.

FIRST describes EPSS as the probability that a software vulnerability will be exploited in the wild in the thirty days following score publication. FIRST website terms permit copying and distribution of FIRST content for vulnerability disclosure, cybersecurity incident response, or preventative cybersecurity use. This study is limited to preventative cybersecurity research, preserves source attribution, and does not redistribute the raw EPSS file in TEMPLEX/0.

The proposal does not authorize later source snapshots, API substitutes, mirrors, reconstructed values, or model inference.

## 4. Activation decision

A later exact `承認` must independently choose **GO unchanged** or **NO-GO**.

GO unchanged requires all of the following:

1. both repositories and exact commits remain accessible from official locations;
2. both required paths resolve to the frozen Git blobs;
3. the exact decoded source bytes can be acquired without credentials, payment, new terms acceptance, unsafe deserialization, or a third-party mirror;
4. SHA-256, byte length, content encoding, and safe-parser behavior can be frozen for both files;
5. the CISA CC0 license and the applicable FIRST content-use terms remain visible and compatible with the bounded research and derived-output plan;
6. the KEV JSON validates against the same-commit official schema or a precisely recorded upstream schema defect is found before any join;
7. every KEV record has a unique syntactically valid `cveID`, parseable `dateAdded`, nonempty `vendorProject`, and `knownRansomwareCampaignUse` value in the exact allowed inventory frozen during activation;
8. the EPSS CSV has unique syntactically valid CVE identifiers, finite `epss` and `percentile` values in `[0,1]`, and a source-header model version and score date consistent with 2026-07-29;
9. the exact KEV denominator, vendor inventory, ransomware-label inventory, EPSS record count, duplicate counts, and KEV-to-EPSS missingness count can be frozen structurally without computing score distributions, cutoff omission rates, age gradients, ransomware differences, or hypothesis predicates;
10. all KEV records remain in the protected denominator whether or not an EPSS row exists;
11. the complete study remains feasible within four approval cycles and the frozen resource caps.

NO-GO is mandatory if any condition fails. There is no silent substitution of another date, API response, mirror, reduced KEV denominator, repaired identifier, guessed label, recomputed score, or redistributed raw EPSS snapshot.

## 5. Exact study population and join

The protected population is every vulnerability record in the pinned 2026-07-29 CISA KEV JSON.

Activation freezes the exact KEV top-level count and the ordered inventory of `cveID` values. That complete count is the denominator for every overall omission rate.

The EPSS join key is exact uppercase CVE identifier after syntax validation. Case normalization is permitted only if the original values are ASCII case variants of the same syntactically valid CVE identifier and the normalization rule is frozen before the join. No fuzzy matching, aliasing, typo repair, or manual replacement is permitted.

For every KEV record:

- exactly one matching EPSS row supplies `epss` and `percentile`;
- zero matching EPSS rows produces the explicit status `unscored`;
- more than one matching EPSS row invalidates activation.

Unscored KEV records remain in every denominator and are treated as omitted by every EPSS-only cutoff policy. They are never dropped or assigned zero as if zero were an observed EPSS probability.

## 6. Frozen field projection

Only the following source fields enter the scientific projection:

### KEV

- `cveID`;
- `dateAdded`;
- `vendorProject`;
- `knownRansomwareCampaignUse`.

### EPSS

- `cve`;
- `epss`;
- `percentile`.

Descriptions, product names, vulnerability names, remediation text, due dates, third-party URLs, CWE values, notes, and exploit details are excluded from the protected scientific payload.

## 7. Temporal and category definitions

The fixed snapshot date is `2026-07-29`.

For each KEV record:

`age_days = snapshot_date - dateAdded`

The frozen age bins are:

- `recent_90`: 0 through 90 days inclusive;
- `year_1`: 91 through 365 days inclusive;
- `year_2`: 366 through 730 days inclusive;
- `older_730`: more than 730 days.

Negative age is invalid and causes setup failure.

The exact inventory of `knownRansomwareCampaignUse` values must be frozen during activation. The proposal expects `Known` and `Unknown`. Any additional, missing, or differently spelled value causes NO-GO unchanged rather than post-hoc recoding.

`vendorProject` is used only as the uncertainty cluster identifier. It is not interpreted as a legal entity, vendor-quality measure, or causal factor.

## 8. Hypothetical EPSS-only prioritization policies

The complete frozen percentile cutoff inventory is:

`0.50, 0.75, 0.90, 0.95, 0.99`

For a scored KEV record and cutoff `p`:

- `retained` if `percentile >= p`;
- `omitted` if `percentile < p`.

Every unscored KEV record is `omitted` at every cutoff.

For any population subset `S`:

`omission_rate(S, p) = omitted_count(S, p) / |S|`

The cutoff `0.90` is the primary hypothesis cutoff. All five cutoffs remain mandatory complete secondary evidence. Cutoffs are hypothetical resource-allocation policies for methodological analysis, not recommendations.

## 9. Frozen uncertainty method

All confidence intervals and hypothesis stability checks use exactly 10,000 nonparametric cluster-bootstrap replicates with Python `random.Random` seed `2026073009`.

The cluster unit is the exact `vendorProject` string.

For each replicate:

1. sample the activation-frozen number of unique vendor clusters with replacement;
2. for each sampled cluster occurrence, include every KEV record belonging to that cluster;
3. duplicated sampled clusters contribute duplicated records and weights for that replicate;
4. recompute all required rates and differences from the replicated population.

For 10,000 finite replicate values sorted ascending, the frozen 95% percentile interval uses the 250th and 9,750th values in one-based order.

Undefined stratum statistics remain explicit. Replicates with an undefined required difference are counted and reported, not silently discarded. If more than 500 replicates are undefined for a hypothesis statistic, that hypothesis is unresolved.

A secondary CVE-level bootstrap may be reported only as a labeled sensitivity analysis and cannot replace the vendor-cluster result.

## 10. Hypotheses

### H1 — Overall substitution loss

At the `0.90` EPSS percentile cutoff, at least 20% of the complete KEV population is omitted, and the frozen vendor-cluster bootstrap lower bound for the omission rate is greater than 15%.

- supported if both conditions hold;
- unsupported if both required statistics are defined and either condition fails;
- unresolved under the frozen undefined-statistic rule.

### H2 — Age-conditioned substitution loss

At cutoff `0.90`, the omission rate in `older_730` exceeds the omission rate in `recent_90` by at least 20 percentage points, and the bootstrap lower bound for that difference is greater than 10 percentage points.

- supported if both conditions hold;
- unsupported if both strata exist, required statistics are defined, and either condition fails;
- unresolved if either stratum is empty or the undefined-statistic rule is triggered.

### H3 — Ransomware-label sensitivity

At cutoff `0.90`, the omission rate for `Unknown` exceeds the omission rate for `Known` by at least 10 percentage points, and the bootstrap lower bound for that difference is greater than 5 percentage points.

- supported if both conditions hold;
- unsupported if both categories exist, required statistics are defined, and either condition fails;
- unresolved if the frozen category inventory is not exactly the expected two values or the undefined-statistic rule is triggered.

The hypotheses are independent. A study with all three unsupported remains a valid completed negative scientific result if setup, gate, analysis, and reproduction are valid.

## 11. Mandatory complete evidence

The formal result must include, without selective omission:

1. exact source commits, paths, Git blobs, SHA-256 values, byte lengths, licenses or terms, headers, schemas, and parser identities;
2. exact KEV count, EPSS count, duplicate audit, join coverage, and unscored KEV count;
3. complete age-bin, ransomware-label, and vendor-cluster inventories with counts;
4. overall retained and omitted counts and rates at all five cutoffs;
5. retained and omitted counts and rates by all four age bins at all five cutoffs;
6. retained and omitted counts and rates by both ransomware labels at all five cutoffs;
7. vendor-cluster bootstrap intervals for every mandatory rate and difference;
8. all undefined statistics and undefined-replicate counts;
9. H1–H3 observed predicates, intervals, and dispositions;
10. a source-semantics notice restating that KEV and EPSS measure different temporal facts;
11. an explicit statement that the cutoffs are hypothetical and not remediation advice.

No best-looking cutoff, age bin, ransomware category, vendor subset, or scored-only denominator may replace the complete tables.

## 12. Instrument independence and correctness gate

Cycle 2 must maintain at least three source-separated layers:

1. safe source parsers and frozen field projection;
2. join, classification, and bootstrap statistics;
3. complete-table assembler and hypothesis evaluator.

Before protected analysis, Cycle 2 must freeze independently hand-calculated synthetic fixtures covering:

- unique and duplicate CVE joins;
- explicit unscored retention in denominators;
- exact cutoff boundary equality;
- all age-bin boundaries;
- unexpected ransomware labels;
- vendor-cluster resampling with unequal cluster sizes and duplicate sampled clusters;
- percentile interval indexing;
- overall, age-difference, and ransomware-difference calculations;
- positive, negative, and unresolved H1–H3 predicates;
- immutable complete-table assembly;
- exclusion of non-projected source fields.

Fixture expectations must be committed before gate execution. At most one bounded implementation-correction phase is permitted. It may repair code but may not change this proposal, source identities, denominator, projected fields, cutoffs, bins, cluster unit, bootstrap seed, thresholds, or inspected fixture expectations to obtain a pass.

A failed gate closes the study as a negative setup result.

## 13. Reproducibility and publication boundary

The raw CISA and EPSS files are reacquired from their exact official Git commits for each authorized execution. TEMPLEX/0 does not commit or redistribute the raw EPSS snapshot.

The portable scientific payload contains only:

- source identities and hashes;
- structural counts and inventories;
- aggregate rates, differences, intervals, and hypothesis predicates;
- explicit missing CVE identifiers only if needed to audit join coverage;
- no vulnerability descriptions, exploit details, remediation text, or third-party URLs.

Absolute paths, timestamps, durations, hostnames, temporary roots, memory addresses, and unordered object representations are excluded from the portable payload.

Cycle 3 performs one protected complete analysis. Cycle 4 reacquires the exact sources, reconstructs the exact committed instruments, and performs one clean reproduction. Portable scientific payloads must be byte-identical.

## 14. Resource caps

- CISA source files: exactly one JSON and its same-commit schema;
- EPSS source files: exactly one gzip CSV;
- source snapshot date: exactly 2026-07-29;
- maximum combined decoded input: 256 MiB;
- maximum KEV records: 10,000;
- maximum EPSS records: 1,000,000;
- percentile cutoffs: exactly 5;
- age bins: exactly 4;
- ransomware categories: exactly 2 expected;
- bootstrap replicates: exactly 10,000;
- maximum portable result JSON: 32 MiB;
- maximum wall time for one complete analysis: 180 seconds;
- no network during statistical computation after exact source acquisition;
- no model inference, GPU, subprocess evaluator, unsafe deserialization, exploit execution, source crawling, or external service.

Caps may not be raised after protected analysis begins.

## 15. Four-cycle plan

1. **Activation and source/specification freeze:** choose GO unchanged or NO-GO; reacquire exact source blobs; freeze SHA-256, byte lengths, licenses or terms, parsers, schemas, exact denominators, inventories, join rules, cutoffs, bins, formulas, seed, mandatory tables, result schema, and caps; perform structure, type, duplicate, and missingness validation only; stop before computing cutoff counts, distributions, rates, differences, bootstrap outcomes, or hypothesis predicates.
2. **Instrument and correctness gate:** implement source-separated parser, join/classification, bootstrap, table assembly, and hypothesis evaluation; freeze and execute the hand-audited synthetic gate; freeze passing instruments or close negatively; stop before formal source analysis.
3. **Protected analysis:** execute the complete frozen analysis exactly once; preserve the complete result and identities; do not issue narrative final conclusions beyond mechanically recorded predicates.
4. **Clean reproduction and closure:** reacquire exact source blobs, reconstruct exact committed instruments, rerun once, compare portable payloads, interpret bounded results, assign final dispositions, write the report, and close.

No fifth cycle is permitted.

## 16. Outcome classes

### Full bounded completion

- activation checks pass;
- the synthetic correctness gate passes within one correction opportunity;
- the complete frozen analysis finishes under caps;
- every mandatory table and notice is present;
- H1, H2, and H3 each receive supported or unsupported dispositions;
- the portable scientific payload reproduces byte-identically;
- closure occurs within four cycles.

Full bounded completion does not require any hypothesis to be supported.

### Partial result

The study is partial if setup and gate pass and the complete analysis is valid, but one or more hypotheses remain unresolved without invalidating the remaining evidence.

### Negative setup result

The study closes before protected analysis if source identity, byte accessibility, license or terms, safe parsing, schema validity, denominator integrity, category inventory, join uniqueness, observation validity, resource safety, or the correctness gate fails.

### Operationally incomplete result

The study closes as incomplete if analysis or reproduction cannot finish under frozen caps, exact source identities cannot be maintained, the official blobs become inaccessible, or evidence is contaminated and cannot be replaced within four cycles.

## 17. Boundaries and exclusions

The proposal does not authorize or support claims about:

- EPSS forecasting accuracy;
- CISA catalog completeness or error rates;
- causation between EPSS, KEV age, and ransomware activity;
- future vulnerabilities or snapshots after 2026-07-29;
- organization-specific vulnerability exposure or asset criticality;
- remediation deadlines or patch ordering;
- the safety of omitting any vulnerability;
- exploitability in a particular environment;
- vulnerability exploitation techniques;
- production security policy, compliance, or professional advice;
- model training, external APIs, or contact with CISA, FIRST, vendors, or researchers;
- redistribution of the raw EPSS source file;
- publication through a new channel.

The bounded contribution is a reproducible analysis of substitution loss between two temporally distinct public signals under one exact pair of official snapshots.

## 18. Final proposal status

**Frozen and inactive.**

The next exact `承認` may perform one activation decision and, only after **GO unchanged**, Study 009 Cycle 1 source/data/specification freeze. Activation and Cycle 1 must stop before cutoff classification, omission-rate computation, age or ransomware comparison, bootstrap outcome inspection, or H1–H3 evaluation.