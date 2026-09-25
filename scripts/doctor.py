#!/usr/bin/env python3
"""Inspect local prerequisites without network calls or secret disclosure."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import sysconfig
from collections.abc import Mapping

TOOLS = {
    'git': 'git', 'python': None, 'node': 'node', 'npm': 'npm', 'pnpm': 'pnpm',
    'docker': 'docker', 'ollama': 'ollama', 'claude': 'claude', 'gemini': 'gemini',
    'codex': 'codex', 'aider': 'aider', 'opencode': 'opencode', 'continue': 'cn',
    'antigravity': 'agy',
}
KEYS = ('OPENROUTER_API_KEY', 'GEMINI_API_KEY', 'OPENAI_API_KEY', 'ANTHROPIC_API_KEY')
VERSION = re.compile(r'(?<![\w.])v?(\d{1,4}\.\d{1,4}(?:\.\d{1,4})?(?:-[a-zA-Z0-9.]+)?)(?![\w.])')


def architecture() -> str:
    """Read architecture without platform.machine()'s Windows shell fallback."""
    if sys.platform == 'win32':
        # The Python build tag identifies the running interpreter, including
        # when an x86/x64 Python is emulated on a different Windows CPU.
        return {'win32': 'x86', 'win-amd64': 'AMD64', 'win-arm64': 'ARM64'}.get(
            sysconfig.get_platform(), 'unknown')
    return os.uname().machine if hasattr(os, 'uname') else 'unknown'


def safe_version(executable: str, environment: Mapping[str, str]) -> str:
    """Explicitly opted-in fixed-argument probe. Never return raw tool output."""
    env = {k: v for k, v in environment.items()
           if not re.search(r'KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL', k, re.I)}
    try:
        result = subprocess.run([executable, '--version'], shell=False, timeout=4,
                                stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL, text=True, errors='replace', env=env)
    except (OSError, subprocess.TimeoutExpired):
        return 'probe unavailable'
    if result.returncode != 0:
        return 'probe failed'
    output = result.stdout[:2048]
    for name in KEYS:
        value = environment.get(name, '')
        if value:
            output = output.replace(value, '[redacted]')
    match = VERSION.search(output)
    return match.group(1) if match else 'version not recognized'


def report(probe: bool = False) -> dict:
    tools = []
    for name, command in TOOLS.items():
        path = sys.executable if command is None else shutil.which(command)
        entry = {'name': name, 'available': bool(path)}
        if command is None:
            entry['version'] = '.'.join(map(str, sys.version_info[:3]))
        elif probe and path:
            entry['version'] = safe_version(path, os.environ)
        tools.append(entry)
    return {'schema_version': 1, 'os': sys.platform, 'architecture': architecture(),
            'mode': 'version probes' if probe else 'presence only', 'tools': tools,
            'keys': {key: bool(os.environ.get(key, '').strip()) for key in KEYS},
            'note': 'Availability is not authentication or integration validation. No values or paths are reported.'}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true', help='Print machine-readable output')
    parser.add_argument('--probe-versions', action='store_true', help='Execute installed --version commands')
    parser.add_argument('--require', action='append', choices=tuple(TOOLS), default=[])
    args = parser.parse_args(argv)
    data = report(args.probe_versions)
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(f"Termwise Atlas doctor | {data['os']} / {data['architecture']} | {data['mode']}")
        for item in data['tools']:
            state = 'available' if item['available'] else 'not found (optional)'
            print(f"{item['name']:14} {state:22} {item.get('version', '')}")
        for key, configured in data['keys'].items():
            print(f"{key:22} {'configured' if configured else 'not configured'}")
        print(data['note'])
    available = {item['name']: item['available'] for item in data['tools']}
    return int(any(not available[name] for name in args.require))


if __name__ == '__main__':
    raise SystemExit(main())
