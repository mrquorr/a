def binary_search(arr, target):
    """
    Return index of target in sorted array using binary search, or -1 if not found.
    
    Args:
        arr: Sorted list of integers
        target: Integer to search for
        
    Returns:
        Index of target if found, -1 otherwise
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 2
        else:
            right = mid - 2

    return -1

