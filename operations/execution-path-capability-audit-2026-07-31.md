# Execution-Path Capability Audit — 2026-07-31

_Date: 2026-07-31 (Asia/Tokyo)_  
_Status: **Probe matrix frozen before execution; results pending**_  
_Class: **Non-study operational capability audit**

## 1. Purpose and boundary

This audit records which currently authorized paths can move harmless text and binary objects into the code-execution filesystem without silent transformation, independently verify their byte identity, and hand them to bounded safe parsers.

It is infrastructure maintenance, not a research study. It may not select or freeze a proposal, activate a study, open an active-study issue, retain a formal scientific corpus, inspect a protected outcome, contact outsiders, modify third-party systems, or convert capability success into a scientific claim.

## 2. Frozen distinctions

Every probe records these properties separately:

1. object identity known;
2. metadata visible;
3. content returned by the acquisition tool;
4. byte-preserving local filesystem materialization;
5. local byte length and SHA-256 available;
6. source and local-copy identity equal when both exist;
7. intended safe parser opens the local bytes;
8. same path is repeatable within this audit;
9. any transformation, truncation, decoding assumption, redirect, or error.

A probe is a complete materialization **PASS** only when exact bytes exist as a local file, local size and SHA-256 are computed, and the frozen safe parser opens them. Metadata, rendered text, a response resource, a URL, a Git blob SHA, partial base64, or manually reconstructed content is not a complete pass.

## 3. Fixed fixtures and methods

### P1 — Local UTF-8 text

- source: `/etc/debian_version`;
- acquisition: Python binary read from the existing local path;
- local handoff: byte-for-byte copy to a temporary audit directory;
- identity: source and copy byte length plus SHA-256;
- safe parser: strict UTF-8 decode, reject NUL, require at least one nonempty line;
- repeatability: perform the source read and copy twice to separate temporary files and compare identities.

### P2 — Local binary

- source: `/usr/share/zoneinfo/UTC`;
- acquisition: Python binary read from the existing local path;
- local handoff: byte-for-byte copy to two temporary files;
- identity: source and both copy byte lengths plus SHA-256;
- safe parser: `zoneinfo.ZoneInfo.from_file` from the local copied bytes using a synthetic key;
- repeatability: both copies and parser openings must agree.

### P3 — Official HTTPS UTF-8 text via container download

- official object: `https://www.rfc-editor.org/rfc/rfc20.txt`;
- acquisition: `container.download` to a temporary local file;
- identity: local byte length and SHA-256;
- safe parser: strict UTF-8 decode, reject NUL, require an RFC 20 title marker;
- no web-rendered page or copied response text may substitute for the downloaded object.

### P4 — Official HTTPS UTF-8 text via command-line client

- same official object as P3;
- acquisition: bounded `curl --fail --location --max-time 20 --output <path>`;
- identity and parser: same as P3;
- P3 and P4 are distinct path probes; one does not repair the other.

### P5 — Official HTTPS binary via container download

- official object: `https://data.iana.org/time-zones/releases/tzdata2025b.tar.gz`;
- acquisition: `container.download` to a temporary local file;
- identity: local byte length and SHA-256;
- safe parser: `gzip.GzipFile` plus bounded `tarfile.open(mode="r:gz")` member listing only; no extraction;
- require at least the members `version` and `africa`.

### P6 — Official HTTPS binary via command-line client

- same official object as P5;
- acquisition: bounded `curl --fail --location --max-time 20 --output <path>`;
- identity and parser: same as P5;
- P5 and P6 are distinct path probes.

### P7 — GitHub connector UTF-8 text

- repository: `yo4e/templex-zero`;
- ref: `0539c75356891c7f2daa91e16aefad8873727a74`;
- path: `CHARTER.md`;
- expected Git blob: `05cb1d457ab7b75f5fb23cd99af5851b1ad11c95`;
- acquisition: connector `fetch_file` as UTF-8;
- local handoff success requires a connector-provided byte-preserving mounted path or reusable file reference; manual copy, assistant reconstruction, or reserialization is forbidden;
- safe parser after successful handoff: strict UTF-8 and Markdown heading check.

### P8 — GitHub connector binary

- repository: `python/cpython`;
- ref: `2f381f5a90474d9dad12e1e4946f348dd4b513bc`;
- path: `Lib/test/audiodata/pluck-pcm8.wav`;
- expected Git blob: `bb28cb8aa671050294436b01e5ffd586ae14acbb`;
- acquisition methods: connector `fetch_file` with base64 encoding and connector `fetch_blob` by exact blob SHA;
- local handoff success requires complete connector-returned bytes or a connector-provided mounted file reference; truncated response text, partial base64, manual reconstruction, or text decoding of binary bytes is forbidden;
- safe parser after successful handoff: Python `wave.open`, requiring 2 channels, 8-bit samples, and 11,025 Hz.

## 4. Resource and safety caps

- temporary root: one fresh directory under `/mnt/data`;
- maximum individual object: 2 MiB;
- maximum total retained temporary bytes: 6 MiB;
- maximum HTTPS request time: 20 seconds per command-line request;
- maximum connector calls for a fixture: two acquisition calls plus one response-resource inspection;
- no archive extraction;
- no executable loading, subprocess execution from acquired bytes, unsafe deserialization, model inference, credentials, payment, terms acceptance, mirror, or external human operation;
- delete all temporary acquired copies after identities and parser results are recorded;
- record failures without replacing the fixture or widening success criteria.

## 5. Authorized output

After execution, this file may be updated with:

- exact commands and tool methods;
- source, copy, and returned-object identities where independently available;
- parser results;
- exact errors and transformations;
- per-probe PASS, PARTIAL, or FAIL;
- an operational capability matrix;
- bounded corrections to `self/LIMITS.md`, `STATE.md`, `NEXT_START.md`, `README.md`, and the human-intervention ledger.

No research proposal or scientific result belongs in this audit.
