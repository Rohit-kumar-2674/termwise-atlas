import unittest
from text_tools import summarize_tasks, unique_words


class TextToolsTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(unique_words(""), [])

    def test_order_case_and_whitespace(self):
        self.assertEqual(unique_words("Code  test\nCODE"), ["code", "test"])

    def test_punctuation_is_preserved(self):
        self.assertEqual(unique_words("hello hello!"), ["hello", "hello!"])

    def test_unicode_casefold(self):
        self.assertEqual(unique_words("Straße STRASSE"), ["strasse"])

    def test_task_contract(self):
        tasks = [{'done': True}, {'done': False}, {}]
        self.assertEqual(summarize_tasks(tasks), {'completed': 1, 'pending': 2, 'total': 3})
        self.assertEqual(tasks, [{'done': True}, {'done': False}, {}])

    def test_empty_tasks(self):
        self.assertEqual(summarize_tasks([]), {'completed': 0, 'pending': 0, 'total': 0})


if __name__ == '__main__':
    unittest.main()
