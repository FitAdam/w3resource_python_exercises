"""109. Write a Python program to check if a number is positive, negative or zero."""

def check_number(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


print(check_number(3))
print(check_number(-3))
print(check_number(0))