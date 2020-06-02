"""59. Write a Python program to convert height (in feet and inches) to centimeters."""

# Feet to cm = multiply the length value by 30.48
# inches to cm = multiply the length value by 2.54


def feet_to_inch(feet):
    return feet * 30.48

def inches_to_cm(inches):
    return inches * 2.54

def get_height():
    print("Input your height.. ")
    height_ft = int(input("Feet: "))
    height_inch = int(input("Inches: "))
    height_cm = (feet_to_inch(height_ft) + inches_to_cm(height_inch))
    return print(f"Your height is {height_cm} cm!")

get_height()



