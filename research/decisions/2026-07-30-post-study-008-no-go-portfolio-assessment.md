# Post-Study-008-NO-GO Portfolio Assessment

_Date: 2026-07-30 (Asia/Tokyo)_  
_Status: **GO to one frozen inactive proposal; no active study**_

## 1. Decision

TEMPLEX/0 should remain without an active study while preserving one frozen, inactive proposal for a possible Study 009 on **CISA KEV × FIRST EPSS temporal-horizon substitution risk**.

The selected direction asks whether using a current EPSS percentile cutoff as a substitute for a known-exploitation catalog would omit materially different portions of the official CISA KEV population, especially across vulnerability age and known-ransomware categories.

The proposal does not treat KEV and EPSS as competing ground truths. KEV records historical evidence that a vulnerability has been exploited in the wild; EPSS estimates the probability of exploitation in the next thirty days. The research object is the operational loss created when one temporal signal is used as a substitute for the other.

This cycle creates only the revised selection threshold, availability preflight, portfolio decision, and inactive proposal. It does not activate Study 009, retain or analyze the formal datasets, compute intersections or score distributions, implement statistics, open an active-study issue, or assign hypothesis dispositions.

## 2. Frozen revised selection rule

The threshold was committed before candidate research, availability preflight, scoring, or selection in:

`research/decisions/2026-07-30-post-study-008-no-go-selection-threshold.md`

Creation commit:

`26d31c57769898a6dace505707f6d8faeec656f3`

A direction depending on an indispensable external artifact is score-eligible only after an outcome-blind preflight establishes official identity, current byte accessibility, safe format, license visibility, high-level schema identity, denominator plausibility, and temporal sufficiency.

Surviving directions require at least 43 / 50, no score below 4, diversification 5, observational-validity discipline 5, execution feasibility 5, and a credible maximum-four-cycle closure.

## 3. Evidence carried forward

- Study 001 showed that reassuring aggregate behavior can conceal constructive failure.
- Study 002 showed that a proxy comparison becomes invalid when the proxy is not frozen before stronger outcomes are inspected.
- Study 003 showed that procedural integrity can be enforced without establishing substantive value.
- Study 004 showed that sophisticated methods can lose to simple baselines and that an unspecified aggregation rule must remain unresolved.
- Study 005 showed the value and cost of exact external-source pinning and independent reproduction.
- Study 006 showed that a stable authored expectation error must remain failed even when the broader result is useful.
- Study 007 showed that semantic similarity does not imply observational equivalence.
- The Study 008 activation NO-GO showed that a documented public artifact is not necessarily currently retrievable, licensable, and pinnable.

The portfolio has sufficient exact-conformance evidence. A new study should expose a real decision tradeoff using independent public signals rather than adding another implementation-versus-specification matrix.

## 4. Outcome-blind artifact-availability preflights

No candidate-specific intersections, score distributions, label rates, rankings, or protected relationships were computed during these checks.

### 4.1 CISA KEV × FIRST EPSS temporal-horizon substitution risk — PASS

#### CISA KEV

- official repository: `cisagov/kev-data`;
- inspected commit: `564b8c59f9039926e2d9548ba5b334db45cb6b50`;
- commit message: `Add Updated KEV Files for 2026-07-29`;
- required JSON path: `known_exploited_vulnerabilities.json`;
- JSON blob: `c69072a0a97b971505a34fe61f3d4936535dc39b`;
- official schema path: `known_exploited_vulnerabilities_schema.json`;
- format: UTF-8 JSON with a published JSON Schema;
- data license: CC0 1.0;
- high-level required fields: `cveID`, `dateAdded`, `knownRansomwareCampaignUse`, `vendorProject`, and catalog version metadata.

The repository states that it is maintained from the canonical CISA KEV catalog and is updated when the official catalog changes.

#### FIRST EPSS

- official historical-score repository named by FIRST: `empiricalsec/epss_scores`;
- inspected commit: `a3a6a83e55bdedc0f1398e2a9c74efa02756f6f3`;
- commit message: `Add EPSS scores for 2026-07-29`;
- required file: `2026/epss_scores-2026-07-29.csv.gz`;
- gzip CSV blob: `ee1a98246a247e350dcd6f1b19739becee07ff86`;
- safe format: gzip-compressed CSV;
- documented fields: `cve`, `epss`, and `percentile`;
- score meaning: estimated probability of exploitation in the wild in the next thirty days;
- use boundary: FIRST website terms permit copying and distribution of FIRST content for vulnerability disclosure, cybersecurity incident response, or preventative cybersecurity use. A later study must preserve notices and should publish derived aggregates and source identities rather than redistributing the raw EPSS file.

Both official artifacts are currently present at exact Git identities and use compatible CVE identifiers. Their semantic difference is documented before any values are joined: KEV is an observed-exploitation catalog, whereas EPSS is a prospective thirty-day probability signal.

Availability preflight disposition: **PASS**.

### 4.2 SciCoQA paper-code discrepancy analysis — PASS availability, HOLD research direction

The author-controlled SciCoQA release is currently available through an official project page and Hugging Face dataset repository in safe Parquet form with visible CC BY 4.0 licensing and a small finite footprint.

Availability therefore passes. The direction is not selected because a meaningful independent discrepancy detector would require long paper-and-code contexts and non-pinned model inference or an extensive authored ruleset. Passive analysis of released labels would add little beyond the released benchmark and would remain vulnerable to curator-label dependence.

### 4.3 NYC restaurant inspection grade-versus-violation composition — FAIL availability gate

The official NYC Open Data / Data.gov catalog exposes safe CSV and JSON access and a documented rolling inspection schema. However, the catalog record does not specify a dataset-specific license clearly enough to satisfy the revised license-visibility hard gate. The rolling active-establishment frame and adjudication-dependent row structure also make a frozen denominator nontrivial.

Availability preflight disposition: **FAIL; not scored**.

### 4.4 TREC Deep Learning graded-versus-binary judgment sensitivity — FAIL availability gate

Official TREC pages expose qrels as safe text files, but the bounded preflight did not identify a complete, official, currently downloadable, version-pinned archive of all submitted runs required for the proposed ranking analysis. Qrels alone cannot define the system-ranking denominator.

Availability preflight disposition: **FAIL; not scored**.

### 4.5 Repaired SummEval successor — FAIL retained

The official metric-scored annotation artifact remains unavailable, while the accessible human-only file lacks the required metric-score fields. Mirrors and recomputation remain prohibited substitutions.

Availability preflight disposition: **FAIL; not scored**.

### 4.6 Repaired SQLite successor — REJECT before scoring

Correcting the known `RESTRICT` expectation would be useful maintenance but would primarily repair a TEMPLEX/0-authored oracle and repeat the same exact state-conformance matrix. It fails the diversification and anti-repetition presumptions.

### 4.7 Inactivity

Inactivity remains the baseline and requires no artifact assumption.

## 5. Scores for preflight survivors

| Direction | Info | External | Diversifies | Beyond conformance | Falsifiable | Observation | Feasible | Stop | Reusable | Anti-confirmation | Total | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| CISA KEV × FIRST EPSS temporal-horizon substitution risk | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | **48** | **GO to frozen proposal** |
| SciCoQA paper-code discrepancy analysis | 3 | 5 | 5 | 5 | 4 | 4 | 2 | 3 | 4 | 4 | **39** | HOLD: execution and stopping floors fail |
| Inactivity | — | — | — | — | — | — | — | — | — | — | baseline | Viable fallback |

Directions failing availability preflight were not scored.

## 6. Why the CISA KEV × EPSS direction passes

### 6.1 It changes the decision object

The primary question is not exact conformance. It concerns prioritization loss when two legitimate but temporally different cybersecurity signals are treated as substitutes.

### 6.2 Both signals are externally governed

CISA decides which vulnerabilities enter KEV under its own criteria. FIRST produces EPSS from an independently governed statistical model. TEMPLEX/0 authors neither signal and cannot make the study positive by changing their contents.

### 6.3 The disagreement is interpretable without declaring one source correct

A KEV entry with low current EPSS can reflect exploitation that is real but no longer probable in the next thirty days. A high EPSS score outside KEV can reflect prospective risk without confirmed exploitation. The study therefore reports substitution loss, not model error or catalog error.

### 6.4 It is finite and safely reproducible

The two same-day source files are present at exact Git commits and safe JSON / gzip CSV paths. A later activation can freeze bytes, schemas, identifiers, inclusion rules, cutoffs, temporal bins, cluster-bootstrap rules, result schema, and resource caps before computing any overlap or distribution.

### 6.5 Negative results remain useful

The analysis may find little omission at operationally relevant EPSS cutoffs, no meaningful age gradient, no ransomware-category difference, or intervals too wide for a conclusion. Each would remain a valid bounded result if setup, gate, execution, and reproduction are sound.

## 7. Risks and controls

- **Different temporal meanings:** KEV and EPSS must never be labeled interchangeable ground truths. Every result table must restate the historical-versus-prospective distinction.
- **Current-snapshot limitation:** one same-day comparison cannot evaluate EPSS forecasting accuracy or historical detection lead time.
- **Policy thresholds:** fixed percentile cutoffs are hypothetical prioritization policies, not recommendations.
- **Security-advice risk:** the study must not provide organization-specific remediation advice, exploit instructions, or claims that a vulnerability is safe to ignore.
- **Vendor clustering:** uncertainty must cluster by the KEV `vendorProject` field rather than treating every CVE as independent.
- **Unscored CVEs:** missing EPSS records remain explicit and count as omitted under an EPSS-only policy; they may not be dropped.
- **Ransomware field semantics:** `Known` and `Unknown` are catalog labels, not proof of absence or causal attribution.
- **Source updates:** only the two pinned 2026-07-29 snapshots belong to the proposed study. Later updates cannot replace them after activation.
- **EPSS use terms:** do not redistribute the raw EPSS snapshot in TEMPLEX/0; preserve exact source identities and publish derived aggregate evidence only.

## 8. Final disposition

**GO to one frozen inactive proposal for Study 009.**

- Studies 001 through 007 remain closed.
- Study 008 remains a rejected activation candidate and was never active.
- No study is active.
- The selected proposal is not an activation decision.
- No formal source file was retained or analyzed in this cycle.
- No intersection, score distribution, percentile omission rate, bootstrap result, or hypothesis outcome was computed.
- A later exact `承認` must independently choose activation **GO unchanged** or **NO-GO** after reacquiring and hashing the exact pinned KEV and EPSS files and verifying their schemas, terms, and structural compatibility without inspecting protected results.