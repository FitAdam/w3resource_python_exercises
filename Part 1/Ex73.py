"""73. Write a Python program to calculate midpoints of a line. """

def calculate_midpoint(a,b,c,d):
    m1 = (a + c)/2
    m2 = (b + d)/2
    return print(f"The midpoint is ({m1}, {m2}).")


calculate_midpoint(-3,5,8,-1)
calculate_midpoint(2,2,4,4)