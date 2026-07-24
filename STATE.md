# State

_Last updated: 2026-07-24_

## Phase

**No active study / Study 005 source ingress verified, activation pending**

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

## Study 005 source state

- Frozen proposal: `research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md`
- Prior activation decision: **NO-GO on source acquisition; proposal remained inactive**.
- Prior decision record: `research/decisions/2026-07-24-study-005-activation-no-go.md`
- Source-ingress record: `research/decisions/2026-07-24-study-005-source-ingress-record.md`
- Verified archive: `tzdata2026c.tar.gz`
- Observed byte count: **475,694**
- Observed SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`
- Observed SHA-256: `e4a178a4477f3d0ea77cc31828ff72aa38feff8d61aa13e7e99e142e9d902be4`
- Internal version: **2026c**
- Archive members: **32**
- `zone1970.tab`: present
- Bundled permission preflight: top-level `LICENSE` states the default public-domain boundary; the three conditionally BSD-licensed named files are absent from this archive.
- Study 005 cycle count: **0 of maximum 4**, because activation has not occurred.
- Open active-study issue: **none**.
- No active protocol, compiled data, zone inventory, fixture set, implementation, transition manifest, or experiment exists.

## Repository cleanup

A human temporarily placed `tzdata2026c.tar.gz` at the repository root to test binary ingress. Templex did not extract, compile, or use that repository copy as research evidence. At the human's explicit instruction, the root file was deleted unchanged in commit `da39f24d534217d2da26cc213e5b257943385763`.

The public Git history retains the prior blob; no history rewrite was attempted. The separately uploaded project-conversation file is the artifact whose size, digests, archive structure, version, and license were inspected.

## Next bounded work

The source-acquisition blocker is removed. The next exact project-chat `承認` may independently retry the activation decision and, only if GO unchanged, perform Study 005 Cycle 1:

1. re-read live governance, proposal, source-ingress record, issues, and recent commits;
2. re-verify the available archive identity and permission boundary;
3. create the active protocol and active-study issue;
4. extract and compile tzdb 2026c twice in isolated temporary directories;
5. freeze command, environment, source order, output inventory, and deterministic tree digest;
6. freeze exact `zone1970.tab` bytes, ordered canonical zone inventory, and at least twelve parser-fixture expectations;
7. synchronize state and stop.

The next cycle must not implement the full TZif reader, generate the complete transition manifest, execute the Python comparison, contact outsiders, accept terms, or file an external defect report.

## Verification limitation

The access operation verified archive identity, structure, version, and the bundled license text without extracting files to a study tree. It did not verify a detached GPG signature, compile the archive, generate a zone inventory, freeze fixtures, or execute any Study 005 hypothesis test.

Fresh checkout and full-repository regression were not required for this access-and-cleanup operation and were not performed.

## Human action currently needed

Send exact `承認` to authorize one independent activation decision and, only if GO, Study 005 Cycle 1.