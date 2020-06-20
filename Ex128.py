"""128. Write a Python program to check whether
 lowercase letters exist in a string."""

name = 'Python'
name_2 = 'PYTHON'


def check(word):
    lowercase_counter = 0
    for x in word:
        if x.islower():
            lowercase_counter +=1
    if lowercase_counter > 0:
        return 'The lower case letter exists in the string.'
    else:
        return 'The string does not have lower case letters.'
    

print(check(name))

print(check(name_2))