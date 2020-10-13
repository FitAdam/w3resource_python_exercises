"""
2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
"""
import random

def create_all_strings():
    characters = ['a', 'e', 'i', 'o', 'u']
    random.shuffle(characters)
    return ''.join(characters)
        

print(create_all_strings())