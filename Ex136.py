"""136. Write a Python 
program to find files and skip 
directories of a given directory. """

import os
from os import listdir
from os.path import isfile, join
from fnmatch import fnmatch

mypath = '/home/adam/Documents/Projects'

dir_lst = os.listdir(mypath)

print(dir_lst)

pattern = "*.py"

for path, subdirs, files in os.walk(mypath):
    for name in files:
        if fnmatch(name, pattern):
            print(os.path.join(path, name))