"""24. Write a Python program to test whether a passed letter is a vowel or not."""

def check_vovel(letter):
    if letter in 'aeiou':
        print(f"{letter} is a vovel.")
    else:
        print(f"{letter} is not a vovel.")

check_vovel('a')
check_vovel('b')