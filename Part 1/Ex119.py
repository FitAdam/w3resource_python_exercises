"""119. Write a Python program to display a floating number in specified numbers."""

def display(f_num):
    if type(f_num) == float:
        print(round(f_num))
    else:
        print(f_num)

display(2342)

display(9.99992329)