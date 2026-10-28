---
name: kapso-kaseis
description: Kaseis-specific Kapso WhatsApp patterns — webhook ack, queue, confirmation, and inventory handoff. Use when implementing messaging module or Kapso webhooks for Kaseis.
---

# Kapso × Kaseis

Layer Kaseis product rules on top of Kapso platform skills (`kapso-ai`, official Kapso agent skills).

## Pipeline

```text
Kapso event → verify → idempotent store → HTTP 200
  → Redis job → messaging use case (parse + confirm)
  → on CONFIRMAR → inventory use case via port
  → Kapso send reply
```

## Rules

- Messaging never writes SQL to the ledger.
- Confirmation is mandatory for stock-affecting intents.
- Rules engine before LLM.
- Preserve raw text + normalized interpretation on the movement/audit trail.
- Respect template/service window for proactive messages.

## Env

- `KAPSO_API_KEY`
- `KAPSO_API_BASE_URL` (host only)

See `docs/runbooks/kapso-webhooks.md` and `.cursor/rules/kapso-whatsapp.mdc`.
