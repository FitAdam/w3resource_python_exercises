"""126. Write a Python program to get the actual module object
 for a given object."""
import random
from inspect import getmodule

print(getmodule(random))