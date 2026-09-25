---
title: "API keys: handle them like passwords"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions"
  - "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository"
  - "https://openrouter.ai/docs/quickstart"
  - "https://geminicli.com/docs/get-started/authentication/"
  - "https://developers.openai.com/codex/auth"
---

# API keys: handle them like passwords

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Four places a key should never appear

Do not put a real key in a README, screenshot, Git commit, or public issue. Avoid literal values in shell history and process arguments. A key can authorize spending or access; a “test” key is still a credential.

Use the smallest available scope, a dedicated learning project, and a budget cap where supported. Keep provider keys separate from GitHub tokens. A frontend browser application cannot keep a bundled key secret.

## Enter a temporary key without showing it

### Bash

```bash
read -r -s -p 'OpenRouter key: ' OPENROUTER_API_KEY
printf '\n'
export OPENROUTER_API_KEY
```

This is **Bash-specific**; on zsh either start Bash for the session or use that shell's documented hidden-input method. The literal key is not in the command history. It remains available to child processes, so only launch trusted programs from this session.

### PowerShell

```powershell
$secureKey = Read-Host 'OpenRouter key' -AsSecureString
$env:OPENROUTER_API_KEY = [System.Net.NetworkCredential]::new('', $secureKey).Password
Remove-Variable secureKey
```

The key becomes plaintext in the process environment because API clients need it. The hidden input protects display/history, not the entire operating system. Clear it after use with `Remove-Item Env:OPENROUTER_API_KEY`; Bash uses `unset OPENROUTER_API_KEY`.

For another provider, use that client's documented variable name. Do not run `env`, `set`, `printenv`, or a verbose HTTP trace to share debugging output without first checking what it exposes.

## `.env` and `.gitignore`

Copy `.env.example` to an ignored local `.env` only if your tool explicitly loads it. A `.env` file is ordinary plaintext; it is not an encrypted vault. Set file access appropriately (`chmod 600 .env` on a POSIX filesystem), and confirm it is ignored:

```bash
git check-ignore -v .env
git status --short
```

Do not `source` an untrusted `.env`: shell sourcing executes code, whereas dotenv parsers have their own limited syntax. Claude Code and other clients may require environment variables instead of automatically reading `.env`. Read the tool page.

A secret manager or OS credential store is better for persistent secrets. Use provider-specific auth stores only as documented. Never commit the stores themselves, copy them into images, or attach them to troubleshooting reports.

## GitHub Actions and Codespaces

Use the appropriate GitHub Secrets settings and scope access to trusted repositories/environments. Do not expose provider credentials to untrusted pull-request code or print them to prove they are configured. Masking is a backup measure, not a guarantee against transformed or fragmented values leaking.

This project's validation needs **no model API keys**. Its examples are deterministic and its browser chooser makes no model requests.

## If you exposed a key

1. Revoke or rotate it in the provider's official account console immediately. Deleting a post is insufficient.
2. Review usage/billing and account access; report unauthorized activity through that provider.
3. Replace the value in legitimate secret stores and remove the exposed copy.
4. If committed, follow GitHub's sensitive-data removal process and coordinate with collaborators before rewriting history. Forks/caches may retain it.
5. Check why it leaked and add an appropriate prevention step.

Never publish a still-valid key in a security report. Use the key's non-secret identifier or a short redacted suffix only if needed by the provider's private support process.

## Documentation sources

- [GitHub Actions secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [GitHub sensitive-data remediation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [OpenRouter quickstart](https://openrouter.ai/docs/quickstart)
- [Gemini CLI authentication](https://geminicli.com/docs/get-started/authentication/)
- [Codex authentication](https://developers.openai.com/codex/auth)
