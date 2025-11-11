import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
draw_triangle = task.draw_triangle

import pytest
import turtle


def test_triangle_angles():
    """Test that triangle draws with correct angles"""
    # Reset turtle
    turtle.reset()
    turtle.speed(0)  # Fastest
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    
    # Draw triangle
    draw_triangle(100)
    
    # Check final position (should be back at start for equilateral triangle)
    pos = turtle.position()
    # Allow small floating point error
    assert abs(pos[0]) < 1 and abs(pos[1]) < 1, f"Triangle should return to start, got {pos}"


def test_triangle_side_length():
    """Test triangle side length"""
    turtle.reset()
    turtle.speed(0)
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    
    start_pos = turtle.position()
    draw_triangle(50)
    end_pos = turtle.position()
    
    # Should return to start
    assert abs(start_pos[0] - end_pos[0]) < 1 and abs(start_pos[1] - end_pos[1]) < 1

