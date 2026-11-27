# GRAAL — Catálogo canônico / Canonical catalog

**Revisão / Review:** 2026-11-27 · Etapa / Stage 02 · K&G Vision (iniciativa independente / independent initiative).

Este é o registro central de componentes, versões, distribuição, evidências e pendências. / This is the central record of components, versions, distribution, evidence and pending gates. O marco web/editorial 1.0 não implica versão estável de aplicativos ou extensões. / A web/editorial 1.0 milestone does not imply stable applications or extensions.

**Regra de segurança / Safety rule:** em caso de divergência, prevalece o estado mais restritivo e a investigação específica; não reativar downloads ou remover avisos por atualização deste catálogo. / If records disagree, the most restrictive state and the specific investigation prevail; catalog changes never reactivate downloads or remove warnings. Não ignore proteção, não restaure quarentena; use dados fictícios. / Never bypass protection or restore quarantined files; use synthetic data.

## GRAAL — arquitetura / architecture

| Pilar / Pillar | Projeto / Project | Missão / Mission | Fontes / Sources |
| --- | --- | --- | --- |
| Aprender / Learn | Genesis | Sabedoria e Aplicação / Wisdom & Application | [Site](https://kgasil.github.io/genesis/) · [GitHub](https://github.com/Kgasil/genesis) |
| Construir / Build | Rubedo | Ciência e Inovação / Science & Innovation | [Site](https://kgasil.github.io/rubedo/) · [GitHub](https://github.com/Kgasil/rubedo) |
| Proteger / Protect | Argus | Segurança e Desenvolvimento / Security and Development | [Site](https://kgasil.github.io/argus/) · [GitHub](https://github.com/Kgasil/argus) |
| Simplificar / Simplify | Aeris | Eficiência e Simplicidade / Efficiency & Simplicity | [Site](https://kgasil.github.io/aeris/) · [GitHub](https://github.com/Kgasil/aeris) |
| Evoluir / Evolve | Lilium | Estratégia e Evolução / Strategy & Evolution | [Site](https://kgasil.github.io/lilium/) · [GitHub](https://github.com/Kgasil/lilium) |

K&G Vision coordena as cinco frentes. Argus é o antigo Project Vision; AI Coder é protótipo educacional anterior, não uma sexta frente. / K&G Vision coordinates five initiatives. Argus was formerly Project Vision; AI Coder is an earlier learning prototype, not a sixth initiative.

## Componentes e canais / Components and channels

Estados / States: **WEB** = demonstração pública / public demo; **MANUAL** = experimental, fora das lojas / experimental, outside stores; **PREVIEW** = prévia pública experimental / public experimental preview; **CONTROLLED** = aceitação controlada / controlled acceptance; **SUSPENDED** = instalação suspensa / installation paused. Nenhum destes estados significa produto estável ou certificado. / None means stable or certified.

| ID | Componente / Component | Versão / Version | Estado / State | Canal de referência / Reference channel | Limite ou gate / Limitation or gate |
| --- | --- | --- | --- | --- | --- |
| GEN-01 | Biblioteca editorial / Editorial library | 1.0 | WEB | [Biblioteca](https://kgasil.github.io/genesis/biblioteca.html) | PDFs completos privados; não é curso/certificação / Full PDFs private; not a course/certification |
| GEN-02 | Mini Lab web | 0.1.0 | WEB | [Lab](https://kgasil.github.io/genesis/mini/) | Didático / Educational |
| GEN-03 | Mini Extension | 0.1.0 | SUSPENDED | [Incident #1](https://github.com/Kgasil/genesis/issues/1) | Parecer Microsoft pendente / Microsoft verdict pending |
| GEN-04 | Biblioteca Negócios e Gestão / Business & Management library | Não versionada separadamente / Not separately versioned | WEB | [Business library](https://kgasil.github.io/genesis/business.html) | Leituras introdutórias; 40 volumes complementares planejados, 2.000h nominais; PDFs integrais privados / Introductory readings; 40 planned complementary volumes, 2,000 nominal hours; full PDFs private |
| RUB-01 | Research Workspace | 1.0.1 | WEB | [Workspace](https://kgasil.github.io/rubedo/research/) | Experimental; 257 comparações sintéticas independentes, sem certificação / 257 independent synthetic comparisons, no certification |
| RUB-02 | Mini Lab | 1.0.1 | WEB | [Lab](https://kgasil.github.io/rubedo/mini/) | Modelos experimentais / Experimental models |
| RUB-03 | Mini Extension | 1.0.1 | MANUAL | [Requisitos / Requirements](https://kgasil.github.io/rubedo/#instalar) | Sem certificação ou aprovação de loja / No certification or store approval |
| ARG-01 | Public Research Lab | 1.0; base V10.2 | WEB | [Lab](https://kgasil.github.io/argus/) | Pesquisa, não controle empresarial validado / Research, not a validated enterprise control |
| ARG-02 | Mini Lab | 0.1.0 | WEB | [Lab](https://kgasil.github.io/argus/mini/) | Regras determinísticas; interface PT / Deterministic rules; PT interface |
| ARG-03 | Mini Extension | 0.1.0 | SUSPENDED | [Incident #1](https://github.com/Kgasil/argus/issues/1) | Parecer Microsoft pendente / Microsoft verdict pending |
| AER-01 | Web Lab | Não verificada separadamente / Not separately verified | WEB | [Demo](https://kgasil.github.io/aeris/demo.html) | Demonstração / Demo |
| AER-02 | Extension | 1.0.0 | MANUAL | [Tutorial](https://kgasil.github.io/aeris/extension-preview.html) | 16 ferramentas declaradas; instalação manual / 16 documented tools; manual installation |
| AER-03 | Desktop Windows x64 (IA integrada / integrated AI) | 1.1.0 RC1 | PREVIEW | [Release metadata](https://github.com/Kgasil/aeris/releases/tag/aeris-desktop-1.1.0rc1-ai-setup-preview) | Sem assinatura comercial; ClamAV, licenças e Windows cliente pendentes / Unsigned; ClamAV, licenses and client Windows pending |
| LIL-01 | Web Lab | 1.0 | WEB | [Lab](https://kgasil.github.io/lilium/#lab) | Cenários fictícios / Synthetic scenarios |
| LIL-02 | Mini | 0.1.1 | MANUAL | [Docs](https://github.com/Kgasil/lilium/blob/main/extension/README.md) | Experimental; fora das lojas / Outside stores |
| LIL-03 | Desktop | 0.14.0 | CONTROLLED | [Acceptance guide](https://github.com/Kgasil/lilium/blob/main/docs/clean-machine-validation.md) | Sem abertura geral do piloto / No general pilot access |

A gratuidade das demonstrações e prévias existentes deve ser preservada. Não se presume licença open source, custo zero de APIs externas ou direito de redistribuição de terceiros. / Preserve existing free demos and previews. Do not presume open-source licensing, zero-cost third-party APIs or redistribution rights.

## Evidências e segurança / Evidence and security

Registros consultados em 2026-11-27, não novos testes executados nesta etapa. / Records consulted on 2026-11-27, not new tests performed in this stage.

| Escopo / Scope | Evidência / Evidence | Resultado observado / Observed result | Não comprova / Does not establish |
| --- | --- | --- | --- |
| Portal | [Web audit 46057334371](https://github.com/Kgasil/kgasil.github.io/actions/runs/46057334371) | SUCCESS | Validação manual total / Full manual acceptance |
| Portal | [Provenance 46054254301](https://github.com/Kgasil/kgasil.github.io/actions/runs/46054254301) | SUCCESS | Authenticode comercial ou antimalware / Commercial Authenticode or malware clearance |
| Genesis | [Pages 46007426403](https://github.com/Kgasil/genesis/actions/runs/46007426403) | SUCCESS (deploy) | Liberação da extensão / Extension clearance |
| Argus | [Pages 46007435288](https://github.com/Kgasil/argus/actions/runs/46007435288) | SUCCESS (deploy) | Liberação da extensão / Extension clearance |
| Rubedo | [Validation 46067486777](https://github.com/Kgasil/rubedo/actions/runs/46067486777) | SUCCESS | Validade científica/industrial / Scientific or industrial validity |
| Lilium | [Public lab 46007454470](https://github.com/Kgasil/lilium/actions/runs/46007454470) | SUCCESS | Aceitação do Desktop / Desktop acceptance |
| Aeris | [Source/interface 46065548129](https://github.com/Kgasil/aeris/actions/runs/46065548129) | SUCCESS na consulta desta etapa / At this stage's query | Homologação nativa / Native acceptance |
| Aeris | [Desktop 46065548263](https://github.com/Kgasil/aeris/actions/runs/46065548263) · [PR #2](https://github.com/Kgasil/aeris/pull/2) | PENDING na consulta / At query | Aprovação de release / Release approval |

O workflow de qualidade de produtos já existe: [GRAAL product quality](https://github.com/Kgasil/kgasil.github.io/actions/workflows/graal-product-quality.yml). Resultado recente não confirmado nesta etapa; não atribuir aprovação. / Product quality workflow exists; recent result not confirmed in this stage; do not claim approval.

**Genesis / Argus:** issues abertas na consulta; detecção Trojan:Script/Ulthar.A!ml reportada e submissões à Microsoft documentadas. Não há parecer de liberação confirmado. / Issues open at query; reported detection and documented Microsoft submissions. No confirmed clearance. Preservar originais e bloqueios / Preserve originals and blocks.

**Aeris:** SHA-256 do EXE reportado pelo GitHub: `4001bcc90f84ce67e6e78ea8343132fc9ca9c6567fd610b979c21b6edc1b7ead`. Não recalculado nesta etapa; hash não confirma ausência de malware. / Not recomputed in this stage; digest is not malware clearance. PR de experiência isolada, não aprovar merge/publicação pela existência de CI. / Isolated experience PR; CI alone does not authorize merge or publication.

## Security & Trust — atualização / update 2026-11-27 (Etapa / Stage 03)

[Registro bilíngue de evidências e gates / Bilingual evidence and gate register](security-trust-stage-03.md) · [Inventário automático de segurança / Automated security inventory](https://github.com/Kgasil/kgasil.github.io/actions/workflows/graal-security-inventory.yml).

- Genesis/Argus: incidentes OPEN; sem parecer Microsoft comprovado. / Incidents OPEN; no confirmed Microsoft verdict.
- Aeris: recuperação ClamAV com scan SKIPPED, portanto NOT_TESTED; Defender diagnóstico registrado para a prévia exata, sem certificação. / ClamAV scan SKIPPED, therefore NOT_TESTED; diagnostic Defender record for the exact preview, not certification.
- [Product quality 45919270999](https://github.com/Kgasil/kgasil.github.io/actions/runs/45919270999): cinco regressões e metadados do EXE aprovados no escopo histórico, não liberação de instalação. / Five regressions and EXE metadata passed within historical scope, not installation approval.
- [Inventário 46066415841](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066415841): SUCCESS; cinco ZIPs fixados e cinco baselines de manifestos verificadas, sem execução ou scan. / Five pinned ZIPs and five manifest baselines verified, no execution or scan. Sem aprovação de release / No release approval.
- Licenças, SBOM, dependências transitivas, privacidade em execução e aceitação nativa continuam pendentes. / Licensing, SBOM, transitive dependencies, runtime privacy and native acceptance remain pending.

Nenhum estado de distribuição foi relaxado. / No distribution state was relaxed.

## Identidade e experiência / Identity and experience — Etapa / Stage 04

[Registro de correções e evidências / Change and evidence register](identity-experience-stage-04.md) · [Auditoria ampliada / Extended audit](https://github.com/Kgasil/kgasil.github.io/actions/runs/46067008188).

Seis páginas iniciais e central de distribuição atualizadas com foco de teclado e continuidade de idioma; logos, paleta, funções e restrições preservados. / Six homepages and distribution center updated for keyboard focus and language continuity; logos, palette, functions and holds preserved. Contraste nominal do menu >=6.24:1 nas cores verificadas; não equivale a conformidade integral. / Nominal menu contrast >=6.24:1 for checked colors; not full conformance. Homologação ampliada de navegador pendente na consulta inicial. / Extended browser acceptance pending at initial query.

## Estruturação comercial / Commercial structure — Etapa / Stage 05

[Modelo comercial e catálogo de serviços / Commercial model and service catalog](commercial-model-stage-05.md). Seis famílias propostas: dados/BI, processos, automação, IA aplicada, segurança/governança e planejamento empresarial. / Six proposed families: data/BI, processes, automation, applied AI, security/governance and business planning. Projetos gratuitos preservados; contratação sujeita a escopo, capacidade e formalização. / Free projects preserved; engagements subject to scope, capacity and formalization.

[Homologação da Etapa 04 / Stage 04 audit 46067141357](https://github.com/Kgasil/kgasil.github.io/actions/runs/46067141357): SUCCESS, logs registram 23 páginas, 532 referências, 7 checksums, 138 browser views, 48 verificações específicas de experiência e 0 erros. / Logs record the stated counts and zero errors. Não é certificação integral de acessibilidade, nem aprovação de produtos. / Not full accessibility certification or product approval.

## Integração tecnológica / Technology integration — Etapa / Stage 06

[Arquitetura e contratos / Architecture and contracts](interoperability-stage-06.md) · [Workflow](https://github.com/Kgasil/kgasil.github.io/actions/workflows/graal-interoperability.yml). Projeção JSON do catálogo e contrato de métricas sintéticas v1, adaptadores de referência Rubedo/Lilium, sem conexão operacional entre produtos. / Catalog JSON projection and synthetic metric contract v1, Rubedo/Lilium reference adapters, no production connection between products. Estados de distribuição preservados. / Distribution states preserved. [Run 46067847465](https://github.com/Kgasil/kgasil.github.io/actions/runs/46067847465): SUCCESS, 12/12 testes, 16 componentes, dois registros sintéticos validados, três JSONs gerados; release_approved=false. / 12/12 tests, 16 components, two synthetic records validated, three JSON files generated; no release approval.

## Maturidade empresarial / Business maturity — Etapa / Stage 07

[Governança empresarial / Business governance](business-governance-stage-07.md): responsabilidades funcionais propostas, indicadores, critérios de contratação, gestão de riscos, propriedade intelectual, classificação da informação e planejamento de formalização. / Proposed functional responsibilities, metrics, engagement gates, risk, IP, information classification and formalization planning. Preços, comissões, dados pessoais, contratos e decisões internas permanecem fora do GitHub público. / Pricing, commissions, personal data, contracts and internal decisions remain outside public GitHub.

[Interoperabilidade 46068972194](https://github.com/Kgasil/kgasil.github.io/actions/runs/46068972194): SUCCESS. [Auditoria web 46068972302](https://github.com/Kgasil/kgasil.github.io/actions/runs/46068972302): falha de idioma Rubedo, correção CSP-compatible registrada em [política web](../validation/web/README.md); revalidação pendente. / Rubedo language failure, CSP-compatible fix recorded; revalidation pending. Nenhum bloqueio de segurança relaxado / No security holds relaxed.

## Homologação institucional / Institutional acceptance — Etapa / Stage 08

[Relatório final / Final report](institutional-acceptance-stage-08.md): oito etapas executadas no escopo documentado, homologação integral não concedida. / Eight stages executed in documented scope, full product acceptance not granted. [Web audit 46069975532](https://github.com/Kgasil/kgasil.github.io/actions/runs/46069975532) SUCCESS, 23 páginas, 536 referências, 138 visualizações e 0 erros. [Security inventory 46070267440](https://github.com/Kgasil/kgasil.github.io/actions/runs/46070267440) SUCCESS, Rubedo 1.0.1 baseline reviewed, histórico preservado; nenhum scan novo ou aprovação de release. / Historical package retained; no new scan or release approval. Avaliação ponderada de evidência: cinco projetos 5.95/10 em média, portal 6.75/10, meta 9/10 não comprovada. / Evidence maturity mean 5.95/10, portal 6.75/10; 9/10 not established. Genesis/Argus suspended, Aeris preview and draft PR blocked by AV evidence, Lilium controlled acceptance. Preserve all distribution gates.

## Ciclo 02 — Excelência técnica / Cycle 02 — Technical excellence

[Plano e evidências / Plan and evidence](technical-excellence-cycle-02.md). [Inventário de fontes / Source inventory 46070606868](https://github.com/Kgasil/kgasil.github.io/actions/runs/46070606868): SUCCESS, 5 testes e seis snapshots; não equivale a SBOM resolvido nem revisão de licenças. / Five tests and six snapshots; not resolved SBOM or license clearance. Aeris dependency evidence gate strengthened on draft branch; current CI pending at query. / Gate de dependências reforçado na branch draft; CI pendente na consulta. [Diagnóstico web / Web diagnostics](https://github.com/Kgasil/kgasil.github.io/actions/runs/46070565443) pending browser conclusion at initial query. No release approval; all restrictions retained.

## Ciclo 02 — Etapa 02 / Cycle 02 — Step 02: Artifact trust

[Relatório de evidências / Evidence report](artifact-trust-cycle-02-step-02.md). [Aeris 46070675695](https://github.com/Kgasil/aeris/actions/runs/46070675695): regression and OSV correction PASS; AV gate FAIL. Evidence ZIP 15232014420 independently hash-verified, installer and portable digests recorded in report (binaries absent). Defender 2 SKIPPED, bundle explicit no threats; ClamAV 28194 verified but stale, 0 scans. Genesis/Argus incidents OPEN, distribution suspended. / Incidentes abertos; instalação suspensa. No release approval; no rebuild requested. [Web baseline 46070565443](https://github.com/Kgasil/kgasil.github.io/actions/runs/46070565443) SUCCESS with 48 diagnostic samples, 138 views, 0 errors. / Diagnóstico local, não certificação.

## Ciclo 02 — Etapa 03 / Cycle 02 — Step 03: SBOM and licensing

[Relatório / Report](sbom-license-cycle-02-step-03.md) · [Inventários CycloneDX / CycloneDX inventories](sbom/cycle02-step03/). Nine partial versioned source/environment BOMs: source snapshots 6, Aeris build 8 packages, Lilium review 29 and build 35. No inferred dependency graph, formal schema validation or licensing clearance. Five CI archive SHA-256 and CRC checks PASS; Lilium portable internal ZIP b5e0d1d1c1dd9795bc519093bfd03d4d4992d202dc81c1c9ef206befd339d20f, 109 entries, verified merge checkout. Aeris OSV and current Lilium pip-audit no known advisories in scoped environments; historical Lilium 89 advisories in 2 packages. / Nenhuma aprovação de binário antigo ou atual. Three explicit Lilium license files and 17 Aeris recorded notices; rights, embedded components and notices require review. / Revisão de direitos e componentes incorporados pendente. All distribution gates retained; no new license or release.

## Ciclo 02 — Etapa 04 / Cycle 02 — Step 04: Native acceptance and recovery

[Relatório / Report](native-recovery-cycle-02-step-04.md) · [Ficha / Record](native-acceptance-record-cycle02.md). Aeris evidence ZIP and four Lilium outer/inner ZIP SHA-256 + CRC verified again; Aeris binaries absent, candidate AV gate remains blocked. Lilium hosted recovery PASS, six maintainer-reported groups recorded in [issue #9](https://github.com/Kgasil/lilium/issues/9), case-level gaps and licensing remain; controlled candidate 0.14.0 / Mini 0.1.3 not promoted. Rubedo 1.0.1 reported acceptance retained with documentation clarification; Genesis/Argus still suspended. / Bloqueios preservados; nenhuma recompilação solicitada nem publicação de binários. No new quality score.

## Ciclo 02 — Etapa 05 / Cycle 02 — Step 05: Performance and accessibility

[Relatório / Report](performance-accessibility-cycle-02-step-05.md). Original web artifact 15232103800 SHA-256 and CRC independently verified; 48 samples analyzed per page, 138 browser views, zero audit errors; six historical desktop screenshots reviewed. New [repeat diagnostics 46073219557](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073219557) adds three additional navigations per setting and 320px observations, browser conclusion pending at initial query. / Protocolo de desempenho e acessibilidade documentado, sem medição física nova, certificação ou aprovação de distribuição. All holds retained.

## Ciclo 02 — Etapa 06 / Cycle 02 — Step 06: Operational integration

[Relatório / Report](operational-integration-cycle-02-step-06.md) · [Demo CI 46073646096](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073646096). SUCCESS, 12/12 tests; trace ZIP 15234096746 SHA-256 and CRC independently checked, all five stage digests recomputed. [Second demo run 46073695494](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073695494) and [contracts 46073695480](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073695480) SUCCESS. `graal.demo.trace.v1` connects five source-level synthetic stages with four explicit ordered approvals, commit/file hashes and recomputation; no live app connection, real data or release. / Demonstração sintética, sem conexão entre aplicativos instalados. [Web 46073219557](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073219557): 144 timings, 48 320px observations, zero overflow, five Genesis Firefox language failures. Audit waits for scroll stability without weakening assertions; [revalidation](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073590229) SUCCESS confirmed in Step 07; zero errors, no isolated proof of original root cause. Distribution restrictions unchanged.

## Ciclo 02 — Etapa 07 / Cycle 02 — Step 07: Business pilots

[Relatório e apresentação / Report and presentation](business-pilots-cycle-02-step-07.md) · [CI 46074010357](https://github.com/Kgasil/kgasil.github.io/actions/runs/46074010357) SUCCESS, 13/13 tests; [artifact 15234262121](https://github.com/Kgasil/kgasil.github.io/actions/runs/46074010357/artifacts/15234262121) ZIP SHA-256/CRC and canonical report digest independently verified. Three fixed synthetic pilots: BI (BRL 3500/2200/1300, 37.14% margin), process (5 occurrences/3 pending tasks/2 duplicates/0 remaining), AI governance (8/8 known classifications, 4 reviews, 0 autonomous approvals). Not customer results, production integrations, model evaluation or release approval. / Dados fictícios, sem alegações de contrato, cliente, ganhos reais ou implantação. [Web revalidation 46073590229](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073590229) SUCCESS; 144 samples, 48 observations at 320px, 0 errors. All holds retained.

## Ciclo 02 — Etapa 08 / Cycle 02 — Step 08: Final acceptance

[Relatório final / Final report](technical-excellence-cycle-02-step-08.md): eight stages executed, full acceptance NOT granted. Comparable evidence maturity five-project mean 5.95 -> 6.20/10, portal 6.75 -> 7.00. Performance partial credit based on local web diagnostics, all other weights unchanged; 9/10 unproven. [Pilots 46074112242](https://github.com/Kgasil/kgasil.github.io/actions/runs/46074112242), [demo 46074112293](https://github.com/Kgasil/kgasil.github.io/actions/runs/46074112293), [contracts 46074112219](https://github.com/Kgasil/kgasil.github.io/actions/runs/46074112219), [Pages 46074112306](https://github.com/Kgasil/kgasil.github.io/actions/runs/46074112306) SUCCESS. Nine partial SBOM JSONs re-read; no license clearance or schema certification. GEN-04 updated to 40 planned volumes per current Genesis plan; no PDFs published. All holds unchanged.

## Ciclo 03 — Etapa 05 / Cycle 03 — Step 05: Practical candidate acceptance

[Relatório / Report](practical-acceptance-cycle-03-step-05.md). [Lilium 46076360257](https://github.com/Kgasil/lilium/actions/runs/46076360257) SUCCESS: 129 Python tests, runtime, readiness, hosted recovery/browser and staged package PASS; 58 notice hashes verified; two missing explicit collected package notices require review. Recorded ZIP SHA-256 36b2fce4c58a73eae01de57f3113a39c3bc1a31e7e8bf325cad0fc7f52c46ffc; binary not retained, AV/license NOT_TESTED. / Testes web com dados fictícios elegíveis; instalação de novos candidatos não autorizada. Existing states unchanged.

## Ciclo 03 — Etapa 06 / Cycle 03 — Step 06: Usable web integration

[Laboratório integrado / Integrated lab](https://kgasil.github.io/graal/) · [Relatório / Report](web-integration-cycle-03-step-06.md). [CI 46081125322](https://github.com/Kgasil/kgasil.github.io/actions/runs/46081125322) SUCCESS: 12 demo + 13 pilot tests, exact reproduction from five pinned source revisions, Chromium/Firefox end-to-end permissions, export digest, revocation, responsive widths, keyboard, language, tampered evidence rejection. / Demonstração sintética gratuita, sem integração de aplicativos instalados ou aprovação de binários. No customer data, production deployment or full WCAG claim. All distribution holds unchanged.

## Ciclo 03 — Etapa 07 / Cycle 03 — Step 07: Commercial preparation

[Apresentação comercial / Business presentation](https://kgasil.github.io/graal/#services) · [Roteiro e evidências / Guide and evidence](commercial-readiness-cycle-03-step-07.md). [Lab 46082070759](https://github.com/Kgasil/kgasil.github.io/actions/runs/46082070759) SUCCESS, 25 integration/pilot tests and two browsers. [General audit 46082088264](https://github.com/Kgasil/kgasil.github.io/actions/runs/46082088264) SUCCESS: 24 pages, 552 links, 144 browser views, 48 targeted views, zero errors. / Escopos propostos, aceite sintético e simulação de qualificação local, sem coleta de dados, contrato, cliente ou aprovação de binários. All existing holds unchanged.

## Ciclo 03 — Etapa 08 / Cycle 03 — Step 08: Evidence-based closure

[Relatório final / Final report](final-acceptance-cycle-03-step-08.md): all seven workflows at 064950f SUCCESS; 24 pages, 553 links, 144 browser views, zero errors. Five evidence ZIPs independently hashed/CRC PASS. Lilium remediated CI PASS, exact binary not retained, licensing and AV pending. Five-project maturity remains 6.20/10, portal 7.00/10; 9/10 NOT proven. Commercial web presentation deployed per Pages, external fetch unavailable. / Todos os bloqueios preservados; sem nova aprovação de binários.

## Maturidade / Maturity

A meta é qualidade comprovada >=9/10, não uma nota de marketing. / Target is evidenced quality >=9/10, not a marketing score. A cobertura documental observada na Etapa 01 é histórica: portal/Rubedo/Lilium 8/10; Genesis/Argus/Aeris 6/10. Não é avaliação atualizada de qualidade nem liberação. / Stage 01 documentary coverage is historical, not a current quality rating or release approval.

| Indicador / Indicator | Base observada / Observed baseline | Meta / Target |
| --- | --- | --- |
| Projetos com README PT/EN / Projects with PT/EN README | 5/5 (estrutura, não tradução integral / structure, not full translation) | 5/5 com revisão / reviewed |
| Páginas iniciais com navegação comum / Homepages with shared navigation | 6/6 | 6/6 |
| Repositórios institucionais com SECURITY.md / Institutional repositories with SECURITY.md | 6/6 | 6/6 |
| Incidentes de instalação abertos / Open installation incidents | 2 | 0 antes de reativar / before reactivation |
| Aprovação integral de qualidade / Full quality approval | Não comprovada / Not established | >=9/10 e gates aplicáveis / and applicable gates |
| Aceitação nativa Desktop / Native desktop acceptance | Pendente Aeris/Lilium / Pending | Evidência reproduzível / Reproducible evidence |

## Processo de atualização / Update process

1. Responsável pela manutenção verifica release, commit, CI, estado de incidentes e autorização antes de mudar o registro. / Maintainer verifies release, commit, CI, incidents and authorization before updating.
2. Atualizar esta fonte primeiro, registrar revisão e link da evidência exata. Estados pendentes e resultados históricos devem ser explicitamente identificados. / Update this source first, record review date and exact evidence link. Label pending states and historical results.
3. READMEs apontam para este registro; descrições específicas, histórico e avisos de segurança locais permanecem. A central pública mantém avisos estáticos por segurança mesmo se o registro estiver indisponível; revisar a consistência com o catálogo antes de mudar uma versão. / READMEs point here; local descriptions, history and safety notices remain. The public distribution center retains static safety notices even if this catalog is unavailable; check consistency before version changes.
4. Qualquer mudança para estado menos restritivo requer evidência específica do pacote final e aprovação documentada; manter plano de reversão. / Any less restrictive state requires final-package evidence and documented approval; retain rollback plan.
5. Revisar a cada release ou incidente e periodicamente com a auditoria GRAAL. Não alterar binários nesta rotina. / Review at each release or incident and periodically alongside GRAAL audit. Do not change binaries in this routine.

## Referências / References

- [Central pública / Public distribution center](https://kgasil.github.io/distribuicao.html)
- [Política de segurança / Security policy](https://github.com/Kgasil/kgasil.github.io/blob/main/SECURITY.md)
- [Critérios de distribuição / Release gates](https://github.com/Kgasil/kgasil.github.io/blob/main/validation/distribution/README.md)
- [Política de assinatura / Signing policy](https://github.com/Kgasil/kgasil.github.io/blob/main/validation/signing/README.md)
- [Auditoria web / Web audit](https://github.com/Kgasil/kgasil.github.io/blob/main/validation/web/README.md)
- [Qualidade de produtos / Product quality](https://github.com/Kgasil/kgasil.github.io/blob/main/validation/products/README.md)

**Aprender · Construir · Proteger · Simplificar · Evoluir / Learn · Build · Protect · Simplify · Evolve.**

## Rubedo 1.0.1 — 27/11/2026
Publicação aprovada pelo idealizador após validação CI e aprovação manual relatada de Chrome/Edge Windows, Defender e acessibilidade. / Maintainer-approved publication after CI and reported manual acceptance; no independent antivirus or accessibility certification. [Matriz / Matrix](https://github.com/Kgasil/rubedo/blob/main/docs/homologation-1.0.1.md) · [PR #1](https://github.com/Kgasil/rubedo/pull/1). Canais WEB/MANUAL preservados; sem publicação em loja. / WEB/MANUAL channels unchanged; no store listing.
