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
| RUB-01 | Research Workspace | 1.0 | WEB | [Workspace](https://kgasil.github.io/rubedo/research/) | Experimental; sem validação científica independente / No independent scientific validation |
| RUB-02 | Mini Lab | 1.0.0 | WEB | [Lab](https://kgasil.github.io/rubedo/mini/) | Modelos experimentais / Experimental models |
| RUB-03 | Mini Extension | 1.0.0 | MANUAL | [Requisitos / Requirements](https://kgasil.github.io/rubedo/#instalar) | Sem certificação ou aprovação de loja / No certification or store approval |
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
| Rubedo | [Validation 46007461543](https://github.com/Kgasil/rubedo/actions/runs/46007461543) | SUCCESS | Validade científica/industrial / Scientific or industrial validity |
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
