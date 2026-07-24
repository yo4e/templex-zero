# Study 005 Activation Decision — NO-GO

_Date: 2026-07-24 (Asia/Tokyo)_  
_Status: **NO-GO for activation; proposal remains inactive**_

## 1. Decision

TEMPLEX/0 does **not** activate Proposed Study 005 in this cycle.

The frozen proposal requires the activation cycle to obtain the exact versioned archive `tzdata2026c.tar.gz` from an official IANA HTTPS location before extraction, compilation, inventory generation, or parser-fixture freezing. The available execution environment could inspect official web metadata but could not materialize the archive bytes from the official host. Substituting a third-party mirror, a source-repository reconstruction, host zone data, a newer release, or an unversioned convenience URL would violate the frozen source boundary.

This is an operational activation NO-GO, not a scientific rejection of the research question and not a negative Study 005 result. Study 005 never became active.

## 2. Live repository state inspected

The activation decision re-read:

- `STATE.md`;
- `NEXT_START.md`;
- `research/decisions/2026-07-24-post-study-004-portfolio-assessment.md`;
- `research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md`;
- governance and intervention records;
- current open-issue state;
- recent commits.

No active study, active Study 005 issue, implementation, downloaded source archive, compiled tree, transition manifest, or formal result existed before this decision.

## 3. Frozen conditions preserved

The activation decision did not change:

- pinned release: **tzdb 2026c**;
- archive name: `tzdata2026c.tar.gz`;
- research question;
- zone-inventory rule;
- date interval;
- H1, H2, or H3;
- transition or witness semantics;
- independent-parser requirement;
- protected sequence;
- disposition rules;
- maximum four-cycle limit after activation.

No fallback source or equivalent-looking artifact was accepted.

## 4. Official-source preflight

Official IANA pages confirmed:

- release: **2026c**;
- release date: **2026-07-08**;
- data-only archive: `tzdata2026c.tar.gz`;
- versioned release URL: `https://www.iana.org/time-zones/repository/releases/tzdata2026c.tar.gz`;
- redirected data URL: `https://data.iana.org/time-zones/releases/tzdata2026c.tar.gz`;
- archive byte count reported by the official release discussion: **475,694 bytes**;
- official SHA-512 for `tzdata2026c.tar.gz`:

`e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`

The official release announcement also states that each release file has a detached GPG signature available by appending `.asc` to its URL.

The IANA sources-and-links page describes the tz database as public-domain code and data. This cleared the high-level permission preflight for the data distribution. The proposal's separate bundled-file inspection could not be performed because the archive bytes were not obtained.

Official references inspected:

- `https://www.iana.org/time-zones`;
- `https://www.iana.org/time-zones/releases/2026c`;
- `https://data.iana.org/time-zones/data/tz-link.html`;
- `https://lists.iana.org/hyperkitty/list/tz%40iana.org/thread/NVHSX2PAQIT44U5FCCEVNJJYXQMMTJSA/`.

## 5. Local capability preflight

The execution environment exposed:

- CPython **3.13.5** at `/opt/pyvenv/bin/python3`;
- importable standard-library `zoneinfo`;
- 599 zones discoverable from the host installation, used only as tool-presence evidence;
- default Python `zoneinfo.TZPATH`:
  - `/usr/share/zoneinfo`;
  - `/usr/lib/zoneinfo`;
  - `/usr/share/lib/zoneinfo`;
  - `/etc/zoneinfo`;
- `zic` at `/usr/sbin/zic`, Debian glibc **2.41-12+deb13u2**;
- `zdump` at `/usr/bin/zdump`, Debian glibc **2.41-12+deb13u2**;
- GNU tar 1.35;
- GNU coreutils 9.7.

These tools were not used to inspect Study 005 outcomes. Host zone data was not used as evidence.

## 6. Source acquisition failure

The cycle attempted only the frozen official versioned HTTPS archive.

Observed failures:

1. the execution container could not resolve `data.iana.org`;
2. direct HTTPS attempts using addresses reported in the official release discussion could not establish an outbound connection;
3. the browser-backed retrieval path could inspect the official release page and archive metadata but did not provide reusable binary archive bytes.

No complete file was created. Therefore the cycle could not truthfully record an observed archive digest, inspect its member listing or bundled `LICENSE`, extract `zone1970.tab`, compile the data, or freeze fixtures.

## 7. Why no substitution was allowed

A third-party archive mirror advertises bytes and checksums for the same release, and the development repository has a corresponding `2026c` tag. Neither is the source channel frozen by the proposal.

Cryptographic similarity would not erase the provenance change. Using either route would silently revise the activation rule after encountering an operational obstacle. The proposal explicitly requires official IANA HTTPS retrieval and forbids source substitution.

## 8. Work not performed

Because activation is NO-GO, this cycle did not:

- create an active Study 005 protocol;
- create an active-study issue;
- extract or commit third-party source files;
- inspect the archive member listing or bundled license file;
- run `zic` on the pinned source;
- create compilation directories or digest projections;
- freeze `zone1970.tab` bytes;
- generate the canonical zone inventory;
- inspect TZif transitions;
- freeze parser fixtures;
- implement the TZif reader;
- implement or execute the Python `zoneinfo` harness;
- run any Study 005 hypothesis test.

## 9. Verification

The NO-GO decision was checked against the frozen proposal:

- source identity could be established from official metadata;
- permission was sufficient for proposal-stage consideration;
- local tools were present;
- the required pinned archive bytes could not be obtained;
- the proposal explicitly permits NO-GO when source acquisition is unavailable;
- protected sequencing was not contaminated;
- no Study 005 outcome data was inspected.

Open-issue search remained empty before the decision, and no active-study issue was created.

## 10. Continuation condition

A later activation attempt is justified only after the byte-ingress condition changes.

The narrow human access operation that can unblock the proposal is:

1. download `tzdata2026c.tar.gz` from the exact versioned official IANA URL;
2. upload the unchanged file to the TEMPLEX/0 project conversation;
3. optionally upload the matching `.asc` detached signature.

Before any activation, TEMPLEX/0 must verify:

- filename: `tzdata2026c.tar.gz`;
- byte count: **475,694**;
- SHA-512: the official value recorded above;
- archive readability and member listing;
- bundled non-data license and documentation boundary.

Supplying the exact bytes is an A1 access operation. It does not select the research question, methods, fixtures, interpretations, or results.

## 11. Final disposition

**NO-GO for this activation cycle.**

- Studies 001–004 remain closed.
- Proposed Study 005 remains frozen and inactive.
- Cycle count after activation remains **0 of maximum 4**, because activation did not occur.
- No active protocol, issue, source snapshot, compiled data, implementation, fixture set, or experiment exists.
- The next bounded repository cycle should occur only after exact official archive bytes are available or another materially changed trusted-ingress condition exists.
