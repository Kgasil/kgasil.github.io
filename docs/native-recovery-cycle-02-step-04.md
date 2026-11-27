# GRAAL — Homologação nativa e recuperação / Native acceptance and recovery · Cycle 02 · Step 04
2026-11-27. **No new release approval / Sem nova aprovação de distribuição.** No new executable run, build or scan in this institutional review. Existing product-specific approvals and restrictions retained.

## Verified workflow closure / Revalidação
[Pages 46071764129](https://github.com/Kgasil/kgasil.github.io/actions/runs/46071764129) and [interoperability 46071764215](https://github.com/Kgasil/kgasil.github.io/actions/runs/46071764215) SUCCESS. Aeris d6e03bc draft PR #2 remains open, source review 46070675700 SUCCESS, candidate 46070675695 AV gate FAILURE; Lilium draft PR #8 remains open, head b4b0f698, Windows 46067881283 and Mini 46067881286 SUCCESS. Genesis/Argus incidents #1 OPEN. Rubedo 46069960180 SUCCESS. No rerun of existing candidate builds requested.

## Exact artifacts / Artefatos exatos
Recomputed SHA-256 and ZIP CRC in local read-only inspection:
- Aeris evidence-only ZIP 15232014420, SHA-256 5fcda4df6daa24c9cc235b60ce234faa8ad37be9f12203369fb1fd47ad06cb21, 33 entries, CRC PASS. Candidate installer/portable not available as bytes: recorded hashes f336945dcdbc3bad234468a649b7a7e9a5a7414c81648437fed5af8798ff4741 / 44fabffd6a3086e25a98ac21d6583a4ead89c79e7ba5366666b08cbc950b7b31. Do not transfer evidence to the public preview.
- Lilium Desktop 0.14.0 artifact 15231318535: wrapper f89ec0348c693b0ab017f731c8d9b50f84fd28c58d9e32c7231a4944946f1af9; inner b5e0d1d1c1dd9795bc519093bfd03d4d4992d202dc81c1c9ef206befd339d20f, 23956079 bytes, 109 entries. Manifest build commit 871c2e5c91654a8bf518e6f3d1b78c6f0ee8e13d (PR merge).
- Lilium Mini 0.1.3 artifact 15231721743: wrapper 4358a8ff7d99590f7836ccd9bf73b75872324dd37a19df2ccf86d4dc620f0efc; inner 5b960d274a670a278a3db5211aec71c94416f615c62881548d108806b7f8f495, 6511 bytes, 6 entries. Both Lilium wrapper/inner CRC PASS. Exact artifact records in [issue #9](https://github.com/Kgasil/lilium/issues/9). No binaries promoted.
- Prior SBOM bundle SHA-256 951d0ee971336ace81aa97b272ad024ef10b06883ba8c27d6ab756285d7e6b41, 13 entries CRC PASS. [Versioned source/environment BOMs](sbom/cycle02-step03/) remain partial; no license clearance.
- Rubedo 1.0.1 runtime commit 166763ff57b920f18d947fe365311cb01f10d1f4, recorded exact ZIP a2fd6017a4f5a3813b924b0d249f91090f57857054ff565b80dc633d5eb95424, [acceptance matrix](https://github.com/Kgasil/rubedo/blob/main/docs/homologation-1.0.1.md). Not downloaded again in this step.

## Matrix / Matriz
PASS_CI = automated evidence in bounded runner scope; REPORTED = maintainer report, not independent measurements; NOT_RUN = no case-level evidence; BLOCKED = prerequisite not met; N/A = scenario not applicable to the component. No implied PASS for entire group.

| Component | Hosted / CI evidence | Maintainer report | Native or remaining gates | State |
| --- | --- | --- | --- | --- |
| Genesis Mini 0.1.0 | Historical package integrity | No new report | Extension tests BLOCKED; Microsoft #1 open | SUSPENDED |
| Rubedo Mini 1.0.1 | Chromium isolated install, calculations, JSON, Studio restore/migration, privacy boundaries | Three groups reported passed 27 Nov: Chrome/Edge Windows, updated Defender no detections, visual/keyboard/accessibility | Individual reload/uninstall, browser versions, logs, screen-reader details NOT_RUN in this audit; no broader certification | MANUAL experimental approved as previously recorded |
| Argus Mini 0.1.0 | Historical package integrity; development tests distinct | No new report | Extension tests BLOCKED; Microsoft #1 open | SUSPENDED |
| Aeris Desktop RC1 d6e03bc | 566 regressions each Ubuntu and Windows; hosted Windows Server 20348: hashes, terms refusal, install, self-test, 49 installed files, terms, same-version reinstall, uninstall preserving synthetic marker PASS | No new acceptance of exact candidate | AV BLOCKED (Defender 2 skipped; ClamAV stale no scans); Windows 10/11 client, upgrade from earlier supported version, native recovery and physical AI/mic/screen/meeting/OCR NOT_RUN | Candidate blocked |
| Aeris Extension 1.0.0 | Historical manifest/integrity checks | No new report | Exact browser installation, optional local AI consent and revocation NOT_RUN | Existing MANUAL experimental |
| Lilium Desktop 0.14.0 exact candidate | Windows job 140737504294: source and bundled lifecycle 3 launches, token rotation, persistence and backup recovery PASS; independent downloaded executable job 140738422856 SUCCESS | Six groups reported passed 27 Nov per issue #9: Defender no detections, Desktop, ten modules, Mini Chrome/Edge, Ollama, performance/layout | Clean client edition/build, cold start/RAM measurements, detailed recovery/rollback, per-model and consent/fallback, screen-reader/contrast, license review NOT_RUN/not documented | CONTROLLED, no promotion |
| Lilium Mini 0.1.3 candidate | 46067881286 PASS, local popup and package, not installed extension in that job | Chrome/Edge reported passed as above | Case-level profile and permissions/reload/clear evidence not supplied; no promotion | CONTROLLED candidate; existing 0.1.1 MANUAL unchanged |

Aeris installed self-test scope: catalog/window construction, not real audio, AI, DPAPI roundtrip or performance. Source regression tests are not installed-app acceptance. Lilium is portable, not MSI; upgrade means isolated replacement/migration, not an installer claim. No repetition of six already reported Lilium groups: only collect missing details in authorized environment.

## Reusable acceptance record / Ficha reutilizável
Use [native acceptance record](native-acceptance-record-cycle02.md). For each exact candidate, record environment, SHA-256, scanner status and case-level expected/observed results; keep private evidence outside public repo. Unknown fields remain unknown; no approval inferred from a hash, CI success, or general satisfaction.

## Corrections / Correções
Rubedo English README said manual acceptance pending despite existing PT and matrix report: [0a9450d](https://github.com/Kgasil/rubedo/commit/0a9450dd8a06bd63095e106baf9e39d91713fca1). Matrix rows implied detailed logs/measurements not supplied; corrected attribution without changing previous experimental authorization or package: [465f23f](https://github.com/Kgasil/rubedo/commit/465f23ff32220cddc0bae155054783619943553c). Historical internal 10/10 is 7 points automated + 3 reported, not institution-wide 9/10 proof. No reproducible runtime defect established in this review. Preserve all holds, logo, free access, and five projects.

## Next / Próximo
Prioritize missing evidence and physical tests only when prerequisites pass. No bypass of security or quarantine. Licensing, full artifact SBOM and production-grade performance/accessibility still pending; no new score. Review web/native performance and accessibility in Step 05.
