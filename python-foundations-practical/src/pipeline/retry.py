from collections.abc import Callable
from functools import wraps


def retry(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable: #Define the decorator function that takes a function as an argument
        @wraps(func) #Preserve the original functions metadata
        def wrapper(*args, **kwargs): #Define the wrapper function that will replace the original
            attempts = 0 #Initialize the attempts counter
            while attempts < max_attempts: #Loop until the max attempts
                try:
                    return func(*args, **kwargs) #Try to call the original function
                except Exception as e: #If an exception occurs
                    attempts += 1 #Increment the attempts counter
                    print(f"Attempt {attempts} failed: {e}") #Print the error message
                    if attempts == max_attempts: #If the max attempts is reached
                        raise #Raise the exception
        return wrapper #Return the wrapper function
    return decorator #Return the decorator function
