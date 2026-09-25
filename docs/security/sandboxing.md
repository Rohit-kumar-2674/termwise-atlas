---
title: "What isolation does\u2014and does not\u2014protect"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.docker.com/engine/security/"
  - "https://learn.chatgpt.com/docs/agent-approvals-security"
  - "https://code.claude.com/docs/en/permissions"
  - "https://github.com/termux/proot-distro"
---

# What isolation does—and does not—protect

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Choose the right boundary

| Environment | Useful protection | Important limit |
| --- | --- | --- |
| Git branch | Separates source history | Cannot block commands, network, or file reads |
| Python virtual environment | Separates dependencies | Not a security sandbox |
| Disposable clone | Limits valuable working files | Process may still reach your home and network |
| Container / devcontainer | Filesystem/process separation when configured | Shared kernel; mounts and credentials can defeat isolation |
| Virtual machine | Separate guest OS | Shared folders, clipboard, and networking still matter |
| Cloud Shell / Codespaces | Disposable remote compute | Host account, secrets, quota, and remote storage remain exposed |
| PRoot on Android | Different userland and path translation | Not a VM, privileged kernel, or strong security boundary |

## Container practice

Use a trusted base image and review its build instructions. Run as a non-root user when feasible, minimize mounts, avoid privileged mode, and don't expose the Docker daemon socket to a coding agent. Keep provider keys out of image layers and build arguments. Containers with network access can still upload mounted source files.

This repository's Dockerfile serves the **built static guide** as a non-root process; it is not an AI-agent sandbox. Its Compose file binds the preview only to the host's loopback address. The development container installs documentation dependencies, so inspect its setup before using it.

## Agent sandbox settings

Codex and Claude Code offer platform-specific controls, with different support across native Windows, WSL, Linux, and macOS. Consult the installed version's documentation. Permission prompts and OS sandboxing are complementary, not interchangeable.

If a sandbox fails under an unsupported phone/PRoot environment, use a supported remote host. Globally disabling protections can turn a compatibility problem into a much larger one.

## A safe first experiment

Clone a small public example into a disposable directory, provide no private credentials, restrict the task to one file, run existing tests, and review the diff. Add access only after you understand why the task needs it. Keep production data, deployment keys, and personal backups out of the experiment.

## Documentation sources

- [Docker Engine security](https://docs.docker.com/engine/security/)
- [Codex permissions and sandboxing](https://learn.chatgpt.com/docs/agent-approvals-security)
- [Claude Code permissions](https://code.claude.com/docs/en/permissions)
- [PRoot-Distro upstream manual](https://github.com/termux/proot-distro)
