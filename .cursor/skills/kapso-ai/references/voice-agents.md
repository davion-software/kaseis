# Kapso Voice Agents (Pipecat) Reference

## Core Architecture

Kapso voice call flow:

1. Meta emits `calls` webhook to Kapso.
2. Kapso resolves WhatsApp config and primary enabled voice agent assignment.
3. Kapso starts Pipecat session using public API endpoint (for example `POST /public/{agent_name}/start`).
4. Pipecat handles call acceptance and media pipeline (STT -> LLM -> TTS).
5. Kapso tracks call lifecycle and termination.

## Quickstart Notes

The official quickstart uses repository:

- `gokapso/whatsapp-voice-agent-pipecat`

Typical flow:

- Configure environment (`OPENAI_API_KEY`, optional prompt overrides).
- Authenticate with Pipecat Cloud.
- Build and push container.
- Deploy service.
- Link agent in Kapso dashboard and assign to WhatsApp config.

## API Setup Pattern

Enable calls on WhatsApp config first, then create and assign voice agent.

Examples documented in Kapso voice API setup:

- Enable calls on WhatsApp config (`calls_enabled: true`)
- Create voice agent with Pipecat provider config
- Assign voice agent to WhatsApp config with:
  - `is_primary: true`
  - `enabled: true`

## Operational Checks

Before testing live calls:

- WhatsApp config has calls enabled.
- Provider credentials are valid.
- `agent_name` matches deployed Pipecat service.
- Assignment is enabled and primary.

During incidents:

- Check call records/history for status transitions.
- Confirm Pipecat service health and auth.
- Confirm incoming webhook processing and signature verification.
