# GRAAL Security & Trust 1.1 — Etapa 10 / Tratamento de detecções
Data: 2026-11-26. Estado: investigação e procedimento registrados; incidente Genesis aberto, causa indeterminada. Nenhum novo scan, envio externo ou aprovação de distribuição.

## Inventário de evidências
Consulta às Issues dos seis repositórios antes da abertura do incidente: Genesis, Argus, Rubedo, Aeris e portal sem Issues; Lilium com Issue #1 de aceite manual, não detecção de malware. Ausência de relato não comprova segurança.
- Genesis Mini 0.1.0: alerta relatado pelo titular durante instalação, sem captura, produto, nome de ameaça ou hash do arquivo afetado. Original 10.651 bytes, SHA-256 654d46b77439a4c196bd6c70bda0fc664f1f59e8a6fe745cad76e10ed7fc67b4; [auditoria estática e CI](https://github.com/Kgasil/genesis/blob/main/docs/security-trust-1.1/genesis-mini-review.md). Cinco entradas, zero permissões especiais, 19 testes aprovados; não estabelece segurança antimalware. Download direto permanece suspenso. [Incidente público #1](https://github.com/Kgasil/genesis/issues/1).
- Argus Mini, Rubedo Mini, Aeris Extension, Lilium Mini e Lilium Desktop: nenhum relato específico de detecção localizado nesta consulta; scan com proteção ativa não realizado.
- Aeris Desktop: [diagnóstico anterior](https://github.com/Kgasil/aeris/blob/main/downloads/rc5-defender-diagnostic-evidence.json) sem ameaças nos alvos examinados; EICAR positivo foi controle de teste, não detecção no produto. Proteção em tempo real inativa; não equivale à análise exigida. Etapa 07 separada.
- [Etapa 09](defender-validation.md): os dois runners falharam no gate de ambiente. Não é detecção nos pacotes. Nenhum resultado de scan novo.

## Triagem e contenção
1. Interromper instalação/execução quando houver alerta. Preservar originais autorizados no backup; nunca restaurar quarentena, desativar proteção, contornar SmartScreen ou alterar bytes para evitar detecção.
2. Registrar produto e texto exato, código/nome da ameaça se houver, data/fuso, versão do sistema/motor/definições, versão do aplicativo, nome do arquivo e hash disponível, contexto e ação da proteção. Redigir dados privados; não publicar amostras nem logs pessoais em Issues.
3. Comparar hash da amostra identificada com o [inventário de originais](defender-validation.md). Se não puder identificar, manter indeterminado. Não presumir que o ZIP e um arquivo extraído têm o mesmo hash.
4. Classificar: detecção de malware/PUA pelo antivírus; aviso reputacional SmartScreen/Smart App Control; aviso de navegador/instalação manual ou política administrativa; indeterminado. Um aviso de procedência não é necessariamente detecção de malware. Não classificar PUA automaticamente como falso positivo.
5. Investigar em ambiente isolado elegível conforme [roteiro](defender-local-guide.md). Não executar amostra bloqueada. Se houver falha real de segurança, corrigir a causa, validar regressões, preservar original e gerar novo candidato com novo hash. Não alterar recursos legítimos apenas para escapar de detecções.

## Encaminhamento oficial de possível falso positivo
Portal: https://www.microsoft.com/en-us/wdsi/filesubmission . A Microsoft aceita arquivos suspeitos ou incorretamente detectados, inclusive de desenvolvedores. Identificar o componente correto (Defender Antivirus ou outro produto efetivamente envolvido). A reputação insuficiente de um aplicativo novo não tem garantia de revisão manual/remoção de aviso; consultar a documentação SmartScreen específica. Avisos do Chrome/Edge ou políticas administrativas devem seguir o canal correspondente, não ser automaticamente enviados como malware.
Somente após identificar o alerta, obter autorização para compartilhar a amostra exata e verificar que não contém informações privadas, utilizar cópia original autorizada e preservada, sem restaurar quarentena. Se o próprio envio for bloqueado, não contornar; buscar orientação do fornecedor. Preencher como desenvolvedor quando aplicável, explicar a função, fornecer hash, versão, mensagem exata e evidências. Registrar protocolo, data, parecer e hash; não prometer prazo ou alteração de reputação. Não anexar amostras a Issues. Sem submissão efetivada nesta etapa.

### Minuta em inglês (preencher antes de enviar)
We develop Genesis Mini, a local study browser extension (Manifest V3). A user reported a warning during manual installation of version 0.1.0. We are investigating the exact cause and request review of the identified file, not an exemption from security controls.
Product reporting the warning: [confirmed product].
Exact detection or warning: [verbatim text].
Affected file and SHA-256: [verified affected file and hash].
Original reference archive: Genesis-Mini-v0.1.0-install.zip, SHA-256 654d46b77439a4c196bd6c70bda0fc664f1f59e8a6fe745cad76e10ed7fc67b4.
Observed date and definitions: [verified information].
The original archive was checked against its source; static review and functional CI do not constitute malware clearance. Direct download links are paused. Please provide your determination for the exact sample.
Source: https://github.com/Kgasil/genesis
Do not send with placeholders or an unidentified file.

## Encerramento
Status OPEN_UNCLASSIFIED para Genesis; NOT_TESTED para scan novo dos demais. Só encerrar incidente após parecer ou investigação documentada, causa esclarecida, correção quando necessária e nova análise válida dos bytes finais. Não prometer ausência de alertas, assinatura ou aprovação. Nenhuma mudança de código, versão, pacote, layout, proteção ou custo contratado. A etapa 11 pode verificar prontidão, mas não marcar gates pendentes como aprovados. Etapa 12 não reativa o download Genesis sem resolução.
## Referências oficiais (consultadas em 26/11/2026)
- https://www.microsoft.com/en-us/wdsi/filesubmission/
- https://learn.microsoft.com/en-us/defender-endpoint/defender-endpoint-false-positives-negatives
- https://learn.microsoft.com/en-us/unified-secops/submission-guide
- https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/
- https://learn.microsoft.com/windows/apps/package-and-deploy/smartscreen-reputation


## Atualização — identificador da detecção Genesis
Evidência do titular: Histórico de proteção de 26/11/2026 às 15:18, categoria Cavalo de Tróia, gravidade Grave, ação Removido; ZIP de origem oficial. O link Saiba mais identifica Trojan:Script/Ulthar.A!ml, ThreatID 2147751841. A página específica da enciclopédia não retornou conteúdo na consulta. Main e snapshot do ZIP têm blob 323c674cf71a0336f519e37446f5f1806e3a7f17 e bytes coincidentes, sem hash observado do arquivo removido. Incidente #1 permanece aberto como DETECTION_REVIEW_REQUIRED. Submissão oficial ainda não realizada. A análise de possível falso positivo deve tratar a cópia original preservada, sem contornar proteções ou modificar bytes para evitar a detecção. Referências consultadas: https://www.microsoft.com/en-us/wdsi/filesubmission ; https://learn.microsoft.com/en-us/unified-secops/submission-guide .