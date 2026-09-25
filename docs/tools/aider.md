---
title: "Aider"
last_verified: 2026-09-22
tool_version: "v0.86.0 latest GitHub release observed (2025-08-09); check project activity separately"
verification: source-reviewed
status: "OFFICIAL"
sources:
  - "https://aider.chat/docs/install.html"
  - "https://aider.chat/docs/llms/openrouter.html"
  - "https://aider.chat/docs/llms/ollama.html"
  - "https://aider.chat/docs/usage.html"
  - "https://github.com/Aider-AI/aider"
---

# Aider

> **OFFICIAL** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** v0.86.0 latest GitHub release observed (2025-08-09); check project activity separately. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What is it?

An Apache-2.0 command-line pair programmer with Git-oriented editing. [Aider-AI/aider](https://github.com/Aider-AI/aider) is the upstream project. A release date is a snapshot, not proof of current maintenance or model quality.

## Best For

Small, reviewable edits, learning diffs, regression tests, and comparing a cloud provider with a local text-editing model.

## Cost

**FREE / OPEN SOURCE** client. **LOCAL** models require your hardware; cloud calls use the chosen provider's pricing or limited free offer. OpenRouter support does not make Anthropic/OpenAI models free.

## Requirements

Git and Python. Upstream recommends `aider-install`, which manages an isolated Aider environment and can provision Python 3.12. Direct pip installation has narrower Python support; do not assume a phone's newest Python will work.

## Supported Platforms

Upstream documents Windows, macOS, Linux, and hosted development routes. Termux/PRoot are **COMMUNITY** paths; ARM packages and dependencies can fail. On an Android phone, a remote Linux workspace is often simpler.

## Installation

### Linux / macOS — Bash

```bash
python3 -m venv .aider-bootstrap
.aider-bootstrap/bin/python -m pip install aider-install
.aider-bootstrap/bin/aider-install
```

### Windows PowerShell

```powershell
py -3 -m venv .aider-bootstrap
.\.aider-bootstrap\Scripts\python.exe -m pip install aider-install
.\.aider-bootstrap\Scripts\aider-install.exe
```

Read the installer's PATH guidance, reopen your shell, and run `aider --version`. Keep this bootstrap environment outside repositories you publish. If your architecture lacks a supported managed Python, use a supported host rather than forcing an incompatible binary.

## Configuration

Load `OPENROUTER_API_KEY` securely for OpenRouter. `aider --list-models openrouter/` helps discover accepted identifiers; confirm the exact model and price in the provider catalog.

For Ollama, set `OLLAMA_API_BASE` to `http://127.0.0.1:11434`. The documented model prefix is `ollama_chat/`. Choose a context length that fits memory. Review `.aider.conf.yml` and automatic-commit behavior; chat/history files may contain private code and should stay out of Git.

## First Command

Once Ollama is installed and the small model downloaded:

```bash
aider --model ollama_chat/qwen2.5-coder:1.5b --no-auto-commits
```

This is a small learning exercise, not a claim that a 1.5B model reliably handles a large repository. Ask it to explain one function first.

## Example Workflow

Open the [Python lab](../examples/fix-a-bug.md), add only the relevant file with `/add`, ask for one minimal patch, use `/diff`, and run its tests. `/help` lists installed commands. With automatic commits disabled, you choose the final commit after review.

## Troubleshooting

- `aider` absent after installation: check the installer's PATH instructions; avoid a second unrelated system install.
- Model cannot produce edits: reduce the scope or use a more capable model; successfully generating text is a weaker test.
- OpenRouter 404: do not omit Aider's `openrouter/` prefix before the provider/model identifier.
- Python wheel build failure on ARM: read the failing package and supported Python range; use the remote or Debian route if needed.
- Privacy routing error: choose a provider compatible with your data policy; do not enable training just to make a request succeed.

## Documentation sources

- [Aider installation](https://aider.chat/docs/install.html)
- [Aider OpenRouter provider](https://aider.chat/docs/llms/openrouter.html)
- [Aider Ollama provider](https://aider.chat/docs/llms/ollama.html)
- [Aider usage](https://aider.chat/docs/usage.html)
- [aider upstream source and license](https://github.com/Aider-AI/aider)
