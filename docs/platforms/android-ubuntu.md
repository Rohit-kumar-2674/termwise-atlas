---
title: "Android + PRoot Ubuntu"
last_verified: 2026-09-22
tool_version: "Current OCI-based PRoot-Distro manual; legacy alias interface called out separately"
verification: source-reviewed
status: "COMMUNITY \u00b7 NOT A VM"
sources:
  - "https://github.com/termux/proot-distro"
  - "https://github.com/termux/termux-app"
  - "https://nodejs.org/en/download"
  - "https://docs.python.org/3/library/venv.html"
---

# Android + PRoot Ubuntu

> **COMMUNITY · NOT A VM** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Current OCI-based PRoot-Distro manual; legacy alias interface called out separately. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## What this route changes

PRoot supplies a Linux distribution's userland on the phone. It does not install a new kernel, grant real root, create a security boundary, or turn Android into an officially supported desktop. It can help with glibc dependencies, but sandboxes, system services, GPU drivers, and native extensions can still fail.

## Install from the outer Termux shell

```bash
pkg update
pkg install proot-distro
proot-distro --version
proot-distro install --help
```

Current upstream PRoot-Distro supports OCI image references. For that version:

```bash
proot-distro install ubuntu:24.04
proot-distro login ubuntu
```

If your installed release uses the older distribution-alias interface, consult its `list` and `install --help`; the legacy form is `proot-distro install ubuntu`. Do not paste an OCI tag into a legacy installer or reinstall an existing distribution to fix a PATH problem. Tag selection here is an example of a known distribution, not a demand to downgrade your existing installation.

## Inside Ubuntu

The default PRoot session is commonly the distribution's emulated root user. Install prerequisites there without `sudo`:

```bash
apt update
apt install git curl ca-certificates python3 python3-venv python3-pip build-essential nodejs npm
uname -m
node --version
python3 --version
```

Distribution Node packages may be too old for a selected CLI, particularly Debian Bookworm. Check the [current LTS instructions](https://nodejs.org/en/download) before continuing; do not force a package requiring a newer Node through an engine warning. Use a user-owned runtime setup from its official upstream if needed. PRoot runs slower than native Termux and some installers cannot determine the platform correctly.

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/Rohit-kumar-2674/termwise-atlas.git
cd termwise-atlas
python3 scripts/doctor.py
```

Follow [Aider](../tools/aider.md), [OpenCode](../tools/opencode.md), or the selected tool's instructions **only when its binary and runtime fit this environment**. This is a community route, not certification of those agents on Android. For a first guaranteed project exercise, run the standard-library [Python lab](../examples/fix-a-bug.md) without an AI provider.

## Files, previews, and exit

Keep the repository in the distribution's home directory. Bind mounts expose outer files deliberately; do not bind an entire private storage tree for convenience. A simple `python3 -m http.server 8000 --bind 127.0.0.1` can be opened from the phone browser while it runs. Port conflicts can occur with outer Termux processes because PRoot does not provide a separate network stack.

Type `exit` to return to Termux. Run `proot-distro login ubuntu` to resume. Back up from the outer shell using the backup options printed by your installed `proot-distro --help`; review the destination and available space first.

## If a native build fails

Record the distribution, architecture, Node/Python versions, package name, and the first actual error without secret values. Native `rollup`, `esbuild`, cryptography, or sandbox packages may need platform-specific fixes. A WASM fallback must be documented by the affected project and tested; this guide does not recommend randomly replacing transitive packages. Move the build to [Codespaces](codespaces.md) or [SSH](remote-ssh.md) when the supported binary is unavailable.

Do not try nested Docker daemons, disable every agent permission, or assume emulated root can repair kernel features. [Sandboxing](../security/sandboxing.md) explains the boundary.

## Documentation sources

- [PRoot-Distro upstream manual](https://github.com/termux/proot-distro)
- [Termux installation and limitations](https://github.com/termux/termux-app)
- [Node.js official downloads](https://nodejs.org/en/download)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
