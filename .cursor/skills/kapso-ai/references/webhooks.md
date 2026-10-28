# Kapso Webhooks Reference

## Header Contract

Kapso webhook headers commonly include:

- `X-Webhook-Event`
- `X-Webhook-Signature`
- `X-Idempotency-Key`
- `X-Webhook-Payload-Version`

Batch-specific headers:

- `X-Webhook-Batch: true`
- `X-Batch-Size`

Meta passthrough webhook payloads can use:

- `Content-Type: application/json`
- `X-Idempotency-Key` (payload hash)

## Delivery Model

Treat deliveries as at-least-once.

- Retry schedule documented: approximately `10s`, `40s`, `90s`.
- Duplicate event delivery is possible.

## Receiver Pattern

1. Read raw body (before JSON mutation).
2. Verify signature with your configured webhook secret.
3. Check and persist `X-Idempotency-Key`.
4. Respond `200` quickly.
5. Process event in async/background worker.

## Eventing Guidance

Use event routing by `X-Webhook-Event` (or event field in JSON body) and isolate handlers:

- onboarding/connection events
- message lifecycle events
- error or status callbacks

Keep handlers idempotent and deterministic.

## Local Testing

Use an HTTPS tunnel for local webhook receiver development (for example ngrok or Cloudflare Tunnel), then register that URL in Kapso webhook settings.
