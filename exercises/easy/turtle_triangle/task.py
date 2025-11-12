import turtle

def draw_triangle(L):
    """
    Draw an equilateral triangle with side length L.
    
    Args:
        L: Side length of the triangle
    """
    for i in range(3):
        turtle.forward(L)
        turtle.right(190) 
