import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
sum_even = task.sum_even

import pytest


def test_sum_even_basic():
    """Test basic sum of evens"""
    assert sum_even([1, 2, 3, 4, 5]) == 6


def test_sum_even_all_odd():
    """Test list with only odd numbers"""
    assert sum_even([1, 3, 5, 7]) == 0


def test_sum_even_all_even():
    """Test list with only even numbers"""
    assert sum_even([2, 4, 6, 8]) == 20


def test_sum_even_empty():
    """Test empty list"""
    assert sum_even([]) == 0


def test_sum_even_negative():
    """Test with negative numbers"""
    assert sum_even([-2, -1, 0, 1, 2]) == 0

