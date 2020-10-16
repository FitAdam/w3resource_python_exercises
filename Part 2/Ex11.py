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

def subsetsum(array, num):
    
    if sum(array) == num:
        return array
    if len(array) > 1:
        for subset in (array[:-1], array[1:]):
            result = subsetsum(subset, num)
            if result is not None:
                return result


print(subsetsum([10, 30, 30], 70))

