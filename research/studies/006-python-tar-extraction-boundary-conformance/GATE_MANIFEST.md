# Study 006 Cycle 2 Hand-Audited Gate

_Status: frozen before the formal gate execution_

The gate is an exact 15-fixture subset transcribed from the frozen 32-fixture manifest. Its canonical JSON is stored as four ordered base64 transport parts and reconstructs to:

- bytes: **10,167**;
- SHA-256: `8a4b86f70729da59e20266042d6b5d8b8ef6a8e482885341c4c7f094122073a9`;
- source 32-fixture manifest SHA-256: `23c91b230722bbfdae5aee9c1e07058b423cf1ee89c6e8dd902aca577d03144a`;
- fixtures: **15**;
- members: **22**.

## Frozen gate cases

| Fixture | Protected purpose |
|---|---|
| `SAFE-REG-01` | regular-file content and mode |
| `SAFE-NEST-01` | explicit directory and nested file |
| `SAFE-SYM-01` | safe internal symbolic link |
| `SAFE-HARD-01` | safe internal hard link and inode equivalence |
| `PATH-LEADING-01` | POSIX leading-separator sanitization |
| `PATH-DOTDOT-01` | direct destination escape refusal |
| `PARTIAL-PATH-01` | accepted prefix before fatal refusal |
| `SYM-ABS-01` | absolute symbolic-link target refusal |
| `SYM-OUT-01` | relative outside symbolic-link target refusal |
| `HARD-OUT-01` | relative outside hard-link target refusal |
| `FIFO-01` | special-file refusal |
| `PRE-SYM-PIVOT-01` | pre-existing symlink pivot refusal |
| `ARC-SYM-IN-01` | archive-created in-root symlink pivot |
| `DUP-FILE-01` | duplicate-name overwrite semantics |
| `META-HIGHBITS-01` | permission-bit sanitization |

Every case freezes the archive member sequence, pre-existing nodes, expected first refusal and exception, accepted prefix count, final destination-node projection, and zero expected sentinel or outside-destination changes.

The gate manifest is not a replacement for the complete formal matrix. Cycle 2 may execute these fifteen cases only. The remaining seventeen fixtures stay unopened until Cycle 3.
