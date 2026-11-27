# Ficha de aceitação nativa / Native acceptance record
Template only — all cases initially NOT_RUN. This does not authorize installation or distribution. Use only authorized exact candidate bytes after prerequisites pass. Do not bypass antivirus, browser policy or quarantine. Use synthetic data and a disposable authorized client environment; never delete real data.

## Identification / Identificação
- Product, version, candidate commit, package filename, expected SHA-256, computed SHA-256, provenance URL:
- OS edition/build/architecture, browser version, CPU/RAM, display scaling, peripheral/model/version (when applicable):
- Tester, UTC timestamp, active antivirus/version/definitions, scan targets and evidence reference:
- Scope (source, installed, portable or extension), license/notice review status:

## Cases / Casos
| ID | Expected observable result / Resultado esperado | Status | Evidence / Evidência |
| --- | --- | --- | --- |
| N01 | Candidate identity, hash, AV gates and authorized execution verified | NOT_RUN | |
| N02 | Decline installer terms without install; approved install or isolated portable extraction; launch and diagnostic | NOT_RUN | |
| N03 | Prior supported version upgrade or portable migration in isolated test profile; no data loss | NOT_RUN | |
| N04 | Export backup of synthetic records; verify restore and duplicate policy | NOT_RUN | |
| N05 | Corrupt synthetic backup rejected; original data unchanged | NOT_RUN | |
| N06 | Interrupted operation and restart recover consistent state; no stale token or action | NOT_RUN | |
| N07 | Permission denial/revocation and offline behavior, no unexpected transmission | NOT_RUN | |
| N08 | Uninstall/remove or portable cleanup; retain/delete only agreed synthetic files | NOT_RUN | |
| N09 | Browser extension installation, popup, reload, removal where applicable and policy permits | NOT_RUN | |
| N10 | Real local model/peripheral tests where applicable, consent and cancellation | NOT_RUN | |
| N11 | Keyboard, screen reader, zoom, contrast, focus, logo/theme | NOT_RUN | |
| N12 | Cold start, response times, RAM, repeated open/close and recovery | NOT_RUN | |

For each case add expected and observed result, duration/units, severity, exact evidence and timestamp. States: PASS_CI (separate hosted record), PASS_NATIVE (case-level evidence), REPORTED (owner report only), FAIL, BLOCKED, NOT_RUN, N/A (justification required). A report may cover a group without proving individual cases. A changed package or runtime commit requires review of affected evidence. No native execution on blocked components. Project-specific matrices take precedence; this template does not relax their gates or imply all cases apply.

## Recovery / Recuperação
Keep prior authorized package and synthetic backup separately, verify restore before upgrade, stop on any unexpected corruption or security alert. Record rollback outcome; do not overwrite real files or restore quarantined content. Keep confidential logs, user data and credentials out of public repositories.

## Decision / Decisão
Mandatory gates passed: NOT_RUN. Score: N/D. Authorization: NOT_GRANTED by this template. Release: not approved. Owner authorization, licensing, complete security and quality gates remain independent.
