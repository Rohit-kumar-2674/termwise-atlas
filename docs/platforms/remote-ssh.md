---
title: "VPS and remote SSH development"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://docs.cloud.google.com/shell/docs/how-cloud-shell-works"
  - "https://docs.ollama.com/faq"
---

# VPS and remote SSH development

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## A remote terminal is a separate computer

Use a Linux VPS you control or your own workstation. The provider bills the machine separately from any model API. A cloud VM without a GPU does not become suitable for a large local model simply because it has a terminal.

Install an SSH client through your platform's official package system. Termux uses `pkg install openssh`; Windows offers OpenSSH as an optional feature. Obtain the host address and fingerprint from your host administrator or control panel.

```bash
ssh developer@your-host.example
```

Replace the example hostname and user. Verify the fingerprint through a trusted channel on first connection. Use an unprivileged development user; configure SSH keys using your host's documented process, protect the private key, and never commit it. Do not disable host-key checking to silence a changed-host warning.

Inside the host, follow [Linux setup](linux.md), clone the project, and run diagnostics. Keep long-running tasks in a terminal multiplexer if one is installed and allowed, while saving and pushing work regularly.

## Private preview tunnel

Run a web server on the host's `127.0.0.1:8000`, then open a second terminal **on your client device**:

```bash
ssh -N -L 8000:127.0.0.1:8000 developer@your-host.example
```

Open `http://127.0.0.1:8000` on the client. The tunnel lasts while SSH runs. Choose another local port if it is occupied. No public inbound web-server port is needed.

Use the same pattern for [remote Ollama](../providers/ollama.md), forwarding port 11434. That model runs on the server, not the phone; your server operator's access is part of the privacy boundary. Limit who can reach the machine and stop tunnels when finished.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [Cloud Shell environment](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works)
- [Ollama FAQ and local-only configuration](https://docs.ollama.com/faq)
