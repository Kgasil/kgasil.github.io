# GRAAL — Identidade e experiência / Identity and experience · Stage 04

Revisão / Review: 2026-11-27. Preserve official branding, functions, free access and distribution holds.

## Correções / Changes
- Six homepages: keyboard skip link with focusable main, named PT/EN controls, translated titles and navigation label, English deep-link initialization (?lang=en), language propagation along ecosystem and distribution links.
- Distribution center: translated skip link, focusable main, named language controls and language propagation on ecosystem links.
- Six READMEs: reconcile Rubedo historical validation status with [CI 46007461543](https://github.com/Kgasil/rubedo/actions/runs/46007461543); preserve scientific/industrial limitations. Profile README already described this distinction.
- No logo asset, binary, version or security state changed. Genesis and Argus issues remain open. / Nenhum logo, binário, versão ou estado de segurança alterado.

## Evidências / Evidence
- [Stage 03 Pages](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066541414), [security inventory](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066415841), [Stage 02 web audit](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066111392): SUCCESS.
- Six homepage files re-read after commit: matching returned Git blobs, skip/main and language script present, six canonical navigation links and shared shield reference preserved. Genesis/Argus hold text present. / Seis páginas relidas com blobs coincidentes e avisos preservados.
- Nominal WCAG contrast calculation from declared menu colors, normal background #101B2B and active #20334C: K&G Vision 15.64/11.58, Genesis 9.23/6.84, Rubedo 9.45/7.00, Argus 8.42/6.24, Aeris 10.05/7.44, Lilium 8.90/6.59. All exceed 4.5:1 for normal text in this specific palette. This is not a site-wide computed contrast or accessibility audit. / Cálculo nominal restrito à paleta do menu; não comprova acessibilidade integral.
- [Extended web audit](https://github.com/Kgasil/kgasil.github.io/actions/runs/46067008188): includes targeted keyboard, language, title, direct English URL, link and menu contrast checks for seven pages in Chromium/Firefox at 390, 768, 1440 px. Run in progress at review; verify final result before claiming PASS. / Execução em andamento nesta consulta; confirmar conclusão.
- Innove Consult card retains partner link, external logo reference, text alternative, explicit dimensions and no-referrer policy. Third-party image availability and rights not independently verified; use an authorized local asset only if supplied/approved. / Marca e link preservados; disponibilidade e autorização não comprovadas.

## Limitações / Limitations
Direct public-page retrieval failed in this session; source inspection is not a live visual review. No comprehensive screen-reader test, 200% zoom review, complete translation inventory, all-element contrast audit or partner brand authorization verification. / Abertura pública indisponível nesta sessão; inspeção de código não é revisão visual ao vivo. Revisões integrais pendentes. No 9/10 product or website approval claimed. / Sem aprovação integral 9/10.

[Canonical catalog / Catálogo](graal-catalog.md) · [Web audit policy / Política](../validation/web/README.md).

## Correção adicional após CI / Additional CI-driven fix

[Run 46066889994](https://github.com/Kgasil/kgasil.github.io/actions/runs/46066889994) FAILED: logs report exactly two errors in the newly added Genesis business.html page (missing GRAAL labels and centered navigation CSS). Fixed in [Genesis commit 72610df](https://github.com/Kgasil/genesis/commit/72610df33422db3b4dccb942b406c0b4ba6b6b98), preserving its planned-volume disclosures and adding shared keyboard/language controls. Source re-read confirmed navigation, CSS and language script. The earlier extended run may still use the pre-fix snapshot. [Audit commit ba9e45a](https://github.com/Kgasil/kgasil.github.io/commit/ba9e45a365569e14ef5135e0c79e7cfff68d7c1b) adds this eighth page to targeted checks. [New run 46067141357](https://github.com/Kgasil/kgasil.github.io/actions/runs/46067141357): queued at query; no PASS claimed. / CI anterior falhou por dois erros de navegação na página de negócios; correção aplicada e conferida no código, nova rodada pendente. Não declarar aprovação até conclusão.
