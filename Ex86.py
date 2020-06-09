"""86. Write a Python program to get the ASCII value of a character."""

def get_ASCII(x):
    c = x
    return "The ASCII value of '" + c + "' is", ord(c)

def get_character():
    num = int(input("Enter ASCII value: "))
    return chr(num)

print(get_ASCII('p'))
print(get_ASCII('q'))
print(get_ASCII('2'))

print(get_character())