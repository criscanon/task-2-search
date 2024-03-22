def binary_search(arr, target):
    """
    Perform binary search on the given sorted array.

    Args:
        arr (list): The sorted input array.
        target: The target element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# Complexity O(log n)