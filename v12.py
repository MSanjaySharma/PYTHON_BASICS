# Modules

# importing modules
import math

print(math.sqrt(16))  # Returns 4.0

#!#######*********@@@@@@@@################************
# get specific functions from a module:
from math import ceil, floor

print(ceil(3.7))  # Returns 4.0
print(floor(3.7))  # Returns 3.0

#!#######*********@@@@@@@@################************
# shorten module names:
import math as m

print(math.sqrt(16) == m.sqrt(16))  # Returns True

#!#######*********@@@@@@@@################************
# find out which functions and attributes are defined in a module using dir
print(dir(math))
