def fibonacci(n):
    """
    Return the nth Fibonacci number.
    
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1
    
    Args:
        n: Non-negative integer
        
    Returns:
        The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev = 0
    curr = 1
    ith = curr
    for i in range(n - 2):
        ith = curr + prev
        prev = curr
        curr = ith
    return ith

