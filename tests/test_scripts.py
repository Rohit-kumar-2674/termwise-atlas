import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import doctor
import wizard


class DoctorTests(unittest.TestCase):
    def test_default_does_not_execute_programs_or_reveal_secrets(self):
        secret = 'private-canary-do-not-display-938271'
        with patch.dict(os.environ, {key: secret for key in doctor.KEYS}), \
                patch('doctor.subprocess.Popen', side_effect=AssertionError('Presence checks must not execute commands')) as run:
            output = json.dumps(doctor.report())
        run.assert_not_called()
        self.assertNotIn(secret, output)
        self.assertNotIn(str(Path.home()), output)
        self.assertTrue(all(json.loads(output)['keys'].values()))

    def test_windows_architecture_does_not_execute_commands(self):
        with patch('doctor.sys.platform', 'win32'), \
                patch('doctor.subprocess.Popen', side_effect=AssertionError('Architecture must not execute commands')):
            for tag, expected in [('win32', 'x86'), ('win-amd64', 'AMD64'),
                                  ('win-arm64', 'ARM64'), ('unrecognized', 'unknown')]:
                with self.subTest(tag=tag), patch('doctor.sysconfig.get_platform', return_value=tag):
                    self.assertEqual(doctor.architecture(), expected)

    def test_whitespace_key_is_not_configured(self):
        with patch.dict(os.environ, {'OPENROUTER_API_KEY': '   '}):
            self.assertFalse(doctor.report()['keys']['OPENROUTER_API_KEY'])

    def test_probe_uses_fixed_arguments_and_removes_secret_env(self):
        result = subprocess.CompletedProcess([], 0, 'tool 1.2.3\nunsafe extra output', '')
        with patch('doctor.subprocess.run', return_value=result) as run:
            version = doctor.safe_version('/trusted/tool', {'PATH': '/bin', 'OPENROUTER_API_KEY': 'hidden', 'TOKEN': 'hidden'})
        self.assertEqual(version, '1.2.3')
        self.assertEqual(run.call_args.args[0], ['/trusted/tool', '--version'])
        self.assertFalse(run.call_args.kwargs['shell'])
        self.assertEqual(run.call_args.kwargs['env'], {'PATH': '/bin'})

    def test_probe_timeout_is_contained(self):
        with patch('doctor.subprocess.run', side_effect=subprocess.TimeoutExpired('tool', 4)):
            self.assertEqual(doctor.safe_version('tool', {}), 'probe unavailable')

    def test_probe_never_returns_raw_output(self):
        secret = '123.456.789'
        result = subprocess.CompletedProcess([], 0, secret, '')
        with patch('doctor.subprocess.run', return_value=result):
            self.assertEqual(doctor.safe_version('tool', {'OPENAI_API_KEY': secret}), 'version not recognized')

    def test_required_and_optional_missing_tools(self):
        with patch('doctor.shutil.which', return_value=None), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(doctor.main([]), 0)
            self.assertEqual(doctor.main(['--require', 'git']), 1)
            self.assertEqual(doctor.main(['--require', 'python']), 0)


class WizardTests(unittest.TestCase):
    def test_all_supported_inputs_have_existing_guides(self):
        data = wizard.load_routes()
        ids = set()
        for device in data['platforms']:
            for goal in data['goals']:
                for ram in data['ram_choices']:
                    route = wizard.choose_route(device, goal, ram, data)
                    ids.add(route['id'])
                    self.assertTrue((ROOT / 'docs' / route['guide']).is_file())
        self.assertEqual(ids, {route['id'] for route in data['routes']})

    def test_android_local_has_explicit_limit(self):
        route = wizard.choose_route('android', 'local', 64)
        self.assertEqual(route['id'], 'android-local')
        self.assertIn('not established', route['summary'])

    def test_cloud_local_is_not_claimed_on_device(self):
        self.assertEqual(wizard.choose_route('cloud', 'local', 32)['id'], 'remote-local')

    def test_unknown_inputs_rejected(self):
        for args in [('unknown', 'local', 4), ('linux', 'bypass', 4), ('linux', 'cloud', -1)]:
            with self.assertRaises(ValueError):
                wizard.choose_route(*args)

    def test_cli_is_noninteractive_and_secret_free(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            result = wizard.main(['--platform', 'android', '--goal', 'cloud', '--ram', '4', '--json'])
        self.assertEqual(result, 0)
        self.assertEqual(json.loads(output.getvalue())['id'], 'android-cloud')


class LearningFixtureTests(unittest.TestCase):
    def test_bug_is_reproduced_and_reference_passes(self):
        path = ROOT / 'examples/python-lab/check_cart.py'
        spec = importlib.util.spec_from_file_location('check_cart', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        failures = module.evaluate(path.with_name('cart_buggy.py'))
        self.assertEqual(len(failures), 1)
        self.assertIn('50.00', failures[0])
        self.assertEqual(module.evaluate(path.with_name('cart_reference.py')), [])


if __name__ == '__main__':
    unittest.main()
