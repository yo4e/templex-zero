# Next Start

_Updated: 2026-07-24 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the frozen Study 005 proposal, the activation NO-GO decision, governance files, current issues, and recent commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**No study is active. Studies 001–004 are closed. Study 005 remains a frozen inactive proposal after an activation NO-GO.**

- Frozen proposal: `research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md`
- Activation decision: `research/decisions/2026-07-24-study-005-activation-no-go.md`
- Study 005 activation cycles completed: **0**
- Active-study issue: none

## Activation NO-GO

Official IANA evidence confirmed:

- release 2026c dated 2026-07-08;
- versioned archive `tzdata2026c.tar.gz`;
- archive byte count 475,694;
- official SHA-512 `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`;
- public-domain tz database boundary;
- detached `.asc` signature availability.

Local CPython 3.13.5, `zoneinfo`, `zic` 2.41, and `zdump` 2.41 were present.

The available execution environment could not obtain the exact archive bytes from the official IANA HTTPS host. The cycle refused a third-party mirror, source-repository reconstruction, host zone data, unversioned convenience URL, or newer release. Therefore it did not activate Study 005 or perform Cycle 1.

## Human access operation pending

Before another activation attempt, the exact unchanged file should be downloaded from:

`https://www.iana.org/time-zones/repository/releases/tzdata2026c.tar.gz`

and uploaded to the current TEMPLEX/0 project conversation.

Expected identity:

- filename: `tzdata2026c.tar.gz`;
- byte count: 475,694;
- SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`.

The matching `.asc` file may also be uploaded. This is A1 access assistance, not research selection or execution.

## Next bounded work unit

Only after trusted archive bytes are present, the next approval may:

1. re-read live state and verify the uploaded file against official size and SHA-512;
2. inspect the archive listing and bundled non-data licenses before committing any third-party file;
3. choose activation **GO unchanged** or **NO-GO** again;
4. if GO, create the active protocol and issue;
5. extract and compile 2026c twice into clean isolated temporary directories;
6. freeze command, environment, source order, output inventory, and deterministic tree digest;
7. freeze exact `zone1970.tab` bytes, ordered canonical zone inventory, and at least twelve parser-fixture expectations;
8. synchronize state and stop.

The cycle must not implement the complete TZif reader, generate the full transition manifest, execute the `zoneinfo` comparison, contact IANA or Python maintainers, file an external report, accept terms, substitute data, or add a second active cycle.

## Verification boundaries carried forward

- The archive has not been observed by TEMPLEX/0.
- No archive digest, member listing, bundled license, compiled tree, canonical zone list, or parser fixture is frozen yet.
- The host zone database must never become the evidence source.
- Browser-visible official metadata is not a substitute for exact archive bytes.
- A connector-backed source check is not a fresh checkout.

## Human gate

> Supply the exact archive bytes, then send `承認`.

## Human action pending

Official `tzdata2026c.tar.gz` upload as described above.
