# MAGIC METHODS
# These are special methods of class which add additional functionality or modify functionality of classes. They always follow __<magic_methods_name>__() syntax

#! https://rszalski.github.io/magicmethods/ : ALL MAGIC METHODS

# Common magic methods
# 1. Construction and initialization:
"""
It defines the initialization behaviour of object.
var_a = SampleClass()
The above SampleClass() when called __init__ is not the first method that's called though. The first method called is actually __new__()
__new__(), creates the instance, then passes any arguments at creation on to the initializer (__init__())

    1. __new__() is the first method to get called in an object's instantiation. It takes the class, then any other arguments that it will pass along to __init__(). __new__() is used fairly rarely, but it does have its purposes, particularly when subclassing an immutable type like a tuple or a string.
    2. __init__() is the initializer for the class. It gets passed whatever the primary constructor was called with (so, for example, if we called x = SomeClass(10, 'foo')), __init__() would get passed 10 and 'foo' as arguments. __init__() is almost universally used in Python class definitions.
    3. __del__(): If __new__() and __init__() formed the constructor of the object, __del__() is the destructor. It doesn't implement behavior for the statement del x (so that code would not translate to x.__del__()). Rather, it defines behavior for when an object is garbage collected. It can be quite useful for objects that might require extra cleanup upon deletion, like sockets or file objects. Be careful, however, as there is no guarantee that __del__() will be executed if the object is still alive when the interpreter exits, so __del__() can't serve as a replacement for good coding practices (like always closing a connection when you're done with it. In fact, __del__() should almost never be used because of the precarious circumstances under which it is called; use it with caution!
"""


# 2. Comparison Magic Methods:
"""
    1. __cmp__() is the most basic of the comparison magic methods. It actually implements behavior for all of the comparison operators (<, ==, !=, etc.), but it might not do it the way you want (for example, if whether one instance was equal to another were determined by one criterion and and whether an instance is greater than another were determined by something else).
    __cmp__() should return a negative integer if self < other, zero if self == other, and positive if self > other. It's usually best to define each comparison you need rather than define them all at once, but __cmp__() can be a good way to save repetition and improve clarity when you need all comparisons implemented with similar criteria.
    2. __eq__(): Defines behavior for the equality operator, ==.
    3. __ne__(): Defines behavior for the inequality operator, !=.
    4. __lt__(): Defines behavior for the less-than operator, <.
    5. __gt__(): Defines behavior for the greater-than operator, >.
    6. __le__(): Defines behavior for the less-than-or-equal-to operator, <=.
    7. __ge__(): Defines behavior for the greater-than-or-equal-to operator, >=.
"""

# 3. Numeric Magic Methods
# 3.1. Unary Operators and Functions
"""
    __pos__(): Implements behavior for unary positive (e.g. +some_object)
    __neg__(): Implements behavior for negation (e.g. -some_object)
    __abs__(): Implements behavior for the built in abs() function.
"""
# 3.2. Normal Arithmetic Operators
"""
    __add__(): Implements addition.
    __sub__(): Implements subtraction.
    __mul__(): Implements multiplication.
    __floordiv__(): Implements integer division using the // operator.
    __div__(): Implements division using the / operator.
"""


class FunctionalList:
    """A class wrapping a list with some extra functional magic, like head,
    tail, init, last, drop, and take."""

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if key is of invalid type or value, the list values will raise the error
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)
