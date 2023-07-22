def quick_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


sample_array = [890, 23, 2, 582, 0, 73, 33, 31, 31]
print(quick_sort(sample_array))

# high level programming language, multi paradigm programming language (functional & object oriented programming patterns can be achieved), dynamically typed language.

# Guido Von Rossum is creator of python
# Indentation: Prefer to use spaces over tabs: 4 spaces is the norm for demarcating code blocks
# Comments: Single line comments use #, while multi-line comments use """ """ triple double quotes syntax

# Variables: dynamically typed, no concept of declaration, only assignments to values

sample_number_variable = 131
print(sample_number_variable)

# print(some_unknown_variable) # Raises NameError # Python always raises class errors

# In python everything is a object. For example
sample_string_variable = "323"
# is read as name sample_string_variable points to string object in memory whose value is "323"
print(type(sample_string_variable))  # will give us <class 'string'>
# Also in python every object created in memory is given a unique id to identity it which can shown as follows
print(id(sample_string_variable))  # Object id

# For purposes of optimization, the interpreter creates objects for the integers in the range [-5, 256] at startup, and then reuses them during program execution.
m = 30
n = 30
print(id(m))  # 1405569120
print(id(n))  # 1405569120
# above example using cached value for small integers

# since all variables are essentially named references to the underlying objects in memory, we can use them like
sample_variable_1 = 4
sample_variable_2 = sample_variable_1
print(sample_variable_1)  # 4
print(sample_variable_2)  # 4


# `is` operator is used to check if both operands (In this case variables) point to the same underlying object in memory
# == equality operator is used to check if both operands (In this case variables) hold equal values for their respective underlying object in memory (It doens't check if operands point to same object in memory)

print(sample_variable_1 is sample_variable_2)  # True
print(sample_variable_1 == sample_variable_2)  # True

# But let's see one more example
var_a = [28, 91, 1]
var_b = [28, 91, 1]
print(var_a is var_b)  # False # reference object in memory are different
print(var_a == var_b)  # False # values are equal

#! CaUtIoN: Check below example
sample_variable_2 = sample_variable_2 + 5
print(sample_variable_2)  # 9 # new reference object is created for primitive types
print(sample_variable_1)  # 4 # still pointing to old object

sample_variable_1 = [2, 3, 1]  # reassign to list
sample_variable_2 = sample_variable_1  # add reference to sample_varialable_1
sample_variable_2 += [5]  # add 5 to list, But here reference is still not changed
print(sample_variable_1)  # [2, 3, 1, 5]
print(sample_variable_2)  # [2, 3, 1, 5]
print(sample_variable_1 is sample_variable_2)  # True
print(sample_variable_1 == sample_variable_2)  # True

sample_variable_2 = [
    2,
    3,
    1,
    5,
]  # Point variable2 to different reference object (list in this case) but keep the values same
print(sample_variable_1 is sample_variable_2)  # False
print(sample_variable_1 == sample_variable_2)  # True


# None type is used to denote if a variable name is not pointing to any object in memory. But since in python everything is an object so, even None is an object
sample_none_var = None
print(id(sample_none_var))  # 7123003 # some unique id

#! CaUtIoN: In light of the above example, don't use == to compare with None rather prefer to use is to check both operands point to same object None
print("etc" is None)  # False
print(None is None)  # True


# Python has concepts of scopes for variables where they are used. There is local and global variables
variable_with_same_name = 10


def add_to_global_var(number_to_add):
    global variable_with_same_name  # Now with use of global keyword variable `global_scope_ex_var` points to global scoped variable.
    variable_with_same_name = variable_with_same_name + number_to_add
    return variable_with_same_name


def add_to_local_var(number_to_add):
    variable_with_same_name = 100
    variable_with_same_name = variable_with_same_name + number_to_add
    return variable_with_same_name


print(add_to_local_var(13))  # 113
print(add_to_global_var(13))  # 13
