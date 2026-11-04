from collections.abc import Callable
from functools import wraps
from time import perf_counter


def timer(func: Callable) -> Callable:
    @wraps(func) #Preserve the original function's metadata
    def wrapper(*args, **kwargs): # Accept any arguments and keyword arguments
        start_time = perf_counter() # Record the start time
        result = func(*args, **kwargs) #call the original function with the provided arguments
        end_time = perf_counter() # Record the end time
        elapsed_time = end_time - start_time # Calculate the elapsed time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds") # Print the elapsed time
        return result # Return the result of the original function
    return wrapper # Return the wrapper function
