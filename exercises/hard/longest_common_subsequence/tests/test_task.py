import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
longest_common_subsequence = task.longest_common_subsequence

import pytest


def test_lcs_simple():
    """Test simple LCS"""
    assert longest_common_subsequence("abcde", "ace") == 3


def test_lcs_same():
    """Test same strings"""
    assert longest_common_subsequence("abc", "abc") == 3


def test_lcs_no_common():
    """Test no common subsequence"""
    assert longest_common_subsequence("abc", "def") == 0


def test_lcs_complex():
    """Test complex case"""
    assert longest_common_subsequence("afloof", "flooferfoof") == 5


def test_lcs_empty():
    """Test with empty string"""
    assert longest_common_subsequence("", "abc") == 0
    assert longest_common_subsequence("abc", "") == 0

