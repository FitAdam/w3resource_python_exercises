"""89. Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal."""


def foo(x):
    if x == 1:
        return print("First day of a Month!")
    else:
        pass

foo(1)
foo(2)