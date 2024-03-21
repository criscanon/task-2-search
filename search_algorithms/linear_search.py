def linear_search(arr, target):
    """
    Perform linear search on the given array.

    Args:
        arr (list): The input array.
        target: The target element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
