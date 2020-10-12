"""84. Write a Python program to count 
the number occurrence of a specific character in a string."""

def check_occurance(new_string, s):
    occurrence = 0
    for x in new_string:
        if x == s:
            occurrence += 1
    return occurrence


print(check_occurance('live','o'))