# WhatsApp / Kapso flow

Design or implement a Kapso conversation flow with confirmation.

## Steps

1. Define intent examples and happy path + CORREGIR / CANCELAR.
2. Rules-first parser; LLM fallback only if needed.
3. Webhook: verify → idempotent → 200 → enqueue.
4. Worker: resolve context → propose → await confirm → call inventory use case.
5. Keep messaging adapters in `packages/modules/messaging`; inventory writes via ports.
6. Follow `docs/runbooks/kapso-webhooks.md` and skills `kapso-kaseis`, `kapso-ai`.

## Output

- Flow diagram (states)
- Files to touch
- Idempotency key strategy
