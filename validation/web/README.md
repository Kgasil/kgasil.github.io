# Auditoria pública do ecossistema GRAAL

Workflow: [GRAAL public website audit](https://github.com/Kgasil/kgasil.github.io/actions/workflows/graal-web-audit.yml). Execução diária às 07:20 (Brasília), manual e em alterações do site institucional ou do script. Cada rodada registra os commits reais dos seis repositórios. As alterações nos projetos irmãos são cobertas na próxima rodada ou por execução manual.

- Descobre HTML público rastreado, excluindo backups, popups de extensão e Workspace/API local.
- Verifica navegação, referências locais e entre sites, âncoras, nomenclatura, versões dos Mini Labs e SHA-256 dos pacotes com manifestos de checksums.
- Chromium e Firefox em 390, 768 e 1440 px: carregamento, erros JavaScript, largura horizontal, fundo e centralização do menu. Capturas dos casos com problemas e páginas principais no artefato de CI.
- Preserva bloqueios de distribuição do Genesis/Argus enquanto os incidentes estiverem abertos; mudança de política exige revisão explícita.
- Não executa binários, não envia dados pessoais, não instala extensões e não acessa APIs externas durante os testes de navegador. Hash e testes web não equivalem a análise antimalware, certificação de segurança, acessibilidade completa ou teste manual de todas as funcionalidades.

Segurança: [Genesis #1](https://github.com/Kgasil/genesis/issues/1) e [Argus #1](https://github.com/Kgasil/argus/issues/1) aguardam parecer Microsoft; [Aeris prévia](https://github.com/Kgasil/aeris/releases/tag/aeris-desktop-1.1.0rc1-ai-setup-preview) permanece experimental, com análise independente pendente. Não retirar avisos sem comprovação específica do pacote final.

Relatórios e screenshots ficam no artefato de cada execução por 14 dias. A primeira execução precisa ser conferida antes de declarar aprovação dos testes de navegador.

## Regressão Rubedo / Rubedo regression — 2026-11-27

[Run 46068972302](https://github.com/Kgasil/kgasil.github.io/actions/runs/46068972302): 24 erros de idioma no Rubedo (quatro verificações em seis combinações navegador/viewport). A CSP `script-src 'self'` impede a execução do script inline introduzido na Etapa 04. Correção: mover sincronização GRAAL para o script externo local, sem afrouxar CSP, e remover script inline ([95b8a20](https://github.com/Kgasil/rubedo/commit/95b8a201782bcc22fd3f4107a8a3ac1939ceddb5), [fe81fe1](https://github.com/Kgasil/rubedo/commit/fe81fe1f1522430259eccea5d15131bb93356d82)). / Move synchronization to local external script, remove blocked inline script, retain CSP. Reexecutar a auditoria antes de declarar aprovação. / Re-run audit before claiming acceptance.
