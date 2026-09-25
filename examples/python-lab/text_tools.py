"""Small pure functions for the test-generation and refactoring labs."""

def unique_words(text: str) -> list[str]:
    """Return case-folded whitespace-delimited tokens in first-seen order.

    Punctuation is preserved. Empty input returns an empty list.
    """
    return list(dict.fromkeys(text.casefold().split()))


def summarize_tasks(tasks: list[dict]) -> dict:
    """Count completed/incomplete items; missing done means incomplete."""
    completed = 0
    pending = 0
    for task in tasks:
        if task.get('done', False):
            completed += 1
        else:
            pending += 1
    return {'completed': completed, 'pending': pending, 'total': len(tasks)}
