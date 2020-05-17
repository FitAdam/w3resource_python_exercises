"""21. Write a Python program to find whether a given number (accept from the user) 
is even or odd, print out an appropriate message to the user."""

num = 15
def check_num(num):
    # the % operator returns the remainder of the division
    if num % 2 == 0:
        return 'It is even'
    else:
        return 'It is odd'

print(check_num(num))

#An even number is a number that can be divided into two equal groups.
#  An odd number is a number that cannot be divided into two equal groups.