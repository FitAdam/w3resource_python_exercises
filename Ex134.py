"""134. Write a Python program to input two integers in a single line."""


def double_input():
    x, y = map(int, input('Type two intgers: ').split())
    print(x,y)

double_input()