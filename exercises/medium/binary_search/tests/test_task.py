import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
binary_search = task.binary_search

import pytest


def test_binary_search_found():
    """Test finding element"""
    assert binary_search([1, 2, 3, 4, 5], 3) == 2


def test_binary_search_first():
    """Test finding first element"""
    assert binary_search([1, 2, 3, 4, 5], 1) == 0


def test_binary_search_last():
    """Test finding last element"""
    assert binary_search([1, 2, 3, 4, 5], 5) == 4


def test_binary_search_not_found():
    """Test element not in array"""
    assert binary_search([1, 2, 3, 4, 5], 6) == -1


def test_binary_search_empty():
    """Test empty array"""
    assert binary_search([], 5) == -1

