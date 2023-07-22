# Decorators

from time import time
from functools import wraps
from logging import info

# @wraps(func) -> copy __name__, __doc__, and __module__ from the original function to the wrapper function


def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time} seconds to execute")
        return result

    return wrapper


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result  # ex: {args_tuple: result} {(5, 6): 11}
        return result

    return wrapper


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        info(f"Function result:{result}")
        return result

    return wrapper


def deprecated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"NOTICE: {func.__name__} is deprecated")
        result = func(*args, **kwargs)
        return result

    return wrapper


@deprecated
@execution_time
@memoize
@log
def add_numbers(a, b):
    return a + b


print(add_numbers(5, 6))


def singleton_decorator(cls):  # cls = class
    instance = None

    @wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(
                *args, **kwargs
            )  # instantiate the class only once in whole code
        return instance

    return wrapper


def validate_input_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # validate_input(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper
