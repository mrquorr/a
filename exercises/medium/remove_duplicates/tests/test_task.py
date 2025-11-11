import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
remove_duplicates = task.remove_duplicates

import pytest


def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    nums = [1, 1, 2]
    length = remove_duplicates(nums)
    assert length == 2
    assert nums[:length] == [1, 2]


def test_remove_duplicates_multiple():
    """Test multiple duplicates"""
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = remove_duplicates(nums)
    assert length == 5
    assert nums[:length] == [0, 1, 2, 3, 4]


def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    nums = [1, 2, 3]
    length = remove_duplicates(nums)
    assert length == 3
    assert nums[:length] == [1, 2, 3]


def test_remove_duplicates_all_same():
    """Test list with all same elements"""
    nums = [1, 1, 1]
    length = remove_duplicates(nums)
    assert length == 1
    assert nums[:length] == [1]

