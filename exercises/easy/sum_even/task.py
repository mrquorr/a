def sum_even_numbers(numbers):
    """
    Return the sum of all even numbers in a list.
    
    Args:
        numbers: List of integers
        
    Returns:
        Sum of all even numbers (0 if no even numbers)
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:
            total += num
    return total