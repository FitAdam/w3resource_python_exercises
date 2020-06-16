"""115. Write a Python program to compute the product of a list of integers (without using for loop). """
from functools import reduce

sum = lambda x, y : x + y
print(sum(3,4))

lst = [1,2,3,5,6]

sum_of_lst = reduce(lambda x, y: x+y, lst)
print(sum_of_lst)

