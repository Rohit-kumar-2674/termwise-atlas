---
title: "Windows 11 + WSL Ubuntu"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://learn.microsoft.com/en-us/windows/wsl/install"
  - "https://nodejs.org/en/download"
  - "https://docs.ollama.com/linux"
  - "https://docs.ollama.com/gpu"
  - "https://code.claude.com/docs/en/setup"
---

# Windows 11 + WSL Ubuntu

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Install WSL

In an **Administrator PowerShell** session on a supported Windows system:

```powershell
wsl --install -d Ubuntu
```

Restart if Windows requests it. Launch Ubuntu from Windows Terminal or Start and create a Linux user and password. Your Linux password is not your Windows PIN; password entry displays no characters.

In **PowerShell**, inspect the installation:

```powershell
wsl --status
wsl --list --verbose
```

Use WSL 2 for the Linux kernel features expected by modern tooling. If virtualisation is unavailable, follow Microsoft's error-specific WSL guidance; some managed or nested virtual machines cannot enable it. Do not alter firmware or machine policies without understanding the machine's ownership and requirements.

## Inside Ubuntu

```bash
sudo apt update
sudo apt install git curl ca-certificates python3 python3-venv python3-pip build-essential
mkdir -p ~/projects
cd ~/projects
```

Install a supported Node LTS using the [official Node installation choices](https://nodejs.org/en/download), then check `node --version` and `npm --version`. Keep Linux projects in `~/projects` for Linux filesystem behavior and performance. Access Windows files through `/mnt/c` only when needed; avoid sharing one `node_modules` directory between Windows and Linux.

```bash
git clone https://github.com/Rohit-kumar-2674/termwise-atlas.git
cd termwise-atlas
python3 scripts/doctor.py
```

Then choose [Claude Code](../tools/claude-code.md), [Codex](../tools/codex.md), [Gemini's supported API route](../tools/gemini-cli.md), or [OpenCode](../tools/opencode.md). Install and authenticate inside Ubuntu; a Windows npm installation is a separate installation.

## Local models and previews

For the simplest documented Linux arrangement, run Ollama inside WSL using its Linux instructions, subject to [GPU compatibility](https://docs.ollama.com/gpu). Running the Windows Ollama application and connecting from WSL is another networking arrangement, but loopback forwarding differs by WSL network mode. Diagnose connectivity before changing listen addresses. Never expose an unauthenticated inference port publicly.

Start the [website exercise](../examples/build-a-website.md) in Ubuntu and open the printed `http://localhost:8000` in Windows. If forwarding fails, consult the current WSL networking documentation and local firewall policy. Do not turn the firewall off as a general fix.

## Common problems

| Symptom | Check | Fix and verify |
| --- | --- | --- |
| No distribution installed | `wsl --list --verbose` in PowerShell | Finish Ubuntu setup; launch it once |
| Linux CLI missing | `command -v node` in Ubuntu | Install in Ubuntu and verify its version |
| File watcher slow | `pwd` | Put the clone on the Linux filesystem |
| Permission failures in npm | Runtime ownership | Use user-owned Node, avoid `sudo npm` |
| Disk fills after model downloads | `df -h`, `ollama list` | Remove an explicitly selected unused model; back up first |
| Sandbox unsupported in WSL 1 | WSL version from PowerShell | Use supported WSL 2 or a supported remote host |

Back up important files before resetting or unregistering a distribution. Unregistering WSL erases its filesystem; it is not an ordinary troubleshooting step.

## Documentation sources

- [Microsoft WSL installation](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Node.js official downloads](https://nodejs.org/en/download)
- [Ollama Linux installation](https://docs.ollama.com/linux)
- [Ollama GPU support](https://docs.ollama.com/gpu)
- [Claude Code installation](https://code.claude.com/docs/en/setup)
