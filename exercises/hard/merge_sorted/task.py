def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        arr1: First sorted list of integers
        arr2: Second sorted list of integers
        
    Returns:
        New sorted list containing all elements from both arrays
    """
    result = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    return result
