"""72. Write a Python program to get the details of math module."""
import math

info = math.__doc__
math_ls = dir(math)
print(info)
print(math_ls)