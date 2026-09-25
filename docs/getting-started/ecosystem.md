---
title: "How agents and providers fit together"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://developers.openai.com/codex/config-advanced"
  - "https://docs.ollama.com/api/openai-compatibility"
  - "https://openrouter.ai/docs/quickstart"
  - "https://code.claude.com/docs/en/permissions"
---

# How agents and providers fit together

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Follow one request

| Layer | Example | Job |
| --- | --- | --- |
| You | “Fix the failing date parser test” | Define scope, constraints, validation |
| Coding agent | Aider, Codex, OpenCode | Select context, request model output, propose edits/tools |
| API protocol | OpenAI-compatible, Anthropic-compatible, native Ollama | Define message and tool-call format |
| Provider | OpenRouter, OpenAI, Anthropic, local Ollama | Authenticate, route, and execute inference |
| Model | An exact provider model ID or Ollama tag | Predict the response |
| Execution environment | Your shell or sandbox | Run approved tests and commands |

Aider can send an OpenAI-compatible request to OpenRouter, which routes it to a selected model provider. Another setup sends a native Ollama request to a model running on your machine. The editor interface can look the same while privacy and cost differ completely.

## Compatibility is more than a URL

An API-compatible service may support only part of a protocol. Chat Completions, Responses, Anthropic Messages, streaming, images, tool calls, prompt caching, and model discovery are distinct features. Changing `base_url` does not prove that a whole agent works.

Ask four questions: Does the **client** support this provider? Does the **endpoint** implement the needed protocol? Does the **model** support the agent's tool format? Does your **environment** support the agent's execution/sandbox behavior?

“Official” in this guide always identifies whose documentation is involved. An Ollama guide for Claude Code is provider-documented compatibility, not blanket Anthropic certification. Unknown and unavailable are different: an unreviewed integration is labelled **not established**, rather than invented or declared impossible.

## Context and permissions

Context includes your prompt, selected source files, repository instructions, conversation history, and tool output. A large context window is a maximum capacity, not a promise of accurate understanding. Secrets in a repository can be copied into context; `.gitignore` alone does not prevent an agent reading them.

A model's suggestion is not an authorization. The agent and execution environment enforce permission controls, while you remain responsible for reviewing consequential actions. Continue with [provider routing](../providers/routing.md) and [agent safety](../security/agent-safety.md).

## Documentation sources

- [Codex provider configuration and OSS mode](https://developers.openai.com/codex/config-advanced)
- [Ollama API compatibility](https://docs.ollama.com/api/openai-compatibility)
- [OpenRouter quickstart](https://openrouter.ai/docs/quickstart)
- [Claude Code permissions](https://code.claude.com/docs/en/permissions)
