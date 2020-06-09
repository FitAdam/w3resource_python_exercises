"""87. Write a Python program to get the size of a file."""

import sys

path = r"Ex79.py"

def see_the_size(x):
    y = sys.getsizeof(x)
    # Return the size of an object in bytes.
    return y


print(f"The size of file '{path}' is {see_the_size(path)} bytes.")