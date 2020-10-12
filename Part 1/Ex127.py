"""127. Write a Python program to check whether 
an integer fits in 64 bits"""



def check(n):
    b = bin(n)
    b = n.bit_length()
    if b < 64:
        return True
    else:
        return False
    
print(check(33))