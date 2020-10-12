"""111. Write a Python program to make file lists from current directory using a wildcard."""

# Regular expression library
import re
import glob
# Crates a list of directiories
files_dir = glob.glob('*.*')
files_list = []

for word in files_dir:
        # The . symbol is used in place of ? symbol
        if re.search('0.+', word) : 
                files_list.append(word)

files_list.sort()

for file in files_list:
    print(file)
