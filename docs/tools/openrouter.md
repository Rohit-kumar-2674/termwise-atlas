---
title: "OpenRouter"
last_verified: 2026-09-22
tool_version: "Hosted API; model catalog and account limits are dynamic"
verification: source-reviewed
status: "OFFICIAL"
sources:
  - "https://openrouter.ai/docs/quickstart"
  - "https://openrouter.ai/docs/api/reference/limits"
  - "https://openrouter.ai/models"
  - "https://aider.chat/docs/llms/openrouter.html"
---

# OpenRouter

> **OFFICIAL** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Hosted API; model catalog and account limits are dynamic. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What is it?

A hosted model API/router, not a local inference engine or an installable coding agent. A single account can access different upstream models. The hosted service is not labeled open source.

## Best For

A provider layer beneath your chosen coding agent. Learn the distinction between the editor, agent, protocol, and inference host before connecting them.

## Cost

**FREE TIER / PAID API / REQUIRES API KEY** depending on the selected model and account limits. Free models can disappear or be rate-limited; paid models are not made free by routing.

## Requirements

Internet access, a legitimate account/key, and a client that speaks a supported API protocol.

## Supported Platforms

The API is OS-independent; the coding client determines native platform support. Browser and Android clients remain cloud inference.

## Installation

There is no OpenRouter coding CLI to install for this tutorial. Create an account through the official service, create a scoped key, then install a compatible agent such as Aider or OpenCode.

## Configuration

Follow the [OpenRouter guide](../providers/openrouter.md) to select a model, inspect price and limits, and load `OPENROUTER_API_KEY` safely.

## First Command

```bash
aider --list-models openrouter/
```

This lists local models or client-known model identifiers; it is not a billed inference request.

## Example Workflow

Complete [local coding](../examples/local-ollama.md) or [multi-provider coding](../examples/openrouter-agent.md), check the active model and endpoint, then make one reviewed change.

## Troubleshooting

Separate transport failures, authentication failures, model selection, context limits, and tool-use errors. Follow the [provider troubleshooting entries](../troubleshooting/models.md); do not solve a routing error by exposing the server publicly or weakening data policies.

## Documentation sources

- [OpenRouter quickstart](https://openrouter.ai/docs/quickstart)
- [OpenRouter rate limits](https://openrouter.ai/docs/api/reference/limits)
- [OpenRouter model catalog](https://openrouter.ai/models)
- [Aider OpenRouter provider](https://aider.chat/docs/llms/openrouter.html)
