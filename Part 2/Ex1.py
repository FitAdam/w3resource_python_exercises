"""
1. Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
"""

def foo(lst):
    """determines if all the numbers are different from each other"""
    if len(lst) == len(set(lst)):
        return 'unique'
    else:
        return 'some numbers are the same.'

print(foo([1,2,3,9]))