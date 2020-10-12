"""69. Write a Python program to sort three integers 
without using conditional statements and loops."""

def sort(a,b,c):
    lst = [a,b,c]
    lst.sort()
    return lst
    
print(sort(3,4,1))