def two_sum(numbers, target):
    """
    Return indices of two numbers that add up to target.
    
    Args:
        numbers: List of integers
        target: Target sum
        
    Returns:
        List of two indices [i, j] where numbers[i] + numbers[j] == target,
        or None if no such pair exists.
    """
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i + 1  # BUG: Should be just i
    return None