import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
find_max = task.find_max

import pytest


def test_find_max_positive():
    """Test with positive numbers"""
    assert find_max([1, 5, 3, 9, 2]) == 9


def test_find_max_negative():
    """Test with negative numbers"""
    assert find_max([-5, -2, -8, -1]) == -1
