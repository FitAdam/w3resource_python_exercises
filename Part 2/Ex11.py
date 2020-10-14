"""11. Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. 
Print all those three-element combinations. 
Sample data:
/*
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70
*/

"""

def sum_of_three(arr):
    for x in arr:
        if x + x[+1]