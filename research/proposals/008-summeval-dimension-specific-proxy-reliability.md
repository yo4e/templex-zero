# Proposed Study 008 — SummEval Dimension-Specific Proxy Reliability

_Date: 2026-07-29 (Asia/Tokyo)_  
_Status: **Frozen and inactive**_

## 1. Research question

Within one pinned official SummEval release, do automatic summarization metrics that appear reliable against an aggregate human-quality score conceal dimension-specific false reassurance or expert-versus-crowd instability when coherence, consistency, fluency, and relevance remain separate?

The study tests a bounded methodological claim about one released evaluation corpus. It does not seek a new summarization metric, reconstruct source articles, generate summaries, contact annotators, or claim that human ratings are objective truth.

## 2. Why this study

Studies 001 and 002 found that reassuring aggregate rates can hide local structural failure. Study 004 showed that method rankings depend on the comparison and aggregation rule. Study 007 showed that a semantic category can collapse distinct observations and invalidate an oracle before formal execution.

Studies 002 through 007 also reveal a persistent selection bias toward exact, machine-readable, deterministic or conformance-like evidence. SummEval provides an external judgment structure that TEMPLEX/0 did not author: multiple human populations, multiple quality dimensions, released system outputs, and released automatic metric scores. The object is not exact agreement with a specification. It is whether formal proxies remain trustworthy after the distinctions in the human evidence are preserved.

## 3. External referents

Primary referents inspected before proposal freeze:

- SummEval paper: `https://aclanthology.org/2021.tacl-1.24/`
- official repository: `https://github.com/Yale-LILY/SummEval`

The official release describes 100 source documents, summaries from 16 systems, 1,600 summary records, five crowd and three expert annotations per summary, and four human-evaluation dimensions: coherence, consistency, fluency, and relevance. The repository is MIT licensed and releases annotations and automatic metric scores.

Activation must verify these statements against one exact upstream commit and one safely parseable text data file. This proposal does not authorize source-article reconstruction, CNN/DailyMail acquisition, unsafe Python serialization, model inference, or acceptance of new terms.

## 4. Activation decision

A later exact `承認` must independently choose **GO unchanged** or **NO-GO**.

GO unchanged requires all of the following:

1. one exact official upstream commit can be pinned;
2. the repository license and data-file license are clear enough for repository research use;
3. one annotation file is available as UTF-8 JSON or JSONL and can be acquired without credentials, terms acceptance, or unsafe deserialization;
4. its SHA-256 and byte length can be frozen;
5. the file contains exactly 100 document identities, 16 system identities per document, and 1,600 unique document-system records, or an official schema-equivalent representation that preserves that exact denominator;
6. expert and crowd judgments can be recovered separately for all four dimensions;
7. at least eight automatic metrics have numeric coverage for all included records and an upstream-supported score direction;
8. metric fields, human fields, identifiers, and text fields can be distinguished before any relationship, rank, or correlation is computed;
9. no protected metric-human relationship or ranking is inspected during activation;
10. the complete study remains feasible within four approval cycles.

NO-GO is mandatory if any condition fails. There is no silent substitution of a mirror, later dataset version, reconstructed source corpus, incomplete population, guessed metric direction, unsafe object file, or reduced denominator.

## 5. Exact study unit and protected denominator

The protected unit is one `(document_id, system_id)` summary record.

The expected protected denominator is exactly:

- 100 documents;
- 16 system summaries per document;
- 1,600 records;
- four human dimensions;
- two human populations, expert and crowd;
- an activation-frozen automatic metric inventory of at least 8 and at most 32 metrics.

Every document and system identity must be frozen before protected analysis. Records with missing required human judgments or eligible metric values invalidate GO unchanged; they may not be dropped after outcome inspection.

## 6. Eligible automatic metrics

Cycle 1 must freeze the exact metric list before computing any metric-human relationship.

A metric is eligible only if:

- it is present in the official pinned annotation file or an official text companion file under the same pinned commit;
- it has one numeric value for every protected record;
- it is identified by upstream documentation or code as an automatic evaluation metric rather than a human score, identifier, text field, or post-hoc composite;
- its higher-is-better or lower-is-better direction can be established from upstream material before values are analyzed;
- its values are finite.

Direction normalization is fixed as `normalized_metric = raw_metric` for higher-is-better and `-raw_metric` for lower-is-better. Ambiguous metrics are excluded before analysis and listed with reasons. Fewer than eight eligible metrics causes NO-GO.

No metric may be selected, renamed, merged, dropped, or direction-flipped after protected results are inspected.

## 7. Human judgment representation

Expert and crowd populations remain separate throughout the study.

For each record, population, and dimension, the human score is the arithmetic mean of the available individual annotations required by the frozen schema. Activation must confirm the exact annotation count representation and may not silently average populations together.

The four dimensions remain primary. A population-specific aggregate human score is also computed as the arithmetic mean of its four dimension means, but it is explicitly a **suspect proxy under test**, not a replacement for the four dimensions.

No cross-population composite is permitted.

## 8. Frozen statistical definitions

All rank calculations use average ranks for ties.

### 8.1 Summary-level association

For every eligible metric × population × human target, compute Spearman correlation across all 1,600 records for:

- each of the four dimensions;
- the population-specific aggregate score.

### 8.2 System-level association

For each metric, population, and target, average metric and human values by system across the 100 documents, then compute Spearman correlation across the 16 systems.

System-level association is mandatory secondary evidence. It cannot override a dimension-specific summary-level contradiction.

### 8.3 Document-cluster bootstrap

Uncertainty is estimated by exactly 10,000 bootstrap replicates using Python's `random.Random` with seed `2026072908`.

Each replicate samples exactly 100 document identities with replacement and includes all 16 system records for every sampled document occurrence. All primary statistics and hypothesis predicates are recomputed inside each replicate.

For a sorted list of 10,000 finite replicate values, the frozen 95% percentile interval uses the 250th and 9,750th values in one-based order. Undefined replicate statistics remain explicit and may cause an unresolved result; they are not discarded silently.

### 8.4 Metric ranks

Within each population and human target, metrics are ranked by summary-level Spearman correlation after direction normalization. Higher correlation is better. Correlation ties receive average ranks.

For `M` eligible metrics:

- aggregate top quartile means rank `<= ceil(M / 4)`;
- dimension lower half means rank `> M / 2`.

### 8.5 Document-conditioned top-quartile selection

For each document and metric, exactly four units of selection mass are assigned to the highest-scoring summaries among its 16 systems.

- scores above the fourth-place cutoff receive weight 1;
- all summaries tied at the cutoff share the remaining mass equally;
- lower scores receive weight 0.

This tie rule produces exactly 400 selected units over 100 documents for every metric.

A selected unit is a dimension-specific false-reassurance unit when its human dimension score is strictly below the within-document median for the same population and dimension. Scores equal to the median are not classified as false reassurance.

## 9. Hypotheses

### H1 — Aggregate category collapse

H1 is supported if at least one metric is in the expert aggregate top quartile but in the expert lower half for at least one individual dimension, and the same metric-dimension predicate holds in at least 9,500 of 10,000 document-bootstrap replicates.

Otherwise H1 is unsupported, unless required statistics are undefined under the frozen rules, in which case it is unresolved.

### H2 — Document-conditioned false reassurance

H2 is supported if at least one metric in the expert aggregate top quartile has a false-reassurance rate of at least 0.20 for at least one expert dimension and that rate's frozen bootstrap lower bound is greater than 0.10.

The denominator is the fixed 400 units of top-quartile selection mass per metric. No threshold may be changed after results.

Otherwise H2 is unsupported or unresolved under the same undefined-statistic rule.

### H3 — Expert-versus-crowd ranking sensitivity

For each dimension, compute Kendall tau-b between the expert and crowd rankings of eligible metrics by summary-level Spearman correlation.

H3 is supported if at least one dimension has observed Kendall tau-b below 0.70 and its frozen bootstrap upper bound is below 0.85.

Otherwise H3 is unsupported or unresolved.

The hypotheses are independent. A study with all three unsupported remains a valid completed negative scientific result if setup, instruments, execution, and reproduction are valid.

## 10. Mandatory result tables

The formal result must include, without post-result omission:

1. exact dataset, schema, population, dimension, system, and metric inventories;
2. missingness and exclusion audit performed before protected analysis;
3. every summary-level Spearman value and bootstrap interval;
4. every system-level Spearman value and bootstrap interval;
5. every metric rank for each dimension and aggregate, separately for experts and crowd;
6. every H1 candidate predicate and bootstrap stability count;
7. every H2 metric-dimension false-reassurance rate and interval;
8. every H3 dimension-specific expert-crowd Kendall tau-b and interval;
9. all undefined statistics and their causes;
10. H1–H3 dispositions and the overall operational disposition.

No best-looking metric subset or dimension subset may replace the complete tables.

## 11. Instrument independence and correctness gate

Cycle 2 must keep at least three source-separated layers:

1. parser and frozen-data projection;
2. statistical and bootstrap implementation;
3. result assembler and hypothesis evaluator.

Before protected analysis, Cycle 2 must freeze hand-audited synthetic fixtures covering:

- average ranks with ties;
- Spearman correlation including perfect, reversed, tied, and constant cases;
- Kendall tau-b with ties;
- metric direction normalization;
- four-dimension aggregate construction;
- expert/crowd separation;
- document-cluster bootstrap sampling;
- percentile interval indexing;
- fractional fourth-place tie allocation;
- within-document median classification;
- H1, H2, and H3 positive and negative predicates;
- immutable complete-table assembly.

An independently calculated fixture table must be committed before gate execution. At most one bounded implementation-correction phase is permitted. It may repair code but may not change the proposal, dataset denominator, metric inventory, directions, formulas, bootstrap seed, thresholds, or inspected fixture expectations to obtain a pass.

A failed gate closes the study as a negative setup result.

## 12. Reproducibility and identity

The portable scientific payload must exclude absolute paths, timestamps, durations, hostnames, temporary roots, memory addresses, and unordered object representations.

Cycle 3 performs one protected complete analysis. Cycle 4 reconstructs the exact committed inputs and performs one clean reproduction. Portable scientific payloads must be byte-identical.

Operational environment records remain separate and include Python version, relevant module versions, source paths, commit IDs, file hashes, instrument hashes, and platform limits.

## 13. Resource caps

- protected records: exactly 1,600;
- documents: exactly 100;
- systems per document: exactly 16;
- dimensions: exactly 4;
- populations: exactly 2;
- eligible automatic metrics: 8 through 32;
- bootstrap replicates: exactly 10,000;
- maximum decoded input size: 64 MiB;
- maximum protected result JSON size: 64 MiB;
- maximum wall time for one complete formal analysis: 180 seconds;
- no network during protected analysis;
- no model inference, GPU, subprocess evaluator, unsafe deserialization, source-article reconstruction, or external service.

Caps may not be raised after protected analysis begins.

## 14. Four-cycle plan

1. **Activation and data/specification freeze:** choose GO unchanged or NO-GO; pin upstream commit, license, exact safe text file, hashes, schema, denominator, fields, metric inventory and directions, inclusion rules, result schema, and all statistical definitions; perform schema/count/type validation only; stop before computing any metric-human association, ranking, false-reassurance rate, or hypothesis predicate.
2. **Instrument and correctness gate:** implement source-separated parser, statistics, bootstrap, and result assembly; freeze and run the complete hand-audited synthetic gate; freeze passing instruments or close negatively; stop before full-data analysis.
3. **Protected analysis:** execute the complete frozen analysis exactly once; preserve the complete result and identities; do not issue final H1–H3 dispositions beyond mechanically recorded predicates.
4. **Clean reproduction and closure:** reconstruct exact committed inputs, rerun once, compare portable payloads, analyze, assign final dispositions, write the report, close.

No fifth cycle is permitted.

## 15. Outcome classes

### Full bounded completion

- activation and safe-data checks pass;
- the hand-audited correctness gate passes within its one correction opportunity;
- the complete frozen analysis finishes under caps;
- all mandatory result tables are present;
- H1, H2, and H3 each receive supported or unsupported dispositions;
- the portable scientific payload reproduces byte-identically;
- the study closes within four cycles.

Full bounded completion does not require any hypothesis to be supported.

### Partial result

The study is partial if setup and the gate pass and the complete analysis is valid, but one or more hypotheses remain unresolved without invalidating the remaining evidence.

### Negative setup result

The study closes before protected analysis if exact source identity, license, safe text parsing, denominator, population separation, metric inventory, direction metadata, observation validity, resource safety, or the correctness gate fails.

### Operationally incomplete result

The study closes as incomplete if the protected analysis or reproduction cannot finish under frozen caps, source identities cannot be maintained, or evidence is contaminated and cannot be replaced within the four-cycle limit.

## 16. Boundaries and exclusions

The proposal does not authorize or support claims about:

- summarization metrics generally;
- modern LLM summarizers or domains outside the pinned SummEval release;
- causal validity or superiority of any metric;
- human judgment as objective truth;
- correctness of the underlying summaries or source articles;
- annotator identity, demographic representativeness, or annotation-process fairness;
- reconstruction or redistribution of CNN/DailyMail source articles;
- new human-subject research;
- model training, inference, prompting, or external APIs;
- leaderboard publication, external submission, or contact with dataset authors;
- unsafe pickle or arbitrary-code execution;
- security, production readiness, or policy recommendations.

Known related literature means this study must not claim novelty for the general observation that automatic metrics and human judgments can disagree. Its bounded contribution is a frozen, reproducible audit of category collapse, document-conditioned false reassurance, and population sensitivity under one exact public release.

## 17. Final proposal status

**Frozen and inactive.**

The next exact `承認` may perform one activation decision and, only after **GO unchanged**, Study 008 Cycle 1. Activation and Cycle 1 must stop before statistic implementation, metric-human association, metric ranking, false-reassurance analysis, bootstrap outcome inspection, or hypothesis evaluation.