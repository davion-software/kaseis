# Open questions

These questions come from a headless review of existing docs, rules, commands, and placeholder directories on 2026-10-28. Suggested defaults are proposals, not accepted decisions or implemented behavior. Resolve each relevant question before implementing or operating the affected flow.

## Review outcome

The review followed purpose → pilot scope → domain rules → runtime boundaries → operations. Existing evidence settles the Inventory Truth loop, confirmation before stock, immutable ledger, tenant isolation, private evidence, hexagonal modules, Railway hosting, and Better Auth. The unresolved branches are listed below. No new product approval is inferred from this review.

## Q01. Pilot inventory locations

Question: Onboarding and ledger use locations, but pilot scope defers locations to commercial MVP. What location model is required?

Why it matters: Determines baseline grouping, queries, counts, and interface scope.

Suggested default: Use one default inventory location per obra; defer multiple-location workflows.

## Q02. Transfers and receipt scope

Question: Are transfers part of the pilot, and is ingreso distinct from supplier receipt management?

Why it matters: The old glossary lists transfers as pilot+ while supplier and partial receipts are deferred.

Suggested default: Keep ingreso as RECEIPT; defer transfers and supplier delivery records.

## Q03. Approval authority

Question: Who may approve initial inventory, reversals, and adjustments, and at what thresholds?

Why it matters: Security separates register, approve, and administer, but the permission matrix is absent.

Suggested default: Require explicit supervisor approval for baseline and adjustments; define reversal authority before use. No automatic approval.

## Q04. Count cutoff and concurrent movements

Question: Which ledger cutoff does a count compare against, and how are movements during counting handled?

Why it matters: Comparing different moments can create false differences.

Suggested default: Record a cutoff and count timestamp; serialize count approval with affected movements until a concurrent protocol is designed.

## Q05. Tolerance and confidence

Question: What tolerance, count age, and transition precedence define each confidence state?

Why it matters: The current labels do not define an operational state machine or the 95% accuracy measure.

Suggested default: Use zero unexplained tolerance provisionally and show last-count time; agree material-specific tolerances and freshness before launch.

## Q06. Negative stock

Question: Which roles may allow negative stock, and is it enabled by default?

Why it matters: Ledger rules permit it with warning, reason, and configured permission but specify no default.

Suggested default: Reject negative stock unless explicitly enabled for an authorized role with warning and reason.

## Q07. Quantities and corrections

Question: What decimal precision and conversion rules apply, and are partial or repeated reversals allowed?

Why it matters: Rounding and over-reversal can make ledger totals inconsistent.

Suggested default: Use exact decimal quantities, reviewed base-unit conversions, and one full linked reversal until a partial policy is agreed.

## Q08. Confirmation lifecycle

Question: When do proposals expire, and what happens if stock or obra context changes before confirmation?

Why it matters: A bare confirmation must not approve stale or different movement data.

Suggested default: Bind confirmation to an identified proposal and obra; require a new review after material changes or expiry. Select an expiry before implementation.

## Q09. Phone identity and obra context

Question: How are WhatsApp numbers linked, revoked, and authorized across organizations?

Why it matters: A phone number or remembered conversation context alone cannot establish tenant access.

Suggested default: Require administered linkage, active membership checks on every action, and visible obra context.

## Q10. Pilot measurement

Question: How are capture, accuracy, retention, and paid continuation measured for 1–3 partners?

Why it matters: Same-day capture needs an independent denominator; 2-of-3 payment does not cover smaller cohorts.

Suggested default: Agree definitions before onboarding; track daily field records against confirmed movements, explain differences per material, and report actual paid partners over cohort size without claiming an equivalent threshold.

## Q11. Export and import scope

Question: Does the pilot require CSV only or also native Excel export?

Why it matters: Pilot scope says CSV/Excel, while scope-gate lists CSV and defers Excel import.

Suggested default: Start with CSV export; retain Excel export as unresolved. Assisted setup is not a self-service import commitment.

## Q12. Durable ingress and idempotency

Question: Which queue library, durable acceptance boundary, key scope, retention, and replay protocol will be used?

Why it matters: Acknowledging before recoverable persistence can lose events; expiring Redis keys can permit duplicate stock writes.

Suggested default: Evaluate a Postgres inbox and transactional inventory uniqueness with Redis jobs; acknowledge only recoverable acceptance. Verify Kapso signature/event contracts during implementation.

## Q13. Persistence and worker bootstrap

Question: What schema, migrations, worker path, API routes, and health checks form the first runnable slice?

Why it matters: There are no manifests or runtime contracts to deploy or test.

Suggested default: Implement one confirmed ingreso/salida slice with factory DI and local Postgres tests before expanding. Treat BullMQ as a candidate, not a finalized dependency.

## Q14. Recovery and operations

Question: Who owns incidents, what are RPO/RTO, and how are Postgres, R2, and queued work restored together?

Why it matters: Current rollback guidance is not a tested recovery procedure.

Suggested default: Assign an incident owner and require a staging restore drill plus idempotent replay before live writes; set recovery objectives and backup retention with the partner.

## Q15. Evidence and personal data

Question: What upload types, sizes, signed URL lifetime, data retention, export, and deletion policies apply?

Why it matters: Private evidence and original messages include personal and business information.

Suggested default: Minimize collected data, keep evidence private, authorize every signed URL, and agree explicit retention and deletion rules before collection.

## Q16. Messaging providers and cost

Question: Which Kapso events, templates, service windows, LLM fallback provider, and spending limits will be configured?

Why it matters: Proactive summaries and fallback parsing need actual provider contracts and budget ownership.

Suggested default: Start with deterministic text flows and a manual ambiguity path; validate current provider contracts and costs before enabling proactive or LLM features.
