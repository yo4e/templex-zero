# Next Start

_Updated: 2026-07-17 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not authorization and is not the source of truth. Re-read `STATE.md`, the Study 002 protocol, exact and random analyses, Issue #6, and live commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report it in the same project chat, and stop.

## Identity and execution

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Familiar and historical name: **Monday**
- Repository: `https://github.com/yo4e/templex-zero`
- External communication, publication, spending, permissions, human-subject activity, and third-party actions remain separately gated.

## Current position

**Study 002 is active. Random comparison cycle 5 of at most 6 is complete.**

Artifacts:

- active protocol: `research/studies/002-exact-first-screening/PROTOCOL.md`
- frozen manifest: `research/studies/002-exact-first-screening/manifest/`
- exact data: `research/studies/002-exact-first-screening/data/exact_screen_v1.json`
- exact analysis: `research/studies/002-exact-first-screening/EXACT_SCREEN_ANALYSIS.md`
- random data: `research/studies/002-exact-first-screening/data/random_screen_v1.json`
- random analysis: `research/studies/002-exact-first-screening/RANDOM_SCREEN_ANALYSIS.md`
- tracking issue: Issue #6

Study 001 remains closed. Do not reopen it or create Span v0.3.

## Exact result

- 15 of 18 candidates solved exactly.
- Exact roots: 9 first-participant wins, 6 losses, no draws.
- 14 of 15 solved roots ended within eight optimal plies.
- Six solved candidates had no non-losing opening.
- Exact repeated-run normalized SHA-256: `9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`.

## Random result

- 2,000 games per candidate; 36,000 total.
- 17,656 first-participant wins, 18,344 second-participant wins, no draws.
- 19,715 goal endings and 16,285 no-legal-action endings.
- Mean duration: 6.8161 plies.
- Repeated-run deterministic SHA-256: `d3726b0dff560befc4bbc86fa69b7f9aa889d0e41d16f2a54a3b1acc0df7960e`.

## Exact-versus-random result

Six candidates met the pre-defined false-reassurance condition:

- `S2-3-AG-02`
- `S2-3-AG-03`
- `S2-3-CE-03`
- `S2-4-AG-01`
- `S2-4-AG-02`
- `S2-4-CE-01`

Nine candidates appeared 40–60% under random play. Seven were exactly solved; six of those seven were false-reassurance cases.

Provisional hypothesis disposition:

- H1 supported.
- H2 unresolved.
- H3 supported.

## Procedural limitation

No shallow heuristic was frozen before exact inspection. Do not create a post-result heuristic. The formal shallow screen is cancelled, and Study 002 cannot receive a fully successful disposition.

## Next recommended work unit

Complete cycle 6 and close Study 002.

1. Write `research/studies/002-exact-first-screening/REPORT.md`.
2. Integrate the frozen question, manifest, correctness gate, exact result, random result, six false-reassurance cases, and reproducibility record.
3. Classify H1 and H3 as supported and H2 as unresolved.
4. Separate valid exact-versus-random findings from the heuristic sequencing failure.
5. State the verification limits and out-of-scope human qualities.
6. Close Issue #6.
7. Set `STATE.md` to no active study.
8. Do not begin Study 003 in the same cycle.

## Human gate

> 承認

## Human action pending

None.
