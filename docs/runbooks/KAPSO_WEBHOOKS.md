# Runbook — Kapso webhooks

Status: planned procedure. App routes, deployment commands, replay tooling, and recovery have not been implemented or verified.

## Principles

1. Verify webhook signatures before processing.
2. Enforce idempotency using the provider event identity verified during integration. The exact header or field is not specified here.
3. Acknowledge only after recoverable acceptance; process asynchronously via Redis/worker. The durable handoff is an [open decision](../OPEN_QUESTIONS.md#q12-recepción-persistente-de-eventos-e-idempotencia).
4. Treat delivery as at-least-once.
5. Never affect inventory until the user confirms (see ledger docs).

## On failure

| Symptom | Check |
| ------- | ----- |
| No messages arriving | Kapso project webhook URL, HTTPS, subscription events |
| Duplicates | Idempotency store / unique constraints on movements |
| 5xx from our API | Sentry + Railway `web` logs; worker backlog |
| Connected number missing after onboarding | Kapso `whatsapp.phone_number.created` subscription |

## Env

- `KAPSO_API_KEY`
- `KAPSO_API_BASE_URL` (host only, e.g. `https://api.kapso.ai`)
- Webhook signing secret as provided by Kapso

Use skills `kapso-ai`, `kapso-kaseis`, and official Kapso agent skills when implementing handlers.

Do not replay unknown events directly into stock. Inspect acceptance and movement records, preserve the original identity, and use an authorized retry path once implemented. Verify current Kapso signature headers and event contracts before building the handler.
