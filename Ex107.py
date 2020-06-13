"""107. Write a Python program to retrieve file properties."""

import os
import time

def retrieve_properties(new_file):
    statinfo = os.stat(new_file)
    print(f"File mode: file type and file mode bits (permissions). {statinfo.st_mode}.")
    print(f"User identifier of the file owner. {statinfo.st_uid}")
    print(f"Size of the file in bytes, if it is a regular file or a symbolic link. {statinfo.st_size}")
    print(f"Time of the file creation {statinfo.st_ctime}")

retrieve_properties('output.txt')
