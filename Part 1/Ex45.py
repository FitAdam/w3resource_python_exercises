"""45. Write a python program to call an external command in Python."""

import subprocess

with open('output.txt', 'w') as f:
    subprocess.run('dir', shell=True, stdout=f, text= True)
