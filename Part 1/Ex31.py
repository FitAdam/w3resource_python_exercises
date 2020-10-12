""" 31. Write a Python program to compute 
the greatest common divisor (GCD) of two positive integers."""

def foo(a,b):
    if a != 0 and b != 0:
        # calculate the reminder
        r = a%b
        #print("This is r ", r)
        if r != 0:
           # print(f"This is the b {b}")
            foo(b,r)
        else:
            return print(f"1This is the GCD {b}")
    else:
        if a == 0:
            return print(f"2This is the GCD {b}")
        elif b == 0:
            return print(f"3This is the GCD {a}")
        else:
            return print("give something diffirent")


foo(14,22)