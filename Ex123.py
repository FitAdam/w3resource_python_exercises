"""123. Write a Python program to determine the largest and smallest integers, longs, floats."""
import sys

def determine(x):
    a = type(x)
    if a == int:
        return sys.int_info
    elif a == float:
        return sys.float_info
    else:
        return 'wrong input'


print(determine(3099999.99999999999999999999999999999999999999999999999999999999))



