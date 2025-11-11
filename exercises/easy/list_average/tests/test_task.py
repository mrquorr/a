import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
list_average = task.list_average

import pytest


def test_list_average_basic():
    """Test basic average"""
    assert list_average([1, 2, 3, 4, 5]) == 3.0


def test_list_average_single():
    """Test single element"""
    assert list_average([5]) == 5.0


def test_list_average_empty():
    """Test empty list"""
    assert list_average([]) == 0.0


def test_list_average_decimal():
    """Test with decimal result"""
    assert list_average([1, 2, 3]) == 2.0


def test_list_average_negative():
    """Test with negative numbers"""
    assert list_average([-2, 0, 2]) == 0.0

