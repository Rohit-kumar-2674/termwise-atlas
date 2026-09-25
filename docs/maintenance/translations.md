---
title: "Translations and accessibility"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://squidfunk.github.io/mkdocs-material/"
  - "https://docs.github.com/en/get-started/using-github/github-flow"
---

# Translations and accessibility

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## English is canonical for now

The first release has one maintained English source. Future translations can live under `docs/i18n/LANGUAGE/` with language code, canonical source path, source commit, translator/reviewer, and last synchronization date. Planned languages include Hindi, Spanish, French, Portuguese, German, Japanese, and Korean; these are plans, not currently available translations.

Translate explanations and navigation while preserving commands, API names, model IDs, source URLs, and status distinctions. Do not translate FREE TIER into an unqualified promise of free service. Mark a stale translation when its canonical guide changes and link readers to the current English page.

## Make contributions accessible

Use descriptive link text, semantic headings, text equivalents for diagrams, and alt text for screenshots. Keep command blocks separate by platform. Avoid relying on badge color alone: every status needs words. Test keyboard navigation and narrow screens, especially the setup chooser and compatibility filters.

AI-assisted translation needs review by someone fluent in the language and able to verify the technical meaning. Never label an unreviewed automatic translation as authoritative.

## Documentation sources

- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
