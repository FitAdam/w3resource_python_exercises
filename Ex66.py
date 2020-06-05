"""66. Write a Python program to calculate body mass index."""

def calculate_bmi(weight, heigth):
    bmi = weight / heigth
    return bmi


print(calculate_bmi(199,98))