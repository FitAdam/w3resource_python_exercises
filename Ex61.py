"""61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. """


def feet_to_inch(feet):
    return feet * 12

def feet_to_yards(feet):
    return feet / 3

def feet_to_miles(feet):
    return feet / 5280

def convert_distances():
    print("Input distance in feet.. ")
    distance_ft = int(input("Feet: "))
    inch = feet_to_inch(distance_ft)
    yard = feet_to_yards(distance_ft)
    miles = feet_to_miles(distance_ft)
   
    return print(f"Your distance in feet is {inch} inches, {yard} yards and {miles} miles!")

convert_distances()
