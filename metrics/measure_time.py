import time

def measure_time(func, *args):
    """
    Measure the execution time of a function.

    Args:
        func (callable): The function to be measured.
        *args: Variable-length argument list to pass to the function.

    Returns:
        tuple: A tuple containing the result of the function and the execution time in microseconds.
    """
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()

    # Convert the time difference to microseconds
    execution_time_microseconds = (end_time - start_time) * 1e6

    return result, execution_time_microseconds
