"""125. Write a Python program to sum of all counts in a collections?"""

numbers = [2, 2, 5, 1, 3, 8, 9, 0]
numbers_2 = [3, 3]

def calculate_sum(new_list):
    sum = 0
    for x in new_list:
        sum += x
    return sum

       

print(calculate_sum(numbers))
print(calculate_sum(numbers_2))