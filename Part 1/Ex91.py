"""91. Write a Python program to swap two variables."""

def swap(a,b):
    temp = a
    a = b
    b = temp
    return print(f"so now A is {a} and B is {b}!")


swap('a','b')