"""50. Write a Python program to print without newline or space."""


def print_without_space():
    for i in range(0, 10):
        print('*', end="")
    print("\n")

print_without_space()