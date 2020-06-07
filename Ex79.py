"""79. Write a Python program to get the size of an object in bytes."""

import sys

class Mag:

    ml = 0

    def __init__(self, size, capacity):
        self.size = size
        self.capacity = capacity

    def pour_coffe(self, x):
        self.ml += x
        return self.ml

    def drink(self):
        if self.ml > self.capacity:
            return print('Oh no')
        else:
            return print('mm good taste')

new_mag = Mag(300, 300)

new_mag.pour_coffe(300)

new_mag.drink()

#Return the size of an object in bytes.
print(sys.getsizeof(new_mag))

new_mag.pour_coffe(300)
new_mag.drink()