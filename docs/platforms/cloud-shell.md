---
title: "Google Cloud Shell: a fresh start"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.cloud.google.com/shell/docs/how-cloud-shell-works"
  - "https://docs.cloud.google.com/shell/docs/uploading-and-downloading-files"
  - "https://docs.cloud.google.com/shell/docs/using-web-preview"
  - "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
  - "https://git-scm.com/docs"
---

# Google Cloud Shell: a fresh start

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Know where your work lives

Open [Google Cloud Shell](https://shell.cloud.google.com/) with your own authorized account. It is a hosted development shell with usage limits, a persistent home area, and an ephemeral machine environment. It is not unlimited free compute or a GPU workstation. Treat a temporary VM's system packages differently from files in your home directory.

## Inspect before installing

```bash
pwd
uname -m
git --version
python3 --version
node --version
npm --version
command -v gemini
```

Cloud Shell may already include Gemini CLI and other Google tooling. Inspect versions first. **Consumer Gemini CLI access changed in 2026**; a preinstalled executable does not prove you have free model access. Read [the Gemini guide](../tools/gemini-cli.md) and [Antigravity migration](../tools/antigravity.md). Never enable a billable cloud API without checking the selected project and its billing controls.

If a runtime is missing or too old, follow its current official installation guidance using a user-owned location. Then choose one CLI from the [directory](../getting-started/comparison.md) and use its published install command. No special “free Claude” installer is legitimate.

## Clone and inspect

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/Rohit-kumar-2674/termwise-atlas.git
cd termwise-atlas
python3 scripts/doctor.py
git switch -c learn/cloud-shell
```

For a private repository, authenticate through a documented GitHub CLI, browser, or SSH flow. Never embed an access token in the repository URL. Configure your selected provider with the [hidden Bash key prompt](../security/api-keys.md). Cloud Shell's Google login does not automatically authenticate GitHub or another model provider.

Start the chosen coding assistant in this directory and ask for read-only analysis first. Complete [one lab](../examples/index.md), run its checks, inspect `git diff`, and commit explicitly chosen files. Use [the GitHub tutorial](../git/github.md) to push to a repository you own or a fork.

## See files and preview a website

Use `ls`, `pwd`, the built-in editor, or `cat README.md` for short non-secret files. From this repository, a web preview can use:

```bash
python3 -m http.server 8080 --bind 0.0.0.0 --directory examples/website
```

Use Cloud Shell's **Web preview** menu for port 8080. This host-bound address is required for the preview proxy; it is not advice to expose arbitrary services on a public VPS. Supported preview ports are documented by Google. Do not serve a directory containing `.env`, credentials, or the whole home directory. Stop the server with `Ctrl+C`.

## Download your work

Create an archive of an explicit exercise directory, not your whole home folder:

```bash
tar -czf website-exercise.tar.gz -C examples website
```

Use Cloud Shell's menu **Download** and choose the archive's path, or use the documented file-download control. On Android, choose an accessible destination in the browser's download dialog. A permission error in the remote terminal is not fixed by making the phone's storage world-writable. Git push is the usual durable source backup; archives are useful for offline transfer.

## SSH and session boundaries

For connecting to Cloud Shell from another machine, follow Google's documented `gcloud cloud-shell ssh` workflow after installing and authenticating the official Google Cloud CLI there. Inside Cloud Shell, ordinary `ssh user@host` can reach a host you control when allowed by network policy. Verify host fingerprints and protect private keys.

Do not leave key values in startup scripts or archives. Session restarts can remove system-level changes, so keep installation notes and dependencies in your repository, not only terminal history.

## Documentation sources

- [Cloud Shell environment](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works)
- [Cloud Shell file transfer](https://docs.cloud.google.com/shell/docs/uploading-and-downloading-files)
- [Cloud Shell web preview](https://docs.cloud.google.com/shell/docs/using-web-preview)
- [Google consumer CLI transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
- [Git reference](https://git-scm.com/docs)
