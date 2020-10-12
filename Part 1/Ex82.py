"""82. Write a Python program to calculate 
the sum over a container."""


def calculate(some_list):
    new_sum = sum(some_list)
    return new_sum


new_list = [2,3,4,231]

print(calculate(new_list))