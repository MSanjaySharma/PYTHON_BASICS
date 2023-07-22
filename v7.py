# Iterator protocol

#! Sequence: A sequence is an ordered collection of items that can be indexed and iterated over.
#! Iterables: An iterable is any object that can be looped over or iterated upon, providing a sequence of values one at a time.

"""
| Data Structure | Sequence | Iterable |
| -------------- | -------- | -------- |
| List           | ✔️        | ✔️        |
| Tuple          | ✔️        | ✔️        |
| String         | ✔️        | ✔️        |
| Range          | ✔️        | ✔️        |
| Bytes          | ✔️        | ✔️        |
| Byte Arrays    | ✔️        | ✔️        |
| Array          | ✔️        | ✔️        |
| Deque          | ✔️        | ✔️        |
| Dictionary     |          | ✔️        |
| Set            |          | ✔️        |
| Generator      |          | ✔️        |
| File           |          | ✔️        |
| Enumerations   |          | ✔️        |
|________________|__________|__________|

+------------------------------------------+
| ITERABLES                                |
|        +--------------------------+      |
|        | SEQUENCES                |      |
|        |                          |      |
|        +--------------------------+      |
|                                          |
+------------------------------------------+
"""

from itertools import count

# iterators can be infinitely long
for i in count():
    if i > 10:
        break

# Iterators
#! iterator is an object that implements the iterator protocol, which consists of two methods: __iter__() and __next__(). The __iter__() method returns the iterator object itself, and the __next__() method returns the next element from the sequence. When there are no more elements to return, it raises the StopIteration exception.

my_list = [1, 2, 3]

# my_list is an iterable, but not an iterator
for item in my_list:
    print(item)

# To use an iterator explicitly, you can call iter() on an iterable
my_iter = iter(my_list)

# my_iter is an iterator, we can use the next() function to get elements one by one
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3

# If we try to call next() when there are no more elements, it will raise StopIteration
# print(next(my_iter))  # Raises StopIteration


# for in loop is automatically doing what we were doing manually in below while loop : calling iter to get an iterator and then calling next over and over until a StopIteration exception is raised.


def cloned_for_loop(input_iterable):
    iterator = iter(input_iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            print(item)


cloned_for_loop("zcx")


print("****************************************************************")

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(
    our_iterable
)  # Returns dict_keys(['one', 'two', 'three']). This is an object that implements Python's iterator protocol.

# We can loop over it.
for i in our_iterable:
    print(i)  # Prints one, two, three

# However we cannot address elements by index, since a dict is not a sequence (but is an iterable).
# our_iterable[1]  # Raises a TypeError

# An iterable is an object that knows how to create an iterator.
our_iterator = iter(our_iterable)

# Our iterator is an object that can remember the state as we traverse through it.
# We get the next object with "next()".
next(our_iterator)  # Returns "one"

# It maintains state as we iterate.
next(our_iterator)  # Returns "two"
next(our_iterator)  # Returns "three"

# After the iterator has returned all of its data, it raises a StopIteration exception
# next(our_iterator)  # Raises StopIteration

# We can also loop over it, in fact, "for" does this implicitly!
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)  # Prints one, two, three

# You can grab all the elements of an iterable or iterator by calling list() on it.
list(our_iterable)  # Returns ["one", "two", "three"]
list(our_iterator)  # Returns [] because state is saved


print("****************************************************************")


# build custom iterator
class Count:
    def __init__(
        self,
        start=0,
        end=100,
    ):
        self.__num = start
        self.__end = end

    def __iter__(self):
        return self

    def __next__(self):
        current = self.__num
        self.__num = current + 1

        if self.__num >= self.__end:
            raise StopIteration()
        else:
            return current


for i in Count():
    if i > 3:
        break
    print(i)

print(sum(Count(1, 10)))


print("*********************************************************************")
# Generators
# generator is an iterator whose type is generator. Generator are a way to generate iterators
# GENERATOR FUNCTION -> A function which has yeild keyword instead of return. A generator function is a special syntax that allows us to make a function which returns a generator object when we call it.


def first_n_numbers(n):
    num = 0
    while num < n:
        yield num
        num += 1


numbers_result = first_n_numbers(10)
print(numbers_result)  # <generator object first_n_numbers at 0x1006d4790>
print(type(numbers_result))  # <class 'generator'>
print(next(numbers_result))  # 0
print(next(numbers_result))  # 1


def square_all(numbers):
    for n in numbers:
        yield n**2


squares = square_all([2, 3, 1])
print(type(squares))
print(list(squares))

# GENERATOR EXPRESSIONS -> A generator expression is a comprehension-like syntax that allows you to create a generator object inline.

doubles_generator_expression = (2 * n for n in range(5))


def doubles_generator_function():
    for num in range(5):
        yield num * 2


doubles_generator_function_call = doubles_generator_function() # this function call return generator object
print(doubles_generator_expression)  # <generator object <genexpr> at 0x104f82a80>
print(type(doubles_generator_expression))  # <class 'generator'>
print(doubles_generator_function_call)
# <generator object doubles_generator_function at 0x10521eb50>
print(type(doubles_generator_function_call))  # <class 'generator'>

print(list(doubles_generator_expression))  # [0, 2, 4, 6, 8]
print(list(doubles_generator_function_call))  # [0, 2, 4, 6, 8]
