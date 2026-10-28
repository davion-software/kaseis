---
name: inventory-truth
description: Implement or change inventory ledger movements, balances, confirmation gates, and physical reconciliation in Kaseis. Use when touching inventory or reconciliation modules, stock math, or movement types.
---

# Inventory Truth

## When to use

Ledger movements, balances, counts, reconciliations, confidence states, or anything that changes stock.

## Mandatory rules

1. Confirmed movements are immutable; reverse or compensate.
2. WhatsApp paths confirm before write.
3. Idempotent keys on ingress.
4. Balances rebuildable from ledger.
5. Domain has no SQL/Zod; adapters own I/O.

## Workflow

1. Read `docs/architecture/LEDGER.md` and `.cursor/rules/inventory-ledger.mdc`.
2. Change domain → application → adapters → `packages/di`.
3. Add tests for duplicates, reversal, and org isolation.
4. Update glossary/ledger docs if introducing a new movement type.

## Anti-patterns

- Editable `stock` column as source of truth
- LLM auto-confirming movements
- Writing ledger from Vue components
