# Pilot scope

Source of truth for what belongs in the validation pilot (Fase 1 — Inventory Truth). Contrast every feature request against this file and `/scope`.

## Goal

Prove that Kaseis becomes part of daily obra operations and produces inventory reliable enough to influence real purchase and execution decisions.

## Limits

| Dimension | Limit |
| --------- | ----- |
| Customers | 1–3 design partners |
| Projects | One obra per pilot |
| Materials | 20–50 critical materials |
| Users | 3–5 active users |
| Channels | WhatsApp text + optional photo evidence + web dashboard |
| Documents | No productive OCR; manual guide/reference numbers |
| Duration | ~30 operating days with founder support |

## In scope

- Configure obra, users, materials, aliases, units, minimums
- Approved initial inventory count
- Ingreso, salida, devolución, ajuste, anulación (with confirmation)
- Optional photo evidence (R2)
- Stock and low-material queries on WhatsApp
- Daily summary and pending items
- Dashboard: stock, movements, alerts, differences
- Guided physical count and weekly reconciliation
- Basic CSV/Excel export

## Out of scope (pilot)

- Productive OCR of photos/PDFs
- Purchase orders, quotes, invoices
- Budget / metrado comparison
- S10, accounting, or SUNAT emission integrations
- Native mobile app, audio, QR
- Tareo / planilla CAPECO
- Multi-obra commercial packaging (basic multi-tenant may exist in schema; pilot runs one obra)

## Success criteria (continue if met)

| Metric | Threshold |
| ------ | --------- |
| Same-day capture | ≥ 85% of movements |
| Usage | Operate in Kaseis ≥ 4 days/week |
| Reconciliation | ≥ 95% accuracy on critical materials or explainable difference |
| Value | ≥ 1 purchase or shortage prevention influenced by Kaseis |
| Retention | Team keeps using after novelty fades |
| Payment | ≥ 2 of 3 design partners continue on a paid plan |

## MVP commercial (later)

Multi-obra, locations, suppliers, partial receipt, assisted OCR, roles/approvals, Excel import, repeatable onboarding. Do not pull these into the pilot because they are “technically interesting.”
