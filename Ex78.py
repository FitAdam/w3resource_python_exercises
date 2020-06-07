"""78. Write a Python program to find the available built-in modules."""

import sys

info = sys.builtin_module_names

for x in info:
    print(x)
