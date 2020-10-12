"""27. Write a Python program to concatenate all elements in a list into a string and return it."""

new_list = []

def foo():
    n = str(input("give some elements: "))
    new_list.append(n)
    a = ""
    new_string = a.join(new_list)
    return print(new_string)

while True:
    foo()


