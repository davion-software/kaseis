---
name: kapso-ai
description: Kapso Platform and Voice Agents integration for WhatsApp onboarding, setup links, connection detection, project webhooks, broadcasts, inbox operations, and Pipecat voice call routing. Use when building or debugging Kapso-based WhatsApp products, multi-tenant onboarding, webhook processing, campaign broadcasts, or voice-agent orchestration.
---

# Kapso AI

## Overview

Use this skill to implement or troubleshoot Kapso-powered WhatsApp systems end-to-end: customer onboarding, event ingestion via webhooks, broadcast campaigns, inbox operations, and voice call routing to Pipecat.

## Quick Start Workflow

1. Confirm integration scope.
- Onboarding: setup links + connection detection.
- Runtime messaging: webhooks + inbox + broadcasts.
- Voice: Pipecat voice agent assignment and call lifecycle.

2. Validate environment and base URLs.
- `KAPSO_API_KEY` is required.
- `KAPSO_API_BASE_URL` should point to host only (for example `https://api.kapso.ai`).
- Use Platform API routes under `/platform/v1`.

3. Implement onboarding first.
- Create customer setup links.
- Persist `customer_id`, `phone_number_id`, and onboarding status.
- Handle completion using project webhooks and/or success redirect query params.

4. Implement webhook reliability before business logic.
- Verify signatures.
- Enforce idempotency using `X-Idempotency-Key`.
- Return `200` quickly, then process async.

5. Add operational flows.
- Broadcast lifecycle: create draft -> add recipients -> send -> monitor statuses.
- Inbox rules: respect handoff/workflow state when human takeover is needed.

6. Add voice only after messaging path is stable.
- Enable calls for the WhatsApp config.
- Create Pipecat-backed voice agent.
- Assign one primary enabled voice agent per WhatsApp config.

## Working Rules

- Keep customer and WhatsApp identifiers explicit in every request and log entry.
- Fail fast on missing IDs or missing API key.
- Treat webhook handlers as at-least-once delivery.
- Do not send messages from closed conversations unless the flow explicitly reopens or hands off.
- For voice routing, verify that assignment is both `is_primary: true` and `enabled: true`.

## Troubleshooting Checklist

1. Onboarding completed but no connected number:
- Check `whatsapp.phone_number.created` project webhook subscription.
- Check webhook signature verification and idempotency handling.

2. Broadcast stuck in draft/sending:
- Confirm recipients were added to the same `broadcast_id`.
- Inspect recipient status list for delivery-level failures.

3. Voice calls not reaching Pipecat:
- Confirm calls are enabled on the WhatsApp config.
- Confirm provider credentials and `agent_name`.
- Confirm the voice-agent assignment is primary and enabled.

## References

- Platform endpoints and implementation patterns: `references/platform.md`
- Webhook semantics and reliability controls: `references/webhooks.md`
- Voice agent architecture and API setup: `references/voice-agents.md`

## Upstream Skill Pack

If you need prebuilt scripts, install Kapso's public agent skills and adapt the relevant skill:

```bash
npx skills add https://github.com/gokapso/agent-skills
```
