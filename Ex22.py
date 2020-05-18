"""22. Write a Python program to count the number 4 in a given list"""
new_list = [1,2,4,3,4]

def count_4(new_list):
    counter = 0
    for x in new_list:
        if x == 4:
            counter+=1
    return counter

print(count_4(new_list))
