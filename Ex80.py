"""80. Write a Python program to get the current value of the recursion limit."""

import sys
#Return the current value of the recursion limit, the maximum depth of the Python interpreter stack.
print(sys.getrecursionlimit())