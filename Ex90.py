"""90. Write a Python program to create a copy of its own source code."""

def foo():
    print(open(__file__).read())

foo()