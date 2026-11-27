# GRAAL — qualidade dos produtos e aceitação

[Pipeline de regressão](https://github.com/Kgasil/kgasil.github.io/actions/workflows/graal-product-quality.yml) — semanal, manual e em alterações do pipeline. Cada job registra o commit real do projeto. Testes não autorizam distribuição por si só.

- Genesis / Argus: integridade do ZIP original sem instalação, testes de fonte, interações do Mini Lab com dados fictícios. Os pacotes seguem suspensos.
- Rubedo: regressões dos modelos, pacote, referência e interface no Chromium.
- Aeris: integridade e paridade dos ZIPs da extensão, testes Node, interações das seis ferramentas do Web Lab; inspeção separada de hash, tamanho e estado Authenticode do EXE público exato em Windows, sem execução.
- Lilium: fonte Mini fixada, compilação temporária reproduzível, testes de cálculos e UI. Desktop continua em prévia controlada.

## Aceitação nativa ainda pendente
Não instalar versões com detecção aberta. Para cada candidato elegível, registrar versão, SHA-256, ambiente Windows 10/11 limpo, proteção e definições, requisitos, resultado de instalação/remoção/atualização, permissões, falha de dependências, interrupção/reinício, acessibilidade e dados residuais. Aeris: adicionalmente testar consentimento e progresso de instalação Ollama, cancelamento, internet indisponível, download de modelo, primeira resposta local e explicação de funcionalidades indisponíveis. Não marcar PASS sem execução e evidências. Lilium: usar a [matriz de aceitação existente](https://github.com/Kgasil/lilium/blob/main/docs/manual-acceptance-matrix.md). Genesis/Argus: [incidente Genesis](https://github.com/Kgasil/genesis/issues/1) e [incidente Argus](https://github.com/Kgasil/argus/issues/1) aguardam parecer.

O job Windows não altera proteção, não executa instalador e não equivale a análise antimalware. O hash fixado identifica a prévia atual; qualquer alteração de pacote exige revisão explícita, não atualização automática do hash. Nenhum certificado, assinatura, aceite real ou aprovação de fornecedor é presumido.
