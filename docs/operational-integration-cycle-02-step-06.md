# GRAAL — Integração operacional / Operational integration · Cycle 02 · Step 06
2026-11-27. **Synthetic source-level demonstration only / Demonstração sintética em código-fonte. No release approval.**

## Previous checks / Revalidação
[Interoperability 46073306356](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073306356) and [Pages 46073307023](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073307023) SUCCESS. [Web 46073219557](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073219557) FAILURE: five assertions on English selection in Genesis Firefox 390px (language, pressed states, title, links). Downloaded evidence-only ZIP 15234510919, 4486720 bytes, SHA-256 e07441a19920c2138f6eac256fc3e173fa8fb4b28bd3691a05201bf944fd550e matches API; CRC PASS. 144 repeat navigation samples: DOM interactive median 24/max 265.7 ms, DCL median 30.4/max 266.1 ms, load median 40.5/max 348.2 ms; 48 320px observations, zero horizontal overflow, first Tab focus-visible on skip link in 48/48. Local routed CI only.
[ba1c7e8](https://github.com/Kgasil/kgasil.github.io/commit/ba1c7e8cd756b6c40834754458bcad2841e5dcd7) waits for position stability after skip navigation before the original click; no retries of clicks or removed assertions. Smooth scroll is a hypothesis, not a proved root cause; no Genesis site change. [Revalidation 46073590229](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073590229) pending at initial query.

## Demonstration / Demonstração
[521b5e1](https://github.com/Kgasil/kgasil.github.io/commit/521b5e1819548670396de2edbd6225b2b1daa2f6) introduces `graal.demo.trace.v1`, separate from and compatible with existing `graal.metric.v1` and catalog contract.

| Stage | Real source used | Synthetic output |
| --- | --- | --- |
| Genesis | extension/core.js reading | Fixed queue study, reading word count and duration, inputs [6,10] per hour |
| Rubedo | examples/reference-results.json via existing adapter | Reference queue wait 9 min, total 15 min (stored reference, not solver execution) |
| Argus | extension/core.js review | Deterministic pattern review of numeric record; no flags, no sensitive pattern found; not guarantee of privacy |
| Aeris | desktop/aeris/checklist.py at d6e03bc | One pending in-memory task to review waiting time; no meeting, AI, disk, reminder or installed app |
| Lilium | core/metrics.py analyze_csv | Independent synthetic CSV: revenue 30000, cost 18000, result 12000 BRL cents; not revenue inferred from queue |

Four explicit ordered approvals passed via CLI, all required before running; no automatic application access. Workflow test grants are synthetic test inputs, not real user consent. No arbitrary imported data or upload input. Source code is read/executed only in CI; suspended Genesis/Argus ZIPs not touched or installed. Aeris pinned draft commit, no native execution. Sources bound to actual checked-out commit and byte SHA-256. Trace binds each stage to predecessor digest, catalog digest and explicit edge; verification recomputes the whole fixed demonstration, not just a hash chain. No signature or authentication claim. No writes to native stores or real data; CLI writes only trace file. Source cloning uses GitHub; demonstrated stages do not require external services or new dependencies beyond existing Python and Node runtimes.

Run in authorized local clones at expected revisions (Aeris pinned):
```sh
python3 validation/integration/demo.py /path/to/snapshots docs/graal-catalog.md trace.json --approve genesis:rubedo --approve rubedo:argus --approve argus:aeris --approve aeris:lilium
```
No approvals by default; missing/reordered/extra edges fail. Existing restricted distribution states remain enforced by registry. Twelve new tests cover ordered grants, chain, tampering and rehashed tampering, release flag, hold, data classification, provenance, reconciliation, pending status and repeatability. [Demo CI 46073646096](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073646096) and [existing contracts CI 46073646147](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073646147) pending at initial query. No native candidate changed.

## Boundaries / Limites
No production integration, UI handoff, native permission change, arbitrary-data sanitizer or external certification. Source-level demonstration can be replayed with exact sources; no client or revenue claim. Genesis/Argus incidents remain open; Aeris and Lilium draft PRs remain open, all distribution gates retained. Quality 9/10 not established. Next: prepare bounded synthetic business pilot, define authorization and measurable acceptance, no customer data or release.
