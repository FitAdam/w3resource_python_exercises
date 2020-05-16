"""15. Write a Python program to get the volume of a sphere
 with radius 6.
"""
import math

pi = math.pi

def get_volume(r=6):
    return 4/3 * pi * r **3

print(get_volume())