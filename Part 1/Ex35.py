"""35. Write a Python program that will return true 
if the two given integer 
values are equal or their sum or difference is 5. """

def foo(a,b):
    if (a + b) == 5 or abs(a - b) == 5 or (b - a) == 5:
        return True
    elif a == b:
        return True
    else:
        return False

print(foo(7,2))
print(foo(3,2))
print(foo(2,2))