"""36. Write a Python program to add two objects 
if both objects are an integer type."""

def add_only_int(a,b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        raise TypeError("Inputs must be integers")


print(add_only_int('a', 3))
print(add_only_int(2,3))