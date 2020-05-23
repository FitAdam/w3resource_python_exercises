"""Write a Python program to compute 
the distance between the points (x1, y1) and (x2, y2)."""

import math

def distance(x1,y1,x2,y2):
    x3 = (x1) - (x2)
    y3 = (y1) - (y2)
    return print(f"x3 is {abs(x3)}\ny3 is {abs(y3)}")


distance(-3,-3,3,3)

def distance_formula(x1,y1,x2,y2):
    d = ((x2-x1)**2) + ((y2-y1)**2)
    return print(f"The distance is {math.sqrt(d)}")
    
distance_formula(-3,-3,3,3)
