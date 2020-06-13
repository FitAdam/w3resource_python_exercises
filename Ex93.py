"""93. Write a Python program to get the identity of an object. """

def get_identity(new_obj):
    return print(id(new_obj))


get_identity('x')