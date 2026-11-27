# GRAAL — política operacional de distribuição

Aplicável aos sites e versões publicadas pela iniciativa independente K&G Vision. O marco web 1.0 não implica que aplicativos, extensões ou instaladores estejam estáveis.

## Estados
- Web público: demonstração acessível, com limites e dados fictícios.
- Experimental/manual: versão identificada, canal oficial e riscos explícitos; não equivale a produto estável ou publicação em loja.
- Controlado: somente aceitação autorizada, sem download geral.
- Suspenso: manter avisos e não promover download enquanto a investigação estiver aberta.
- Estável: somente após satisfazer os critérios aplicáveis abaixo e decisão documentada.

## Checklist de liberação
1. Versão, commit, plataforma, requisitos, mudanças, limitações e canal oficial identificados.
2. Pacote final imutável e SHA-256, comparação com fontes e inventário de dependências; revisão de licenças.
3. CI funcional e regressão, teste em máquina limpa com proteção ativa, instalação/remoção/atualização e recuperação verificadas.
4. Scan do pacote final com definições atualizadas; detecções investigadas e parecer registrado. Nunca modificar bytes para contornar detecção. Hash e CI não substituem scan.
5. Assinatura digital quando aplicável, ou declarar explicitamente ausência; assinatura não é garantia de segurança.
6. Documentação de permissões, privacidade, armazenamento e suporte. Não prometer recursos não validados.
7. Decisão de distribuição registrada com evidências, revisão de avisos, histórico e plano de reversão. Não retirar aviso automaticamente por um resultado de CI genérico.

## Estado em 26/11/2026
Genesis Mini e Argus Mini: incidentes abertos e submissões Microsoft pendentes. Aeris Desktop 1.1.0 RC1: prévia experimental não assinada, análise independente pendente. Lilium Desktop: aceitação controlada. Rubedo Mini, Aeris Extension e Lilium Mini: distribuição experimental manual conforme documentação de cada projeto. Não há aprovação nova de binários nesta alteração.

[Central pública](https://kgasil.github.io/distribuicao.html) · [Auditoria web](https://github.com/Kgasil/kgasil.github.io/actions/workflows/graal-web-audit.yml) · [Segurança](../../SECURITY.md)
