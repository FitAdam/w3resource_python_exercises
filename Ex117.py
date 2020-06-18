"""117. Write a Python program to prove that two string variables of same value point same memory location."""

def prove(x,y):
    memory_location = (hex(id(x)))
    memory_location_2 = (hex(id(y)))
    if memory_location == memory_location_2:
        return True
    else:
        return False

print(prove(99,99))

