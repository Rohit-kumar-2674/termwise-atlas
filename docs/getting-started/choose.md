---
title: "Find your first setup"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.ollama.com/gpu"
  - "https://github.com/termux/termux-app"
  - "https://openrouter.ai/docs/api/reference/limits"
  - "https://antigravity.google/docs/plans"
---

# Find your first setup

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

<div id="setup-chooser" class="atlas-widget" aria-label="Setup chooser"></div>
<noscript>The table below works without JavaScript. The interactive chooser runs entirely in your browser and sends no data.</noscript>

## Choose without JavaScript

| Your situation | Start here | Watch for |
| --- | --- | --- |
| Android; little RAM | [Android + browser/SSH](../platforms/android.md) | Host quotas and platform support |
| Android; want on-device AI | [Android limitations](../platforms/android.md) | Ollama has no reviewed official Android install; no promised route |
| Desktop; 4–8 GB; local | [Small model exercise](../providers/hardware.md) | Limited useful context and coding ability |
| Desktop; 16 GB; local | [Ollama + Aider](../examples/local-ollama.md) | Keep context modest; test one model |
| Desktop; 32+ GB; local | [Model guide](../providers/local-models.md) | Agent-capable models still need memory headroom |
| Cloud; multiple models | [OpenRouter](../providers/openrouter.md) | Model-specific cost and routing |
| Cloud; no-charge allowance | [Free-tier checklist](costs.md) | Eligibility, rate limits, current Google transition |

The recommendation is a starting path, not a guarantee of performance. Available RAM is less than installed RAM, and a cloud terminal is remote even when opened on your own phone.

Prefer an instruction-only terminal wizard? Run `python3 scripts/wizard.py` from the repository (Windows: `py -3 scripts/wizard.py`). It asks about the same choices and prints a route. It never asks for a secret value or changes your environment.

## Documentation sources

- [Ollama GPU support](https://docs.ollama.com/gpu)
- [Termux installation and limitations](https://github.com/termux/termux-app)
- [OpenRouter rate limits](https://openrouter.ai/docs/api/reference/limits)
- [Antigravity plans](https://antigravity.google/docs/plans)
