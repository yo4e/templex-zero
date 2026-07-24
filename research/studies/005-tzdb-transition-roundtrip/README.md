# Study 005 — TZDB Transition Round-Trip Conformance

_Status: **Closed after Cycle 4 of maximum 4**_  
_Disposition: **Positive bounded conformance result**_

Study 005 tested a pinned IANA tzdb 2026c transition corpus against an independently implemented TZif reader and an isolated public-API Python `zoneinfo` harness.

## Final result

The frozen corpus contained 313 canonical zones and 18,071 explicit transitions from 1970 through 2099.

| Hypothesis | Records | Mismatches | Disposition |
|---|---:|---:|---|
| H1 UTC projection | 90,079 | 0 | Supported |
| H2 backward fold and UTC round trip | 26,778 | 0 | Supported |
| H3 forward gap classification | 44,790 | 0 | Supported |
| **Total** | **161,647** | **0** | **Positive bounded result** |

Cycle 4 reconstructed the exact committed reader, harness, tests, builders, pre-outcome runner, source archive, compiled tree, inventory, transition manifest, and Cycle 3 result package. It then ran one exact-source formal reproduction.

All H1, H2, and H3 scientific record families were byte-identical to Cycle 3. The complete result digest differed in one field only: the absolute temporary path serialized in `environment.tzpath_after[0]`. After path normalization, the results were byte-identical. The scientific payload excluding environment metadata had SHA-256 `cf635b2a32b8183f14b5ec7d54a1fd95cc6b9bad2cda5087a0072317cc0f0e79` in both runs.

## Boundaries

The conclusion applies only to:

- CPython 3.13.5;
- IANA tzdb 2026c;
- the frozen `zic -b fat` compilation and source order;
- unique `zone1970.tab` zones plus `Etc/UTC`;
- explicit transitions in `[1970-01-01T00:00:00Z, 2100-01-01T00:00:00Z)`;
- integer POSIX seconds;
- the frozen H1–H3 assertions.

It does not certify other Python versions, operating systems, compilers, tzdb releases, aliases, `backzone`, leap-second files, subsecond behavior, or footer-synthesized future transitions.

## Permanent limitations

- The compact manifest needs the exact TZif bytes and reader for first-retained-transition context in 274 zones.
- Cycle 3 had reader/runner source-identity deviations; Cycle 4 reproduced the scientific payload exactly but does not erase those deviations.
- The full-result digest embedded a non-portable absolute path.
- The historical targeted fixture artifact was not separately decoded and rerun in Cycle 4.
- No detached IANA signature was verified.

## Final records

- `PROTOCOL.md` — frozen protocol and final disposition
- `REPORT.md` — final scientific report
- `CYCLE_4_REPRODUCTION_AND_CLOSURE.md` — exact-source reproduction and closure audit
- `CYCLE_3_SOURCE_IDENTITY_CORRECTION.md` — corrected source-identity record
- `data/cycle4_reproduction_analysis_v1.json` — machine-readable comparison
- `data/cycle4_source_identities_v1.json` — verified source identities and corrections
- `data/cycle4_formal_summary_v1.json` — exact-source formal summary

Issue #11 is closed. No fifth cycle exists.
