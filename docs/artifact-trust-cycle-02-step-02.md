# GRAAL — Segurança e confiança dos artefatos / Artifact security and trust · Cycle 02 · Step 02

2026-11-27. **No release approval / Sem aprovação de distribuição.** Evidence review only; no new executable, scan, protection change or rebuild requested in this institutional step.

## Verified CI / CI confirmado
- [Web 46070565443](https://github.com/Kgasil/kgasil.github.io/actions/runs/46070565443): SUCCESS, 23 pages, 138 browser views, 48 diagnostic samples, zero errors, zero missing alt attributes or unnamed buttons in targeted checks. Local DOM interactive 10–98 ms; DOMContentLoaded 10.7–102 ms; document transfer 17909–380222 bytes. Not real-user metrics or WCAG certification.
- [Source inventory 46070606868](https://github.com/Kgasil/kgasil.github.io/actions/runs/46070606868), [interoperability 46070737171](https://github.com/Kgasil/kgasil.github.io/actions/runs/46070737171), [Pages 46070737489](https://github.com/Kgasil/kgasil.github.io/actions/runs/46070737489): SUCCESS.
- Aeris [source review 46070675700](https://github.com/Kgasil/aeris/actions/runs/46070675700) SUCCESS; [candidate 46070675695](https://github.com/Kgasil/aeris/actions/runs/46070675695) FAILURE at AV gate. Four new OSV fail-closed tests passed on Ubuntu and Windows; 566 tests run per regression job (not 1132 distinct tests). Actual build OSV response NO_REPORTED_ADVISORIES for eight PyPI build packages; excludes embedded runtime, OS and optional software.

## Exact candidate evidence / Evidência do candidato exato
Commit `d6e03bc428fa3506fe5ec06d243e14438722432e`, [draft PR #2](https://github.com/Kgasil/aeris/pull/2), [job 140747038575](https://github.com/Kgasil/aeris/actions/runs/46070675695/job/140747038575).
Downloaded [evidence-only ZIP 15232014420](https://github.com/Kgasil/aeris/actions/runs/46070675695/artifacts/15232014420), 62,339 bytes; independently computed SHA-256 matched GitHub metadata and upload log: `5fcda4df6daa24c9cc235b60ce234faa8ad37be9f12203369fb1fd47ad06cb21`. Examined JSON and logs directly. Evidence ZIP contains no installer or portable executable archive. Artifact retention is temporary; preserve this summary. Candidate package digests below are recorded by CI, not independently computed from absent binaries.

| Target / Alvo | Bytes | SHA-256 recorded / registrado |
| --- | ---: | --- |
| Setup.exe | 12964170 | f336945dcdbc3bad234468a649b7a7e9a5a7414c81648437fed5af8798ff4741 |
| Portable ZIP | 13942538 | 44fabffd6a3086e25a98ac21d6583a4ead89c79e7ba5366666b08cbc950b7b31 |
| Bundled Aeris.exe | not separately recorded here | c57112bd453fba412d6d5dff08902c7ca8172587a4bdbb493aa14d12cdc32365 |

Package inventory, SHA256SUMS and ClamAV candidate hash fields agree. ClamAV post-scan inventory integrity PASS; not evidence of a completed scan. Hosted install, terms refusal, installed self-test, 49 installed files, reinstall and uninstall preservation PASS with synthetic marker. Installer NotSigned; 17 notices inventoried, license review pending. Three packaged smoke runs 3004, 2819, 2845 ms; not real-user startup/AI latency.

## Antivirus / Antivírus
Defender: enabled, engine 1.1.26100.4, signature updated from 1.463.440.0 to 1.463.499.0; age 26572 s (within 24h). Exact target-specific exclusion logs report all three targets not excluded (exit 1). Scan logs: Setup and Portable explicitly SKIPPED despite exit 0; bundle explicit no-threat result; 0 matched detections in queried event scope. Overall INCONCLUSIVE. Cause of skips not established; no inference of false positive or clearance.
ClamAV 1.5.5: official scanner archive verification true; daily version 28194, build 2026-11-25 06:26 UTC; sigtool Verification OK; age 227246 s (>86400), official DNS also advertised 28194. No scan targets executed (empty list). Overall INCONCLUSIVE. No change to freshness limit.
No rebuild requested: repeating the same environment without changed evidence is not a corrective action. Preserve the current gate; require exact approved candidate bytes and authorized clean Windows client environment with active protection and fresh verified definitions. If same bytes are unavailable, any reconstruction is a NEW candidate and requires new hashes and evidence.

## Other products / Outros projetos
- [Genesis #1](https://github.com/Kgasil/genesis/issues/1), [Argus #1](https://github.com/Kgasil/argus/issues/1) OPEN, no comments or official verdict observed. Installation SUSPENDED; do not restore quarantine. Historical ZIP SHA values (not confirmed quarantined-file hashes): Genesis 654d46b77439a4c196bd6c70bda0fc664f1f59e8a6fe745cad76e10ed7fc67b4; Argus 3248c6c204b5651a9f63c5630547e1a18f021a0ffdc08feaba1566e7925fb8b1.
- Rubedo [46069960180](https://github.com/Kgasil/rubedo/actions/runs/46069960180) SUCCESS and [central inventory 46070267440](https://github.com/Kgasil/kgasil.github.io/actions/runs/46070267440) SUCCESS. v1.0.1 ZIP a2fd6017a4f5a3813b924b0d249f91090f57857054ff565b80dc633d5eb95424. Manual experimental state unchanged.
- Aeris existing public [preview](https://github.com/Kgasil/aeris/releases/tag/aeris-desktop-1.1.0rc1-ai-setup-preview) GitHub asset digest 4001bcc90f84ce67e6e78ea8343132fc9ca9c6567fd610b979c21b6edc1b7ead differs from candidate. Do not transfer evidence between them.
- Lilium [Windows review 46067881283](https://github.com/Kgasil/lilium/actions/runs/46067881283) and [dependency review 46067881301](https://github.com/Kgasil/lilium/actions/runs/46067881301) SUCCESS in scoped CI. Native client acceptance and exact distribution approval not inferred. Controlled state retained.

## Next / Próximo
Review full per-artifact SBOM, licenses and redistribution rights. Keep all gates; no new binaries, certification or quality score granted. Preserve five projects, logos, features and free access.
