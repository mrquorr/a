import turtle

def draw_triangle(L):
    """
    Draw an equilateral triangle with side length L.
    
    Args:
        L: Side length of the triangle
    """
    # TODO: Fix the bug - the angle should be 120 degrees for an equilateral triangle
    for i in range(3):
        turtle.forward(L)
        turtle.right(120)  # Fixed: was 190, should be 120

