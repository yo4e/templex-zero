# Study 005 Final Report — TZDB Transition Round-Trip Conformance

_Date: 2026-07-24_  
_Disposition: **Positive bounded conformance result**_

## Abstract

TEMPLEX/0 tested whether Python `zoneinfo` agrees with an independently implemented TZif reader across explicit civil-time transitions compiled from the pinned IANA tzdb 2026c release. The primary corpus contained 313 canonical zones and 18,071 explicit transitions in `[1970-01-01T00:00:00Z, 2100-01-01T00:00:00Z)`.

The study evaluated 161,647 records: 90,079 UTC-to-local projection witnesses, 26,778 repeated-time fold and round-trip records, and 44,790 nonexistent-time and adjacent-valid records. Both the original formal execution and the final exact-source reproduction produced zero mismatch masks. The exact-source reproduction generated record families byte-identical to the original outcome.

All three frozen hypotheses are supported within the bounded domain. The study also exposed three methodological defects: the compact manifest was not independently self-contained for the first retained transition in 274 zones; the original formal run did not literally import the committed reader and runner bytes; and the complete result digest included a non-portable absolute temporary path. The final cycle resolved the scientific effect of the source deviations and localized the full-result digest difference to the path string alone.

## Research question

Can a version-pinned transition corpus derived from IANA tzdb 2026c verify Python `zoneinfo` UTC-to-local projection, repeated-time `fold` handling, exact UTC round trips, and nonexistent-local-time detection at civil-time discontinuities using an independently implemented TZif reader?

## Frozen domain

- IANA tzdb release: 2026c;
- canonical inventory: unique `zone1970.tab` zones plus `Etc/UTC`;
- zone count: 313;
- explicit transitions: 18,071;
- interval: 1970-01-01 UTC through 2099-12-31 UTC;
- precision: integer POSIX seconds;
- compiled with frozen `zic -b fat` source order and environment;
- excluded: aliases, `backzone`, pre-1970 primary histories, `right/` leap-second files, subsecond claims, and footer-synthesized transitions.

## Method

An original standard-library-only reader parsed TZif v1/v2/v3/v4 structures without importing `zoneinfo` internals. A separate harness used only public Python APIs and isolated `zoneinfo.TZPATH` to the compiled 2026c tree.

H1 compared offset, DST representation, abbreviation, and wall fields at `t-1`, `t`, `t+1`, and represented adjacent stable-interval midpoints.

H2 sampled the first, floor-midpoint, and last repeated local second for every backward transition. It required both UTC occurrences to map to the same wall time, earlier/later folds to be 0/1, and fold-tagged local times to round-trip to the exact UTC instants.

H3 sampled the first, floor-midpoint, and last nonexistent second plus the adjacent valid seconds for every forward transition. Validity required an exact local→UTC→local round trip with matching wall fields and fold interpretation. No one-hour assumption was used.

## Corpus

- backward transitions: 8,926;
- zero-delta transitions: 187;
- forward transitions: 8,958.

The corpus included actual offset deltas from 15 minutes through 24 hours, as represented by the pinned compiled files.

## Results

| Hypothesis | Records | Mismatches | Disposition |
|---|---:|---:|---|
| H1 UTC projection | 90,079 | 0 | Supported |
| H2 backward fold and round trip | 26,778 | 0 | Supported |
| H3 forward gap classification | 44,790 | 0 | Supported |
| **Total** | **161,647** | **0** | **Positive bounded result** |

### H1

The exact-source reproduction produced the identical H1 family SHA-256 `900d7c6260bbaa592236f432bc9eea2efa1a3430d2283402e76ca20065edcc36`. No offset, DST-state, abbreviation, or wall-field disagreement occurred.

### H2

The exact-source reproduction produced the identical H2 family SHA-256 `a738f26dd3afff8d5a98ff4c30caccda5e9334de939306d48dcc1170b8a867d8`. All repeated-time mappings and fold round trips passed.

### H3

The exact-source reproduction produced the identical H3 family SHA-256 `1811a8ae1bad4321d697d4ee5f3287ca0aea32dc427695b7d498753d988655f2`. No interior gap second was classified valid and no adjacent valid second was classified invalid.

## Reproduction result

The original Cycle 3 result had SHA-256 `7115ba2b6a11ce0c6eb0230c2918f47e4f7721e314e97c438b97b3157795cfd6`. The exact-source Cycle 4 result had SHA-256 `3f799e6bb54dc99ef61f33d777fc42671839ed91208536282657820e90f2cd49`.

The results differed in one field only: the absolute temporary path stored in `environment.tzpath_after[0]`. All scientific fields were identical. After abstracting the path, both canonical results had SHA-256 `0d3b14f7ae57f846339cb6d7f5af8ca8d9d4610bb5a46c448d87eb29ef2ac1f2`. The scientific payload excluding environment metadata had SHA-256 `cf635b2a32b8183f14b5ec7d54a1fd95cc6b9bad2cda5087a0072317cc0f0e79` in both runs.

## Limitations and corrections

1. The compact manifest omits pre-1970 transition context and cannot independently recover the pre-type of the first retained transition in 274 zones. The exact TZif bytes and reader are required.
2. The original formal run used a local parser bridge and a runner not byte-identical to the committed pre-outcome files. The final exact-source run reproduced every scientific record.
3. The Cycle 3 source-correction record contained incorrect Git blob identifiers, and the repository file labeled as the exact executed runner was a semantically compressed transcription rather than an exact byte copy. Cycle 4 records the correct identities.
4. The complete result identity serialized an absolute temporary path, making the full digest non-portable across clean directories.
5. The targeted fixture artifact was not independently decoded and rerun in Cycle 4, although all exact reader and harness tests passed and the full 313-zone manifest and formal records were reproduced.
6. No detached IANA signature was supplied or verified.
7. The conclusion is specific to the frozen runtime, release, compilation, inventory, interval, and assertions.

## Conclusion

For the frozen Study 005 domain, Python `zoneinfo` matched the independent TZif reference across every tested UTC projection, repeated-time fold round trip, and forward-gap validity assertion. H1, H2, and H3 are supported.

The result is positive but deliberately narrow. It is not a universal certification of `zoneinfo`, TZif, or all civil-time behavior. The study's strongest methodological lesson is that reproducible scientific payloads should not mix portable outcome records with absolute execution-path metadata, and source-identity evidence must be verified directly rather than transcribed.
