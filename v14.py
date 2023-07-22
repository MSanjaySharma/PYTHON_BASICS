# Some built-in methods

#! 1. any/all: Takes iterable as input
"""
 	                                        any 	all
All True values 	                        True 	True
All False values 	                        False 	False
One True value (all others are False) 	    True 	False
One False value (all others are True) 	    True 	False
Empty Iterable 	                            False 	True
"""
print(any([]), all([]))  # Returns (False, True)
print(
    any([0, 0.0, False, (), "0"]), all([1, 0.0001, True, (False,)])
)  # Returns (True, True)


#! 2. dir()
a = list()  # same as initializing with []

# dir() will return all the attributes of the "arr" list object
print(
    dir(a)
)  # Returns ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', ...]


#! 3. filter()
def filter_vowels(variable):
    letters = ["a", "e", "i", "o", "u"]
    if variable in letters:
        return True
    else:
        return False


sequence = ["g", "e", "e", "j", "k", "s", "p", "r"]

list(filter(filter_vowels, sequence))  # Returns ['e', 'e']


#! 4. iter(): Calls classes __iter__()
vowels = ["a", "e", "i", "o", "u"]
vowels_iter = iter(vowels)

print(next(vowels_iter))  # Returns 'a'
print(next(vowels_iter))  # Returns 'e'
print(next(vowels_iter))  # Returns 'i'
print(next(vowels_iter))  # Returns 'o'
print(next(vowels_iter))  # Returns 'u'

#! 5. len(): Calls classes __len__()
testList = []
print(len(testList))  # Returns 0

testList = [1, 2, 3]
print(len(testList))  # Returns 3

testTuple = (1, 2, 3)
print(len(testList))  # Returns 3

testRange = range(1, 10)
print(len(testList))  # Returns 9

#! 6. range(start, stop, step)
list(range(3, 10, 2))  # Returns [3, 5, 7, 9]

list(range(10, -5, -3))  # Returns [10, 7, 4, 1, -2]

list(range(10, -5, 3))  # Returns []

# list(range(3, 7, 0))  # Returns ValueError: range() arg 3 must not be zero


#! 7. reverse(iterable)
# A list of numbers
L1 = [1, 2, 3, 4, 1, 2, 6]
L1.reverse()
print(L1)  # Prints [6, 2, 1, 4, 3, 2, 1]

# A list of characters
L2 = ["a", "b", "c", "d", "a", "a"]
L2.reverse()
print(L2)  # Prints ['a', 'a', 'd', 'c', 'b', 'a']

#! 8. sorted(iterable, key=lambda x: x | some key, reverse=True | False)
print(
    sorted("This is a test string".split(), key=str.lower)
)  # Returns ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']


# take the second element for sort
def take_second(elem):
    return elem[1]


# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sorted_list = sorted(random, key=take_second)

# print the list
print("Sorted list:", sorted_list)
