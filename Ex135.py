"""135. Write a Python program to print a variable without spaces between values."""


def print_out(a,b):
    new_str = ''
    new_str+=str(a)
    new_str+=str(b)
    return new_str

print(print_out(6,7))