# GRAAL — Pilotos empresariais / Business pilots · Cycle 02 · Step 07

2026-11-27. Demonstrações gratuitas, dados exclusivamente fictícios, sem cliente ou contrato. / Free demonstrations, synthetic data only, no client or contract. **No production or release approval.**

## Revalidação / Revalidation
[Web 46073590229](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073590229) SUCCESS, 138 browser views, 144 repeated samples, 48 targeted views and 48 observations at 320px, zero errors/overflow; median load 32.95 ms versus 40.5 ms previously. Variability between CI runs, not proof of speed optimization. Five previous Genesis Firefox language assertions did not recur after scroll-settlement adjustment; root cause not independently proved. [Demo 46073754381](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073754381), [contracts 46073754371](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073754371), [Pages 46073754605](https://github.com/Kgasil/kgasil.github.io/actions/runs/46073754605) SUCCESS. Downloaded demo artifact 15233637661, 1557 bytes, SHA-256 f85682bbf280d3ef0cf29cae3fa04bb529a8eaf9f78c4db1b1ce5a1c7e3b5f6a, CRC PASS; all five stage digests and predecessor links recomputed.

## Pilotos / Pilots
| ID | Scope and deliverable / Escopo e entrega | Acceptance targets / Critérios esperados |
| --- | --- | --- |
| P01 Dados & BI | Four synthetic revenue/cost rows across two months; Lilium engine, reconciled monthly totals and margin; JSON report | Revenue BRL 3500, cost 2200, result 1300, margin 37.14%; monthly results 550 and 750; exact cent reconciliation |
| P02 Automação / Process automation | Five fixed event occurrences, Aeris in-memory task list, duplicate handling, conflict rejection and failure cleanup | Three unique pending tasks, two duplicate occurrences suppressed, zero completed automatically, zero tasks remaining after cleanup; denied and conflicting batches leave no list |
| P03 Governança de IA / AI governance | Eight fixed fictional texts, Argus deterministic pattern review; counts and human-review routing only | 8/8 expected fixture classifications, four flagged for human review, zero autonomous approvals; no raw text in output |

P02 deduplicates within one batch only; not durable idempotency or a production transaction. Rollback removes created list; does not reset internal task ID allocation. P03 evaluates a tiny known fixture against deterministic rules, not actual AI model quality, recall on unknown data, privacy certification or a production security gate. No-pattern-match does not authorize an action. P01 result is revenue minus supplied cost, not accounting profit. No measured business savings, customer volume or SLA.

## Execution / Execução
[Implementation 2efd99d](https://github.com/Kgasil/kgasil.github.io/commit/2efd99d95a2dc815c5067c9e84fd240ff93ac47b) uses the five exact source commits recorded in the earlier trace, and verifies the synthetic GRAAL demonstration before pilots. New contract `graal.business.pilots.v1`, three explicit ordered synthetic grants, commit/file digests, fixture digests, previous demo terminal digest and recomputable final digest. No arbitrary data input, native installation, external app integration or new runtime package. CI source fetch uses GitHub; execution uses existing Python and Node runtimes. [CI 46074010357](https://github.com/Kgasil/kgasil.github.io/actions/runs/46074010357) initial status pending; 13 tests implemented. Reproducibility is scoped to exact sources, fixtures and catalog.

```sh
python3 validation/integration/test_pilots.py /path/to/pinned/snapshots
python3 validation/integration/pilots.py /path/to/pinned/snapshots docs/graal-catalog.md pilots.json --approve bi:synthetic --approve process:synthetic --approve ai-governance:synthetic
```

## Risks and acceptance / Riscos e aceite
| Risk / Risco | Control and remaining limitation / Controle e limite |
| --- | --- |
| Wrong financial interpretation | Integer cents, independently specified expected totals; customer definitions and fiscal rules not validated |
| Duplicate/replayed events | In-memory dedup within fixed batch, conflict and rollback tests; durable state and concurrency need separate design |
| Sensitive or unauthorized transfer | Fixed fixtures, explicit grants, no raw texts in report; real data and integrations excluded |
| AI false negatives or false positives | Human review, no autonomous approval; broader evaluation and model-specific validation required |
| Unapproved deployment | Existing catalog holds and release flags remain; no installer or real environment access |
| Commercial overclaim | Synthetic examples identified; no guaranteed savings, certification or verified client reference |

Proposed delivery: qualify problem and sponsor, agree baseline and bounded scope, obtain written authorization and review rights/privacy, demonstrate with fictitious data, define acceptance and rollback, only then consider separate authorized pilot with agreed data and controls. No real customer data under this stage. The professional partnership with Innove Consult is a creator relationship already described on portal; no joint pilot, endorsement, referral, new contract or permission to represent the partner assumed. No logo or partner assets changed.

## Public presentation / Apresentação pública
PT: A K&G Vision conecta dados, automação de processos e governança de IA pela metodologia GRAAL. Apresentamos três demonstrações gratuitas e reproduzíveis com dados fictícios: indicadores reconciliados, fluxo de tarefas com prevenção de duplicidades e revisão de informações com supervisão humana. Cada possível colaboração depende de descoberta, autorização, formalização e critérios de aceite.
EN: K&G Vision connects data, process automation and AI governance through GRAAL. Three free, reproducible synthetic demonstrations show reconciled metrics, duplicate-aware task routing and human-supervised information review. Any collaboration is subject to discovery, authorization, formalization and acceptance criteria.

[Commercial model](commercial-model-stage-05.md) · [Governance](business-governance-stage-07.md) · [Integration](operational-integration-cycle-02-step-06.md)
No actual client, invoice, paid service, additional license or binary released. Preserve project autonomy, logos, free access and holds. Final institutional score 9/10 not established.
