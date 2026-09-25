---
title: "Models troubleshooting"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://nodejs.org/en/download"
  - "https://docs.python.org/3/library/venv.html"
  - "https://git-scm.com/docs"
  - "https://github.com/termux/termux-app"
  - "https://github.com/termux/proot-distro"
  - "https://docs.ollama.com/faq"
  - "https://docs.ollama.com/gpu"
  - "https://openrouter.ai/docs/api/reference/limits"
  - "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
  - "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository"
---

# Models troubleshooting

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

Find the exact symptom, then check the cause before changing your system. Replace uppercase command placeholders deliberately. Never attach unredacted logs.

## Model not found

**SYMPTOM:** The provider cannot resolve the requested model.

**CAUSE:** Wrong ID/tag, missing local download, wrong provider prefix, or model removal.

**CHECK:** Use `ollama list` locally or inspect the provider’s current model catalog; compare exact identifiers.

**FIX:** Pull the intended local tag or select an available remote ID. Aider provider prefixes are part of its syntax.

**VERIFY:** A small inference request succeeds with the displayed intended model.

## Connection refused on 11434

**SYMPTOM:** Client cannot reach the Ollama server.

**CAUSE:** Server stopped, wrong machine/port, broken SSH tunnel, or incorrect base URL.

**CHECK:** Check the host running the server and `ollama list`; inspect the documented service status or manual server terminal.

**FIX:** Start the official service or one manual `ollama serve` instance; correct the endpoint/tunnel. Do not expose a public unauthenticated port.

**VERIFY:** `ollama list` and a tiny local request work from the intended client.

## Address already in use

**SYMPTOM:** A service cannot bind its requested port.

**CAUSE:** Another process already owns the port, often the existing Ollama app.

**CHECK:** Inspect running applications and the current server; on supported Linux use `ss -ltn` for listening TCP ports.

**FIX:** Use the existing intended server or stop only the identified conflicting process. Choose a different preview port if appropriate.

**VERIFY:** Exactly one intended service answers on the chosen port.

## Out of memory / process killed

**SYMPTOM:** Inference or build fails during loading or long context.

**CAUSE:** Weights, KV cache, concurrency, OS, and other apps exceed memory.

**CHECK:** Check available RAM/VRAM, loaded models via `ollama ps`, context settings, and other applications.

**FIX:** Use a smaller/stronger quantization where appropriate, shorter context, and one request; move heavy work to suitable hardware.

**VERIFY:** Complete a representative small task without swapping excessively or being killed.

## CUDA / GPU unavailable

**SYMPTOM:** Model runs on CPU or the GPU backend fails.

**CAUSE:** Unsupported hardware, mismatched driver/runtime, unavailable device passthrough, or insufficient VRAM.

**CHECK:** Compare exact hardware/driver/OS with Ollama’s current GPU documentation; inspect `ollama ps` processor allocation.

**FIX:** Follow vendor-supported driver guidance. WSL and containers need their own device support; Android PRoot is not desktop CUDA.

**VERIFY:** A known small model reports the intended processor allocation; otherwise use an honest CPU route.

## Malformed tool calls or broken edits

**SYMPTOM:** Chat works but the agent cannot perform reliable actions.

**CAUSE:** Model lacks required tool/edit format, context is too small, or protocol compatibility is partial.

**CHECK:** Check agent/provider/model tool support and inspect a minimal non-sensitive task.

**FIX:** Use a documented tool-capable model or a client with a suitable text-editing mode. Keep permissions intact.

**VERIFY:** The small task completes with valid actions and independently passing tests.

## Context window exceeded

**SYMPTOM:** Request exceeds token or local memory limits.

**CAUSE:** Too many files, long history, verbose tool output, or reserved output budget.

**CHECK:** Inspect selected files and the exact model/runtime context settings.

**FIX:** Start a focused session, select fewer files, summarize relevant history, and keep output budget. Increasing context also costs memory/tokens.

**VERIFY:** A focused task completes without truncating essential requirements.

## Documentation sources

- [Node.js official downloads](https://nodejs.org/en/download)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Git reference](https://git-scm.com/docs)
- [Termux installation and limitations](https://github.com/termux/termux-app)
- [PRoot-Distro upstream manual](https://github.com/termux/proot-distro)
- [Ollama FAQ and local-only configuration](https://docs.ollama.com/faq)
- [Ollama GPU support](https://docs.ollama.com/gpu)
- [OpenRouter rate limits](https://openrouter.ai/docs/api/reference/limits)
- [Google consumer CLI transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
- [GitHub sensitive-data remediation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
