# Study 005 Cycle 3 — Harness Freeze Before Formal Outcomes

_Date: 2026-07-24 (Asia/Tokyo)_  
_Status: **Harness semantics frozen; complete formal execution not yet begun at this commit**_

## Scope and protected sequence

This record freezes the Cycle 3 public-API Python `zoneinfo` harness, witness generation, round-trip assertions, isolation proof, and deterministic result serialization before the complete 313-zone outcome set is executed.

The source release, compiled tree, zone inventory, date interval, transition manifest, hypotheses, transition inclusion, offset classes, and success criteria remain unchanged. No H1–H3 complete-corpus result was inspected while this record and the harness were prepared.

## Reconstructed identities

Before harness work, the trusted project-conversation archive was re-extracted and compiled with the frozen Cycle 1 command. The following reproduced exactly:

- archive SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`;
- compiled-tree projection SHA-256: `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2`;
- `zone1970.tab` SHA-256: `77b5e45415fa684fcc42de3421a6b0f15cc9b2c137f258083850346e8f76eea8`;
- ordered 313-zone inventory SHA-256: `053b3988df8da3276ba63928fab3a1e6b1e9e625d0fa13d16b6f423edc51b582`;
- reconstructed compact manifest: 354,993 bytes, SHA-256 `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`.

## Pre-outcome compact-manifest limitation

Reconstruction exposed a Cycle 2 overstatement. The compact manifest stores all retained `[timestamp, type_index]` pairs and all local-time-type tables, but it omits transition records before 1970. Therefore it does not independently identify the pre-transition type for the first retained transition when an earlier explicit transition exists.

- canonical zones with a retained transition whose actual first pre-type index is not zero: **274**;
- all 274 have pre-type fields different from type zero;
- using type zero would change the computed first-transition delta in all 274 and the backward/zero/forward class in 36.

This was detected before the complete Python outcome execution. The frozen manifest is not modified. The harness uses the already-frozen independent reader and the exact TZif file whose byte identity is recorded in the manifest to recover transition context. It verifies each manifest file identity, local type table, and retained transition list before comparison. Expected field values are then selected from the manifest-verified type table using the frozen reader's explicit transition context.

Cycle 2's manifest bytes and digest remain valid generated evidence, but the claim that the compact file is independently self-contained or lossless without the frozen reader and TZif bytes is withdrawn.

## Frozen UTC witness interpretation

For one retained explicit transition `t`:

- labeled boundary witnesses are `t-1`, `t`, and `t+1` when inside the frozen interval;
- the left stable interval uses integer seconds from the previous retained transition instant, or the frozen start boundary for the first retained transition, through `t-1`;
- its midpoint is the floor of the inclusive endpoint sum;
- a right midpoint is generated only when a later retained explicit transition supplies a represented stable endpoint;
- no right midpoint is generated after the final retained explicit transition because footer-generated transitions are outside the frozen explicit-transition corpus;
- labeled records are retained even if two labels were ever to produce the same UTC second.

## Frozen H1 assertions

For each UTC witness, public `zoneinfo` output is compared with the frozen reference on:

1. total UTC offset seconds;
2. TZif DST representation as `isdst` versus whether public `datetime.dst()` is nonzero; the observed signed DST seconds are also recorded;
3. abbreviation;
4. local calendar and clock fields represented as a naive wall-epoch second.

Mismatch mask bits are offset `1`, DST representation `2`, abbreviation `4`, and local fields `8`.

## Frozen H2 assertions

For every backward transition, the first, floor midpoint, and last repeated local second are generated from the actual offset delta. Each record preserves both implied UTC instants, both observed wall values and folds, and both fold-tagged local-to-UTC round trips.

Mismatch mask bits are wall equality `1`, earlier fold `2`, later fold `4`, fold-zero UTC round trip `8`, and fold-one UTC round trip `16`.

## Frozen H3 validator

For every forward transition, the first, floor midpoint, and last gap second plus the adjacent valid seconds are generated without an hour assumption.

For each naive wall time, both fold assignments are attached. An assignment survives only when local→UTC→local returns the identical wall fields and the same fold value. A wall time is valid when at least one assignment survives. Every attempt, UTC result, returned wall value, fold, and validity bit is preserved.

The H3 mismatch mask is `1` when the observed validity differs from the frozen expected validity.

## Isolation freeze

The formal command must:

- run CPython with `-S` so site packages are not initialized;
- begin with an empty `PYTHONTZPATH`;
- call public `zoneinfo.reset_tzpath()` with only the isolated 2026c compiled directory;
- require `zoneinfo.TZPATH` to equal that one directory;
- require `importlib.util.find_spec("tzdata")` to be absent;
- instantiate all 313 requested keys successfully;
- require a deliberately missing key to raise `ZoneInfoNotFoundError`.

The observed conversion uses public `ZoneInfo`, `datetime.astimezone`, `utcoffset`, `dst`, `tzname`, and `fold` only. It does not inspect CPython private parser state or use host conversion commands.

## Serialization freeze

The canonical full result stores:

- environment and isolation evidence;
- ordered zone names;
- every H1 comparison record;
- every H2 sample and assertion result;
- every H3 wall-classification attempt;
- manifest identity;
- reference-context provenance.

A separate canonical mismatch artifact contains every nonzero-mask record. A canonical summary stores mechanical record and mask counts plus result identity. The full result and mismatch JSON are deterministically XZ-compressed with the Python standard library using XZ format and preset `9 | PRESET_EXTREME`.

## Targeted pre-freeze verification

Seven tests passed before formal execution:

- conservative midpoint generation;
- non-one-hour repeated and gap sample generation;
- fixed-offset two-fold validator behavior;
- New York projection and one-hour fold;
- Lord Howe half-hour fold;
- New York gap detection;
- Apia 24-hour gap detection.

Frozen source identities are recorded in `data/harness_freeze_identity_v1.json`.

## Formal execution boundary

After this record and the harness source, tests, and runner are committed, Cycle 3 may execute the complete corpus exactly once. It must preserve every result and mismatch and must not repair, exclude, reinterpret, or rerun the outcome set inside Cycle 3.
