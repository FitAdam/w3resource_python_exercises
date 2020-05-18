"""23. Write a Python program to get the n (non-negative integer) 
copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2."""

def get_copies(new_str, n):
    if len(new_str) < 2:
        return n * new_str
    else:
        return new_str[:2] * n

print(get_copies('abcdef', 2))