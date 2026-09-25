---
title: "Models, quantization, and context"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.ollama.com/cli"
  - "https://docs.ollama.com/faq"
  - "https://docs.ollama.com/gpu"
---

# Models, quantization, and context

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Read a model label

Parameters describe model size, not a guarantee of coding quality. Quantization reduces weight precision to trade memory for possible quality loss. RAM and VRAM determine fit; CPU/GPU and memory bandwidth affect speed. Context is the amount of input and generated history a model can consider, subject to runtime configuration and memory.

The [maintained model table](model-table.md) records exact Ollama tags and primary model pages, download sizes, planning memory ranges, and context caveats. It is an illustrative ladder, not a permanent ranking. Model licenses are separate from Ollama's MIT runtime license; inspect each upstream card for your intended use.

## Pick for the task

- **Small models:** short explanation, autocomplete, and tiny code transformations. Validate every result.
- **Medium models:** more useful repository edits when the prompt is focused; still test tool/format behavior.
- **Large or agent-oriented models:** richer tool use and longer tasks, with substantial memory/context needs.

Aider can request textual edits, whereas an autonomous agent can require native tool calling. An Ollama tag that answers a chat prompt may still fail an agent's tool schema. If the agent repeatedly emits malformed edits or fake tool calls, changing permissions will not improve the model.

## Compare fairly

Use the same disposable exercise, prompt, context size, and acceptance tests. Record the exact tag/version, quantization, runtime, hardware, latency, memory, and number of repair attempts. Never claim “best” from one answer. Do not benchmark with private data unless every route has permission to process it.

## Manage downloads

Use `ollama show TAG` to inspect an installed model and `ollama list` for stored tags. Tags can change upstream; record the digest when reproducibility matters. Download only what you plan to test, leave disk headroom, and remove an explicitly selected unused model with `ollama rm TAG` when ready.

The [local lab](../examples/local-ollama.md) starts with a small model to teach the workflow. It does not promise production-quality autonomous coding on minimal hardware.

## Documentation sources

- [Ollama CLI reference](https://docs.ollama.com/cli)
- [Ollama FAQ and local-only configuration](https://docs.ollama.com/faq)
- [Ollama GPU support](https://docs.ollama.com/gpu)
