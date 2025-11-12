def quick_sort(arr, low, high):
    """
    Sort array using quick sort algorithm (in-place).
    
    Args:
        arr: List of integers to sort
        low: Starting index
        high: Ending index
        
    Returns:
        The sorted array
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    """
    Partition array around pivot element.
    
    Args:
        arr: List of integers
        low: Starting index
        high: Ending index (pivot index)
        
    Returns:
        Final position of pivot element
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i]
    return i + 1

def sort_array(arr):
    """
    Helper function to sort an array using quick sort.
    
    Args:
        arr: List of integers to sort
        
    Returns:
        New sorted list (original array is not modified)
    """
    if not arr:
        return arr
    return quick_sort(arr[:], 0, len(arr) - 1)
