"""34. Write a Python program to sum of two given integers. 
However, if the sum is between 15 to 20 it will return 20."""

def sum(a,b):
    if (a + b) in range(15,21):
        return 20
    else:
        return a + b
    
print(sum(10, 6))
print(sum(10, 2))
print(sum(10,12))