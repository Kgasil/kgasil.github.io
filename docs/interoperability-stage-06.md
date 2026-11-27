# GRAAL — Interoperabilidade / Interoperability · Stage 06

2026-11-27. Versão do contrato / Contract version: 1.0.0. Implementação de referência offline, somente dados sintéticos; não é integração operacional de produção. / Offline reference implementation, synthetic data only; not production integration.

## Arquitetura / Architecture

| Projeto / Project | Interface observada / Observed interface | Integração / Integration |
| --- | --- | --- |
| Genesis | Biblioteca estática, Manifest V3; leitura complementar de negócios | Metadados no catálogo; referências educacionais, sem exportador novo / Catalog metadata; educational references, no new exporter |
| Rubedo | [JSON de referência](https://github.com/Kgasil/rubedo/blob/main/examples/reference-results.json), modelos JS | Adaptador de referência para espera e tempo total da fila / Reference adapter for queue wait and total time |
| Argus | [Regras locais](https://github.com/Kgasil/argus/blob/main/extension/core.js) | Apenas metadados; nenhum texto ou segredo transferido / Metadata only, no text or secret transfer |
| Aeris | [Integração interna](https://github.com/Kgasil/aeris/blob/desktop-experience/desktop/aeris/integration.py), confirmação e permissões | Apenas metadados; sem alterar branch ou conectar dados reais / Metadata only; no branch change or live-data connection |
| Lilium | [API local](https://github.com/Kgasil/lilium/blob/main/core/README.md), [motor de métricas](https://github.com/Kgasil/lilium/blob/main/core/metrics.py) | Adaptador de totais sintéticos em centavos BRL / Synthetic totals adapter in BRL cents |

## Contratos / Contracts

`graal.catalog.v1`: projeção gerada de `docs/graal-catalog.md`, com IDs, projeto, nome, versão, distribuição, referência e limites. Fonte única continua Markdown; não editar JSON gerado. Alterações de estados restritos falham até revisão explícita da baseline e aprovação documentada. / Generated projection from canonical Markdown; do not edit generated JSON. Restricted state changes fail until explicit baseline review and documented approval.

`graal.metric.v1`: objeto com schema, source, source_schema, data_kind=synthetic e metrics. Cada métrica possui id, unit e value. Campos desconhecidos, métricas duplicadas, tipos incompatíveis, unidade errada, JSON com chaves duplicadas e valores não finitos são rejeitados. / Unknown fields, duplicate metrics/JSON keys, incompatible types, wrong units and nonfinite values rejected. Arquivo de registro limitado a 16 KiB. / Record file limited to 16 KiB.

- Rubedo: queue.wait / queue.total em minutos (strings decimais), caso de referência [6,10] exclusivamente. / Minutes as decimal strings, fixed reference case only.
- Lilium: revenue / cost / result em BRL_cent (inteiros), sem arredondar centavos; receita e custo não negativos, resultado reconciliado no adaptador. / Integer cents, no rounding; nonnegative revenue/cost and reconciled result in adapter.
- Não agregar métricas de origens, períodos ou unidades distintos. Nenhum campo de texto livre, dados pessoais, credenciais, voz, tela ou reuniões. O rótulo synthetic não prova anonimização; o fluxo de teste usa fontes fictícias fixas. / Never aggregate incompatible sources, periods or units. No free-text, personal data, credentials, audio, screen or meetings. The synthetic label does not prove anonymization; CI uses fixed synthetic sources.

## Configuração e evolução / Configuration and evolution

Python padrão, sem pacote de terceiros ou serviço obrigatório. / Standard-library Python, no third-party package or mandatory service. Contratos são independentes das versões de aplicativo; alterações incompatíveis exigem novo identificador v2 e adaptador explícito, preservando v1. / Contracts independent of app versions; breaking changes require v2 and explicit adapter, preserving v1. Não modificar os formatos nativos existentes. / Do not change native formats.

```sh
python3 validation/integration/graal.py registry docs/graal-catalog.md catalog.json
python3 validation/integration/graal.py validate example.json
```

[Workflow](https://github.com/Kgasil/kgasil.github.io/actions/workflows/graal-interoperability.yml): execução semanal, manual ou por mudança de contrato/catálogo. Clona fontes públicas Rubedo e Lilium, registra commits, executa testes de contrato e motor sintético Lilium; gera três JSONs como artefatos temporários. / Weekly/manual and contract/catalog-change execution. Clones public snapshots, records commits, runs contract tests and synthetic Lilium engine; produces three temporary JSON artifacts. Nenhum binário publicado, conexão automática entre apps ou mudança de permissões. / No binaries published, automatic app connections or permission changes.

## Limites / Limits

A validação de contrato não comprova segurança de dados reais, homologação nativa, interoperabilidade de interface, validade científica ou qualidade 9/10. / Contract validation does not prove real-data security, native acceptance, UI interoperability, scientific validity or 9/10 quality. A próxima evolução deve adicionar adaptadores explícitos por caso de uso, consentimento e testes de ponta a ponta antes de conectar produtos. / Next evolution requires explicit use-case adapters, consent and end-to-end testing before connecting products.

## Evidência executada / Executed evidence

[Run 46067847465](https://github.com/Kgasil/kgasil.github.io/actions/runs/46067847465), [job 140737394654](https://github.com/Kgasil/kgasil.github.io/actions/runs/46067847465/job/140737394654): SUCCESS, 12 tests passed, 16 components, two contract validations, three JSON artifacts uploaded. Rubedo snapshot `f2193e4bed955bd1290f822c5538435c0b59cdb2`; Lilium snapshot `d92babb96cd0ad1b514709fdede3ee9ceae95e64`. Rubedo queue: 9 min waiting, 15 min total; Lilium fixed synthetic CSV: 30000 revenue cents, 18000 cost cents, 12000 result cents. Sem aprovação de release / No release approval.
