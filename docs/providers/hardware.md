---
title: "Choose a realistic local setup"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.ollama.com/gpu"
  - "https://docs.ollama.com/faq"
---

# Choose a realistic local setup

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Start with available memory

These are planning ranges, not benchmark results or supported minimums for every model. Leave memory for the OS, browser, editor, and agent. Disk capacity is separate from RAM. Quantization and context size can change the result substantially.

| Installed RAM | Realistic starting point | Main limitation |
| --- | --- | --- |
| 4 GB | Remote inference; tiny local explanation experiments if enough free memory | Little headroom; autonomous coding is unrealistic |
| 8 GB | Roughly 1–3B quantized model, short context | Build tools and browser compete for memory |
| 16 GB | Often a 7B-class quantized model with modest context | Larger context/model combinations can swap |
| 32 GB | Explore 14B-class or selected larger quantized models | GPU VRAM and context still determine speed/fit |
| 64 GB | Larger quantized models and more context, measured incrementally | Not every large model fits; throughput varies |

## CPU and GPU choices

| Hardware | What to expect |
| --- | --- |
| CPU only | Supported local models can work, often slowly; start small |
| Integrated GPU | Support varies; shared memory is not unlimited VRAM |
| NVIDIA GPU | Check exact GPU, driver, and available VRAM in Ollama's current list |
| AMD/other GPUs | Check the documented runtime/backend for your platform |
| Apple Silicon | Unified memory can hold model and cache, shared with the entire system |
| Phone | Thermal, memory, storage, architecture, and OS restrictions dominate |

An external cloud model avoids local inference hardware requirements but introduces provider cost and data transfer. A remote Ollama server uses the server's hardware and trust boundary.

## Estimate weights, then add overhead

A rough lower-bound calculation for 4-bit weights is `parameters × 4 / 8` bytes, before metadata and runtime overhead. A 7-billion-parameter model is about 3.5 GB in that simplified calculation, but an actual quantized file can be larger. Context cache, parallel requests, and application memory come on top.

Mixture-of-experts models may activate fewer parameters per token but still require storage/memory for the larger set of weights. “3B active” does not mean a 30B MoE fits like a dense 3B model.

## Measure instead of guessing

Start one model, one request, and short context. Observe OS memory pressure and `ollama ps`; time a representative task. Increase one variable at a time. Out-of-memory errors mean reduce model/context/concurrency or change hardware, not disable safety features. See [model selection](local-models.md).

## Documentation sources

- [Ollama GPU support](https://docs.ollama.com/gpu)
- [Ollama FAQ and local-only configuration](https://docs.ollama.com/faq)
