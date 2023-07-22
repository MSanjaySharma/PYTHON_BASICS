# Containers
# Containers are data types which can hold arbitrary number of other data types.
# Pythons builtin container data types: list, dictionary, tuple, set

from typing import Container

print(isinstance(list(), Container))  # True
print(isinstance(tuple(), Container))  # True
print(isinstance(dict(), Container))  # True
print(isinstance(set(), Container))  # True

print("****************************************************************")


# List
# Py list is equivalent to the array in other languages

l = [3, 1, 2]  # Create a list
print(l[0])  # Access a list like you would any array; returns "1"
# print(l[4])  # Looking out-of-bounds is an IndexError; Raises an "IndexError"
print(l[::-1])  # Return list in reverse order "[2, 1, 3]"
print((l, l[2]))  # Returns "([3, 1, 2] 2)"
print(l[-1])  # Negative indices count from the end of the list; prints "2"

l[2] = "foo"  # Lists can contain elements of different types
print(l)  # Prints "[3, 1, 'foo']"

l.append("bar")  # Add a new element to the end of the list
print(l)  # Prints "[3, 1, 'foo', 'bar']"
x = l.pop()  # Remove and return the last element of the list
print((x, l))  # Prints "bar [3, 1, 'foo']"

#! CautIoN: Usage of array slicing format: SYNTAX: [start, end, skip]
#! CaUtIoN: in the above syntax end is exclusive (not including end)
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:7])  # [2, 3, 4, 5, 6]
print(my_list[1::2])  # [1, 3, 5, 7, 9]
print(my_list[:6:3])  # [0, 3]
print(my_list[::4])  # [0, 4, 8]
print(my_list[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# ? Lists be “unpacked” into variables:
a, b, c = [1, 2, 3]  # a is now 1, b is now 2 and c is now 3
# You can also do extended unpacking
a, *b, c = [1, 2, 3, 4]  # a is now 1, b is now [2, 3] and c is now 4
# Now look how easy it is to swap two values
b, a = a, b  # a is now [2, 3] and b is now 1

# ? iterate over a list #for in loop to be used
pokemons = ["pikachu", "palkia", "ditto"]
for pokemon in pokemons:
    print(pokemon)

# enumerate returns an iterator which can be used with next() operator
print(enumerate(pokemons))  # <enumerate object at 0x1028c1f80>
print(enumerate(pokemons).__next__())  # (0, 'pikachu')
# to access the inde while iterating over the list
for index, pokemon in enumerate(pokemons):
    print(f"{pokemon} is at position {index}")


#! CaUtIoN: List comprehension is a way to build a list from iterables(list itelself being a iterator)
#! syntax: [<element_for_new_list> for <__next__()> in <iterator> if <condition>]
# Creating a list where elements are squared of existing tuple
existing_tuple = (1, 2, 3, 4, 5)
new_list_from_comprehension = [number**2 for number in existing_tuple]
print(new_list_from_comprehension)

# from existing tuple only square those elements which are even and ignore odd elements
new_list_from_comprehension = [
    number**2 for number in existing_tuple if number % 2 == 0
]
print(new_list_from_comprehension)

# nested list comprehension example
matrix = [[2, 7, 1], [4, 5, 3], [6, 8, 0]]
flattened_matrix = []
for row in matrix:
    for n in row:
        flattened_matrix.append(n)

print(flattened_matrix)

#! CaUtIoN: syntax new_list = [expression for outer_loop_variable in outer_loop_iterable for inner_loop_variable in inner_loop_iterable]
print([target_element for row in matrix for target_element in row])

# ? List functions
l = [1, 2, 3]

l_copy = l[:]  # Make a one layer deep copy of l into l_copy
# Note that "l_copy is l" will result in False after this operation.
# This is similar to using the "copy()" method, i.e., l_copy = l.copy()

del l_copy[2]  # Remove arbitrary elements from a list with "del"; l_copy is now [1, 2]

l.remove(3)  # Remove first occurrence of a value; l is now [1, 2]
# l.remove(2)    # Raises a ValueError as 2 is not in the list

l.insert(2, 3)  # Insert an element at a specific index; l is now [1, 2, 3].
# Note that l.insert(n, 3) would return the same output, where n >= len(l),
# for example, l.insert(3, 3).

l.index(3)  # Get the index of the first item found matching the argument; returns 3
# l.index(4)     # Raises a ValueError as 4 is not in the list

l_copy += [3]  # This is similar to using the "extend()" method

print(l + l_copy)  # Concatenate two lists; returns [1, 2, 3, 1, 2, 3]
# Again, this is similar to using the "extend()" method; with the only
# difference being that "list.extend()" carries out the operation in place,
# while '+' creates a new list object (and doesn't modify "l" and "l_copy").

l.append(
    l_copy
)  # You can append lists using the "append()" method; returns [1, 2, 3, [1, 2, 3]]

1 in l  # Check for existence (also called "membership check") in a list with "in"; returns True

len(l)  # Examine the length with "len()"; returns 4

#! CaUtIoN: List concatenation using .extend() can be achieved using the in-place addition operator, +=
# Extending a list with another iterable (in this case, a list)
l = [1, 2, 3]
l += [4, 5, 6]  # Returns "[1, 2, 3, 4, 5, 6]"
# Note that l += 4, 5, 6 works as well since the source argument on the right is already an iterable (in this case, a tuple)

l += [[7, 8, 9]]  # Returns "[1, 2, 3, 4, 5, 6, [7, 8, 9]]"
l += (
    10,
    11,
    12,
    [10, 11, 12],
)  # [1, 2, 3, 4, 5, 6, [7, 8, 9], 10, 11, 12, [10, 11, 12]]

# For slicing use-cases
l[1:] = [10]  # Returns "[1, 10]"


print("****************************************************************")

# Dictionary
# dictionaries store mappings from keys to values. A dictionary stores (key, value) pairs
d = {"one": 1, "two": 2, "three": 3}  # Create a new dictionary with some data
d["one"]  # Lookup values in the dictionary using "[]"; returns "1"
"two" in d  # Check if a dictionary has a given key; returns "True"
d["four"] = 4  # Set an entry in a dictionary
d["four"]  # Returns "4"
# d["five"] # Raise "KeyError"
d.get("four")  # Returns "4"
d.get("five")  # Returns None
d.get("five", "This key doesn't exist")  # Returns "This key doesn't exist"
print("four" in d)


# default dictionary
from collections import defaultdict

# create an empty defaultdict with default value equal to []
# default_list_d = defaultdict(list()) # raises error: first argument must be callable or None
default_list_d = defaultdict(list)
default_list_d["a"] = 1  # default_list_d is now {"a": [1]}

# create a defaultdict with default value equal to 0
default_int_d = defaultdict(int)
default_int_d["c"] = 3  # default_int_d is now {"c": 1}
print(default_int_d["t"])  # 0

# key membership check
d = {"one": 1, "two": 2, "three": 3}  # Create a new dictionary with some data
doesOneExist = "one" in d  # Return True

# iterating over keys of dict
d = {"a": 0, "b": 5, "c": 6, "d": 7, "e": 11, "f": 19}
# iterate over each key in d
for key in d:
    print(d[key])  # This is OK
    # del d[key]  # Raises a "RuntimeError: dictionary changed size during iteration"
    # d[1] = 0  # Raises a "RuntimeError: dictionary changed size during iteration"

# del keyword to delete the items
d = {"one": 1, "two": 2, "three": 3}  # Create a new dictionary with some data
del d["one"]  # Delete key "numbers" of d
d.get("four", "N/A")  # "four" is no longer a key; returns "N/A"

#! CaUtIoN: Key Datatypes: keys for dictionaries have to be immutable datatypes, such as ints, floats, strings, tuples, etc., This will help in hashing
# invalid_dict = {[1, 2, 3]: "123"}  # Raises a "TypeError: unhashable type: 'list'"
valid_dict = {(1, 2, 3): [1, 2, 3]}  # Values can be of any type, however.

filled_dict = {"one": 1, "two": 2, "three": 3}
# insertion order is guranteed on .key() & .values() functions only Py3.7+
list(filled_dict.keys())  # Can returns ["three", "two", "one"] in Python <3.7
list(filled_dict.keys())  # ["one", "two", "three"] in Python 3.7+
list(filled_dict.values())  # Returns [3, 2, 1] in Python <3.7
list(filled_dict.values())  # [1, 2, 3] in Python 3.7+ (insertion order guranteed)

# iterating on dictionary
for key, value in filled_dict.items():
    print(f"{key}:{value}")


#! Dictionary comprehension SYNTAX { <key>:<value> for <__next__ value> in <iterable> if <condition>}
flipped_filled_dict = {value: key for key, value in filled_dict.items()}
# key is int and value is it's power of two & only if even
sample_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
power_of_two = {element: element**2 for element in sample_tuple if element % 2 == 0}
print(power_of_two)

print("****************************************************************")

# Sets
# A set is an unordered collection of distinct elements
# elements of a set have to be immutable
animals = {"cat", "dog"}  # Note the syntax similarity to a dict.
"cat" in animals  # Check if an element is in a set; prints "True"
"fish" in animals  # Returns "False"
animals.add("fish")  # Add an element to a set
"fish" in animals  # Returns "True"
len(animals)  # Number of elements in a set; returns "3"
animals.add("cat")  # Adding an element that is already in the set does nothing
len(animals)  # Returns "3"
animals.remove("cat")  # Remove an element from a set
len(animals)  # Returns "2"
print(animals)  # Returns "{'fish', 'dog'}"


# ? set operations
# Do set intersection with &
filled_set = {
    1,
    2,
    3,
    4,
    5,
}
other_set = {3, 4, 5, 6}
print(filled_set & other_set)  # Returns {3, 4, 5} # Intersection

# Do set union with |
print(filled_set | other_set)  # Returns {1, 2, 3, 4, 5, 6} # Union

# Do set difference with -
print({1, 2, 3, 4} - {2, 3, 5})  # Returns {1, 4} # elements in A but not in B

# Do set symmetric difference with ^
print({1, 2, 3, 4} ^ {2, 3, 5})  # Returns {1, 4, 5} # non common elements in A and B

# Check if set on the left is a superset of set on the right
print({1, 2} >= {1, 2, 3})  # Returns False # B is a superset of A

# Check if set on the left is a subset of set on the right
print({1, 2} <= {1, 2, 3})  # Returns True # If A is a subset of B

# ? Iterating Over a Set
pokemons = {"pikachu", "palkia", "ditto"}
# to access the index while iterating over the list
for index, pokemon in enumerate(pokemons):
    print(f"{pokemon} is at position {index}")

# ? Set Comprehensions
set_comprehension = {x for x in "abcddeef" if x not in "abc"}
print(set_comprehension)  # Returns {'d', 'e', 'f'}


print("****************************************************************")

# Tuple
# A tuple is an immutable ordered list of values
t = (1, 2, 3)
t[0]  # Returns 1
# t[0] = 3  # Raises a "TypeError: 'tuple' object does not support item assignment"
print(type((1)))  # Returns <class 'int'>
print(type((1,)))  # Returns <class 'tuple'>
print(type(()))  # Returns <class 'tuple'>

# ? A tuple is in many ways similar to a list; one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot:
tup = (1, 2, 3, 4, 5)
print(len(tup))  # Returns 3
print(tup + (4, 5, 6))  # Returns (1, 2, 3, 4, 5, 6)
print(tup[:2])  # Returns (1, 2)
print(2 in tup)  # Returns True

# ? unpack tuples into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6  # Tuple 4, 5, 6 is unpacked into variables d, e and f
# respectively such that d = 4, e = 5 and f = 6
# Now look how easy it is to swap two values
e, d = d, e  # d is now 5 and e is now 4

# ?
a = (1, 2, 3)  # Max addressable index: 2
print(a[:3:])  # Does NOT return an error, instead returns (1, 2, 3)
