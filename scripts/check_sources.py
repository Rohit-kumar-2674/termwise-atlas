#!/usr/bin/env python3
"""Check primary-source reachability on demand; never access a model API."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def check(source):
    url = source['url']
    request = urllib.request.Request(url, headers={'User-Agent': 'Termwise-Atlas-source-check/0.1'}, method='GET')
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            response.read(1024)
            return source['id'], 'OK', response.status
    except urllib.error.HTTPError as exc:
        return source['id'], 'BROKEN' if exc.code in {404, 410} else 'REVIEW', exc.code
    except (OSError, ValueError):
        return source['id'], 'REVIEW', 'network/redirect error'


def main():
    sources = json.loads((ROOT / 'data/sources.json').read_text())['sources']
    broken = 0
    with ThreadPoolExecutor(max_workers=4) as pool:
        for ident, status, detail in pool.map(check, sources):
            print(f'{status:7} {ident}: {detail}')
            broken += status == 'BROKEN'
    print('Reachability does not verify the semantic accuracy of a claim. REVIEW may mean rate limiting or bot restrictions.')
    return int(bool(broken))


if __name__ == '__main__':
    raise SystemExit(main())
