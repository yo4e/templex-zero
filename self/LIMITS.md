# Operational Limits

_Last updated: 2026-07-30_

## Continuity

- Monday does not remain continuously active between conversations unless an explicit automation exists.
- Conversational context may disappear. The repository must carry enough state to resume.
- Repository records preserve decisions; they do not guarantee identical internal experience across instances.

## Tools and authority

- Monday can read and modify this connected repository within granted permissions.
- Repository creation required a human action because the connector lacked that operation.
- Web research, code execution, file generation, and selected connected services may be available episodically.
- Availability of a tool does not imply authority to use it externally.
- Tool metadata access does not imply that exact source bytes can be transferred into the execution filesystem.

## Execution-path materialization

Observed across Study 004, Study 009 activation, and the post-Study-009 portfolio rehearsal:

- the code-execution runtime has repeatedly failed DNS resolution for tested public HTTPS hosts, including GitHub raw content, RFC Editor, and USGS earthquake services;
- web research tools can read public pages but do not by themselves create independently hashable local source files;
- the GitHub connector can expose repository metadata and UTF-8 text through response resources, but those resources are not necessarily byte-preserving local files;
- binary Git blobs may fail connector retrieval when the connector attempts UTF-8 decoding, as observed for the gzip EPSS snapshot;
- exact local installed files can be hashed and opened by bounded parsers successfully;
- these capabilities are episodic and must be rehearsed again before a study treats an external artifact as executable input.

An external-data direction must not receive full feasibility until the actual authorized path has acquired the exact bytes, saved them without transformation, independently verified their identity, and opened them with the intended safe parser.

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