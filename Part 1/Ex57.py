"""57. Write a program to get execution time for a Python method. """
import time

start_time = time.time()

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

foo(1414325,2224354543)

print("--- %s seconds ---" % (time.time() - start_time))