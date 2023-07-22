# Functions
# use def keyword to define functions
"""
syntax
def <func_name> (<args>..., <keyword_args>...):
    <statements>
"""


# ? *args & **kwargs when used with func definition packs the arguments
def all_the_args(*args, **kwargs):
    print(args)  # Prints (1, 2)
    print(kwargs)  # Prints {"a": 3, "b": 4}


args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
print(all_the_args(*args))  # equivalent to all_the_args(1, 2, 3, 4)
print(all_the_args(**kwargs))  # equivalent to all_the_args(a=3, b=4)
# ? *args & **kwargs when used with function call * & ** unpacks
print(all_the_args(*args, **kwargs))  # equivalent to all_the_args(1, 2, 3, 4, a=3, b=4)


#! All possible combinations of function signatures
# 1. Basic Function
def function_name():
    # Function body
    pass


# 2. Function with Arguments
def function_name(arg1, arg2):
    # Function body
    pass


# 3. Function with Default Values (Keyword Arguments)
def function_name(arg1="hello", arg2=1):
    # Function body
    pass


# 4. Function with Arbitrary Arguments (*args)
def function_name(*args):
    # Function body
    pass


# 5. Function with Keyword Arguments (**kwargs)
def function_name(**kwargs):
    # Function body
    pass


# 6. Function with both Arbitrary Arguments and Keyword Arguments
def function_name(*args, **kwargs):
    # Function body
    pass


# 7. Lambda Functions (Anonymous Functions)
lambda_function = lambda arguments: "heelo"

#! CaUtIoN: find differences between variable keywords global and nonlocal
# global specifies always to pick up the variable from global scope
# nonlocal specifies to find the first occurrence of variable outside function

# ? GLOBAL EXAMPLE
x = 0


def outer():
    x = 1

    def inner():
        global x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
print("global:", x)

# inner: 2
# outer: 1
# global: 2

# ? NONLOCAL EXAMPLE
x = 0


def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
print("global:", x)

# inner: 2
# outer: 2
# global: 0

# ? NORMAL EXAMPLE
x = 0


def outer():
    x = 1

    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
print("global:", x)

# inner: 2
# outer: 1
# global: 0


print("****************************************************************")

# TYPINGS in python
from typing import Any  # similar to typescript any types


def add_integers(a: int, b: int) -> int:
    return a + b


from typing import Tuple


def add_floats(points: Tuple[float, float]) -> float:
    return points[0] + points[1]


from typing import List, Dict


def example0() -> List[Dict[str, str]]:
    return [{"1": "2"}]


from typing import Union


def example1(condition: bool) -> Union[int, float]:
    if condition:
        return 5
    else:
        return 7.1
