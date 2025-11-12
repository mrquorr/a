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
    nums = []
    unique_nums = remove_duplicates(nums)
    length = len(unique_nums)
    assert length == 0
    assert unique_nums[:length] == []


def test_remove_duplicates_multiple():
    """Test multiple duplicates"""
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    unique_nums = remove_duplicates(nums)
    length = len(unique_nums)
    assert length == 5
    assert unique_nums[:length] == [0, 1, 2, 3, 4]