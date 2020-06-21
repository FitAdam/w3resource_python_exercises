"""132. Write a Python program to list home directory without absolute path."""


from pathlib import Path
home = str(Path.home())

print(home)