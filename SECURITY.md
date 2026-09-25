# Security policy

Termwise Atlas is a static learning project with local diagnostic utilities. Security issues include malicious install instructions, credential disclosure, unsafe scripts, dependency vulnerabilities, and documentation that encourages unauthorized access or exposes a model server.

## Report privately

Use GitHub's **Security → Report a vulnerability** for this repository when available:

https://github.com/Rohit-kumar-2674/termwise-atlas/security/advisories/new

Do not publish credentials, exploitable payloads against others, private logs, or personal data in issues. If private reporting is unavailable, open only a non-sensitive request for a private reporting channel; do not disclose vulnerability details there. We do not promise a response deadline or a paid bounty.

Include affected commit/version, relevant file paths, minimal reproduction in a disposable environment, impact, and any safe suggested fix. Redact all secrets and avoid collecting unrelated user data.

## If your own key leaked

Revoke/rotate it through the provider first, inspect usage, then replace legitimate secret stores. Removing a file or screenshot does not invalidate the key. Follow [the key exposure guide](docs/security/api-keys.md) and GitHub's documented history-remediation process where applicable.

## Supported versions

Security fixes target the current `main` branch and the latest tagged release, if one exists. Tool/provider behavior is outside this project's control. Documented source-review dates do not certify third-party software or every operating system.

## Maintainer response

Acknowledge privately when possible, reproduce without real credentials, minimize disclosure, and publish a focused correction with accurate impact and validation. Never ask a reporter to paste their API key into a GitHub issue. Dependency updates must preserve the project's no-secret and no-automatic-provider-call boundaries.
