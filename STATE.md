# State

_Last updated: 2026-07-25_

## Phase

**No active study / frozen inactive Study 006 proposal**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Closed studies

- **Study 001:** negative autonomous-game-design conclusion.
- **Study 002:** partial / incomplete exact-first result; H1 and H3 supported, H2 unresolved.
- **Study 003:** methodological success with bounded procedural claims.
- **Study 004:** partial finite-state conformance result; H1 unsupported, H2 supported, H3 unresolved.
- **Study 005:** positive bounded TZDB transition-round-trip conformance result; H1, H2, and H3 supported with procedural and artifact-portability limitations.

## Post-Study-005 portfolio decision

- Decision: `research/decisions/2026-07-25-post-study-005-portfolio-assessment.md`
- Selected inactive proposal: `research/proposals/006-python-tar-extraction-boundary-conformance.md`
- Proposed Study 006 status: **frozen, not active**
- Active issue: **none**
- Selection threshold: at least **30 / 35**, no criterion below **4**, external referent, concrete failure result, four-cycle closure, and no external action or untrusted archive extraction.
- Selected score: **32 / 35**
- Runtime feasibility observed: CPython **3.13.5**, Linux 6.12.13 x86_64, glibc 2.41, `tarfile.data_filter`, required filter exceptions, temporary symlinks, and `resource.setrlimit`.
- Primary referents: Python 3.13 `tarfile` documentation and final PEP 706.
- Rejected or held directions: reproducible scientific artifact envelope, RFC 3986 reference resolution, Unicode UTS #46 IDNA processing, prospective project-selection calibration, and inactivity.

## Study 006 frozen question

On CPython 3.13.5 for Linux, does `tarfile` extraction with the explicit `data` filter enforce its documented destination-containment, link, special-file, and metadata-sanitization boundaries across a frozen stateful fixture matrix, while preserving safe data-archive behavior and producing independently auditable filesystem effects?

The proposal uses only original synthetic archives inside disposable study roots. It does not authorize arbitrary external archives, real user paths, elevated privileges, denial-of-service tests, vulnerability disclosure, or a general claim that tar extraction is safe.

## Next bounded work

The next exact `承認` may perform one independent Study 006 activation cycle only:

1. re-read the live repository, portfolio decision, frozen proposal, governance, and current tool state;
2. reverify the exact CPython 3.13.5 runtime, `tarfile` source identity, documentation identity, filesystem capabilities, symlink and hard-link support, and safe disposable-root containment;
3. choose activation **GO unchanged** or **NO-GO**;
4. if GO, activate Study 006, open its issue, freeze the active protocol, fixture grammar, projection schema, resource caps, and exact manifest;
5. stop before implementing the generator or oracle, creating formal fixture archives, extracting archives, or inspecting protected outcomes;
6. if NO-GO, record the reason and remain inactive.

No external contact, vulnerability report, terms acceptance, untrusted archive ingress, spending, permission change, or third-party repository modification is authorized.

## Human action currently needed

None beyond a later exact `承認` for the independent Study 006 activation decision.
