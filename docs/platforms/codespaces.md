---
title: "GitHub Codespaces"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces"
  - "https://docs.github.com/en/billing/concepts/product-billing/github-codespaces"
  - "https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions"
  - "https://docs.github.com/en/get-started/using-github/github-flow"
---

# GitHub Codespaces

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Start in your browser

On a repository you own or a fork, open **Code → Codespaces → Create codespace**. Use the smallest suitable machine. Personal account allowances are limited; compute and storage beyond allowances can be billed. Stopped environments can still consume storage. Review your account's budget and retention settings before starting a long session.

This repository includes a small development-container definition for its documentation tooling. Inspect `devcontainer.json` before trusting a new repository: setup scripts and extensions execute code. Create the environment, wait for installation, and open a terminal.

```bash
python3 --version
git --version
python3 scripts/doctor.py
```

The supplied container is for the learning hub, not a pre-authorized AI agent. Install your chosen CLI only when needed. Use a supported Node LTS for Node tools, and keep provider auth separate from Codespaces' GitHub sign-in.

## Keys and previews

Use Codespaces secrets scoped only to trusted repositories, or a temporary hidden prompt. Repository-controlled tasks can read environment variables provided to them. Never run untrusted pull-request code with model keys attached.

Run the documentation site according to [development](../maintenance/development.md), bind the dev server to `0.0.0.0` inside the container, and use the Ports panel. Keep forwarded ports private. Browser localhost refers to the device running the browser, not necessarily the codespace.

## Finish safely

Review and commit work, push the branch, then stop the codespace. Verify the commit appears on GitHub before deleting the environment. Deleting a codespace can remove unpushed files. Use [GitHub flow](../git/github.md) for pull requests and reviews.

Android users can do this in a browser; a hardware keyboard helps but is not required. A remote model and remote compute are separate costs, even when one currently has a free allowance.

## Documentation sources

- [GitHub Codespaces overview](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces)
- [Codespaces billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)
- [GitHub Actions secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
