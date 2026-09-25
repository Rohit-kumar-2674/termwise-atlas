# Changelog

## 0.1.0 — 2026-09-25

Initial public learning hub: platform and tool guides, provider/model references, security and Git workflows, troubleshooting, eight runnable learning labs, read-only diagnostics, an instruction-only setup wizard, a searchable documentation site, and automated project checks.

Source review began 2026-09-22. Runtime validation and its limits are recorded separately in `docs/maintenance/validation.md`. Google consumer CLI migration is explicitly documented rather than reusing outdated Gemini CLI free-access claims.

Release verification fixed the doctor's Windows Python 3.11 architecture lookup so presence-only checks never launch a subprocess, and made the Docker smoke check tolerate connection resets during server startup with a bounded retry and failure logs.
