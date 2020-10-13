"""5. Write a Python program to create the combinations of 3 digit combo. """

def combo(lst):
    return lst


print(combo([12,33,51]))


def combo2():
    numbers = []
    for num in range(1000):
        num=str(num).zfill(3)
        print(num)
    numbers.append(num)


combo2()


"""
The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

If the value of the len parameter is less than the length of the string, no filling is done.

Syntax
string.zfill(len)
"""