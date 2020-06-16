"""114. Write a Python program to filter the positive numbers from a list."""


test = [2, 3, 2, 3,2,3,2,-1,23,-2,-3]
nums = [34, 1, 0, -23]

def filter(lst):
    new_lst = []
    for x in lst:
        if x > 0:
            new_lst.append(x)
    return new_lst

print(filter(test))
print(filter(nums))
