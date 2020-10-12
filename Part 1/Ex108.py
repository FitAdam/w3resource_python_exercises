"""108. Write a Python program to find path refers to a file or directory when you encounter a path name."""
import os

def find_file(new_path):
    if os.path.isdir(new_path):
        return 'This is a directory'
    else:
        return 'This is a file'


print(find_file('Ex107.py'))
print(find_file(r'C:\Users\yourName\OneDrive\Documents\Projects\w3resource_python_exercises'))