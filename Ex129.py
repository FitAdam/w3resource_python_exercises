"""129. Write a Python program to add leading zeroes to a string."""

# The first args takes string, the second the chosen number of 0s.
def display(new_str, x):

    x_str =''
    x_list = list(range(0, x))

    for n in x_list:
        x_str += str(0)

    return (f"{x_str}{new_str}")

print(display('seven',7))
print(display('blalba', 3))
print(display('one', 1))
print(display('one', 0))