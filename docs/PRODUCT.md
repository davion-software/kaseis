# Product

Kaseis Obras is a vertical SaaS for materials and supply control in Latin American construction. The first focus is **Inventory Truth**: turn informal field records into a reliable, reconciliable, auditable inventory.

## Promise

Field teams register movements on WhatsApp (via Kapso). Residents, admins, and owners get visibility on the web dashboard to request, receive, consume, and control materials.

## What we sell

The pilot sells verified balances, visible uncertainty, and evidence. Automations depend on those records being trustworthy.

## Entry loop (pilot)

1. Configure one obra and a controlled catalog of critical materials
2. Establish inventory baseline via approved physical count
3. Capture ingresos/salidas/devoluciones/ajustes with confirmation
4. Query stock and low materials from WhatsApp
5. Run guided counts and weekly reconciliation
6. Act on alerts and differences from the dashboard

## Principles

- Expose uncertainty before automating decisions.
- Fit obra language and field conditions; confirm before changing stock.
- Reverse or compensate for errors; never rewrite confirmed movements.
- Show differences and pending items in the dashboard.
- Use deterministic parsing first and an LLM only as fallback; users confirm stock changes.

## Expansion (after pilot PMF)

Request-to-Receive → Cost Control → Procure-to-Pay → Materials Intelligence. Workforce / CAPECO are parallel products, not the core materials roadmap.

See [Pilot scope](PILOT_SCOPE.md) and [Glossary](../GLOSSARY.md).

## Status and users

This is the intended product, derived from repository docs and rules. No application behavior is implemented yet. Existing decisions are preserved; suggested defaults in [open questions](OPEN_QUESTIONS.md) are not confirmed policy.

The initial customer is a small Peruvian contractor. Field staff register material movements, residents and supervisors review exceptions and counts, and administrators manage access and setup. Exact approval permissions remain open.

## Responsibility for stock

WhatsApp interprets a field report into a proposed movement. The user must see the obra, material, quantity, unit, and movement direction before confirming it. Ambiguous material names require a selection. CORREGIR changes the proposal; CANCELAR leaves stock unchanged. Photos support the record but never confirm it.

Inventory use cases validate and record confirmed movements. Corrections preserve the original record and add a reversal or compensating adjustment. A repeated delivery of the same command must not create another movement.

A physical count records what was observed. Reconciliation compares that observation with registered stock, records a reason for differences, and links any approved adjustment. Recording a count alone does not silently overwrite stock.

Stock queries must expose uncertainty: no approved baseline, pending confirmation, aged counts, and unexplained differences. A number without its confidence context does not meet the product promise.

## Pilot boundaries

The [pilot scope](PILOT_SCOPE.md) owns feature limits and success targets. Basic ingreso is a stock movement; supplier purchasing and partial delivery workflows remain commercial MVP work. Transfers and multiple-location workflows are not established pilot commitments. Their proposed treatment is recorded in [open questions](OPEN_QUESTIONS.md).

Assisted onboarding targets an obra usable in about 48 hours. This is an operating target, not a measured guarantee. See the [onboarding runbook](runbooks/ONBOARD_OBRA.md).

## Acceptance evidence to collect

Before pilot use, demonstrate the full loop with one obra and its critical catalog:

1. An authorized person approves the starting count.
2. A proposed WhatsApp ingreso or salida changes no stock until confirmation.
3. A duplicate delivery and a duplicate confirmation produce no extra movement.
4. A stock query can be explained from confirmed movements and count history.
5. A physical difference produces a reviewed, linked adjustment rather than an overwritten balance.
6. The dashboard exposes pending items and differences without leaking another organization's data.

Also demonstrate cancellation, ambiguous materials, reversal, rejected unauthorized approval, and worker retry recovery. These are required future checks, not tests that have passed in this repository.
