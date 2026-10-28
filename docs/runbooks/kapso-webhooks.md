# Runbook — Kapso webhooks

## Principles

1. Verify webhook signatures before processing.
2. Enforce idempotency (`X-Idempotency-Key` or equivalent event id).
3. Return **200 quickly**; process asynchronously via Redis/worker.
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
