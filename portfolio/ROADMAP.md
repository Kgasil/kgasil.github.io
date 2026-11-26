# KG — Professional Portfolio | Roadmap

**Public page:** https://kgasil.github.io/portfolio/  
**Target:** 1.0 — a bilingual, recruiter-friendly professional portfolio.  
**Scope:** personal website only; the K&G Vision institutional home and project sites remain independent.

## Delivery sequence

| Phase | Status | Deliverable | Acceptance criteria |
| --- | --- | --- | --- |
| 01 | Implemented; deployment verification pending | Executive visual foundation and homepage | KG monogram, institutional navy, clear professional positioning, three featured projects, responsive layout, bilingual copy |
| 02 | Implemented; deployment verification pending | Professional experience and capabilities | Evidence-based experience, education, tools, career narrative, no invented outcomes |
| 03 | Implemented; browser verification pending | Project catalogue | Categories, filters, clear project status, links and source documentation |
| 04 | Implemented; browser verification pending | Case studies | Business problem, methodology, architecture, evidence, limitations; synthetic data clearly labelled |
| 05 | Implemented; 16 logic assertions passed; browser verification pending | Interactive lab | Browser-based analytical dashboard, process simulations and practical mini tools; deterministic fixtures and tests |
| 06 | Implemented; print and browser verification pending | Digital résumé | Recruiter view, print styling and approved downloadable résumé without private contact details |
| 07 | Implemented; browser verification pending | Professional integration | GitHub profile, LinkedIn, K&G Vision links, cohesive branding |
| 08 | Source release 1.0 completed; public browser smoke test pending | Release audit and 1.0 | Accessibility, responsive/mobile review, link validation, translation review, performance, deployment and public smoke test |

## Phase 01 changes

- Refined visual foundation using #18263B and the approved KG monogram.
- Executive homepage, professional positioning, experience and education summary.
- Three featured projects: maintenance analytics, registration data enrichment and K&G Vision AI Coder.
- Conceptual illustrations explicitly distinguished from actual project output.
- Existing project catalogue, bilingual switch and print capability retained.
- Source commit: 8a93230a436105e44db018c8386f32a12f1b1f69.

## Phase 02 changes

- Bilingual career narrative connecting industrial operations, technical quoting, data governance and automation.
- Three experience cards with responsibilities and relevant skills, without unsupported performance figures.
- Four capability areas linked to independent public portfolio demonstrations.
- Education and self-reported language levels, plus current learning interests.
- New navigation section, responsive styling and print adjustments.
- Static validation: unique HTML IDs and all internal fragment links resolve.
- Source commit: 6665913c02e1642f453979a6bf1b091e97bb4a7a.

## Phase 03 changes

- Seven independent projects presented in a consistent catalogue, including the AI Coder project.
- Five overlapping focus categories plus an all-project view, bilingual keyword search, live results count, clear filters and empty state.
- Project status labels distinguish demonstrations, conceptual specifications and guided learning.
- Search matches both language versions and ignores accents; catalogue remains readable without JavaScript.
- Static validation: seven project cards, unique IDs and valid internal fragments.
- Source commit: 31cc49c1c9eacbf7e9a1e45ab82e43b285f7e23d.

## Phase 04 changes

- Reviewed the seven project READMEs and created a dedicated bilingual case-study page with an index and seven direct anchors.
- Each study documents the business challenge, technical approach, conceptual architecture, repository evidence, reproduction reference where applicable, and limitations.
- Explicitly distinguishes synthetic data, conceptual workflow specifications, local prototypes and guided AI-assisted learning; no unsupported claims of business impact or independently executed tests.
- Linked all seven catalogue cards and the main navigation to the case-study page, preserving language selection for the outbound links.
- Static checks: unique case-study IDs, valid internal fragments and seven catalogue case links.
- Source commits: 90badb1e32f3a4deb5a4b5c562dff296c2c40839 and df77b99d2c50626523cc61bd6ec2f3a9ff841683.

## Phase 05 changes

- Interactive lab at /portfolio/lab.html: maintenance dashboard, divisor-markup pricing, demand scoring, identifier cleansing and workflow routing.
- Eight deterministic synthetic work orders; interactive area filter, KPIs and downtime chart.
- Local browser-only calculations; no API requests or persistence of entered data. Explicit educational limitations, including format-only identifier validation and demo-specific priority rules.
- Bilingual controls and results, links to case studies, responsive styling and homepage integration.
- 16 logic assertions executed successfully before commit; same selfTest function available in the lab. Static IDs and fragment checks passed. Browser interaction tests still pending.
- Source commits: 6c6ca0b6568bacd072c367981fbc2e7704f919b4, abb5b0f817c4fa2586353285af4002a05fbcf0c9, f10ff5e92f5a168752d6a03ba05b981432d310b1 and 143b5df860a876bcc4b53dfe85db48626cccea6e.

## Phase 06 changes

- Dedicated bilingual recruiter résumé at /portfolio/resume.html, with a single-column reading and A4 print layout.
- Professional summary, experience, education, technical capabilities, independent projects and self-reported language levels.
- Browser print / save as PDF and downloadable UTF-8 plain text in either language. No separate pre-generated PDF file or ATS certification claimed.
- Public contact links only; no telephone, personal email or residential address. Bosch end date omitted pending confirmation.
- Homepage navigation and hero link to the résumé; English selection retained on outbound links.
- Static checks: unique IDs and valid internal fragments. Browser download, print pagination and public deployment still need verification.
- Source commits: e4c273d2f30b553d46a84d2538b011a7e4e72a2f and 163beb5829a8488621dbc02235b47eb5a3addce1.

## Phase 07 changes

- Shared KG header, monogram, professional footer, active-page indication and mobile navigation across homepage, case studies, lab and résumé.
- Consistent palette via shared.css and language-aware page navigation via shared.js.
- Homepage section shortcuts retained; public GitHub avatar added discreetly with user approval and graceful image-failure fallback.
- Main GitHub profile README now links directly to the résumé, case studies and interactive lab; existing clickable banner and ecosystem visuals preserved.
- Institutional K&G Vision site and other projects remain unchanged.
- Static unique-ID checks passed for all four pages during integration. Public deployment, avatar rendering and cross-page browser interaction remain to be verified.
- Source commits: 0b9f2920f99babf7f03af57bdf2011d080b4e33d, 1dd8bb4693ff039ec945a3859d003be21a52baa9, 5e14ea83517cab3a02f73415ef67a9291149559d, 3561f9fb04f0d5884809eb5823211e09e89ed427, 72f7b1da90b93e5ac2f392dcc02279862b597f81, 1267a46e08b86b4dc1772a8360ac86ee1baecaf3 and 5c8e31719d162a5431f0699383a8e525ef805907; profile README e9cf4867d55052a95371237ef5e884c5ad005141.

## Phase 08 changes

- Release polish: KG favicon, page metadata, keyboard focus, reduced-motion support, long-output wrapping and input autocomplete controls.
- Hardened pricing against numeric overflow and priority scoring against fractional SLA days.
- Final repository audit: 4 HTML pages, 82 local resource/fragment references, zero detected missing local targets or duplicate IDs; all inline and external JavaScript parsed successfully.
- Executed the fetched lab-core.js selfTest: 20 of 20 assertions passed.
- Previous GitHub Pages deployment for phase 07 completed successfully (run 45826523268). The release commit's deployment must be checked separately.
- Public HTTP/browser smoke testing could not be performed from the available environment; visual review, actual print pagination, downloads and interactive browser behavior remain pending. This is not an accessibility certification or production security audit.

## Guardrails

Do not claim verified business impact, production deployment, professional certification or independent security validation without evidence. Keep employer/client data private. Distinguish professional experience from personal demonstrations and AI-assisted learning. Avoid publishing personal contact information without approval. Use the same visual palette and preserve the existing institutional site.

## Next task

Version 1.0 source delivery complete. Perform a real-browser smoke test on the public URLs after deployment; log any defects before further features.
