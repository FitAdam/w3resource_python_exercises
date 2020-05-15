"""7. Write a Python program to 
accept a filename from the user and print the extension of that."""

filename = input("Type the name of file:")

new_list = filename.split(".")

the_extention = new_list[1]

print(f"The extention of {filename} is {the_extention}.")