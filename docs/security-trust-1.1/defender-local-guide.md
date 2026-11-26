# GRAAL 1.1 — Alternativa local sem custo adicional
Este roteiro é uma alternativa ao runner hospedado; não é resultado de scan nem autorização para instalação. Use uma máquina Windows de teste já disponível, atualizada, sem dados reais, ou VM descartável com licença existente. A Área Restrita do Windows é uma opção incluída nas edições compatíveis (Pro, Enterprise e Education), sujeita a requisitos de hardware e à confirmação do Defender ativo dentro do ambiente. Se o Defender não estiver plenamente ativo nessa VM, não use esse ambiente para aprovar arquivos. Não compre licenças nem contrate serviço. Não use computador de produção para investigar o Genesis enquanto o alerta não for esclarecido.

## 1. Conferência do ambiente
Abra Segurança do Windows > Proteção contra vírus e ameaças > Atualizações de proteção > Verificar se há atualizações. Mantenha as proteções e SmartScreen ativos. Não altere políticas, exclusões ou configurações para conseguir um resultado.
No PowerShell, consulte somente:
```powershell
Get-MpComputerStatus | Select-Object AntivirusEnabled,AMServiceEnabled,RealTimeProtectionEnabled,BehaviorMonitorEnabled,AMRunningMode,AMProductVersion,AMEngineVersion,AntivirusSignatureVersion,AntivirusSignatureLastUpdated
$p = Get-MpPreference
[pscustomobject]@{
  DisableArchiveScanning = $p.DisableArchiveScanning
  PathExclusions = @($p.ExclusionPath | Where-Object { $_ }).Count
  ExtensionExclusions = @($p.ExclusionExtension | Where-Object { $_ }).Count
  ProcessExclusions = @($p.ExclusionProcess | Where-Object { $_ }).Count
}
```
Gate: serviço, antivírus e proteção em tempo real ativos; modo Normal; definições com idade de 0 a 24 h; análise de arquivos compactados habilitada; nenhuma exclusão explícita (ou parar para revisão). Se não atender, não baixar nem analisar amostras nesse ambiente. Não compartilhe caminhos privados.

## 2. Originais
Consulte a [matriz de hashes](defender-validation.md). Use o commit fixo do backup de cada extensão; para artefatos CI, baixe o ZIP externo original e compare também o hash registrado na auditoria correspondente. Links de artefato CI exigem login e podem expirar. O backup privado da etapa 01 pode ser usado se os hashes corresponderem. O pacote experimental do Lilium Mini tem um ZIP próprio e não equivale ao ZIP público do repositório inteiro. A etapa 07 do Aeris Desktop segue separadamente; não duplicar a execução.
- Genesis: commit 4c255490569cfadee6839d316f14dd7e67de7909, somente em ambiente isolado elegível. Download público direto permanece suspenso.
- Argus: commit 3c498bc9d776fe8c0919e5d003ff23ac22dee0aa.
- Rubedo: commit cf5274868c11e5b6cfb41a5ad1a1c49c2cf1fa45.
- Aeris Extension: commit 35fa603bf110f2d23d98012b06547d33c9c7a2de.
- Lilium Mini: [CI 45736783251, artefato 15078758847](https://github.com/Kgasil/lilium/actions/runs/45736783251/artifacts/15078758847); ZIP público fixado em 447d7414f20e28f6c0440647f2b7be71fc44e71d precisa de registro próprio.
- Lilium Desktop: [CI 45722415976, artefato 15071874653](https://github.com/Kgasil/lilium/actions/runs/45722415976/artifacts/15071874653).
Não ignore bloqueios no download. Não restaure itens da quarentena.

## 3. Verificação e análise
Para cada arquivo original, calcule SHA-256 com Get-FileHash -Algorithm SHA256 (especifique o arquivo com -LiteralPath). Compare com a matriz; se divergir, pare. Na Segurança do Windows, escolha análise personalizada do arquivo/pasta ou clique com botão direito > Mostrar mais opções > Verificar com Microsoft Defender. Aguarde o resultado e confira Histórico de proteção e eventos do Defender. Se houver detecção, interrompa e registre nome, hash, versão e ação do antivírus. Não execute ZIPs, BATs ou EXEs; não instale extensões durante esta etapa. Após análise do ZIP sem detecção e verificação de caminhos/CRC/manifesto, examine separadamente o conteúdo extraído em pasta nova, mantendo o original intacto. Reconfira hashes e condições de proteção ao final. Se arquivo foi removido ou alterado, não restaure; marque detecção ou teste incompleto.
## 4. Registro a devolver
Data/hora e fuso; versão/build do Windows; estado de proteção antes e depois; motor/plataforma/definições e data; hash esperado/observado; arquivo examinado; escopo e conclusão da análise; histórico de detecções e ação; hash pós-scan; limitações. Remova informações privadas. Um resultado limpo não é garantia futura, assinatura ou aprovação de release. Se houver detecção, não publique amostras nem conclua falso positivo sem investigação.
## Referências Microsoft
- https://learn.microsoft.com/pt-br/windows/security/application-security/application-isolation/windows-sandbox/
- https://support.microsoft.com/pt-br/windows/experience/scan-an-item-with-windows-security
- https://support.microsoft.com/pt-br/windows/security/threat-malware-protection/virus-and-threat-protection-in-the-windows-security-app
