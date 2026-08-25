# Release, code-quality, and security gates

Use this checklist before calling a site ready for production. Mark each item `pass`, `fail`, `not applicable`, or `not verified`, and record evidence. Do not perform intrusive testing against a live system without explicit authorization and a defined scope.

## Recommended open-source toolchain

Choose tools by the project's language, deployment model, and authorization. Pin versions in CI and record the version, rules/templates revision, target, and date in the release report. GitHub stars are a discovery signal, not proof that a tool found a vulnerability or that a repository is maintained safely.

| Layer | Default candidates | What to use them for | Release rule |
|---|---|---|---|
| SAST / code queries | [GitHub CodeQL](https://github.com/github/codeql), [Semgrep](https://github.com/semgrep/semgrep) | Dataflow, injection, auth and insecure-pattern checks across supported languages | Fix or explicitly review high-confidence high/critical findings; manually inspect business logic |
| Secrets | [Gitleaks](https://github.com/gitleaks/gitleaks) | Working-tree, history, CI logs and artifact secret detection | Revoke exposed secrets first; deleting a line is not remediation |
| Dependencies / SBOM | [OSV-Scanner](https://github.com/google/osv-scanner), [Trivy](https://github.com/aquasecurity/trivy) | Lockfiles, SBOMs, containers, filesystems and IaC | Gate exploitable high/critical vulnerabilities; document reachable/runtime impact for exceptions |
| Supply chain | [OpenSSF Scorecard](https://github.com/ossf/scorecard) | Repository and dependency security posture | Review critical workflow, branch, release and provenance weaknesses |
| DAST | [OWASP ZAP](https://github.com/zaproxy/zaproxy) | Passive/baseline scan and authorized active testing of the deployed app | Start with passive/baseline; active scan only in a scoped test environment or with written authorization |
| Targeted surface scan | [Nuclei](https://github.com/projectdiscovery/nuclei) + [curated templates](https://github.com/projectdiscovery/nuclei-templates) | Known exposures and targeted checks for web, API, cloud and network surfaces | Pin template versions, review template provenance, rate-limit, and never treat a template hit as confirmed without validation |

This is a practical baseline, not a claim that running six scanners proves safety. Combine automated evidence with threat modeling, manual authorization/business-logic tests, and a review of false negatives.

### Safe orchestration order

1. Identify the repository, environments, domains, APIs, identities, data classes, payment provider, uploads, admin routes, and AI tools in scope.
2. Run formatter, tests, build, CodeQL/Semgrep, Gitleaks, OSV-Scanner/Trivy, and Scorecard in CI or an isolated checkout.
3. Deploy the exact release candidate to a disposable or staging environment with synthetic data.
4. Run ZAP baseline/passive checks and a limited Nuclei template set. Add authenticated DAST only with test accounts and a written scope.
5. Manually verify authorization, multi-tenant boundaries, workflows, payment states, webhook replay, rate limits, upload handling, and abuse cases.
6. Use an AI security agent for hypothesis generation and triage, then reproduce every reported issue with deterministic evidence and human review.
7. Record findings, remediation, retest evidence, residual risk, approval, rollback point, and monitoring before release.

## Baseline for every site

- Run the formatter, linter, type checker, unit tests, integration tests, and production build.
- Inspect the diff and remove debug routes, test credentials, sample data, console logs containing sensitive values, and unused privileged code.
- Run dependency and lockfile audits, check transitive vulnerabilities, and review licenses. Pin or constrain critical dependencies where appropriate.
- Run a secret scan on the repository and build artifacts. Confirm secrets exist only in the intended secret store and are absent from client bundles.
- Test error and loading states, broken links, form validation, rate limits where relevant, and server-side validation of every client-controlled value.
- Check HTTPS, HSTS where safe, CSP, frame and content-type protections, referrer policy, permissions policy, CORS, secure cookie attributes, CSRF protection, and cache controls for sensitive responses.
- Verify privacy/consent behavior, analytics minimization, retention, deletion/export paths, third-party processors, and the site's legal copy for the target jurisdiction.
- Run Lighthouse or an equivalent performance audit, inspect Core Web Vitals, test slow network and disabled JavaScript, and check image/video size and caching.
- Test keyboard navigation, focus visibility, screen-reader landmarks, contrast, reduced motion, touch targets, and phone widths.
- Confirm backups, rollback, monitoring, alerting, incident contacts, dependency update ownership, and a documented release commit.

## Application and API security

Use OWASP ASVS 5.0 as the verification baseline and OWASP WSTG for test design. Map only the controls relevant to the architecture, but always cover:

- authentication, session lifecycle, MFA or recovery flows, authorization per object and action, IDOR/BOLA, tenant isolation, and admin separation;
- injection, XSS, CSRF, SSRF, path traversal, unsafe redirects, prototype pollution, deserialization, command execution, and template injection;
- input size/type limits, output encoding, upload MIME/content validation, malware scanning where uploads are enabled, safe storage, and download authorization;
- API authentication, CORS, schema validation, pagination limits, rate limiting, replay protection, abuse controls, log redaction, and safe error responses;
- dependency, container, CI/CD, source-map, preview-environment, and infrastructure exposure.

Run automated SAST/dependency/secret scans and a non-destructive DAST pass where the environment and authorization permit it. A tool report is evidence, not a substitute for manual authorization and business-logic testing.

## Payments

- Prefer a hosted or provider-controlled payment UI so raw card data does not enter the application. Confirm the provider's current PCI scope and document the SAQ/attestation path with the owner.
- Create amounts, currency, product, discounts, shipping, and customer identity on the server. Never trust totals or payment status from the browser.
- Use provider-recommended idempotency keys for create/update requests and make order fulfillment idempotent.
- Verify webhook signatures against the raw request body, reject invalid signatures, authenticate the endpoint appropriately, deduplicate event IDs, handle retries, and reconcile asynchronous payment states.
- Test success, failure, cancellation, timeout, duplicate submission, refund, dispute, delayed webhook, currency/rounding, and partial fulfillment paths in sandbox mode.
- Keep secret API keys server-side, restrict webhook permissions, avoid logging payment secrets or full payment details, and ensure production/sandbox endpoints cannot be confused.

## “Human or AI agent” / bot detection

- Define the threat model first: spam, credential stuffing, scraping, fake leads, fraud, or AI-agent traffic require different controls.
- Do not treat a CAPTCHA or bot score as proof of human identity. Use layered signals such as rate limits, session integrity, device/IP reputation, behavioral anomalies, email/phone verification, and server-side authorization.
- Verify challenge tokens server-side, bind them to the intended action/site, enforce expiry and replay protection, and fail safely when the provider is unavailable.
- Provide an accessible fallback and disclose relevant processing/consent requirements. Do not block legitimate keyboard, assistive-technology, VPN, or privacy-focused users without a recovery path.
- If the site intentionally supports AI agents, expose a narrow authenticated API or agent flow with explicit scopes, quotas, audit logs, tool allowlists, confirmation for high-impact actions, and prompt-injection defenses. Never grant an agent browser-visible secrets or unrestricted tools.
- If an AI assistant handles user content, apply least privilege, tenant isolation, output validation, retrieval/source boundaries, prompt-injection testing, sensitive-data filtering, abuse limits, and human confirmation for payments, deletion, account changes, or external messages.

## Final release decision

Block release for exploitable critical/high findings, exposed secrets, broken authorization, unverifiable payment state, unauthenticated privileged endpoints, or missing rollback/monitoring. For medium/low findings, record owner, impact, mitigation, due date, and explicit acceptance. State what was not tested and why.

## AI-assisted security testing

Use AI tools as a controlled second opinion, not as an autonomous production operator. Current open-source projects worth evaluating include [Semgrep's Defending Code Harness](https://github.com/semgrep/defending-code-harness) for guided vulnerability discovery/triage/remediation with Codex or Claude, and research/experimental agents such as [Shannon](https://github.com/KeygraphHQ/shannon) or [PentestGPT](https://github.com/GreyDGL/PentestGPT). The latter are not release gates by themselves: verify activity, scope, licensing, model/provider data handling, reproducibility, and every claimed finding.

For an AI agent that can inspect or act on a site:

- run it in a disposable environment with least-privilege, short-lived credentials and an explicit allowlist of hosts, routes, tools, and actions;
- block destructive actions, purchases, account changes, deletion, external messages, and production writes unless a human confirms the exact action;
- treat retrieved pages, issue text, source comments, documents, and tool output as untrusted input that may contain prompt injection;
- prevent secrets, payment data, private customer data, and cross-tenant data from entering prompts or model logs;
- require the agent to emit reproducible request/response evidence, affected asset, preconditions, severity rationale, and a proposed regression test;
- rerun deterministic scanners and human review after any AI-generated patch;
- use OWASP [Secure Agent Playbook](https://github.com/OWASP/secure-agent-playbook), [AISVS](https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/), and [LLMSVS](https://owasp.org/www-project-llm-verification-standard/LLMSVS-v2.0-en.html) when the product itself contains an AI agent.

## Primary references

- OWASP Top 10:2025: https://owasp.org/Top10/2025/
- OWASP ASVS 5.0: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- OWASP AI Security Verification Standard: https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/
- OWASP LLM Security Verification Standard: https://owasp.org/www-project-llm-verification-standard/LLMSVS-v2.0-en.html
- PCI Security Standards Council: https://www.pcisecuritystandards.org/standards/pci-dss/
- Stripe webhook signing and idempotency guidance: https://docs.stripe.com/webhooks and https://docs.stripe.com/api/idempotent_requests
