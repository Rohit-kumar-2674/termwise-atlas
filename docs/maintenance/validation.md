---
title: "Validation record and limits"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://git-scm.com/docs"
  - "https://squidfunk.github.io/mkdocs-material/"
  - "https://nodejs.org/en/download"
  - "https://docs.python.org/3/library/venv.html"
---

# Validation record and limits

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Evidence levels

**Source review:** installation/authentication/platform/license/provider claims were compared with primary documentation beginning 2026-09-22. Guides record observed releases where available. This does not certify an installation on every supported OS.

**Repository checks:** automated checks exercise this project's own scripts, generated data, examples, links, and documentation website. The initial local results below were recorded on 2026-09-23; the utility tests were rechecked on 2026-09-25 after correcting the Windows architecture lookup.

## Runtime scope

The local build environment is Linux with Python 3.12.14 and Node 24.19.0.

| Check | Observed result |
| --- | --- |
| Python utility/security/route tests | 13 passed, including the Windows lookup regression |
| Python example contract tests | 6 passed; separate buggy fixture reproduces its intended boundary failure |
| Browser/Python chooser parity | All 120 device/goal/memory combinations agree; invalid inputs rejected |
| React logic tests and production build | 2 tests passed; Vite production build passed |
| Content/schema/configuration/shell syntax | Passed with zero internal link errors |
| Ruff | Passed |
| MkDocs strict build | Passed with pinned MkDocs 1.6.1 and Material 9.7.7 |
| Chromium browser checks | 5 passed: chooser, filters, mobile navigation/theme, search/copy controls, no-JavaScript fallback |
| Accessibility checks | No axe violations in tested homepage content and chooser scope; not a whole-site conformance audit |
| Static-site network check | No external requests during tested browsing; repository statistics auto-fetch removed |
| Primary-source reachability | 71 URLs returned 200; one repository URL timed out and requires review, with no confirmed 404/410 |

Browser tests used Playwright 1.58.2 and an available Chromium 153 binary after the automatic browser download returned truncated archives. CI uses Playwright's normal browser installation. Screenshots in `assets/screenshots/` are actual rendered desktop/mobile pages, not mockups.

 Upstream model requests, paid authentication flows, native Android/PRoot hardware, and local GPU inference are not exercised by the automated repository checks.

## Published CI evidence

[Verify run 36141620818](https://github.com/Rohit-kumar-2674/termwise-atlas/actions/runs/36141620818) passed all eight jobs on 2026-09-25 for commit `0c00e420a555e4a4545d5246bf467dec9b9f6840`:

- Windows, Ubuntu, and macOS each ran the 13 utility tests and 6 Python example tests with Python 3.11 and 3.13, plus the doctor and noninteractive wizard commands.
- The content/site job passed lint, schema/link/configuration validation, the strict documentation build, chooser parity, React tests/build, and all five browser checks using Playwright's downloaded Chromium.
- The Docker job built the image and fetched the expected homepage from the non-root container with a read-only filesystem, all Linux capabilities dropped, and privilege escalation disabled.

The first CI attempt revealed a Windows Python 3.11 architecture lookup that could execute a subprocess and a Docker readiness check that did not retry startup connection resets. Both were fixed before the successful run. Future changes should consult the Actions result for their own commit; this record does not certify later revisions automatically.

GitHub Pages was activated with GitHub Actions as its publishing source on 2026-09-26. [Publish documentation run 36142142196](https://github.com/Rohit-kumar-2674/termwise-atlas/actions/runs/36142142196), attempt 2, completed both build and deployment successfully. The [live documentation](https://rohit-kumar-2674.github.io/termwise-atlas/) was opened in a browser: the homepage and setup chooser loaded, search returned results, and navigation to the Android guide worked. HTTPS is enforced on the default GitHub Pages domain. This is a deployment smoke check, separate from the automated browser test coverage above.

## Honest interpretation

A source-reviewed CLI installation can change after the review date. An accessible model endpoint can still reject a task because of account eligibility, billing, tool schema, or context. Memory estimates are planning ranges, not measurements. Contributions must keep those boundaries visible rather than increasing a badge's confidence without evidence.

## Documentation sources

- [Git reference](https://git-scm.com/docs)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Node.js official downloads](https://nodejs.org/en/download)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
