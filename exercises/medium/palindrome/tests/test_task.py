import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
is_palindrome = task.is_palindrome

import pytest


def test_palindrome_simple():
    """Test simple palindrome"""
    assert is_palindrome("racecar") == True


def test_not_palindrome():
    """Test non-palindrome"""
    assert is_palindrome("foobar") == False
