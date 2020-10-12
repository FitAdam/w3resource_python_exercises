"""83. Write a Python program to test whether all numbers
 of a list is greater than a certain number."""

# check if all numbers in the list are greater 
def test(test_list, num):
    if num in test_list:
        return 'Some numbers are smaller or equal'
    else:
        for x in test_list:
            if x < num:
                return 'Some numbers are smaller'
    return 'All numbers in the list are greater!'


print(test([7,8,9],6))