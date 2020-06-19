"""121. Write a Python program to determine whether variable is defined or not. """

try:
    x
except NameError:
    print('variable not defined')
else:
    print('variable is defined')


