#!/usr/bin/env python3
"""Print setup guidance. Does not install software, write config, or collect keys."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://rohit-kumar-2674.github.io/termwise-atlas/'


def load_routes() -> dict:
    return json.loads((ROOT / 'data/routes.json').read_text(encoding='utf-8'))


def choose_route(platform: str, goal: str, ram: int, data: dict | None = None) -> dict:
    data = data or load_routes()
    if platform not in data['platforms'] or goal not in data['goals'] or ram not in data['ram_choices']:
        raise ValueError('Select a documented platform, goal, and memory option.')
    for route in data['routes']:
        rule = route['when']
        if 'platform' in rule and platform not in rule['platform']:
            continue
        if 'goal' in rule and goal not in rule['goal']:
            continue
        if 'ram_max' in rule and ram > rule['ram_max']:
            continue
        return route.copy()
    raise ValueError('No route matched; route data needs a fallback.')


def ask(label: str, choices: list, default):
    print(f"{label}: {', '.join(map(str, choices))}")
    while True:
        value = input(f'Choice [{default}]: ').strip().lower() or str(default)
        for option in choices:
            if str(option) == value:
                return option
        print('Choose one of the listed options. Never enter an API key.')


def main(argv: list[str] | None = None) -> int:
    data = load_routes()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--platform', choices=data['platforms'])
    parser.add_argument('--goal', choices=data['goals'])
    parser.add_argument('--ram', type=int, choices=data['ram_choices'])
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    supplied = (args.platform, args.goal, args.ram)
    if any(v is not None for v in supplied) and not all(v is not None for v in supplied):
        parser.error('Supply --platform, --goal, and --ram together, or omit all for interactive mode.')
    if args.json and not all(v is not None for v in supplied):
        parser.error('--json requires --platform, --goal, and --ram.')
    try:
        device = args.platform or ask('Device / environment', data['platforms'], 'android')
        goal = args.goal or ask('Goal (free means a limited legitimate cloud allowance)', data['goals'], 'cloud')
        ram = args.ram or ask('Installed RAM in GB (choose the lower option if unsure)', data['ram_choices'], 4)
    except (EOFError, KeyboardInterrupt):
        print('\nNo changes made. Run with --help for non-interactive usage.')
        return 1
    route = choose_route(device, goal, ram, data)
    if args.json:
        print(json.dumps(route, indent=2))
    else:
        print(f"\n{route['title']}\n{route['summary']}\nCost: {route['cost']}")
        print(f"Read: docs/{route['guide']}\nNext: docs/{route['next']}")
        print(f"Online: {SITE}{route['guide'].removesuffix('.md')}/")
        print('No installations or configuration changes were made. No credentials were collected.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
