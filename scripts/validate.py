#!/usr/bin/env python3
"""Offline content, link, syntax, and credential-template validation."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
TOOL_HEADINGS = ['What is it?', 'Best For', 'Cost', 'Requirements', 'Supported Platforms',
                 'Installation', 'Configuration', 'First Command', 'Example Workflow',
                 'Troubleshooting', 'Documentation sources']
REQUIRED_META = {'title', 'last_verified', 'tool_version', 'verification', 'status', 'sources'}
SKIP = {'.git', '.venv', '.qa', 'node_modules', 'site', 'practice', '__pycache__'}
FENCE = re.compile(r'^\s*(`{3,}|~{3,})([\w+-]*)[^\n]*$')


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {'href', 'src'} and value:
                self.targets.append(value)


def read_json(name: str):
    return json.loads((ROOT / 'data' / f'{name}.json').read_text(encoding='utf-8'))


def markdown_parts(text: str) -> tuple[str, list[tuple[str, str]], bool]:
    prose, blocks, block = [], [], []
    marker, language = None, ''
    for line in text.splitlines():
        match = FENCE.match(line)
        if match and marker is None:
            marker, language = match.group(1), match.group(2)
            block = []
        elif match and marker and match.group(1)[0] == marker[0] and len(match.group(1)) >= len(marker):
            blocks.append((language, '\n'.join(block)))
            marker = None
        elif marker:
            block.append(line)
        else:
            prose.append(line)
    return '\n'.join(prose), blocks, marker is not None


def local_target_exists(source: Path, href: str) -> bool:
    url = urlsplit(href)
    if url.scheme or url.netloc or not url.path or href.startswith(('mailto:', '#')):
        return True
    path = unquote(url.path)
    if path.startswith('/'):
        target = ROOT / 'docs' / path.lstrip('/')
    else:
        target = source.parent / path
    if target.exists():
        return True
    # Raw HTML links use built-site routes, while Markdown links use source files.
    if path.endswith('/'):
        return target.with_suffix('.md').exists() or (target / 'index.md').exists()
    return False


def validate(stale_days: int | None = None) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    today = dt.date.today()
    for path in ROOT.rglob('*.md'):
        if any(part in SKIP for part in path.relative_to(ROOT).parts):
            continue
        relative = path.relative_to(ROOT)
        text = path.read_text(encoding='utf-8')
        if not text.endswith('\n'):
            errors.append(f'{relative}: missing final newline')
        if path.is_relative_to(ROOT / 'docs'):
            if not text.startswith('---\n') or '\n---\n' not in text[4:]:
                errors.append(f'{relative}: missing guide metadata')
                continue
            front = text.split('---', 2)[1]
            try:
                meta = yaml.safe_load(front)
                if not isinstance(meta, dict) or not REQUIRED_META <= meta.keys():
                    raise ValueError('required fields missing')
                date = dt.date.fromisoformat(str(meta['last_verified']))
                if date > today:
                    raise ValueError('verification date is in the future')
                if stale_days is not None and (today - date).days > stale_days:
                    warnings.append(f'{relative}: last review {date} is older than {stale_days} days')
                if not isinstance(meta['sources'], list) or not meta['sources']:
                    raise ValueError('primary sources required')
                if any(not str(u).startswith('https://') for u in meta['sources']):
                    raise ValueError('source must be HTTPS')
            except (ValueError, TypeError, yaml.YAMLError) as exc:
                errors.append(f'{relative}: invalid metadata ({exc})')
        prose, blocks, unclosed = markdown_parts(text)
        if unclosed:
            errors.append(f'{relative}: unclosed code fence')
        if '\t' in prose:
            errors.append(f'{relative}: tab in Markdown prose')
        parser = Links()
        parser.feed(prose)
        targets = parser.targets + re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)', prose)
        for href in targets:
            if not local_target_exists(path, href):
                errors.append(f'{relative}: missing link target {href}')
        if path.parent == ROOT / 'docs/tools':
            headings = re.findall(r'^## (.+)$', prose, re.M)
            if headings != TOOL_HEADINGS:
                errors.append(f'{relative}: tool sections differ from standard')
        bash = shutil.which('bash')
        if bash:
            for language, code in blocks:
                if language in {'bash', 'sh'}:
                    check = subprocess.run([bash, '-n'], input=code, text=True, capture_output=True)
                    if check.returncode:
                        errors.append(f'{relative}: shell syntax error: {check.stderr.strip()}')
    sources = {s['id']: s for s in read_json('sources')['sources']}
    catalog = read_json('catalog')['tools']
    if len({t['id'] for t in catalog}) != len(catalog):
        errors.append('catalog: duplicate tool identifiers')
    for tool in catalog:
        for source in tool['sources']:
            if source not in sources:
                errors.append(f"catalog/{tool['id']}: unknown source {source}")
        if not (ROOT / 'docs' / tool['guide']).is_file():
            errors.append(f"catalog/{tool['id']}: missing guide")
        if set(tool['platforms']) != {'windows', 'linux', 'macos', 'android', 'cloud'}:
            errors.append(f"catalog/{tool['id']}: incomplete platforms")
        if not isinstance(tool['local'], bool):
            errors.append(f"catalog/{tool['id']}: local must be boolean")
    routes = read_json('routes')['routes']
    if not routes or routes[-1]['when'] != {}:
        errors.append('routes: final fallback required')
    for route in routes:
        for key in ('guide', 'next'):
            if not (ROOT / 'docs' / route[key]).is_file():
                errors.append(f"route/{route['id']}: missing {key}")
    for issue in read_json('troubleshooting')['issues']:
        if any(not issue.get(key) for key in ('id', 'symptom', 'cause', 'check', 'fix', 'verify')):
            errors.append('troubleshooting: incomplete record')
    examples = [ROOT / '.env.example', *list((ROOT / 'configs').glob('*.env.example'))]
    for path in examples:
        for line in path.read_text(encoding='utf-8').splitlines():
            if not line or line.startswith('#'):
                continue
            if not re.fullmatch(r'[A-Z][A-Z0-9_]*=.*', line):
                errors.append(f'{path.name}: malformed environment template')
                continue
            name, value = line.split('=', 1)
            if re.search('KEY|TOKEN|SECRET|PASSWORD', name) and value.strip():
                errors.append(f'{path.name}: credential placeholder must be empty')
    for path in (ROOT / 'configs').glob('*.json.example'):
        json.loads(path.read_text(encoding='utf-8'))
    for path in (ROOT / 'configs').glob('*.yaml.example'):
        yaml.safe_load(path.read_text(encoding='utf-8'))
    import tomllib
    for path in (ROOT / 'configs').glob('*.toml.example'):
        tomllib.loads(path.read_text(encoding='utf-8'))
    generated = subprocess.run([__import__('sys').executable, str(ROOT / 'scripts/render_data.py'), '--check'],
                               capture_output=True, text=True)
    if generated.returncode:
        errors.append(generated.stdout.strip())
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stale-days', type=int)
    args = parser.parse_args()
    errors, warnings = validate(args.stale_days)
    for value in warnings:
        print('REVIEW:', value)
    for value in errors:
        print('ERROR:', value)
    print(f'Validation: {len(errors)} errors; {len(warnings)} review reminders.')
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
