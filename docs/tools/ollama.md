---
title: "Ollama"
last_verified: 2026-09-22
tool_version: "v0.34.2 release observed"
verification: source-reviewed
status: "OFFICIAL"
sources:
  - "https://docs.ollama.com/cli"
  - "https://docs.ollama.com/linux"
  - "https://docs.ollama.com/windows"
  - "https://docs.ollama.com/macos"
  - "https://docs.ollama.com/faq"
  - "https://github.com/ollama/ollama"
---

# Ollama

> **OFFICIAL** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** v0.34.2 release observed. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What is it?

A model runtime that can serve downloaded models on your own hardware. It also has distinct cloud offerings. The runtime is MIT licensed.

## Best For

A provider layer beneath your chosen coding agent. Learn the distinction between the editor, agent, protocol, and inference host before connecting them.

## Cost

**FREE / OPEN SOURCE / LOCAL** for the Ollama runtime and local inference; hardware and electricity still cost money. Ollama cloud models have separate account pricing.

## Requirements

Supported host, storage and enough memory for the selected model.

## Supported Platforms

Windows, Linux, macOS; WSL can run the Linux distribution. Native Android is not an upstream-certified runtime here. Remote SSH clients can use a supported machine.

## Installation

Use the platform-specific instructions in the [full Ollama lab](../providers/ollama.md). There is no `ollama install` subcommand: install the application using its official OS installer.

## Configuration

Select a local tag explicitly, inspect its license, and keep the server on loopback. See [remote access](../providers/ollama.md).

## First Command

```bash
ollama list
```

This lists local models or client-known model identifiers; it is not a billed inference request.

## Example Workflow

Complete [local coding](../examples/local-ollama.md) or [multi-provider coding](../examples/openrouter-agent.md), check the active model and endpoint, then make one reviewed change.

## Troubleshooting

Separate transport failures, authentication failures, model selection, context limits, and tool-use errors. Follow the [provider troubleshooting entries](../troubleshooting/models.md); do not solve a routing error by exposing the server publicly or weakening data policies.

## Documentation sources

- [Ollama CLI reference](https://docs.ollama.com/cli)
- [Ollama Linux installation](https://docs.ollama.com/linux)
- [Ollama Windows requirements](https://docs.ollama.com/windows)
- [Ollama macOS requirements](https://docs.ollama.com/macos)
- [Ollama FAQ and local-only configuration](https://docs.ollama.com/faq)
- [ollama upstream source and license](https://github.com/ollama/ollama)
