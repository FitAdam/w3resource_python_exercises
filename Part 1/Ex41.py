"""41 Write a Python program to check whether a file exists."""
import os

path= r"C:\Users\Vdvm\Documents"

new_list = os.listdir(path)

def check_file(filename):
    print(new_list)
    if filename in new_list:
        return print("file exists")
    else:
        return print("no file")

check_file('My Music')