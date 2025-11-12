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

def test_list_average_empty():
    """Test empty list"""
    assert list_average([]) == 0.0

