---
title: "Frequently asked questions"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://code.claude.com/docs/en/authentication"
  - "https://docs.ollama.com/integrations/claude-code"
  - "https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration"
  - "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
  - "https://developers.openai.com/codex/config-advanced"
  - "https://openrouter.ai/docs/api/reference/limits"
  - "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository"
---

# Frequently asked questions

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Is Claude Code free?

Official Claude cloud usage requires eligible paid account/API access. The CLI's availability to download does not make the service free or its license open source. Provider-documented alternative-model routes have their own terms and costs. See [Claude Code](../tools/claude-code.md).

## Can Claude Code use Ollama?

Ollama documents a Claude Code integration and Anthropic-compatible endpoint. Label it **Ollama-documented compatibility**, choose a suitable explicit model, and check context/memory. It is not an Anthropic guarantee or a way to obtain paid Claude models for free. See [routing](../providers/routing.md).

## Can Claude Code use OpenRouter?

OpenRouter documents a recipe with an Anthropic-compatible base URL. Current guarantees are narrower than “every model works”; arbitrary-model experiments need an experimental label. Use your own legitimate provider key and check model cost.

## Is Gemini CLI free?

The software is Apache-2.0. Google announced a consumer-access transition to Antigravity CLI on June 18, 2026, so old consumer free-quota claims are not dependable. Gemini CLI's retained API/enterprise routes and the separate Gemini API free/paid tiers must be checked against your account. See [Google access](../providers/gemini.md).

## Can Codex run locally?

The official Codex CLI runs on your computer and normally connects to its selected provider. OpenAI documents an OSS mode with local providers including Ollama; that uses a local model, not an OpenAI model running on your hardware. Tool capability and context must fit. See [Codex](../tools/codex.md).

## Which coding agents support local models?

Aider, OpenCode, Continue, and Codex have documented local-provider routes. Model compatibility varies by mode. Ollama additionally documents Claude Code compatibility. Review the [matrix](../getting-started/comparison.md) rather than treating all local routes as equivalent.

## What works on Android?

Termux supports useful Git, Python, Node, and SSH workflows. Individual native agent compatibility is not inferred from Linux support. PRoot can help with glibc but is not a VM. Browser terminals or SSH to a supported host are reliable architectural options when native dependencies fail. Read [Android first](../platforms/android.md).

## What is the cheapest setup?

Start with the no-API learning fixtures. If you already own suitable hardware, small local models avoid metered inference fees. Otherwise compare legitimate current allowances with small paid tasks; include compute, storage, retries, time, and privacy. There is no universally cheapest provider for every workload.

## What works without a GPU?

Cloud models do not require a client-side GPU. Small local quantized models can run on supported CPUs, usually with lower speed and capability. [Hardware estimates](../providers/hardware.md) explain realistic starting points.

## Do I need an API key?

Not for local inference or these repository checks. Some official clients use account sign-in. BYOK providers require your own valid key, and an account subscription does not automatically fund API usage. The chosen tool page states its authentication route.

## Can I use a free OpenRouter model?

When a suitable free model is currently available to your account under acceptable data terms, yes. Check the exact free model ID, limits, tool support, and routing behavior. Free availability is not permanent and does not authorize quota abuse.

## Why am I getting 429 errors?

Rate limits, exhausted daily quotas, or upstream capacity can cause them. Read the error and retry guidance, reduce concurrency, and check account usage. See [authentication troubleshooting](../troubleshooting/authentication.md); don't cycle accounts to evade limits.

## Which tool should a beginner choose?

Choose a documented route for your device and budget, then do one small lab. Aider plus Ollama is a clear local learning route on suitable hardware; Aider/OpenCode plus OpenRouter provides provider choice; official account CLIs fit eligible users who want their vendor experience. Use the [chooser](../getting-started/choose.md).

## Are cloud terminals and local inference equally private?

No. “Local to a cloud host” still means your source and model processing are on a remote machine. An agent can also use remote tools even when inference is local. Inspect both model routing and execution permissions.

## I exposed a key. What now?

Revoke/rotate it immediately through the provider, inspect usage, and replace legitimate secret stores. Deleting the visible copy is insufficient. Follow [the incident steps](../security/api-keys.md).

## Documentation sources

- [Claude Code authentication](https://code.claude.com/docs/en/authentication)
- [Ollama-documented Claude Code integration](https://docs.ollama.com/integrations/claude-code)
- [OpenRouter-documented Claude Code integration](https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration)
- [Google consumer CLI transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
- [Codex provider configuration and OSS mode](https://developers.openai.com/codex/config-advanced)
- [OpenRouter rate limits](https://openrouter.ai/docs/api/reference/limits)
- [GitHub sensitive-data remediation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
