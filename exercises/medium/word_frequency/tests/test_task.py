import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
get_most_common_words = task.get_most_common_words

import pytest


def test_most_common_basic():
    """Test basic word frequency"""
    text = "hello world hello"
    result = get_most_common_words(text, 2)
    assert result == [('hello', 2), ('world', 1)]


def test_most_common_multiple():
    """Test with multiple words"""
    text = "the cat sat on the mat the dog ran fast the bird flew"
    result = get_most_common_words(text, 3)
    assert result == [('the', 4), ('cat', 1), ('sat', 1)]


def test_most_common_punctuation():
    """Test with punctuation"""
    text = "hello, world! hello."
    result = get_most_common_words(text, 2)
    assert result == [('hello', 2), ('world', 1)]


def test_most_common_case_insensitive():
    """Test case insensitivity"""
    text = "Hello hello HELLO"
    result = get_most_common_words(text, 1)
    assert result == [('hello', 3)]

