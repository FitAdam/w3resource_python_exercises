"""60. Write a Python program to calculate the hypotenuse of a right angled triangle."""
import math

def the_hypotenuse(a, b):
    #the Pythagorean Theorem
    c = (a ** 2) + (b ** 2)
    return math.sqrt(c)


print(the_hypotenuse(3,4))




