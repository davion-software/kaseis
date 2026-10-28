# Kapso Platform Reference

## API Base and Auth

- Base URL: `https://api.kapso.ai`
- Platform routes: `/platform/v1/...`
- Auth header: `X-API-Key: <api-key>`

## Setup Links (Customer Onboarding)

Create setup link:

- `POST /platform/v1/customers/{customer_id}/setup_links`

Key request options:

- `success_redirect_url`
- `failure_redirect_url`
- `allowed_connection_types` (`coexistence`, `dedicated`)
- `provision_phone_number`
- `phone_number_country_isos`
- `theme_config`

Operational notes:

- Setup links expire (docs state 30 days).
- Store `setup_link.id`, `url`, and expiration.
- Use redirect params for UX and webhooks for backend truth.

## Connection Detection

Primary signal:

- Project webhook event `whatsapp.phone_number.created`

Also available:

- Success redirect query parameters from setup flow completion.

Recommended persistence:

- `customer_id`
- `phone_number_id`
- `connected_at`
- `whatsapp_connected` boolean

## Broadcasts API

Lifecycle:

1. Create draft broadcast
- `POST /platform/v1/whatsapp/broadcasts`

2. Add recipients (up to 1000 per call)
- `POST /platform/v1/whatsapp/broadcasts/{broadcast_id}/recipients`

3. Start send operation
- `POST /platform/v1/whatsapp/broadcasts/{broadcast_id}/send`

4. Monitor recipient delivery
- `GET /platform/v1/whatsapp/broadcasts/{broadcast_id}/recipients`

Implementation pattern:

- Validate template and `phone_number_id` before create.
- Chunk large recipient imports.
- Persist per-recipient status (`sent`, `delivered`, `read`, `responded`) for analytics.

## Inbox (Operational Behavior)

Inbox capabilities include:

- Conversation list + thread + details panel.
- Assignment workflows.
- Handoff from automation to human agents.
- Embedded inbox via iframe (`https://inbox.kapso.ai/embed/{token}`).

Important guardrails:

- Sending can be restricted when conversations are closed.
- Sending can be restricted while workflow automation is running (handoff required).
