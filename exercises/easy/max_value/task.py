def find_max(numbers):
    """
    Find the maximum value in a list of numbers.
    
    Args:
        numbers: List of integers (may include negative numbers)
        
    Returns:
        The maximum value in the list
        Returns None if the list is empty
    """
    max_value = 0
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value