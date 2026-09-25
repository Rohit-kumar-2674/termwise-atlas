---
title: "Develop, validate, and publish this guide"
last_verified: 2026-09-22
tool_version: "Platform-independent concepts; commands use the installed stable release"
verification: source-reviewed
status: "SOURCE CHECKED"
sources:
  - "https://squidfunk.github.io/mkdocs-material/"
  - "https://docs.python.org/3/library/venv.html"
  - "https://git-scm.com/docs"
  - "https://docs.docker.com/engine/security/"
  - "https://docs.github.com/en/get-started/using-github/github-flow"
---

# Develop, validate, and publish this guide

> **SOURCE CHECKED** · **Last verified:** 2026-09-22 (documentation review).<br>
> **Tool version:** Platform-independent concepts; commands use the installed stable release. Platform execution coverage is recorded in [Validation](../maintenance/validation.md).

## Local documentation build

Use Python 3.11+ and a virtual environment. The exact documentation dependencies are in `requirements-docs.lock`. The doctor and wizard themselves need only the standard library.

=== "Linux / macOS / WSL"

    ```bash
    python3 -m venv .venv
    .venv/bin/python -m pip install -r requirements-docs.lock
    .venv/bin/python scripts/render_data.py
    .venv/bin/python scripts/validate.py
    .venv/bin/python -m mkdocs serve --dev-addr 127.0.0.1:8000
    ```

=== "PowerShell"

    ```powershell
    py -3 -m venv .venv
    .\.venv\Scripts\python.exe -m pip install -r requirements-docs.lock
    .\.venv\Scripts\python.exe scripts/render_data.py
    .\.venv\Scripts\python.exe scripts/validate.py
    .\.venv\Scripts\python.exe -m mkdocs serve --dev-addr 127.0.0.1:8000
    ```

Open `http://127.0.0.1:8000`. On Android native Termux, some build dependencies may need compilation; reading Markdown or using a supported browser host is an alternative. Do not call a source-reviewed platform guide a runtime-tested site build unless you actually run it there.

## Reproducible checks

Using the environment's Python (shown below as `python`):

```bash
python scripts/render_data.py --check
python scripts/validate.py
python -m ruff check scripts tests examples/python-lab
python -m unittest discover -s tests -v
python -m unittest discover -s examples/python-lab -v
python -m mkdocs build --strict
```

The validator checks internal Markdown/HTML file targets, required metadata, tool-page structure, fenced shell syntax when Bash is available, JSON/YAML/TOML examples, blank credential templates, and generated-file drift. It does not execute installation instructions or prove an upstream integration works. GitHub's rendered Markdown and the built site use slightly different anchor conventions; browser tests verify key navigation.

With a supported Node LTS, run the deterministic chooser and browser checks:

```bash
npm ci
npm test
npx playwright install chromium
npm run test:browser
npm ci --prefix examples/react-checklist
npm test --prefix examples/react-checklist
npm run build --prefix examples/react-checklist
```

Browser tests use the already-built `site/`. On Linux machines missing browser system libraries, use Playwright's official dependency installation guidance; CI installs them explicitly. Set `PYTHON` for the Node parity test if your Python command has another name. No tests call a model provider or require an API key.

## Data and sources

Edit `data/catalog.json`, `data/models.json`, or `data/routes.json`, then regenerate with `python scripts/render_data.py`. Route rules are ordered, with a required final fallback. Python and browser chooser results are tested against each other across every supported input combination.

`python scripts/check_sources.py` makes network requests to primary documentation URLs. Definite 404/410 results fail; timeouts, bot blocks, and other ambiguous responses request review. The scheduled job is separate from offline PR validation to avoid making every edit depend on vendor uptime. A reachable page can still be outdated.

## Docker preview

After installing Docker from its official platform instructions:

```bash
docker compose up --build
```

Open `http://127.0.0.1:8000`; stop with `Ctrl+C`, then `docker compose down`. The multi-stage image builds static docs and serves them as an unprivileged user. Compose makes the runtime filesystem read-only, drops capabilities, and binds only to local loopback. It contains no model server and needs no credentials. Python's HTTP server is for previews; use static hosting for a public site.

## GitHub Actions and Pages

`verify.yml` checks Python utilities on Windows, Linux, and macOS, then validates/builds the site, runs browser/React checks, and builds/smoke-tests the container. It runs on pushes and pull requests without provider secrets.

For your own fork, set **Settings → Pages → Source → GitHub Actions**. The Pages workflow publishes only after a successful `Verify` push on `main` (or an explicit manual dispatch) and checks out the verified commit. Review `site_url`, `repo_url`, and script documentation URLs when forking. Manual dispatch still runs content/unit/build checks, but is not a replacement for the full verification workflow.

No external analytics, model requests, or third-party fonts are included in the site. Browser search is generated from the documentation at build time.

## Documentation sources

- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Git reference](https://git-scm.com/docs)
- [Docker Engine security](https://docs.docker.com/engine/security/)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
