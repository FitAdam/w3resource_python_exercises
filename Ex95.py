"""95. Write a Python program to check whether a string is numeric."""

def check_numeric(new_str):
    return new_str.isnumeric()

print(check_numeric('python'))
print(check_numeric('python3'))
print(check_numeric('3'))