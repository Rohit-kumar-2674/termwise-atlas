---
title: "Authentication troubleshooting"
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

# Authentication troubleshooting

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

Find the exact symptom, then check the cause before changing your system. Replace uppercase command placeholders deliberately. Never attach unredacted logs.

## 401 / invalid API key

**SYMPTOM:** Provider rejects authentication.

**CAUSE:** Wrong provider key, expired/revoked key, missing environment, or wrong auth route.

**CHECK:** Check only whether the expected variable is configured using the doctor; review the endpoint and selected provider.

**FIX:** Load a valid key through a hidden prompt or documented auth flow. Remove accidental whitespace. Never print the value for debugging.

**VERIFY:** Run one small authorized request and check account usage.

## 403 / access denied

**SYMPTOM:** Authentication may succeed but access is refused.

**CAUSE:** Model, organization, region, policy, or account entitlement does not allow this request.

**CHECK:** Read the redacted provider error and confirm the official account/project/model requirements.

**FIX:** Choose a route your account legitimately supports or contact provider support. Do not bypass policy or region restrictions.

**VERIFY:** Retry only after the entitlement/configuration issue is resolved.

## 429 / too many requests

**SYMPTOM:** Provider rejects requests for rate or quota reasons.

**CAUSE:** Per-minute limit, exhausted allowance, or upstream capacity.

**CHECK:** Inspect retry guidance, account usage, selected free variant, and concurrent agent sessions.

**FIX:** Wait as instructed, reduce concurrency/context where relevant, or deliberately choose an available authorized route. Do not rotate accounts to evade limits.

**VERIFY:** One small request succeeds without a retry storm; usage stays within the intended budget.

## Unexpected model charges

**SYMPTOM:** A task consumes paid usage despite a free-software label.

**CAUSE:** CLI license was confused with model pricing, fallback selected a paid route, or retries expanded usage.

**CHECK:** Stop the agent and inspect account usage, exact model ID, routing/fallback, and API-vs-subscription billing.

**FIX:** Set supported budget controls, select the intended route, and revoke an exposed key if usage is unauthorized.

**VERIFY:** Run a small deliberate task and compare usage to expected pricing.

## Old Gemini consumer login stopped working

**SYMPTOM:** A formerly working personal Gemini CLI sign-in no longer grants requests.

**CAUSE:** Google announced a consumer transition to Antigravity CLI in June 2026.

**CHECK:** Check authentication type, tool version, and the official transition notice linked in the Gemini guide.

**FIX:** Follow the documented migration or an eligible API/enterprise route. Do not assume old free-quota screenshots apply.

**VERIFY:** Confirm the selected product/account route and its current allowance in a new small session.

## Configured key is not visible to the CLI

**SYMPTOM:** A key exists in one shell or file but the program cannot see it.

**CAUSE:** Different process, OS userland, GUI launch environment, or a client that does not load `.env`.

**CHECK:** Check the client’s loading rules and presence-only doctor in the same launch environment.

**FIX:** Load the variable into that process using the documented mechanism; restart the client when required.

**VERIFY:** Check configured/not-configured status without displaying the key, then authenticate.

## Key appeared in Git or a screenshot

**SYMPTOM:** A real credential was published or shared.

**CAUSE:** Secret was included in tracked content, logs, command history, or an image.

**CHECK:** Identify the affected provider and key using non-secret metadata; do not repost the secret.

**FIX:** Revoke/rotate immediately, review usage, replace legitimate secret stores, and follow the API-key incident guide.

**VERIFY:** The old credential is invalid; new secrets are scoped and absent from tracked files/history remediation targets.

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
