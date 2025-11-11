import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
merge_sorted_arrays = task.merge_sorted_arrays

import pytest


def test_merge_sorted_basic():
    """Test basic merge"""
    assert merge_sorted_arrays([1, 3], [2, 4]) == [1, 2, 3, 4]


def test_merge_sorted_different_lengths():
    """Test arrays of different lengths"""
    assert merge_sorted_arrays([1, 2, 3], [4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_sorted_empty_first():
    """Test with empty first array"""
    assert merge_sorted_arrays([], [1, 2, 3]) == [1, 2, 3]


def test_merge_sorted_empty_second():
    """Test with empty second array"""
    assert merge_sorted_arrays([1, 2, 3], []) == [1, 2, 3]


def test_merge_sorted_duplicates():
    """Test with duplicate values"""
    assert merge_sorted_arrays([1, 2, 2], [2, 3, 4]) == [1, 2, 2, 2, 3, 4]

