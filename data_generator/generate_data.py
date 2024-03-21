import random

def generate_data(size):
    """
    Generate a list of random integers.

    Args:
        size (int): The size of the list.

    Returns:
        list: A list of random integers.
    """
    return [random.randint(1, 1000) for _ in range(size)]
