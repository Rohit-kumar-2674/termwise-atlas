---
title: "How this knowledge base stays current"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://squidfunk.github.io/mkdocs-material/"
  - "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
---

# How this knowledge base stays current

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Claims need evidence

Each guide carries LAST VERIFIED, TOOL VERSION, documentation sources, and a status. “Source-reviewed” means the linked primary documentation was checked; it does not mean the CLI was installed or exercised on every named platform. Runtime evidence belongs in [Validation](validation.md).

Compatibility data lives in `data/catalog.json`; model examples in `data/models.json`; chooser rules in `data/routes.json`. Generate the corresponding site assets and tables with `python scripts/render_data.py`. The JSON files and generated Markdown remain readable without the website.

## Review cadence

Review fast-changing installation, authentication, pricing, free-tier, and compatibility claims at least monthly and before a release. The scheduled source-link workflow checks reachability; it cannot prove semantic accuracy. Run `python scripts/validate.py --stale-days 45` to report aging review dates without silently updating them.

For a change, read the primary source, identify the responsible publisher, compare old/new behavior, record the date/version, and test a small task where feasible. Keep deprecated instructions only in clearly marked migration context. Mark known broken routes BROKEN; do not keep an OFFICIAL badge to preserve appearances.

## Resolve conflicting sources

Prefer a specific current release note or dated migration notice over a general older tutorial. Record unresolved contradictions plainly. The Google CLI transition is an example: a quota page can remain indexed after a consumer auth route changes.

## Release checklist

Run offline validation, unit tests, strict site build, browser checks, and all example checks. Review source-link results for real breakage versus robots/rate limits. Record what ran and what did not. Update CHANGELOG and version information, then publish a reviewed commit. CI success is evidence about this repository, not third-party service uptime.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Google consumer CLI transition announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
