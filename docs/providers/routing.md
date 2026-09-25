---
title: "Provider routing: documented support versus experiments"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://aider.chat/docs/llms/openrouter.html"
  - "https://aider.chat/docs/llms/ollama.html"
  - "https://opencode.ai/docs/providers/"
  - "https://docs.continue.dev/cli/configuration"
  - "https://developers.openai.com/codex/config-advanced"
  - "https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration"
  - "https://openrouter.ai/docs/cookbook/coding-agents/codex-cli"
  - "https://docs.ollama.com/integrations/claude-code"
---

# Provider routing: documented support versus experiments

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Read the support label literally

| Integration | Evidence | Boundary |
| --- | --- | --- |
| Aider ↔ OpenRouter / Ollama | Tool documentation | Exact model and runtime still matter |
| OpenCode ↔ OpenRouter / Ollama | Tool documentation | Local model must support intended behavior |
| Continue ↔ providers | Provider config documentation | CLI and IDE authentication differ |
| Codex ↔ Ollama | OpenAI-documented OSS mode | Uses a local model, not an OpenAI model |
| Claude Code ↔ Ollama | Ollama-documented integration | Not blanket Anthropic support |
| Claude Code ↔ OpenRouter | OpenRouter-documented integration | Anthropic-model route has narrower guarantees; arbitrary models experimental |
| Codex ↔ OpenRouter | OpenRouter-documented custom provider | Model metadata and protocol must match |
| Gemini / Antigravity ↔ arbitrary OpenAI endpoint | Not established in reviewed docs | Don't assume an OpenAI-compatible base URL works |

## Endpoint families

OpenRouter's OpenAI-compatible API commonly uses `https://openrouter.ai/api/v1`. Its Claude Code recipe uses an Anthropic-compatible base `https://openrouter.ai/api`. Ollama native clients use `http://127.0.0.1:11434`; OpenAI-compatible clients generally add `/v1`. Use the client's exact protocol, not a guessed URL suffix.

## Claude Code with a provider-documented gateway

For the OpenRouter recipe, load your own `OPENROUTER_API_KEY` securely, inspect the upstream caveats, then in **Bash**:

```bash
export ANTHROPIC_BASE_URL=https://openrouter.ai/api
export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"
export ANTHROPIC_API_KEY=""
claude
```

This changes the model provider and its billing path. It does not grant an Anthropic subscription. Current OpenRouter documentation narrows its guaranteed route to Anthropic model compatibility; treat other model families as experimental. Choose an exact supported model and verify tool use on a small repository.

Ollama documents its own launcher and manual configuration. For a local manual endpoint, its pattern uses `ANTHROPIC_BASE_URL=http://localhost:11434`, a non-secret placeholder `ANTHROPIC_AUTH_TOKEN=ollama`, and an empty `ANTHROPIC_API_KEY`. An explicit local model and sufficient context are required. Inspect `ollama launch --help` and the current integration page before using the launcher, especially where it offers cloud models too.

Cached sign-in and environment configuration can conflict. Follow the CLI's official logout/configuration flow. Do not delete all credential directories or publish their contents to diagnose the problem.

## Codex custom providers

Official Codex config supports custom providers and a documented OSS route. `configs/codex-openrouter.toml.example` demonstrates a provider block using an environment-key reference; confirm the current OpenRouter recipe and Codex schema before merging it into your own config. Never overwrite an existing config blindly.

Provider model metadata may need explicit catalog configuration in current Codex releases. A successful API request does not remove those warnings or guarantee all features. Prefer official OSS mode for the documented Ollama path, and use a model with compatible tool/context behavior.

## Revert cleanly

Use a separate shell for a routing experiment. When finished, close it or remove only the variables you intentionally added, and restore the provider selection through the client's documented settings. Keep a backup of a non-secret config before editing it. Re-run the client's status command and a small task to confirm which provider is active.

## Documentation sources

- [Aider OpenRouter provider](https://aider.chat/docs/llms/openrouter.html)
- [Aider Ollama provider](https://aider.chat/docs/llms/ollama.html)
- [OpenCode providers](https://opencode.ai/docs/providers/)
- [Continue CLI configuration](https://docs.continue.dev/cli/configuration)
- [Codex provider configuration and OSS mode](https://developers.openai.com/codex/config-advanced)
- [OpenRouter-documented Claude Code integration](https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration)
- [OpenRouter-documented Codex integration](https://openrouter.ai/docs/cookbook/coding-agents/codex-cli)
- [Ollama-documented Claude Code integration](https://docs.ollama.com/integrations/claude-code)
