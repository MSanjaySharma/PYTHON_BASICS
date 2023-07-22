# Control statements
test_integer = 10
if test_integer == 0:
    print("Zero")
elif test_integer < 0:
    print("Less")
elif test_integer > 0:
    print("More")
else:
    print("None")

# Conditional expression (?:) equivalent
print("True") if test_integer == 0 else print("False")

print("****************************************************************")


# for loop
alphabet_list = []
for alphabet in ["a", "b", "c", "d", "e", "f"]:
    alphabet_list += [alphabet]
print(alphabet_list)

# ? Range function: syntax: range(start, stop, skip) stop in non-inclusive
numbers = []
for number in range(0, 11):
    numbers += [number]
print(numbers)

numbers = []
for number in range(11):
    numbers += [number]
print(numbers)

numbers = []
for number in range(0, 11, 2):
    numbers += [number]
print(numbers)


# ? else clause for for loop
numbers = []
for number in range(5):
    numbers += [number]
else:
    print(numbers)

print("****************************************************************")

# While loop
x = 10
numbers = []
while x > 0:
    numbers.append(x)
    x -= 1
print(numbers)


print("****************************************************************")

# lambda functions: Anonymous functions equivalent
#! lambda <args>: <return>
numbers = [1, 2, 3, 4, 5]
print((lambda a, b: a + b)(4, 5))
doubled_numbers = map((lambda num: num**2), numbers)
print(list(doubled_numbers))
