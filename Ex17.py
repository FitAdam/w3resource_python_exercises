"""17. Write a Python program to test 
whether a number is within 100 of 1000 or 2000."""

def test_n(n):
    if n <= 100:
        print("The number is within 100")
    elif n <= 1000:
        print("The number is within 1000")
    else:
        print("The number is within 2000")

test_n(1001)