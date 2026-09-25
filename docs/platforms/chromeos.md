---
title: "ChromeOS development"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://support.google.com/chromebook/answer/9145439"
  - "https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces"
  - "https://docs.cloud.google.com/shell/docs/how-cloud-shell-works"
  - "https://docs.ollama.com/gpu"
---

# ChromeOS development

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Option A: Linux development environment

On supported Chromebooks, open Settings and enable **Linux development environment** following Google's instructions. School/work administrators or the device model may make this unavailable. Allocate disk space that leaves room for the browser and updates.

Inside its Linux terminal:

```bash
sudo apt update
sudo apt install git curl ca-certificates python3 python3-venv python3-pip
uname -m
```

Follow [the Debian/Linux guide](linux.md) for Node and coding tools. ARM Chromebooks still need compatible ARM Linux binaries. The environment is Linux support, not native ChromeOS support from every agent vendor.

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/Rohit-kumar-2674/termwise-atlas.git
cd termwise-atlas
python3 scripts/doctor.py
```

## Option B: browser development

Use [Codespaces](codespaces.md) or [Cloud Shell](cloud-shell.md) when Linux is unavailable or memory is limited. Your browser provides the interface while the remote host performs builds and model requests. Check compute quotas and stop unused sessions. Don't upload private projects to a service without permission.

## Local models

CPU-only small models may work inside a sufficiently provisioned Linux environment. Do not assume an integrated GPU is passed through or supported by Ollama. For low-memory Chromebooks, cloud inference or SSH to your own workstation is usually more practical; [hardware estimates](../providers/hardware.md) explain the trade-off.

## Documentation sources

- [ChromeOS Linux environment](https://support.google.com/chromebook/answer/9145439)
- [GitHub Codespaces overview](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces)
- [Cloud Shell environment](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works)
- [Ollama GPU support](https://docs.ollama.com/gpu)
