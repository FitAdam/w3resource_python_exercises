"""16. Write a Python program to get the difference between 
a given number and 17, if the number is greater 
than 17 return double the absolute difference."""

def getValue(n):
    y = 17
    if n <= y:
        return abs(n-y)
    else:
        return 2 * abs(n-y)

print(getValue(14))
