# Exceptions
"""
1. An exception is an illegal operation that occurs during the execution of a program.
"""

# Exceptions handling
"""
    1. The code, which harbors the risk of an exception, is embedded within a try block.
    2. Exceptions are caught by an except clause.
    3. raise statements generate exceptions.
"""

while True:
    try:
        input_number = input("Please enter a number:")
        integer_input = int(input_number)
        break
    except ValueError:
        print("Enter a valid integer number")
print("Valid integer is entered")

################################################################
# Multiple exceptions
import sys

try:
    f = open("integers.txt")
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno, strerror))
    # e can be printed directly without using .args:
    # print(e)
except ValueError:
    print("No valid integer in line.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

################################################################
# Handling multiple Errors in single Exceptions:
try:
    f = open("integers.txt")
    s = f.readline()
    i = int(s.strip())
except (IOError, ValueError):
    print("An I/O error or a ValueError occurred")
except:
    print("An unexpected error occurred")
    raise

################################################################
# handling errors in functions
value_error_message = "got it :-) "
final_print_message = "Let's get on"
value_error_in_function_message = "got it in the function :-) "


def f():
    x = int("thirteen")
    return x


try:
    f()
except ValueError as e:
    print(value_error_message, e)

print(final_print_message)

#!#####*********#########*******#######*********#######********


def f2():
    try:
        x = int("thirteen")
        return x
    except ValueError as e:
        print(value_error_in_function_message, e)


try:
    f2()
except ValueError as e:
    print(value_error_message, e)

print(final_print_message)

#!#####*********#########*******#######*********#######********


def f():
    try:
        x = int("thirteen")
        return x
    except ValueError as e:
        print(value_error_in_function_message, e)
        raise


try:
    f()
except ValueError as e:
    print(value_error_message, e)

print(final_print_message)


# Custom Exceptions
# raise SyntaxError("THIS IS CUSTOM EXCEPTION")


# The Pythonic way to do this is to define an exception class which inherits from the Exception class:
class MyException(Exception):
    pass


# try catch finally
try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity")
finally:
    # loader is false
    print("There may or may not have been an exception.")


################################################################
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass  # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass  # Multiple exceptions can be handled together, if required.
else:  # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")  # Runs only if the code in try raises no exceptions
finally:  # Execute under all circumstances
    print("We can clean up resources here")


# with Statement: Instead of try/finally to cleanup resources, you can use simply use a with context-manager:
with open("myfile.txt") as f:
    for line in f:
        print(line)


# Handling Nested Exceptions
def plan_a(input_number):
    print("plan_a")
    try:
        int(input_number)
    except ValueError:
        raise ValueError("Invalid integer number")


def plan_b(input_number):
    print("plan_b")
    try:
        float(input_number)
    except ValueError:
        raise ValueError("Invalid float number")


try:
    input_number = input("Input the number: ")
    plan_a(input_number)
except ValueError as e:
    try:
        input_number = input("Input the number again: ")
        plan_b(input_number)
    except ValueError as e:
        print(e)

"""
Exception 	Cause of Error
AssertionError 	Raised when an assert statement fails.
AttributeError 	Raised when attribute assignment or reference fails.
EOFError 	Raised when input() hits end-of-file condition.
FloatingPointError 	Raised when a floating point operation fails.
GeneratorExit 	Raise when a generator's close() method is called.
ImportError 	Raised when the imported module is not found.
IndexError 	Raised when the index of a sequence is out of range.
KeyError 	Raised when a key is not found in a dictionary.
KeyboardInterrupt 	Raised when the user hits the interrupt key (Ctrl+C or Delete).
MemoryError 	Raised when an operation runs out of memory.
NameError 	Raised when a variable is not found in local or global scope.
NotImplementedError 	Raised by abstract methods.
OSError 	Raised when system operation causes system related error.
OverflowError 	Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError 	Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError 	Raised when an error does not fall under any other category.
StopIteration 	Raised by next() to indicate that there is no further item to be returned by the iterator.
SyntaxError 	Raised by parser when syntax error is encountered.
IndentationError 	Raised when there is incorrect indentation.
TabError 	Raised when indentation consists of inconsistent tabs and spaces.
SystemError 	Raised when interpreter detects an internal error.
SystemExit 	Raised by sys.exit() function.
TypeError 	Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError 	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeDecodeError 	Raised when a Unicode-related error occurs during decoding.
ValueError 	Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError 	Raised when the second operand of division or modulo operation is zero.
"""
