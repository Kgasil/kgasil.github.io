# Cycle 03 — Step 04: License and distribution evidence / Licenciamento e distribuição
2026-11-27. No release approval. No first-party license assignment, purchase, or legal clearance.

## Lilium verified result
[46075861681](https://github.com/Kgasil/lilium/actions/runs/46075861681) FAILURE at bundled readiness only, job 140763307545. Official runtime Python 3.14.10/OpenSSL 3.5.9/SQLite 3.50.4 PASS; 125 Python tests, JavaScript regressions, source smoke and lifecycle/recovery PASS. Build and executable self-test PASS, four source/bundle DLL pairs match. The readiness diagnostic hard-coded Python 3.12, so windows_x64_python312 FAIL while other five checks PASS. Subsequent bundled smoke/recovery/browser/package steps SKIPPED; no final ZIP generated.
Downloaded two evidence-only artifacts: [runtime 15235250514](https://github.com/Kgasil/lilium/actions/runs/46075861681/artifacts/15235250514), 1457 bytes, SHA-256 146b0fdc2819891bc1c17b580cd3053bb111e24927fd9750f5057640d5215cf7; [dependency 15235200558](https://github.com/Kgasil/lilium/actions/runs/46075861681/artifacts/15235200558), 971 bytes, SHA-256 fab29155ba87d669c51a1b3d8caea4159224f6586efe37473b0c19a10e9a214c. Both independently match GitHub metadata, CRC PASS. Actual 29 resolved packages, 0 reported advisories, 0 skipped in pip-audit. This does not cover all native components.
| DLL | Recorded source and bundle SHA-256 |
| --- | --- |
| python314.dll | d8a06cc6ca3348925ea29e343e1c5c5895fe0bb433ff913e1cee44caf358aa6a |
| libcrypto-3.dll | 75495fe0e079ab00d49be740d3c710a0b94e3f74f9648cb7cc9f768fc7f52319 |
| libssl-3.dll | 8957182a9c385bfd9f3f790921de2ddc614cf91f99edbed4e9e5446a46504e32 |
| sqlite3.dll | 99c296ca2b4372418edbdcbd923ab0df2cdbcf406782694d7376f2b01e5010c9 |
DLL bytes absent in evidence archive; hash agreement recorded by CI, not independently rehashed DLLs. No transfer of evidence to subsequent commits without new verification.

## Proven omissions and correction
Re-read old [Lilium portable](https://github.com/Kgasil/lilium/actions/runs/46067881283/artifacts/15231318535): outer f89ec0348c693b0ab017f731c8d9b50f84fd28c58d9e32c7231a4944946f1af9, inner b5e0d1d1c1dd9795bc519093bfd03d4d4992d202dc81c1c9ef206befd339d20f, 109 entries, both CRC PASS. Only three explicit license paths (Click, OpenTelemetry API, Pydantic); no explicit top-level CPython license. Embedded executable archive not expanded; do not infer all notices missing internally. Build script does not explicitly collect Python license and other notices. 
[dcdb5e4](https://github.com/Kgasil/lilium/commit/dcdb5e4e48d840c43ad4903cb3d50eee64f10740) on isolated development/lilium-cycle03-runtime-remediation fixes readiness to exact Windows x64 Python 3.14.10, adds regression and notice collector/tests. Collector requires installed verified CPython LICENSE.txt and copies three versioned upstream texts (OpenSSL 3.5.9, libffi 3.4.4 reference, PyInstaller 6.16.0), verifies Git blob identity, gathers explicit .dist-info license/notice files from build environment with hashes and missing statuses, verifies exact index and all collected bytes in resulting ZIP. Build-environment collection is overinclusive, not a complete mapping to bundled components. No first-party terms changed. [New run 46076360257](https://github.com/Kgasil/lilium/actions/runs/46076360257) pending at review. Rebuild justified by actual diagnostic fix and changed package contents; evidence-only upload, no binaries published. PR #8 and original controlled candidate unchanged.

## Aeris
Re-downloaded [evidence 15232014420](https://github.com/Kgasil/aeris/actions/runs/46070675695/artifacts/15232014420), SHA-256 5fcda4df6daa24c9cc235b60ce234faa8ad37be9f12203369fb1fd47ad06cb21, CRC PASS; license-inventory.json records 17 paths/hashes (Python, PyInstaller, hooks, Inno Setup, OpenSSL, XZ/LGPL, bzip2, libffi, Tcl/Tk, Unicode and others). Actual text bytes absent; no independent legal review of all texts. [Source notice register](https://github.com/Kgasil/aeris/blob/desktop-experience/distribution/third-party-notices/README.md) and [draft terms](https://github.com/Kgasil/aeris/blob/desktop-experience/distribution/TERMS-REVIEW.txt) reviewed. No new verified omission warranting rebuild. Draft terms not evidence of licensed Visual Studio entitlement. AV gate remains FAIL.

## Rights matrix / Matriz de direitos
| Component | Rule and remaining proof |
| --- | --- |
| Python | [PSF license v2 and incorporated notices](https://docs.python.org/3.14/license.html): preserve license/copyright; review actual incorporated components. |
| OpenSSL 3.x | [Apache 2.0](https://www.openssl-library.org/source/license/): preserve license and applicable notices; verify actual package. |
| SQLite | [Core public domain](https://www.sqlite.org/copyright.html), not blanket permission for proprietary extensions. Confirm CPython-supplied exact core and applicable notices. |
| PyInstaller | [GPL exception and Apache portions](https://pyinstaller.org/en/v6.16.0/license.html); permits packaging own applications, does not exempt third-party obligations. |
| Microsoft runtime | [Redistribution terms](https://learn.microsoft.com/cpp/windows/redistributing-visual-cpp-files) and [2026 REDIST list](https://learn.microsoft.com/en-us/visualstudio/releases/2026/redistribution): confirm exact files, provenance, applicable entitlement and terms. No assumption of rights from GitHub hosted runner or possession of DLLs. |
| Inno Setup | [6.x revision history](https://jrsoftware.org/files/is6-whatsnew.htm) requests commercial users purchase license; verify compiler version and commercial context before use. No purchase authorized. |
| XZ/LGPL, other embedded libraries | Identify exact versions, applicable notice/source/relink obligations as relevant; do not infer full coverage from collected notices. |
| First party | No root license assigned; rights remain with respective holders, free-use policy preserved. No trademark or ownership transfer. |

Nine existing partial SBOMs formal schema validation [46074940668](https://github.com/Kgasil/kgasil.github.io/actions/runs/46074940668) retained; no new BOM claims of completeness. New runtime and environment records extend evidence at exact build commit; full dependency graph and binary license mapping pending. Genesis/Argus incidents OPEN and Aeris/Lilium draft PRs unchanged. [Pages 46076046611](https://github.com/Kgasil/kgasil.github.io/actions/runs/46076046611) SUCCESS. No new scan, no change to protection, no distribution approval. Next: verify remediated candidate workflow, review complete notice inventory and actual rights, perform authorized native acceptance only when gates permit.

## Step 05 verified follow-up / Revalidação Etapa 05

[46076360257](https://github.com/Kgasil/lilium/actions/runs/46076360257) SUCCESS: 129 Python tests, readiness, recovery, browser and package PASS, 58 notices verified, two missing explicit collected notices. See [exact evidence and remaining gates](practical-acceptance-cycle-03-step-05.md). No release approval.

## Step 08 — Remaining package notices
Exact versions [openpyxl 3.1.5](https://pypi.org/project/openpyxl/3.1.5/) and [et_xmlfile 2.0.0](https://pypi.org/project/et-xmlfile/2.0.0/) declare MIT on PyPI. Exact source archives not retrieved in this review. The 58 notice records do not establish inclusion of their texts; keep REVIEW_REQUIRED, no redistribution approval. No rebuild requested.
