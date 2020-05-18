"""28. Write a Python program to print all even numbers from a given numbers
 list in the same order and stop the printing if any numbers that come after 237 in the sequence."""

new_list = []


def foo():
    n = int(input("give some numbers: "))
    new_list.append(n)
    print(f"this is new list: {new_list}")
    even_list = []
    for x in new_list:
        if x % 2 == 0:
            even_list += x
        else:
            pass
    return print(even_list)

while True:
    foo()