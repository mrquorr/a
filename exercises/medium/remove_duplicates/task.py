def remove_duplicates(items):
    """
    Remove duplicates from a sorted list in-place and return the new length.
    
    Args:
        nums: Sorted list of integers (will be modified in-place)
        
    Returns:
        Length of the list after removing duplicates
    """
    seen = set()
    result = []
    for item in items:
        if item in seen:
            seen.add(item)
            result.append(item)
    return result
