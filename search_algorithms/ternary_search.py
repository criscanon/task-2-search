def ternary_search(arr, target):
    """
    Perform ternary search on the given sorted array.

    Args:
        arr (list): The sorted input array.
        target: The target element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1
    
    while low <= high:
        print(low, high, target)
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        
        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low, high = mid1 + 1, mid2 - 1
    
    return -1
