# GRAAL — Desempenho e acessibilidade / Performance and accessibility · Cycle 02 · Step 05

2026-11-27. No release approval. No native build, malware scan or new executable run.

## Previous workflows / Workflows anteriores
[Rubedo 46072885255](https://github.com/Kgasil/rubedo/actions/runs/46072885255), [Interoperability 46072956643](https://github.com/Kgasil/kgasil.github.io/actions/runs/46072956643), [Pages 46072955924](https://github.com/Kgasil/kgasil.github.io/actions/runs/46072955924): SUCCESS. Genesis/Argus #1 OPEN; Aeris #2 and Lilium #8 draft. No distribution changes.

## Baseline analysis / Análise da baseline
Downloaded [web artifact 15232103800](https://github.com/Kgasil/kgasil.github.io/actions/runs/46070565443/artifacts/15232103800), 4292323 bytes; SHA-256 independently computed ddd7d075b9d5c12efa01bb8f6bbe74740b437f432730293bae81d46df60aa4bc matches GitHub metadata, ZIP CRC PASS. Read 48 original samples, report, and six desktop screenshots. 23 pages, 138 browser views, 48 targeted views, 0 errors. All 48 samples: one H1, zero images missing alt attribute, zero buttons lacking name under the limited DOM heuristic. Six homepages visually retain the distinct dark palettes and logo references in historical 1440px captures. Not a live inspection of all pages or proof of accessibility.

| Page / Página | DOM interactive median ms | DOMContentLoaded max ms | Document transfer max bytes |
| --- | ---: | ---: | ---: |
| Portal | 15.55 | 42 | 74127 |
| Genesis | 17.15 | 43 | 82240 |
| Rubedo | 52.60 | 62 | 43832 |
| Argus | 62.60 | 83 | 380222 |
| Aeris | 17.50 | 42 | 68542 |
| Lilium | 58.35 | 82 | 62056 |
| Genesis business | 17.55 | 33 | 62792 |
| Distribution | 11.85 | 102 | 17909 |

Six samples each: two engines x three viewport sizes; not six repeated runs under identical conditions. Argus HTML contains many inline style/script blocks; size is an optimization candidate, not a proven functional defect. No runtime code changed. External requests blocked by the audit; timing does not reflect real network, cache, Core Web Vitals or input latency.

## Repeatable protocol / Protocolo reproduzível
[aa4e2df](https://github.com/Kgasil/kgasil.github.io/commit/aa4e2df267b68237392ecc1473a8f336afbd8d19) adds three extra local routed navigations per setting (144 expected samples) and 48 320px observations including first Tab, focus-visible and horizontal overflow. Existing 138 views and keyboard/language/menu contrast gates retained; additional timings are diagnostic, not performance gates. Output experience-repeat.json. [Run 46073219557](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073219557) static audit PASS, browser conclusion pending at initial query. No independent cold-cache/network testing claimed.

| Dimension | Reproducible measurement | Acceptance guidance (proposed, not measured SLA) |
| --- | --- | --- |
| Local web | Exact commit, engine/version, viewport; three loads per setting, DOM interactive, DCL, load event, bytes, resource count; median/max | Compare like-for-like runs; investigate repeatable >25% median deterioration across >=3 repetitions, no automatic performance fail from one noisy sample |
| Reflow and keyboard | 320/390/768/1440px, 200% zoom separately, Tab/Shift-Tab, Enter, Escape, focus order, skip target, no unexpected overflow | No loss of content/actions; legitimate scroll regions documented |
| Contrast | Computed foreground/background for known solid surfaces; normal text 4.5:1, large 3:1, UI boundaries 3:1 where applicable; inspect gradients/images manually | Existing menu check is limited; screen-reader and full contrast review pending, not WCAG certification |
| Native startup | Exact authorized artifact, OS, CPU/RAM, power mode; 5 cold starts after full exit, stopwatch to usable UI | Median and max recorded, compare same device/version; no SLA until baseline |
| Latency | Fixed synthetic dataset/model/query; 5 repetitions, separate processing and first/full response | Log units, failures, model version and context; no real data |
| Memory | Peak and steady working set/private bytes for process tree, baseline and after 10 repeated open/close cycles | Record trend, investigate sustained growth; threshold set after native baseline |
| Stability | 10 lifecycle cycles, cancellation/restart, synthetic backup/restore, record crashes, unexpected state and recovery | No unhandled crashes/data loss or unauthorized action in applicable test scope |
| Assistive technology | Windows client with supported reader, names/states, keyboard, zoom, focus and consent controls | Record expected/observed, never infer full coverage from DOM heuristics |

## Product-specific evidence / Evidências por produto
- Genesis: public home/business and lab pages covered by historical web audit. Extension blocked (Microsoft issue #1); no native or extension execution.
- Argus: [development 46067800147](https://github.com/Kgasil/argus/actions/runs/46067800147) passed block 06/07 browser and local lab tests; separate development branch, not clearance for suspended extension.
- Rubedo: [matrix](https://github.com/Kgasil/rubedo/blob/main/docs/homologation-1.0.1.md) records 97 HTTP browser checks, selected contrast 16.62:1 text, 6.27:1 border, 11.7:1 primary; 320px, reduced motion, keyboard and isolated extension. Three manual groups reported passed; raw accessibility logs absent. New documentation CI passed; no new runtime changes.
- Aeris: candidate d6e03bc, [source review 46070675700](https://github.com/Kgasil/aeris/actions/runs/46070675700) SUCCESS; [candidate 46070675695](https://github.com/Kgasil/aeris/actions/runs/46070675695) packaged smoke durations 3004, 2819, 2845 ms (median 2845 ms), not startup/AI. AV gate remains blocked. Native microphone, vision, meeting, cold start, RAM and reader tests not run.
- Lilium: [Windows 46067881283](https://github.com/Kgasil/lilium/actions/runs/46067881283) source/bundle browser, keyboard, labels, viewport, PDF and lifecycle recovery; [issue #9](https://github.com/Kgasil/lilium/issues/9) records synthetic 10k analysis/diagnosis 125 ms in CI and owner-reported satisfactory layout/performance. Not independent physical latency/RAM or reader/zoom evidence. Controlled acceptance retained.

## Limitations / Limitações
No new reproducible runtime defect established by prior evidence. New 320px diagnostics will identify candidates for review; do not treat observations as final accessibility audit. No real hardware memory, model latency, screen-reader or full WCAG audit performed. No new numerical quality score; institutional 9/10 remains unproven. Logos, themes, functionality, free access and all security holds retained. Next: explicit authorized synthetic cross-project integration, without real data or binary promotion.
