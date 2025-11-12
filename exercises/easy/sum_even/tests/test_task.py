import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
sum_even = task.sum_even_numbers

import pytest


def test_sum_even_basic():
    """Test basic sum of evens"""
    assert sum_even([1, 1, 2]) == 2


def test_sum_even_all_odd():
    """Test list with only odd numbers"""
    assert sum_even([1, 3, 5, 7]) == 0

