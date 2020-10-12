"""113. Write a Python program to input a number, if it is not a number generate an error message."""

def test_num():
    while True:
        try:
            x = int(input('give me a number: '))
            int(x)
        except ValueError:
            return print('this is not a number')

test_num()