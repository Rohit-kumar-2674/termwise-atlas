---
title: "Free, local, open source, and paid"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://openrouter.ai/models"
  - "https://openrouter.ai/docs/api/reference/limits"
  - "https://antigravity.google/docs/plans"
  - "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
  - "https://developers.openai.com/codex/auth"
---

# Free, local, open source, and paid

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Software price and model price are different

| Label | Meaning | Does not promise |
| --- | --- | --- |
| FREE | A specifically identified no-charge component | Unlimited cloud compute |
| FREE TIER | A limited service allowance with conditions | Permanent access or no rate limits |
| LOCAL | Inference on your selected hardware | Zero electricity cost or zero network traffic from every component |
| OPEN SOURCE | Software available under a stated open-source license | Free API access or identical model licensing |
| PAID API REQUIRED | That documented API route needs funded access | A consumer subscription pays the API bill |
| OPTIONAL PAID PROVIDER | The software offers local/other choices and can use paid providers | Every available provider is free |

## Legitimate no-charge starting points

Run the repository's exercises without an AI account. Use a local open-weight model on hardware you already own when its license permits your use. Check current Google Antigravity account allowances and OpenRouter's current free-model catalog for cloud options. Availability, geography, data terms, context limits, and quotas may exclude your intended task.

Google announced a June 18, 2026 transition away from consumer Gemini CLI sign-in. The [Google provider guide](../providers/gemini.md) explains why older “1,000 free requests a day” Gemini CLI tutorials are not a reliable starting point now.

## Plan a small budget

For a metered provider, estimate **input tokens × input rate + output tokens × output rate**, using the provider's billing units. Cached input, reasoning tokens, tool calls, web tools, retries, and long contexts can have different charges. Agents may call a model many times for one visible task.

Start with a key limited to a small budget where the provider supports it. Read whether a budget setting is a hard cap or only an alert. Disable paid fallback if you need a strictly no-charge route and the service supports that control; otherwise choose a route whose billing behavior you can establish.

There is no universal “cheapest model.” Compare cost per successfully reviewed task, latency, context, tool use, privacy, and reliability. A model that produces repeated broken edits can consume more time and money than a more capable one.

## What this project excludes

No stolen/shared keys, fake-account farming, trial abuse, patched subscription checks, license bypassing, or unauthorised endpoints. If official access does not meet your budget, choose a lawful local or open-source alternative.

## Documentation sources

- [OpenRouter model catalog](https://openrouter.ai/models)
- [OpenRouter rate limits](https://openrouter.ai/docs/api/reference/limits)
- [Antigravity plans](https://antigravity.google/docs/plans)
- [Google consumer CLI transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
- [Codex authentication](https://developers.openai.com/codex/auth)
