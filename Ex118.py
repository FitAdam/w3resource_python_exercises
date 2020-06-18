"""118. Write a Python program to create a bytearray from a list."""

colors = ['blue', 'red', 'yellow', 'black']
numbers = [2, 2, 5, 1, 3, 8, 9, 0]

for color in colors:
    x = bytearray(color, encoding="utf-8", errors="strict")
    print(x)

print('\n')

for number in numbers:
    y = bytearray(number)
    print(y)