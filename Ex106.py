"""106. Write a Python program to divide a path on the extension separator."""
import os

program_file = 'path/to/program.exe'

def divide_path(new_file):
    divide_file = []

    for x in new_file:
        if x == '.':
            x = ' '
            divide_file.append(x)
        else:
            divide_file.append(x)
    
        
    return ''.join(divide_file)

print(divide_path(program_file))

# better function
def divide_path_os(your_path):
    print(os.path.splitext(your_path))

divide_path_os(program_file)
