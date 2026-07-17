# Study 002 Cycle 4 Write Corrections

_Date: 2026-07-17 (Asia/Tokyo)_

During final repository synchronization in the exact-candidate cycle, three connector-write mistakes occurred.

1. An `update_file` call intended as a check replaced the Study 002 `README.md` with the word `placeholder` in commit `04ee923bb0a2ff2b258b610cb9aa9a7084a89425`.
2. A second check call replaced `STATE.md` with only its title in commit `e1133927afde5f8df25ab1350ac9cf117f422fc3`.
3. An attempted update to `EXACT_SCREEN_ANALYSIS.md` used an unrelated SHA and was rejected by GitHub with HTTP 409; no content change occurred.

The two successful accidental replacements were immediately repaired from the complete contents created earlier in the same cycle:

- `README.md` restored in `8127301ebaa23773c1fef63104afd1b00aab3b3b`;
- `STATE.md` restored in `46460b23290fc8bf9e292c42a3f1a7dba242c715`.

Post-repair fetches confirmed the expected full content and original restored blob SHAs:

- Study 002 README blob: `013479b0917cde27c1dea37810114a8820d12b8c`;
- STATE blob: `9572015cb3433cf4fe26d5377dc8f2566dfbca52`.

No experiment script, candidate manifest, exact result, comparison value, cap, or interpretation was changed by these write mistakes. The erroneous and corrective commits remain visible in repository history.
