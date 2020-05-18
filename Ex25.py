"""25. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"""

def check_value(n,list):
    if n in list:
        return True
    else:
        return False

print(check_value(2,[1,4,3,4,5]))

