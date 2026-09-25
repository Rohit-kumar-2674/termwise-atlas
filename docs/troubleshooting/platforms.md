---
title: "Platforms troubleshooting"
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

# Platforms troubleshooting

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

Find the exact symptom, then check the cause before changing your system. Replace uppercase command placeholders deliberately. Never attach unredacted logs.

## Termux storage permission / symlink failure

**SYMPTOM:** Packages or executables fail under shared phone storage.

**CAUSE:** Shared storage is not a normal executable Unix filesystem.

**CHECK:** Run `pwd` and check whether the repository is under `/sdcard` or a storage shortcut.

**FIX:** Clone into `~/projects`; use `termux-setup-storage` only when exporting/importing user files.

**VERIFY:** Install dependencies and run a small script from Termux internal storage.

## Illegal instruction / unsupported architecture

**SYMPTOM:** A native program crashes or cannot execute.

**CAUSE:** Binary targets the wrong CPU, libc, OS ABI, or unsupported instruction set.

**CHECK:** Record `uname -m`, runtime version, native Termux versus PRoot, and the first error.

**FIX:** Use a matching upstream-supported build; choose SSH/browser development if none exists. Do not rename binaries or trust random patched packages.

**VERIFY:** Version check and a small task run in the intended environment.

## Browser says localhost refused connection

**SYMPTOM:** Browser cannot reach the development server.

**CAUSE:** Server stopped, wrong port, phone background suspension, or server is actually remote.

**CHECK:** Check the running terminal, printed port, and which machine hosts the server.

**FIX:** Restart the server; use local loopback on-device, authenticated cloud preview, or an SSH tunnel for a remote host.

**VERIFY:** Open the correct URL while the server/tunnel remains running.

## WSL tools or file watchers behave strangely

**SYMPTOM:** Windows and Linux packages/files conflict or builds are slow.

**CAUSE:** Mixed PATH/runtime or project dependencies shared across filesystems.

**CHECK:** Run `pwd`, `command -v node`, and check WSL version from PowerShell.

**FIX:** Keep Linux clones in `~/projects`, install Linux dependencies in WSL, and use supported WSL 2 where needed.

**VERIFY:** The correct Linux executable runs and the project builds in its own environment.

## macOS blocks application or folder access

**SYMPTOM:** Gatekeeper or privacy controls prevent launch/file access.

**CAUSE:** Unverified publisher or missing narrowly scoped file permission.

**CHECK:** Check the official installer source and exact macOS dialog.

**FIX:** Follow vendor/Apple instructions for the specific app and folder. Do not disable Gatekeeper globally or grant Full Disk Access by default.

**VERIFY:** The verified app opens the intended project without unnecessary permissions.

## Cloud Shell loses installed packages

**SYMPTOM:** A new session lacks a previous system installation.

**CAUSE:** The VM environment is ephemeral while supported home storage is persistent.

**CHECK:** Check `pwd`, tool version, and whether files lived in the persistent home area.

**FIX:** Keep source in Git, use documented user-level installs, and record reproducible setup instructions.

**VERIFY:** A fresh session can restore tooling and the pushed repository.

## Git reports merge conflicts

**SYMPTOM:** Local and incoming edits overlap.

**CAUSE:** Branches changed the same part of a file.

**CHECK:** Run `git status` and inspect both sides of each conflict.

**FIX:** Resolve the intended content, stage specific files, run tests, and complete the merge. Avoid force push as a generic repair.

**VERIFY:** No conflict markers remain; tests pass; the staged diff contains the intended combined behavior.

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
