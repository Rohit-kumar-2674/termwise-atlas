---
title: "Lab 8: an OpenRouter-compatible coding agent"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://openrouter.ai/docs/quickstart"
  - "https://openrouter.ai/docs/api/reference/limits"
  - "https://aider.chat/docs/llms/openrouter.html"
---

# Lab 8: an OpenRouter-compatible coding agent

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Pick a model deliberately

Finish [OpenRouter setup](../providers/openrouter.md) and [Aider installation](../tools/aider.md). Choose an exact current model ID, check tool/editing support, privacy, context, limits, and price. If you require no-charge access, verify the free variant and route now; no permanent model ID is supplied.

Load your own key using the [hidden prompt](../security/api-keys.md), then inspect available models:

```bash
aider --list-models openrouter/
```

Run `aider --model openrouter/PROVIDER/MODEL --no-auto-commits` after replacing the placeholder. Never put a literal key on the command line. Use a low-budget learning key where the service supports it.

## Ask one small question

Ask the agent to explain `examples/python-lab/text_tools.py`, without editing or running commands. Inspect the model shown by the client and account usage. If authenticated requests fail, check the model ID and error status before retrying; don't loop through keys to evade limits.

Then request a narrow change and apply [the Git loop](../git/workflow.md). Run local tests independently. Your code is processed remotely along this route even though the terminal runs on your device. Stop the session when the task is complete and clear the temporary environment variable.

## Documentation sources

- [OpenRouter quickstart](https://openrouter.ai/docs/quickstart)
- [OpenRouter rate limits](https://openrouter.ai/docs/api/reference/limits)
- [Aider OpenRouter provider](https://aider.chat/docs/llms/openrouter.html)
