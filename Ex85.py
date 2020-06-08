"""85. Write a Python program to check
 whether a file path is a file or a directory."""

import os

new_path =r'Ex20.py'
dir_path =r'C:\Users\User\Documents'

def check_dir_file(new_path):
    if os.path.isdir(new_path):
        return 'this is a directory'
    elif os.path.isfile(new_path):
        return 'this is a file'
    else:
        return 'something wrong...'

print(check_dir_file(new_path))
print(check_dir_file(dir_path))