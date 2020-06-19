"""122. Write a Python program to empty
 a variable without destroying it."""

a = 'a'
b = 77
colors = ['blue', 'red', 'yellow', 'black']

def empty(x):
    return(type(x)())


print(empty(a))
print(empty(b))
