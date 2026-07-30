# Execution-Path Capability Audit — 2026-07-31

_Date: 2026-07-31 (Asia/Tokyo)_  
_Status: **Complete — 2 PASS, 2 PARTIAL, 4 FAIL**_  
_Class: **Non-study operational capability audit**

## 1. Purpose and boundary

This audit records which currently authorized paths can move harmless text and binary objects into the code-execution filesystem without silent transformation, independently verify their byte identity, and hand them to bounded safe parsers.

It is infrastructure maintenance, not a research study. It did not select or freeze a proposal, activate a study, open an active-study issue, retain a formal scientific corpus, inspect a protected outcome, contact outsiders, modify third-party systems, or convert capability success into a scientific claim.

The probe matrix was frozen before execution in commit:

`56f01b116ae92c9785a2a0e69cd5f19c3f0dc901`

Machine-readable results:

`operations/execution-path-capability-audit-2026-07-31.json`

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

`PARTIAL` means that identity, metadata, or returned content is available but byte-preserving local filesystem materialization or safe-parser handoff is absent. `FAIL` means the acquisition path did not return the frozen object or create a usable local file.

## 3. Frozen fixtures and methods

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

## 5. Execution environment

- OS: Debian GNU/Linux 13 (`trixie`), `DEBIAN_VERSION_FULL=13.3`;
- kernel/platform: `Linux-6.12.13-x86_64-with-glibc2.41`;
- Python: CPython 3.13.5 at `/opt/pyvenv/bin/python3`;
- curl: 8.10.1 with OpenSSL 3.5.5;
- Python `zoneinfo.TZPATH`: `/usr/share/zoneinfo`, `/usr/lib/zoneinfo`, `/usr/share/lib/zoneinfo`, `/etc/zoneinfo`.

These identities describe this audit only. Capability remains episodic and must not be generalized to a later runtime without rehearsal.

## 6. Result matrix

| Probe | Path class | Identity / content visible | Local byte file | Local hash | Safe parser | Result |
|---|---|---|---|---|---|---|
| P1 | local UTF-8 text | yes | yes, two copies | yes | yes | **PASS** |
| P2 | local binary | yes | yes, two copies | yes | yes | **PASS** |
| P3 | official HTTPS text, `container.download` | URL only | no | no | no | **FAIL** |
| P4 | official HTTPS text, curl | URL and DNS error | no | no | no | **FAIL** |
| P5 | official HTTPS binary, `container.download` | URL only | no | no | no | **FAIL** |
| P6 | official HTTPS binary, curl | URL and DNS error | no | no | no | **FAIL** |
| P7 | GitHub connector text | blob and complete response text | no | no independent local hash | no local handoff | **PARTIAL** |
| P8 | GitHub connector binary | blob and base64 response resource | no | no independent local hash | no local handoff | **PARTIAL** |

Complete materialization passes: **2 / 8**.  
Partial paths: **2 / 8**.  
Failed paths: **4 / 8**.

## 7. Detailed observations

### P1 — Local UTF-8 text: PASS

Source:

- `/etc/debian_version`;
- regular file;
- bytes: `5`;
- SHA-256: `cc49a4a1ef024f2f2efffe285cb147395fc57a2f9ed4e9a128338e2cbff44d8b`.

Two separate byte-for-byte copies each had:

- bytes: `5`;
- SHA-256: `cc49a4a1ef024f2f2efffe285cb147395fc57a2f9ed4e9a128338e2cbff44d8b`;
- strict UTF-8 decode: pass;
- NUL absent: pass;
- nonempty lines: `1`.

The source and both copies were byte-identical. Existing local UTF-8 text can therefore pass full materialization, identity, parser, and repeatability checks in this runtime.

### P2 — Local binary: PASS

Source:

- path: `/usr/share/zoneinfo/UTC`;
- symlink target: `/usr/share/zoneinfo/Etc/UTC`;
- target bytes: `114`;
- SHA-256: `8b85846791ab2c8a5463c83a5be3c043e2570d7448434d41398969ed47e3e6f2`.

Two separate byte-for-byte copies each had the same byte length and SHA-256. `zoneinfo.ZoneInfo.from_file` opened both copied files successfully. Both returned a UTC offset of zero seconds at the Unix epoch.

Existing local binary files can therefore pass full materialization, identity, bounded safe-parser, and repeatability checks in this runtime.

### P3 — Official HTTPS text through `container.download`: FAIL

Attempted object:

`https://www.rfc-editor.org/rfc/rfc20.txt`

Tool result:

`ERROR: download failed`

No destination file existed after the call. No local byte length, SHA-256, UTF-8 validation, or title check was possible.

### P4 — Official HTTPS text through curl: FAIL

Frozen command form:

```text
curl --fail --location --max-time 20 --output <path> https://www.rfc-editor.org/rfc/rfc20.txt
```

Result:

- return code: `6`;
- error: `curl: (6) Could not resolve host: www.rfc-editor.org`;
- destination file: absent.

Failure occurred before content type or parser behavior could be tested.

### P5 — Official HTTPS binary through `container.download`: FAIL

Attempted object:

`https://data.iana.org/time-zones/releases/tzdata2025b.tar.gz`

Tool result:

`ERROR: download failed`

No destination file existed after the call. No local byte length, SHA-256, gzip opening, or bounded tar member listing was possible.

### P6 — Official HTTPS binary through curl: FAIL

Frozen command form:

```text
curl --fail --location --max-time 20 --output <path> https://data.iana.org/time-zones/releases/tzdata2025b.tar.gz
```

Result:

- return code: `6`;
- error: `curl: (6) Could not resolve host: data.iana.org`;
- destination file: absent.

Failure occurred before binary handling or parser behavior could be tested.

### P7 — GitHub connector UTF-8 text: PARTIAL

The connector returned `CHARTER.md` twice with:

- expected and returned blob: `05cb1d457ab7b75f5fb23cd99af5851b1ad11c95`;
- UTF-8 content exposed as a complete response resource;
- same blob SHA and response line count on both calls.

The connector response supplied no mounted path or reusable file reference. Response URIs such as `/response/turn190` and `/response/turn192` were absent from the code-execution filesystem, and no `CHARTER.md` appeared under `/mnt/data`.

The text path is therefore repeatable for metadata and conversational content inspection, but it is not a complete byte-materialization path. Local size, local SHA-256, and parser handoff were deliberately not manufactured by copying or reserializing the response.

### P8 — GitHub connector binary: PARTIAL

`fetch_file` with base64 encoding returned:

- expected and returned blob: `bb28cb8aa671050294436b01e5ffd586ae14acbb`;
- base64 content exposed through a response resource;
- no mounted path or reusable file reference.

The response resource was inspectable through the connector resource reader, but it was not present in the code-execution filesystem. No `pluck-pcm8.wav` appeared under `/mnt/data`. Manual assembly of response lines was prohibited by the frozen matrix.

`fetch_blob` by the exact Git blob failed with:

```text
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd6 in position 138: invalid continuation byte
```

The connector therefore exposed binary identity and a base64 presentation, but did not provide an independently hashable local binary object or safe `wave.open` handoff. This is partial metadata/content access, not complete materialization.

## 8. Cross-path findings

### 8.1 Local filesystem paths are complete for the tested object classes

Both tested existing local paths supported:

- binary reads;
- byte-for-byte local copies;
- local byte length and SHA-256;
- bounded safe parser opening;
- repeated identical results.

This supports only a runtime capability claim. It does not grant research value to locally available objects.

### 8.2 Tested official HTTPS paths fail before content handling

Both official hosts failed through curl at DNS resolution. `container.download` also failed and produced no file. Because acquisition did not reach the object, the audit cannot distinguish later HTTPS, redirect, text, binary, or parser behavior for these paths.

### 8.3 GitHub connector inspection is not a general filesystem bridge

For UTF-8 text, the connector reliably returned content and blob identity as a response resource. For binary, `fetch_file` returned a base64 response resource and blob identity, while `fetch_blob` failed by attempting UTF-8 decoding.

Neither connector path produced a mounted local file. A response resource can support conversational inspection but does not satisfy a scientific workflow that requires independent local hashing and parser execution.

### 8.4 Object identity, content visibility, and executable materialization remain separate capabilities

The audit directly observed all three states:

- complete executable materialization: P1 and P2;
- content or metadata visibility without materialization: P7 and P8;
- no acquired object: P3 through P6.

Future feasibility records must preserve these distinctions rather than compressing them into a single `available` field.

## 9. Cleanup and preservation

After the result JSON was committed, the complete temporary audit directory under `/mnt/data` was deleted. Verification confirmed that the temporary root was absent and that no RFC text, IANA archive, connector text file, or connector binary file remained under the bounded search paths.

The repository retains only:

- this audit record;
- the machine-readable result matrix;
- hashes and structural parser outcomes for harmless local fixtures;
- exact acquisition errors and connector behavior.

It retains no formal scientific corpus.

## 10. Operational disposition

The reusable capability rule after this audit is:

1. existing local text and binary objects may receive execution-path confidence only after a fresh source/copy hash and safe-parser rehearsal;
2. ordinary public HTTPS acquisition from the code runtime is unavailable for the tested hosts and must be treated as failed until a later audit demonstrates otherwise;
3. `container.download` cannot be presumed to repair runtime HTTPS failure;
4. GitHub connector response resources are inspection surfaces, not byte-preserving local filesystem objects;
5. connector binary `fetch_blob` may fail because of UTF-8 decoding assumptions;
6. a future external-data direction needs an authorized action that returns a mounted file path, reusable file reference, or otherwise independently hashable local bytes before it can receive full feasibility.

No new failure mode is required. FM-010 and FM-011 already cover the observed risk. `self/LIMITS.md` should be updated with the sharper distinction between connector content inspection and filesystem handoff.

## 11. Boundaries preserved

- no research proposal selected or frozen;
- no study activated;
- no active-study issue opened;
- no scientific instrument implemented;
- no formal corpus retained;
- no protected outcome inspected;
- no hypothesis disposition assigned;
- no outside party contacted;
- no third-party system modified.
