---
title: "AI coding from Android"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "TERMUX FOUNDATION \u00b7 COMMUNITY AGENT COMPATIBILITY"
sources:
  - "https://github.com/termux/termux-app"
  - "https://github.com/termux/proot-distro"
  - "https://pnpm.io/installation"
  - "https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces"
  - "https://docs.cloud.google.com/shell/docs/how-cloud-shell-works"
  - "https://git-scm.com/docs"
---

# AI coding from Android

> **TERMUX FOUNDATION · COMMUNITY AGENT COMPATIBILITY** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## A phone is a valid starting point

You can edit a real repository, run tests, review diffs, and push a pull request from Android. The practical choice is **where the development process and model run**. Android's Linux kernel does not make every desktop Linux binary compatible with native Termux.

| Route | Runs where? | Best use | Support status |
| --- | --- | --- | --- |
| Native Termux | Phone, Android/Bionic userland | Git, Python, Node scripts, SSH | Termux-supported packages; AI agents individually unverified |
| [Debian in PRoot](android-debian.md) | Phone, glibc userland | Packages expecting Debian paths | COMMUNITY; slower, no full VM isolation |
| [Ubuntu in PRoot](android-ubuntu.md) | Phone, glibc userland | Ubuntu-oriented project exercises | COMMUNITY; native binaries can still fail |
| [Codespaces](codespaces.md) / [Cloud Shell](cloud-shell.md) | Remote cloud machine | Heavy builds and desktop CLI compatibility | Host support applies; quotas and charges may apply |
| [SSH to your computer](remote-ssh.md) | Your supported remote machine | Reuse hardware and local Ollama there | Phone is a terminal client |

**A good first route:** Termux for Git and SSH, or a browser terminal when a phone has little memory/storage. Native coding-agent installs are community experiments unless the specific upstream explicitly supports Android.

## 1. Install Termux safely

Use [Termux's official installation instructions](https://github.com/termux/termux-app#installation), choosing an upstream-recommended distribution such as F-Droid. Keep Termux and its add-ons from the same signing source. Back up your home directory before switching distributions; uninstalling the app can erase it.

In a fresh **Termux shell**, install the foundation:

```bash
pkg update
pkg upgrade
pkg install git python nodejs-lts openssh
```

Review package prompts, especially upgrades. Then check:

```bash
uname -m
python --version
node --version
npm --version
git --version
```

`aarch64` is common on modern phones, but does not prove a package offers an Android ARM64 binary. Prefer `nodejs-lts` when available in your Termux repository. For pnpm, follow its current official method after checking Node compatibility; `npm install -g pnpm` is one documented route. Do not assume Corepack is bundled with every Node release.

## 2. Keep repositories inside Termux

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/Rohit-kumar-2674/termwise-atlas.git
cd termwise-atlas
python scripts/doctor.py
```

Keep code and `node_modules` under `~/projects`, not `/sdcard`. Shared Android storage lacks normal executable and symlink behavior. To **export** files to Downloads later, grant storage access:

```bash
termux-setup-storage
```

Approve the Android permission dialog. Use shared storage for exported archives or screenshots, not working dependencies. Check storage with `df -h` and `du -sh ~/projects`. Inspect before deleting anything.

## 3. Choose one coding agent route

Use the [matrix](../getting-started/comparison.md) to choose a supported host. For native Termux, Node-only packages may install, but dependencies can require native binaries unavailable for Android. Aider's Python dependencies may also lack compatible wheels. Do not mark an install “supported” just because npm or pip downloaded it.

When native install fails, take the [Debian](android-debian.md), [Ubuntu](android-ubuntu.md), or remote route. Within the selected environment, follow the tool's documented installation, configure the provider using a [hidden secret prompt](../security/api-keys.md), and start in a branch. A cloud API still sends selected project content off the phone.

## 4. Preview a simple website

From the cloned repository in **Termux**:

```bash
python -m http.server 8000 --bind 127.0.0.1 --directory examples/website
```

Keep the terminal alive and open `http://127.0.0.1:8000` in your Android browser. `Ctrl+C` stops the server. Preview a React app using the project's documented dev command; plain HTML previews do not build JSX. Android battery management can stop background processes—save frequently, and use an SSH/remote session for longer builds.

## 5. Commit and push

Use [GitHub's browser flow or SSH setup](../git/github.md). Never put a token in a clone URL. Run `git status`, review the diff, commit explicitly selected files, and push your branch. Acode can edit exported plain HTML files, but make sure you know which copy is the Git working tree.

## Phone-specific fixes

| Problem | Check | Practical next step |
| --- | --- | --- |
| Permission denied in shared storage | `pwd` | Move the working clone to `~/projects` |
| Node/native package crashes or illegal instruction | `uname -m`, `node --version` | Check Android vs glibc support; use supported remote host |
| `127.0.0.1` refuses connection | Is the server still running? Which port? | Restart the correct server; keep terminal active |
| Build cannot create symlink | Is repo under `/sdcard`? | Clone into internal app storage |
| PRoot process killed | Available RAM, battery restrictions | Smaller build; no large local model; remote workflow |
| CLI missing after restart | `command -v TOOL` | Check which shell/userland installed it; don't mix PATHs |

The [troubleshooting database](../troubleshooting/index.md) expands these into symptom/cause/check/fix/verify procedures. Never use global permission changes or untrusted patched binaries as a routine repair.

## Documentation sources

- [Termux installation and limitations](https://github.com/termux/termux-app)
- [PRoot-Distro upstream manual](https://github.com/termux/proot-distro)
- [pnpm installation](https://pnpm.io/installation)
- [GitHub Codespaces overview](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces)
- [Cloud Shell environment](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works)
- [Git reference](https://git-scm.com/docs)
