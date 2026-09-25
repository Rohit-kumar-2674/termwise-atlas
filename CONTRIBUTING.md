# Contributing to Termwise Atlas

Useful contributions are small, reproducible, and sourced. Bring Android observations, platform fixes, new troubleshooting entries, updated commands, accessible screenshots, or a new tool that meets the inclusion criteria.

## Make a focused change

1. Open an issue describing the problem, or choose an existing one. Never include secrets.
2. Fork, clone, and create a branch. Follow [GitHub flow](docs/git/github.md).
3. Edit canonical English Markdown or the JSON database; run `python scripts/render_data.py` after data changes.
4. State the OS, architecture, shell, tool version, authentication route, and commands actually tested. “Source reviewed” is not “executed successfully.”
5. Run the [project checks](docs/maintenance/development.md), review the diff, and open a PR.

## Evidence requirements

Pricing, free-tier, API, authentication, licensing, and platform-support changes require primary sources and a review date. Name whose documentation supports an integration. Community experiments must not acquire an OFFICIAL label through repetition. If two official pages conflict, record the conflict and prioritize the more specific, dated notice only with an explanation.

Use the [guide template](docs/maintenance/guide-template.md). New tools should have an identifiable publisher, upstream repository/license where applicable, current installation/authentication docs, and a useful place in the learning path. A public GitHub repository alone is not proof of an open-source license or active maintenance.

## Commands and examples

Separate operating systems and shells. Use placeholders only when clearly identified. Never add real keys, opaque obfuscated scripts, subscription bypasses, unsafe blanket permission changes, or fabricated compatibility. Small deterministic examples should run without paid API access.

Generated comparison/model pages come from `data/`; don't hand-edit generated blocks. Keep diagnostics read-only by default and never print secret values. Tests should protect behavior and security boundaries, not mirror implementation details.

## Reviews and translations

Be specific and respectful. Maintainers may request a smaller patch, upstream evidence, or a clearer support label. Read the [Code of Conduct](CODE_OF_CONDUCT.md) and [translation plan](docs/maintenance/translations.md). English remains canonical until a reviewed language team and update process exist.
