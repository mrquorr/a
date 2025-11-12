def list_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Average as a float
        Returns 0.0 if list is empty
    """
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average