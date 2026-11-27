# GRAAL — Security & Trust · Etapa / Stage 03

Revisão / Review: 2026-11-27. Auditoria de evidências de primeira parte, não certificação independente. / First-party evidence review, not independent certification.

## Resultados confirmados / Confirmed records

- Etapa 02: [Pages](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066111043), [procedência / provenance](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066111341) e [auditoria da central / distribution audit](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066090568): SUCCESS. [Auditoria web final / Final web audit](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066111392): consultar resultado atual / check current result.
- [Product quality 45919270999](https://github.com/Kgasil/kgasil.github.io/actions/runs/45919270999): cinco jobs de regressão e job de metadados do instalador Aeris SUCCESS; não comprova ausência de malware. / Five regression jobs and Aeris installer metadata job SUCCESS; not malware clearance.
- [Genesis #1](https://github.com/Kgasil/genesis/issues/1) e [Argus #1](https://github.com/Kgasil/argus/issues/1): OPEN, submissões relatadas em 26/11, parecer Microsoft não confirmado. Não restaurar quarentena ou promover instalação. / OPEN, submissions reported Nov 26; no confirmed Microsoft verdict. Never restore quarantine or promote installation.
- [Aeris ClamAV recovery 45893625088](https://github.com/Kgasil/aeris/actions/runs/45893625088): job SUCCESS, mas etapas de banco, build e scan SKIPPED. Resultado antimalware NOT_TESTED. / Job SUCCESS but database, build and scan steps SKIPPED; malware result NOT_TESTED.
- [Aeris preview 45895378300](https://github.com/Kgasil/aeris/actions/runs/45895378300): job e passos de Defender SUCCESS, log registra assinatura 1.463.485.0 e detecção do controle inerte EICAR; escopo diagnóstico Windows Server 2022. Sem aceitação Windows cliente, assinatura comercial ou ClamAV. / Job and Defender steps SUCCESS; log records signature version and EICAR control detection; diagnostic Windows Server scope, no client acceptance, commercial signing or ClamAV.
- [Aeris PR #2](https://github.com/Kgasil/aeris/pull/2): aberta e draft; [review](https://github.com/Kgasil/aeris/actions/runs/46065548129) SUCCESS; [Desktop CI](https://github.com/Kgasil/aeris/actions/runs/46065548263) em execução na consulta inicial. Sem autorização de merge ou release. / Open draft; Desktop CI in progress at initial query. No merge or release approval.

## Integridade e permissões / Integrity and permissions

| Componente / Component | SHA-256 de referência / Reference SHA-256 | Estado / State |
| --- | --- | --- |
| Genesis Mini ZIP | `654d46b77439a4c196bd6c70bda0fc664f1f59e8a6fe745cad76e10ed7fc67b4` | SUSPENDED |
| Argus Mini ZIP | `3248c6c204b5651a9f63c5630547e1a18f021a0ffdc08feaba1566e7925fb8b1` | SUSPENDED |
| Rubedo Mini ZIP | `1799dc6ccadd786eb960f38c4f7d67cf241e9630942a9e69daebfe96fcfe6ab2` | MANUAL |
| Aeris Extension ZIP | `e77e6e8596c14e54f22303e7a5d368356c19eaa79df8c8597752790755d9a0d9` | MANUAL |
| Aeris source ZIP | `d0f064c1b73c46465171cc1fb208b530ed66573e054c2ca211b216547bbb3c00` | MANUAL |
| Aeris Desktop EXE (AI preview) | `4001bcc90f84ce67e6e78ea8343132fc9ca9c6567fd610b979c21b6edc1b7ead` | PREVIEW, unsigned |
| Lilium Mini | Manifest git blob `e1abd929ef84c5088d6e65a2f02a549b59e5a109` (not SHA-256) | MANUAL, source-based |

Hashes de referência lidos dos manifestos de checksums/release; não recalculados nesta sessão. O workflow histórico de qualidade recalculou os hashes aplicáveis, incluindo o EXE, e verificou Authenticode NotSigned. / Reference hashes read from checksum manifests/release; not recomputed in this session. Historical quality workflow recomputed applicable hashes including EXE and checked Authenticode NotSigned.

Genesis, Argus, Rubedo e Lilium: manifestos fonte MV3 sem permissões declaradas, host permissions, content scripts ou background. Aeris: manifesto do pacote não recuperado diretamente; verificador existente fixa activeTab, scripting, storage e acesso opcional http://127.0.0.1/*, CSP com conexão local 127.0.0.1:11434. / Four source manifests declare no such capabilities; Aeris package verifier pins the listed permissions and loopback CSP. Permissões mínimas não provam privacidade do comportamento. / Minimal permissions do not prove runtime privacy.

## Licenças, dependências e privacidade / Licenses, dependencies and privacy

- Inventário raiz da auditoria anterior não revelou LICENSE nos cinco projetos; não declarar open source ou redistribuição autorizada sem revisão. / Prior root inventories did not show LICENSE files; do not claim open-source or redistribution rights without review.
- Lilium: requirements.txt fixa fastapi, starlette, uvicorn, httpx, openpyxl, defusedxml; requirements-build inclui pyinstaller e Pillow. Inventário transitivo, SBOM e análise de vulnerabilidades ainda pendentes. / Direct pins observed; transitive inventory, SBOM and vulnerability assessment pending.
- Aeris Desktop: documentação da branch desktop-experience prevê consentimento explícito, instalação opcional Ollama via WinGet e modelos separados, loopback e requisitos de voz/tela. Revisão de termos, inventário de dependências e validação de consentimento em Windows cliente pendentes. / Documentation describes consent, optional Ollama/WinGet and separate models; terms, dependency inventory and native consent validation pending. Não assumir que documentação prova execução. / Documentation is not runtime evidence.
- Uso de dados fictícios; revisar finalidade, permissões, retenção, exclusão, exportação e destinos de rede antes de piloto com dados reais. / Synthetic data only; review purpose, permissions, retention, deletion, export and network destinations before real-data pilots.

## Melhoria operacional / Operational improvement

[Novo workflow / New workflow](https://github.com/Kgasil/kgasil.github.io/actions/workflows/graal-security-inventory.yml): verificação semanal/manual e em alteração do próprio workflow, usando GitHub Actions e Python padrão, sem instalar ou executar os pacotes analisados. Fixa hashes de ZIPs e capacidades MV3, registra commits e presença de arquivos de licença/dependências. / Weekly/manual and workflow-change checks with standard Python, no installation or execution of reviewed packages. Pins ZIP hashes and MV3 capabilities, reports commits and root license/dependency files. Divergências interrompem a verificação; atualizar baseline somente após revisão autorizada. / Drift fails the check; update baseline only after authorized review. Não é scanner de malware ou auditoria de licenças. / Not a malware scanner or license audit.

## Gates obrigatórios / Mandatory gates

Antes de qualquer mudança para distribuição menos restritiva: identificar hash final e commit, inventário de dependências (incluindo transitivas e modelos), revisar licenças, validar permissões e privacidade, executar regressão e aceitação em máquina limpa com proteção ativa, obter resultado de scan aplicável com definições atualizadas, investigar detecções e registrar decisão/autorização. / Before any less restrictive distribution: identify exact final artifact and commit, dependency inventory (including transitive and models), license review, permissions/privacy validation, regression and clean-machine acceptance with active protection, applicable current-definition scan, detection review and documented authorization. Ausência de evidência = PENDING ou NOT_TESTED, não PASS. / Missing evidence = PENDING or NOT_TESTED, not PASS.

Nenhum binário novo, parecer Microsoft, certificação ou nova aprovação de release nesta etapa. / No new binary, Microsoft verdict, certification or new release approval in this stage.

## Primeira execução comprovada / Verified first execution

[Run 46066415841](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066415841), commit do workflow `c2b439ecb152219934b02fb823c6ee3412fceeb2`: SUCCESS, job [140732689702](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066415841/job/140732689702). Logs conferidos / Logs reviewed. Cinco baselines de manifestos PASS, cinco ZIPs fixados verificados (Genesis, Argus, Rubedo, dois Aeris); Lilium conferido por blob de manifesto, não SHA-256 de ZIP. / Five manifest baselines PASS, five pinned ZIPs checked; Lilium manifest blob checked, not ZIP SHA-256. Nenhum arquivo de licença raiz encontrado nos cinco snapshots; Lilium apresentou os dois requirements. / No root license files found in five snapshots; Lilium reported both requirements files. Scan, aceitação nativa e revisão de licenças NOT_TESTED; release_approved=false.

Auditoria final da Etapa 02 [46066111392](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066111392): SUCCESS confirmado / confirmed.
