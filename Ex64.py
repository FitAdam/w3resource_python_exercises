"""64. Write a Python program to
 get file creation and modification date/times."""
import os.path, time

print("Last modified: %s" % time.ctime(os.path.getmtime("Ex30.py")))
print("Created: %s" % time.ctime(os.path.getctime("Ex30.py")))



