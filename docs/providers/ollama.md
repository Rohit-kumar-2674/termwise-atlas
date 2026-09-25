---
title: "Ollama: a complete local inference lab"
last_verified: 2026-09-22
tool_version: "Ollama v0.34.2 release observed; commands checked against rolling CLI reference"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.ollama.com/cli"
  - "https://docs.ollama.com/linux"
  - "https://docs.ollama.com/macos"
  - "https://docs.ollama.com/windows"
  - "https://docs.ollama.com/faq"
  - "https://docs.ollama.com/gpu"
  - "https://docs.ollama.com/api/openai-compatibility"
  - "https://docs.ollama.com/integrations/claude-code"
  - "https://aider.chat/docs/llms/ollama.html"
---

# Ollama: a complete local inference lab

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Ollama v0.34.2 release observed; commands checked against rolling CLI reference. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What runs locally?

Ollama downloads and runs supported model weights and exposes an API. Its runtime is MIT-licensed; each model has its own license. A local inference request to a local model can stay on your hardware. Downloading models, using cloud models, enabling cloud features, or connecting an agent's other network tools changes that privacy boundary.

This lab uses an explicitly local tag. You need disk space for its download plus RAM for weights, context, runtime, and your operating system. [Hardware planning](hardware.md) provides estimates rather than performance promises. Don't download a 19 GB model onto a nearly full phone or laptop.

## 1. Install for your operating system

There is **no `ollama install` CLI command**. Install the application/runtime first.

=== "Windows"

    Download the installer from [ollama.com/download/windows](https://ollama.com/download/windows). Current documented requirements include Windows 10 22H2 or newer. Run the official installer, reopen PowerShell, and check:

    ```powershell
    ollama --version
    ```

    The application normally manages the server. Don't start a second server just because a tutorial says `serve`.

=== "Linux / WSL"

    The official installer is at `https://ollama.com/install.sh`. Download it for inspection before execution:

    ```bash
    curl -fsSL https://ollama.com/install.sh -o ollama-install.sh
    less ollama-install.sh
    sh ollama-install.sh
    ollama --version
    ```

    The script can request elevated privileges and configure a system service. Read the Linux page for manual installs, dependencies, upgrades, and service changes. In WSL, verify the actual GPU/driver support instead of installing random CUDA packages.

=== "macOS"

    Download the app from [ollama.com/download/mac](https://ollama.com/download/mac). Current requirements are macOS 14+, with Apple Silicon GPU support and Intel CPU support. Open it, follow its command-line setup, then run:

    ```bash
    ollama --version
    ```

=== "Android"

    No official Android-native Ollama installation is established by the reviewed documentation. Termux/PRoot builds are community experiments and do not provide desktop GPU drivers. Prefer SSH to a supported computer or use a provider that your chosen client supports. See [Android](../platforms/android.md).

## 2. Understand the server

Ollama normally listens on `127.0.0.1:11434`. On an installation where no app or system service starts it, run this in a separate terminal:

```bash
ollama serve
```

Leave it running while you use the client. “Address already in use” often means the server already exists. Do not start multiple competing services or expose port 11434 on the public internet.

For a local-only policy, Ollama documents `OLLAMA_NO_CLOUD=1`. Set it in the environment of the **server process** and restart that process. Setting it in a client shell does not reconfigure an already-running service. For a manual Bash server:

```bash
OLLAMA_NO_CLOUD=1 ollama serve
```

Use the official service-environment instructions for Linux systemd or the Windows/macOS application. This switch does not disable network tools in a separate coding agent; review those separately.

## 3. Download one small learning model

This model is a manageable introduction on suitable hardware, not a strong autonomous coding-agent recommendation:

```bash
ollama pull qwen2.5-coder:1.5b
ollama list
ollama show qwen2.5-coder:1.5b
ollama run qwen2.5-coder:1.5b
```

Ask: `Explain this Python expression: sorted(set([3, 1, 3]))`. Exit the chat using the exit instruction displayed by your installed version. A successful answer checks basic inference, not correctness on arbitrary code.

```bash
ollama ps
ollama stop qwen2.5-coder:1.5b
```

`list` shows downloaded models. `ps` shows loaded/running models, including useful processor/context information. `stop` unloads a selected model; it does not remove its stored weights. `ollama rm qwen2.5-coder:1.5b` deletes that selected model from storage, so only run it when you intend to remove the download.

## 4. Connect a coding client

Aider documents the native Ollama route. After [installing Aider](../tools/aider.md), in **Bash**:

```bash
export OLLAMA_API_BASE=http://127.0.0.1:11434
aider --model ollama_chat/qwen2.5-coder:1.5b --no-auto-commits
```

In **PowerShell**:

```powershell
$env:OLLAMA_API_BASE = 'http://127.0.0.1:11434'
aider --model ollama_chat/qwen2.5-coder:1.5b --no-auto-commits
```

Start with a tiny explanation or edit and review the diff. Increase model capability when your hardware permits. Aider's editing approach can work with models that don't implement native tool calls, while autonomous agents can require explicit tool support and much more context.

For [Codex OSS mode](../tools/codex.md), [OpenCode](../tools/opencode.md), or [Continue](../tools/continue.md), use that client's own provider instructions. An OpenAI-compatible client generally uses Ollama's `/v1` endpoint; a native Ollama client uses its own API base. These paths are not interchangeable.

## 5. Control memory and storage

Quantization reduces weight precision and usually memory use, with possible quality trade-offs. Model file size is not total required RAM. Longer context increases cache memory, and concurrent requests add pressure. Begin with one model and a small repository selection before enlarging context.

Default storage depends on OS and whether the service runs as your user: macOS commonly uses `~/.ollama/models`, Windows uses the user's `.ollama` directory, and Linux service installations can use the `ollama` service user's location. Follow the FAQ for `OLLAMA_MODELS` changes; set the service environment and directory permissions deliberately. Never move/delete a directory while a model is loading.

For CPU-only hardware, expect slower token generation. A supported GPU helps only when its available memory and driver stack fit the workload. `ollama ps` can help confirm processor allocation. A laptop cooling system and competing applications affect sustained speed.

## 6. Use your own remote Ollama server

Run Ollama on the remote host's loopback interface. On the client machine:

```bash
ssh -N -L 11434:127.0.0.1:11434 developer@your-host.example
```

Replace the example host and user, verify the SSH fingerprint, and keep the tunnel alive. Point the client to its local `http://127.0.0.1:11434`. This encrypts transport through SSH; inference is on the server and is accessible to its operator. If local port 11434 is occupied, use a different local port and update the client base URL.

Do not publish an unauthenticated `OLLAMA_HOST=0.0.0.0` service. Reverse proxies need deliberate authentication, TLS, access controls, and operational maintenance; SSH forwarding is simpler for this learning lab.

## 7. Claude Code compatibility

Ollama documents a Claude Code integration including `ollama launch claude` and an Anthropic-compatible endpoint. That is **OLLAMA-DOCUMENTED COMPATIBILITY**, not an Anthropic guarantee for every model. Review [routing](routing.md), pick an explicit local tag, inspect the generated configuration, and check memory. Recommended agent context sizes can be far beyond a small laptop's practical capacity.

## Completion check

You can name the installed model, tell where inference runs, distinguish downloaded and loaded models, stop a model, and explain which endpoint the agent uses. For errors, use [Ollama troubleshooting](../troubleshooting/models.md).

## Documentation sources

- [Ollama CLI reference](https://docs.ollama.com/cli)
- [Ollama Linux installation](https://docs.ollama.com/linux)
- [Ollama macOS requirements](https://docs.ollama.com/macos)
- [Ollama Windows requirements](https://docs.ollama.com/windows)
- [Ollama FAQ and local-only configuration](https://docs.ollama.com/faq)
- [Ollama GPU support](https://docs.ollama.com/gpu)
- [Ollama API compatibility](https://docs.ollama.com/api/openai-compatibility)
- [Ollama-documented Claude Code integration](https://docs.ollama.com/integrations/claude-code)
- [Aider Ollama provider](https://aider.chat/docs/llms/ollama.html)
