import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
count_vowels = task.count_vowels

import pytest


def test_count_vowels_simple():
    """Test simple vowel counting"""
    assert count_vowels("hello") == 2


def test_count_vowels_all_vowels():
    """Test with all vowels"""
    assert count_vowels("education") == 5