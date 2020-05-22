"""
29. Write a Python program to print out a set 
containing all the colors from color_list_1 
which are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_list_3 = set()
for x in color_list_1:
    if x in color_list_2:
        color_list_3.add(x)

print(f"Common elements: {color_list_3}.")

print(f"Not shared elements: {color_list_1.difference(color_list_2)}" )
