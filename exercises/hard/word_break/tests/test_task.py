import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
word_break = task.word_break

import pytest


def test_word_break_simple():
    """Test simple word break"""
    assert word_break("leetcode", ["leet", "code"]) == True


def test_word_break_multiple():
    """Test multiple words"""
    assert word_break("applepenapple", ["apple", "pen"]) == True


def test_word_break_cannot():
    """Test cannot be segmented"""
    assert word_break("leetcode", ["le", "eet", "code"]) == False


def test_word_break_single():
    """Test single character"""
    assert word_break("a", ["a"]) == True


def test_word_break_empty():
    """Test empty string"""
    assert word_break("", ["a", "b"]) == True

