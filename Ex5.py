""" 5. Write a Python program which accepts the user's first 
and last name and
print them in reverse order with a space between them."""

def reverse_order():
    name_surname = input("What's your name and surname? ")
    a = name_surname.split()
    a = a[1] + ' ' + a[0]
    return print(a)

reverse_order()