---
title: "Lab 7: local Ollama + Aider"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.ollama.com/cli"
  - "https://aider.chat/docs/llms/ollama.html"
  - "https://aider.chat/docs/usage.html"
---

# Lab 7: local Ollama + Aider

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Preconditions

Finish [Ollama setup](../providers/ollama.md), review [hardware estimates](../providers/hardware.md), and install [Aider](../tools/aider.md). Ollama must run on the same machine or the intended SSH tunnel. A small local model can explain code but may struggle with edits.

```bash
ollama pull qwen2.5-coder:1.5b
ollama list
```

In Bash, point Aider at the local server:

```bash
export OLLAMA_API_BASE=http://127.0.0.1:11434
aider --model ollama_chat/qwen2.5-coder:1.5b --no-auto-commits
```

For PowerShell use `$env:OLLAMA_API_BASE = 'http://127.0.0.1:11434'` before the same Aider command. Add only `examples/python-lab/text_tools.py` to the session using Aider's documented file controls.

## Task and validation

Ask for an explanation of `unique_words` without edits. Compare it with the source and tests. Then request one small docstring clarification and review the diff. Run the Python test command from [Lab 3](generate-tests.md).

Check `ollama ps` while the session is active and verify the explicit local model. No paid API key is needed for this local route, but model download needs internet. Review Aider's other features/network behavior before making broader privacy claims. Stop the model when done with `ollama stop qwen2.5-coder:1.5b`.

## Documentation sources

- [Ollama CLI reference](https://docs.ollama.com/cli)
- [Aider Ollama provider](https://aider.chat/docs/llms/ollama.html)
- [Aider usage](https://aider.chat/docs/usage.html)
