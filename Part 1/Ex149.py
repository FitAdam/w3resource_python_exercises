"""149. Write a Python function that takes
 a positive integer and returns the sum of the cube of all the positive 
 integers smaller than the specified number."""

def foo(x):
 newrange = list(range(0,x))
 sum = 0
 cube_range = []

 for element in newrange:
 	cube_range.append(element * element * element)

 for element in cube_range:
 	sum+=element

 return sum

print(foo(8))
