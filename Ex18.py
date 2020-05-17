"""18. Write a Python program to calculate the sum of three
 given numbers, 
if the values are equal then return three times of their sum."""

def calculate(x,y,z):
    if x == y == z:
        return 3*(x+y+z)
    else:
        return x+y+z

print(calculate(3,3,3))