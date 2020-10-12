"""99. Write a Python program to clear the screen or terminal."""
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()
