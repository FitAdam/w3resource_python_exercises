"""70. Write a Python program to sort files by date."""

import os.path, time

# Crates a list of directiories
files_dir = os.listdir()

# to sort it inplace by creation time on Windows:
files_dir.sort(key=os.path.getmtime)

# for every file in list
for x in files_dir:
    #print name of the file and time of the last modification
    print(f"{x} Last modified: %s" % time.ctime(os.path.getmtime(x)))
