# K&G Vision — Maintenance and acceptance — 28/11/2026

Fase de estruturação concluída; manutenção, pesquisa e homologação continuam. Acesso público gratuito às demonstrações; nenhum novo binário liberado. A meta de qualidade 9/10 permanece um requisito, não uma nota já comprovada. / Structuring phase closed; maintenance, research and acceptance continue. Public demos remain free; no new binaries released. The 9/10 quality target remains a gate, not an achieved score.

| Projeto / Project | Disponibilidade e próxima ação / Availability and next action |
| --- | --- |
| Genesis · Aprender / Learn | Biblioteca pública; 75 PDFs originais + 40 edições complementares privadas, 5.280 páginas físicas; 6.000 horas nominais planejadas, não certificadas. Mini 0.1.0 suspenso, [Microsoft #1](https://github.com/Kgasil/genesis/issues/1); revisão acadêmica continua. / Public library; 115 private working documents, planned nominal hours; Mini installation paused; academic review continues. |
| Rubedo · Construir / Build | Public Lab, Workspace e Mini 1.0.1 experimentais; oito modelos, 12 protocolos e Studio; testes CI e aceitação relatada pelo idealizador. / Experimental public 1.0.1; first-party CI and maintainer-reported acceptance, not independent certification. |
| Argus · Proteger / Protect | Laboratório público 1.0, base V10.2; Mini 0.1.0 suspenso, [Microsoft #1](https://github.com/Kgasil/argus/issues/1); licença, proteção de branch e homologação ainda pendentes. / Public research lab; Mini installation paused; license, branch protection and acceptance pending. |
| Aeris · Simplificar / Simplify | Extensão 1.0.0, 16 ferramentas, manual; Desktop 1.1.0 RC1, 50 ferramentas, prévias históricas sem liberação estável. Novo candidato não gerado; [ClamAV](https://github.com/Kgasil/aeris/actions/runs/46140744764) inalterado; [PR #2](https://github.com/Kgasil/aeris/pull/2). / Manual extension; historical desktop previews, no new cleared candidate. |
| Lilium · Evoluir / Evolve | Web Lab 1.0, Mini 0.1.1 manual; Desktop 0.14.0 em homologação fechada, sem novo ZIP disponível. [PR #12](https://github.com/Kgasil/lilium/pull/12) integrou retenção; ClamAV e aceite exato pendentes. / Public web lab and manual Mini; closed Desktop acceptance, no new ZIP. |

[Central de distribuição / Distribution center](https://kgasil.github.io/distribuicao.html)


## Evidências e pendências / Evidence and open gates

- [Relatório do ciclo 03](final-acceptance-cycle-03-step-08.md): homologação integral não concedida. / Full acceptance not granted.
- Microsoft REDIST: [CI 46139207345](https://github.com/Kgasil/aeris/actions/runs/46139207345), duas DLLs 14.51.36247.0 idênticas; [Aeris gate](https://github.com/Kgasil/aeris/actions/runs/46140686137), [Lilium gate](https://github.com/Kgasil/lilium/actions/runs/46140661469). Elegibilidade e termos declarados pelo titular; não é parecer independente. / Two exact DLL source matches; maintainer attestation, not independent legal clearance.
- ClamAV: [preflight](https://github.com/Kgasil/aeris/actions/runs/46138765670) base assinada 28194 desatualizada; [DNS](https://github.com/Kgasil/aeris/actions/runs/46140744764) inalterado. Não recompilar até preflight assinado ≤24h e demais condições. / No build until signed preflight ≤24h and remaining gates.
- Aeris: [branch de preparação](https://github.com/Kgasil/aeris/tree/aeris-controlled-release-handoff); Lilium: [merge #12](https://github.com/Kgasil/lilium/pull/12). Validar inventário, avisos, antivírus completos, retenção restrita, aceite físico Windows e ≥9/10 antes de publicar. / Validate exact inventory, notices, full scans, restricted retention, physical Windows acceptance and ≥9/10 before publication.
- Microsoft malware verdicts: owner checks private submission history; no restoration, exceptions or bypass. / Titular consulta parecer privado; sem restauração, exceções ou contorno.
- Maintenance policy: act on concrete new evidence, failures or approved improvements; no repetitive audit cycle. / Atuar somente sobre nova evidência concreta, falha ou evolução aprovada. Public links and free access preserved; no paid service or binary publication authorized.
