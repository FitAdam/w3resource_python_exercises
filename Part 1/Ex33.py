"""33. Write a Python program to sum of three given integers. 
However, if two values are equal sum will be zero."""

def foo(a,b,c):
    if a == b or a == c or b == c:
        return 0
    else:
        return a + b + c

print(foo(3,3,3))
print(foo(0,3,3))
print(foo(3,0,3))
print(foo(3,3,0))
print(foo(1,2,3))