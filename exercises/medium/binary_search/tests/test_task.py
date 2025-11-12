import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
binary_search = task.binary_search

import pytest


def test_binary_search_one():
    """Test finding element"""
    assert binary_search([1, 2, 3, 4, 5], 3) == 2

def test_binary_search_three():
    """Test finding last element"""
    assert binary_search([1, 2, 3, 4, 5], 4) == 3