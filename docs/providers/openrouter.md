---
title: "OpenRouter: choose models with one API"
last_verified: 2026-09-22
tool_version: "Rolling OpenRouter API and provider documentation"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://openrouter.ai/docs/quickstart"
  - "https://openrouter.ai/models"
  - "https://openrouter.ai/docs/api/reference/limits"
  - "https://aider.chat/docs/llms/openrouter.html"
  - "https://opencode.ai/docs/providers/"
  - "https://docs.continue.dev/customize/model-providers/top-level/openrouter"
  - "https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration"
  - "https://openrouter.ai/docs/cookbook/coding-agents/codex-cli"
---

# OpenRouter: choose models with one API

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Rolling OpenRouter API and provider documentation. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What OpenRouter does

OpenRouter routes model requests to supported providers behind a common API. It is a service, not a local model runner. Developers use it to compare models, manage a provider key, and select routes. Model availability, prices, context limits, supported features, and upstream data policies vary.

## Set up your own account

1. Open [OpenRouter](https://openrouter.ai/) and review its terms and privacy controls.
2. Create your own API key. Use a narrow budget/limit when available and know whether it is enforced or advisory.
3. Choose an exact current model ID from the [catalog](https://openrouter.ai/models). A display name is not necessarily its API identifier.
4. Check input/output pricing, context window, tool support, privacy/routing options, and the selected upstream provider.
5. Load `OPENROUTER_API_KEY` with a [hidden prompt](../security/api-keys.md). Do not paste it into an issue, screenshot, config example, or shell command.

`configs/openrouter.env.example` is a template with an empty key. Copying it does not configure every client. Some clients read `.env`; others only read process environment or a private auth store. Follow the specific tool page.

## Free models and limits

A model explicitly marked free, often using a `:free` ID, can have restricted availability and tighter limits. The catalog and limits page are the source of truth. Do not assume the bare model ID has the same price as its free variant. No free model is hardcoded as always available in this guide.

A 429 response can mean per-minute throttling, a daily allowance, or an upstream capacity issue. Read the error, respect retry guidance, and stop runaway retries. Creating extra accounts or cycling keys to evade limits is not a supported workflow.

For metered models, agent retries and large repository context consume tokens. Check account usage after a small task before allowing a long autonomous session. See [cost planning](../getting-started/costs.md).

## Connect a supported tool

### Aider

Load the key, then choose a model from the list:

```bash
aider --list-models openrouter/
```

Run `aider --model openrouter/PROVIDER/MODEL --no-auto-commits` after replacing the placeholder with an actual catalog ID. The leading `openrouter/` is Aider's provider prefix; the remaining identifier is the OpenRouter model ID.

### OpenCode and Continue

[OpenCode](../tools/opencode.md) has a built-in OpenRouter provider selected through `/connect` and `/models`. [Continue](../tools/continue.md) documents provider configuration with a model ID and secret reference. See the supplied configuration examples and confirm whether you're configuring its CLI or IDE.

### Official CLIs through provider compatibility

OpenRouter separately documents Claude Code and Codex recipes. These are labelled **provider-documented** in [routing](routing.md). Anthropic-compatible and OpenAI-compatible endpoints use different base URLs. Arbitrary-model experiments can break tool use even when an ordinary chat completion succeeds.

## Privacy and request behavior

Your code leaves your device and may pass through OpenRouter to an upstream provider. Review logging, data collection, routing, retention, and training controls for the selected route. If a desired free model requires data terms you cannot accept, pick another model or local inference; don't silently weaken privacy settings.

Context limits include input and output budgets. Agents also need room for tool results. A model's advertised maximum context is not a useful default for every task. Start with selected files and a short prompt.

## Verify

Run one read-only repository question, confirm the selected model in the client, and inspect account usage. Then do a tiny edit on a branch and run tests. A nonempty environment variable only proves a string exists; authentication, funds, provider compatibility, and tool quality need separate checks.

## Documentation sources

- [OpenRouter quickstart](https://openrouter.ai/docs/quickstart)
- [OpenRouter model catalog](https://openrouter.ai/models)
- [OpenRouter rate limits](https://openrouter.ai/docs/api/reference/limits)
- [Aider OpenRouter provider](https://aider.chat/docs/llms/openrouter.html)
- [OpenCode providers](https://opencode.ai/docs/providers/)
- [Continue OpenRouter integration](https://docs.continue.dev/customize/model-providers/top-level/openrouter)
- [OpenRouter-documented Claude Code integration](https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration)
- [OpenRouter-documented Codex integration](https://openrouter.ai/docs/cookbook/coding-agents/codex-cli)
