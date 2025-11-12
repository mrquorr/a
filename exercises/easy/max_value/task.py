def find_max(numbers):
    """Find the maximum value in a list."""
    max_value = 0
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value