---
title: "Linux: Ubuntu, Debian, Fedora, and Arch"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://nodejs.org/en/download"
  - "https://docs.python.org/3/library/venv.html"
  - "https://docs.ollama.com/gpu"
  - "https://git-scm.com/docs"
---

# Linux: Ubuntu, Debian, Fedora, and Arch

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Install a small foundation

Use the package manager for your distribution. The commands below install development prerequisites; **they do not certify every AI CLI on every distribution**.

=== "Ubuntu / Debian"

    ```bash
    sudo apt update
    sudo apt install git curl ca-certificates python3 python3-venv python3-pip build-essential
    ```

=== "Fedora"

    ```bash
    sudo dnf install git curl ca-certificates python3 python3-pip gcc gcc-c++ make
    ```

=== "Arch-based"

    ```bash
    sudo pacman -Syu --needed git curl ca-certificates python python-pip base-devel
    ```

Inspect the [official Node download page](https://nodejs.org/en/download) for a current LTS and your architecture. Distribution packages can lag; check the installed major against each tool's requirements. If you choose a version manager, use its upstream instructions, verify the source, and understand that it is maintained separately from Node.

```bash
uname -m
node --version
npm --version
git --version
python3 --version
```

Don't add `sudo` to an npm command to make a permissions error disappear. Prefer a user-owned runtime installation. Don't use `pip --break-system-packages`; use `python3 -m venv .venv` for project dependencies.

## Create a working repository

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/Rohit-kumar-2674/termwise-atlas.git
cd termwise-atlas
python3 scripts/doctor.py
```

Pick a [coding tool](../getting-started/comparison.md), install it from its guide, and run its version command before authenticating. Choose [Ollama + Aider](../examples/local-ollama.md) if your goal is local inference. Choose an [OpenRouter-compatible agent](../examples/openrouter-agent.md) when you want provider choice and accept remote processing.

## Architecture and desktop considerations

`x86_64` and `aarch64` require different binaries. Alpine/musl is not interchangeable with Ubuntu/glibc; use the tool's explicit musl support or a supported container. Headless servers may need a browser/device login flow or an API key. Avoid forwarding full browser profiles or private credential directories.

For GPU inference, first establish that the [Ollama GPU support list](https://docs.ollama.com/gpu) includes the device and driver combination. Install drivers through your distribution or vendor's official instructions; this guide does not prescribe a universal CUDA installation script.

## Verify your first session

Use [the Git loop](../git/workflow.md). Ask the tool to inspect only, authorize a small edit, review it, and run the project test command. A successful CLI launch is not proof that model tool calls, permissions, GPU acceleration, or billing are configured correctly.

## Documentation sources

- [Node.js official downloads](https://nodejs.org/en/download)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Ollama GPU support](https://docs.ollama.com/gpu)
- [Git reference](https://git-scm.com/docs)
