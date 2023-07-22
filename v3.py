# BASIC DATA TYPES:
# Interger
x = 3
print(x)  # Prints "3"
print(type(x))  # Prints "<class 'int'>"
print(x + 1)  # Addition; returns "4"
print(x - 1)  # Subtraction; returns "2"
print(x * 2)  # Multiplication; returns "6"
print(x**2)  # Exponentiation; returns "9"
x += 1  # Returns "4"
print(x)
x *= 2  # Returns "8"
print(x)
print(x % 4)  # Modulo operation; returns "0"


print("****************************************************************")

# Float
y = 2.5
print(type(y))  # Returns "<class 'float'>"
print((y, y + 1, y * 2, y**2))  # Returns "(2.5, 3.5, 5.0, 6.25)"

#! CaUtIoN: Interger/float division nuances
print(3 / 2)  # Float division Py3 returns 1.5;
print(3 // 2)  # Integer division returns 1; Floor math function is used
# Floor function returns::: largest integer less than or equal to x
print(10.0 / 3)  # Float division returns 3.33..

# Integer division rounds down for both positive and negative numbers
print(-5 // 3)  # -2
print(5.0 // 3.0)  # 1.0
print(-5.0 // 3.0)  # -2.0


#! CaUtIoN: Python doesn't have unary increment (++) and unary decrement (--) operator. It supports += and -= operators

print("****************************************************************")

# Boolean
t = True
f = False
print(type(t))  # Returns "<class 'bool'>"
print(t and f)  # Logical AND; returns False
print(t or f)  # Logical OR; returns True
print(not t)  # Logical NOT; returns False
print(t != f)  # Logical XOR; returns True
print(t == f)  # comparisons returns False

# true evalutates to 1 and false to 0
print(True + True)  # Returns 2
print(True * 8)  # Returns 8
print(False - 5)  # Returns -5

# comparision operator look at numerical values to compare
print(0 == False)  # Returns True
print(1 == True)  # Returns True 1
print(2 == True)  # Returns False # 2 == 1
print(-5 != False)  # Returns True # -5 != 0

#! PyThoNiNteRnAlS: How comparision works in python
print(10 == 10.0)  # True
# The above comparison transaltes to:
# 1. First try left operands __eq__ method if NotImplemented comes as output
# 2. Then try with right operands __eq__ method
print((10).__eq__(10.0))  # NotImplemented
print((10.0).__eq__(10))  # True

#! CaUtIoN: None, 0, and empty strings/lists/dicts/tuples all evaluate to False. All other values are True.
print(bool(0))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool({}))  # False
print(bool(()))  # False

# ? Py3 comparison operators
# Equality is ==
print(1 == 1)  # Returns True
print(2 == 1)  # Returns False

# Inequality is !=
print(1 != 1)  # Returns False
print(2 != 1)  # Returns True

# More comparisons
print(1 < 10)  # Returns True
print(1 > 10)  # Returns False
print(2 <= 2)  # Returns True
print(2 >= 2)  # Returns True

# Seeing whether a value is in a range
print(1 < 2 and 2 < 3)  # Returns True
print(2 < 3 and 3 < 2)  # Returns False

# Chaining makes the above look nicer
print(1 < 2 < 3)  # Returns True
print(2 < 3 < 2)  # Returns False

# ? typecasting to boolean
print(bool(0))  # Returns False
print(bool(4))  # Returns True
print(bool(-6))  # Returns True

# ? Logical operators and short circuits
# shortcircuit AND: return first FALSY value or last operand
# shortcircuit OR: return first TRUTHY value or last operand
print(0 and 2)  # Returns 0
print(0 or -5)  # Returns -5


print("****************************************************************")

# Strings
hello = "hello"  # String literals can use single quotes
world = "world"  # or double quotes; it does not matter.
# But note that you can nest one in another, for e.g., 'a"x"b' and "a'x'b"
print(hello)  # Prints "hello"
print(len(hello))  # String length; returns "5"
print(hello[0])  # A string can be treated like a list of characters, returns 'h'
print(hello + " " + world)  # String concatenation using '+', returns "hello world"

# ? String object methods
s = "hello"
print(s.capitalize())  # Capitalize a string; returns "Hello"
print(s.upper())  # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))  # Right-justify a string, padding with spaces; returns "  hello"
print(s.center(7))  # Center a string, padding with spaces; returns " hello "
print(s.replace("l", "(ell)"))  # Replace all instances of one substring with another;
# returns "he(ell)(ell)o"
print("  world ".strip())  # Strip leading and trailing whitespace; returns "world"

# ? F-strings (FormattedStrings)
city = "Sochi"
print(f"City name is {city}.")  # Returns "City name is Sochi."

# ? Index of a Substring in a Python String
sentence = "Today is Saturaday"  # find() returns the index of the first occurrence of the substring if found and -1 otherwise.
print(sentence.find("day"))  # Returns 2
print(sentence.find("nice"))  # Returns -1

#! CaUtIoN: why len(string) but string.capitalize()? why the inconsistency in methods
"""
1. len() is a built-in function, while capitalize() is a method specific to string objects
2. The len() function is defined as a built-in function in Python's standard library. It is not part of any specific class like the string class. When you call len() with an object as an argument, it internally calls the __len__() method of that object to determine its length.
3. capitalize() is a method specific to string objects in Python. We're calling the capitalize() method on a string object (string). To call a method on an object, you use the dot notation (object.method())
"""


# ? Regular expression and strings
import re

text = "Today is 3/7/2021"
match_pattern = r"(\d+)/(\d+)/(\d+)"

print(re.sub(match_pattern, "Sunday", text))  # Returns 'Today is Sunday'
print(re.sub(match_pattern, r"\3-\1-\2", text))  # Returns 'Today is 2021-3-7'
