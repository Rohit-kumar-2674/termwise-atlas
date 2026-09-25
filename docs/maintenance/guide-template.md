---
title: "Template for a new tool guide"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://docs.github.com/en/get-started/using-github/github-flow"
  - "https://git-scm.com/docs"
---

# Template for a new tool guide

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Required metadata

Use front matter with `title`, `last_verified` (ISO date), `tool_version`, `verification`, `status`, and a list of primary `sources`. State whether the version was observed in a release listing or actually run. Keep an honest platform coverage statement.

## Required section order

Every `docs/tools/` page uses: **What is it? → Best For → Cost → Requirements → Supported Platforms → Installation → Configuration → First Command → Example Workflow → Troubleshooting → Documentation sources**.

## What reviewers should be able to answer

Who publishes the tool? What license applies? What does the software cost, and what do models cost? Which platforms are explicitly supported? What exact official install method and auth route are documented? Who documents OpenRouter/Ollama compatibility? Is Android native, a community PRoot experiment, or a remote client?

Installation examples must match a cited primary source. Don't invent a plausible npm package, shell flag, provider variable, or model ID. Identify placeholders clearly. Link to the platform guide for prerequisites instead of copying a long installation block into every page.

For unsupported integrations write “not established in the reviewed documentation,” or explain a confirmed unavailability with evidence. Experimental recipes need a clear boundary and a way to revert. Never turn a gateway recipe into a subscription-bypass claim.

## Documentation sources

- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [Git reference](https://git-scm.com/docs)
