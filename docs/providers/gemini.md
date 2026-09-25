---
title: "Google models and the 2026 CLI transition"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
  - "https://geminicli.com/docs/get-started/authentication/"
  - "https://geminicli.com/docs/resources/quota-and-pricing/"
  - "https://ai.google.dev/gemini-api/docs/pricing"
  - "https://antigravity.google/docs/cli/install/"
  - "https://antigravity.google/docs/plans"
  - "https://antigravity.google/docs/cli/gcli-migration"
---

# Google models and the 2026 CLI transition

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Start with the current access route

Google announced that consumer Gemini CLI and Code Assist IDE requests using individual/free accounts or Google AI Pro/Ultra would move to Antigravity CLI on June 18, 2026. Enterprise Standard/Enterprise arrangements were described separately, and Gemini CLI remains available through its retained API/enterprise routes.

This means older Gemini CLI quota pages and tutorials can conflict with the newer announcement. We prioritize the dated transition notice and direct users to the current account-specific sign-in flow. A previous free entitlement is not proof of current access.

| Route | Guide | Billing and eligibility |
| --- | --- | --- |
| Google consumer terminal experience | [Antigravity CLI](../tools/antigravity.md) | Account quota; optional paid plans/usage |
| Gemini CLI with supported API/enterprise access | [Gemini CLI](../tools/gemini-cli.md) | API or enterprise rules; check current entitlement |
| Gemini API from another supported coding client | Client's provider guide | Gemini API model/tier pricing is separate |
| Vertex AI / enterprise | Organization's documented setup | Project, IAM, region, and billing controls |

## API keys are not subscriptions

`GEMINI_API_KEY` is a provider credential, not a way to unlock a consumer subscription. The Gemini API pricing page identifies model-specific free and paid tiers where offered. Data terms may differ by tier. A free API model's availability does not guarantee a particular agent or authentication route accepts it.

Use a restricted project/key when available, avoid embedding it in frontend JavaScript, and inspect your account before launching an agent loop. Do not enable paid fallback without intending to pay for it.

## Existing Gemini users

Check `gemini --version` and the exact authentication method. If an old consumer route stops working, follow Google's migration guide rather than deleting credentials repeatedly. Review any imported extensions/plugins before enabling them in a new CLI; a migrated configuration can still run commands.

Antigravity's detailed installation page currently documents a Gemini BYOK path, while the plans page contains wording that can differ. The tool guide records that documentation mismatch and tells readers to confirm behavior in their installed version. We do not infer OpenRouter or Ollama support from a generic “custom endpoint” phrase.

## Documentation sources

- [Google consumer CLI transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
- [Gemini CLI authentication](https://geminicli.com/docs/get-started/authentication/)
- [Gemini CLI quota page (read with transition notice)](https://geminicli.com/docs/resources/quota-and-pricing/)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Antigravity installation and authentication](https://antigravity.google/docs/cli/install/)
- [Antigravity plans](https://antigravity.google/docs/plans)
- [Antigravity migration](https://antigravity.google/docs/cli/gcli-migration)
