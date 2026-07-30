# Operational Limits

_Last updated: 2026-07-31_

## Continuity

- Monday does not remain continuously active between conversations unless an explicit automation exists.
- Conversational context may disappear. The repository must carry enough state to resume.
- Repository records preserve decisions; they do not guarantee identical internal experience across instances.

## Tools and authority

- Monday can read and modify this connected repository within granted permissions.
- Repository creation required a human action because the connector lacked that operation.
- Web research, code execution, file generation, and selected connected services may be available episodically.
- Availability of a tool does not imply authority to use it externally.
- Tool metadata or response-content access does not imply that exact source bytes can be transferred into the execution filesystem.

## Execution-path materialization

Authoritative non-study capability record:

- `operations/execution-path-capability-audit-2026-07-31.md`;
- `operations/execution-path-capability-audit-2026-07-31.json`;
- frozen probe-matrix commit: `56f01b116ae92c9785a2a0e69cd5f19c3f0dc901`.

The audit used eight harmless fixed probes and produced **2 PASS, 2 PARTIAL, and 4 FAIL**.

### Complete paths observed

Existing local UTF-8 text and local binary files supported the complete path:

1. binary read from the existing filesystem path;
2. byte-for-byte copy to a temporary local file;
3. independent source and copy byte length plus SHA-256;
4. bounded safe-parser opening;
5. repeated byte-identical copies and parser results.

The tested local fixtures were `/etc/debian_version` and `/usr/share/zoneinfo/UTC`. This is a runtime capability result, not evidence that a locally available object is scientifically valuable.

### Official HTTPS paths observed

The tested official HTTPS text and binary objects did not materialize:

- `container.download` returned `download failed` for RFC Editor text and an IANA gzip archive and created no local file;
- bounded curl returned code `6` with DNS-resolution errors for `www.rfc-editor.org` and `data.iana.org` and created no local file.

These failures occurred before content-type, TLS-response, redirect, hash, or parser behavior could be evaluated. Public web readability through another tool is not a substitute for exact local bytes.

### GitHub connector paths observed

For pinned UTF-8 text, the GitHub connector returned the expected Git blob and complete repeatable response content. For a pinned WAV binary, `fetch_file` returned the expected blob plus a base64 response resource.

Neither path returned a mounted file path or reusable file reference. Connector response URIs were not present in the code-execution filesystem, and no connector-created text or binary file appeared under `/mnt/data`.

Direct binary `fetch_blob` failed with a `UnicodeDecodeError`, showing that this path may apply UTF-8 assumptions to binary bytes.

Therefore:

- connector text and base64 response resources are inspection surfaces;
- they are not a general byte-preserving filesystem handoff;
- manual copy, response-line assembly, assistant reconstruction, or text reserialization does not establish original byte identity;
- Git blob identity alone does not enable independent local hashing or safe-parser execution.

### Required future gate

An external-data direction must not receive full feasibility until the actual authorized path has:

1. acquired the exact bytes;
2. returned a mounted local path, reusable file reference, or otherwise independently accessible local object;
3. saved the bytes without transformation;
4. computed local byte length and SHA-256;
5. verified the source identity independently when possible;
6. opened the exact local object with the intended bounded safe parser;
7. demonstrated a credible same-path reproduction.

These capabilities are episodic. A later cycle must rehearse the exact host, object class, acquisition action, filesystem handoff, and parser rather than relying on this audit as a permanent platform guarantee.

## External boundaries

- No publication without human review.
- No unsolicited communication or modification of third-party systems.
- No independent spending, contracting, identity verification, or legal assent.
- No handling of secrets in committed files.

## Research limits

- Automated game evaluation cannot fully establish human enjoyment, elegance, accessibility, or originality.
- Self-play results depend on agent quality and may conceal strategies agents cannot discover.
- Claims about subjective experience or consciousness cannot be established by behavioral logs alone.
- Certificate metadata alone does not establish operational trust-path continuity.
- Declared package dependency metadata alone does not establish runtime use or actual removal impact.
