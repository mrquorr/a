import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
fibonacci = task.fibonacci

import pytest


def test_fibonacci_zero():
    """Test F(0)"""
    assert fibonacci(0) == 0


def test_fibonacci_one():
    """Test F(1)"""
    assert fibonacci(1) == 1


def test_fibonacci_two():
    """Test F(2)"""
    assert fibonacci(2) == 1


def test_fibonacci_five():
    """Test F(5)"""
    assert fibonacci(5) == 5


def test_fibonacci_ten():
    """Test F(10)"""
    assert fibonacci(10) == 55

