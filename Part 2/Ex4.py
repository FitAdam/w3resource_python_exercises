"""4. Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers."""
import random
from random import choice

def find_triplets(arr):
    """three numbers from array that gives a 0 after sum"""
    x = arr[0]
    y = arr[1]
    z = arr[2]
    arr_len = (len(arr))-1 
    while x + y + z != 0:
        x_indx = random.randint(0, arr_len)
        x = arr[x_indx]
        y_indx = choice([i for i in range(0,9) if i not in [x_indx]])
        y = arr[y_indx]
        z_indx = choice([i for i in range(0,9) if i not in [x_indx, y_indx]])
        z = arr[z_indx]
    elements = (x, y , z)
    return elements







x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]

#[(-6, 2, 4)]

print(find_triplets(x))