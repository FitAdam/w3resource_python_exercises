"""32. Write a Python program to get
 the least common multiple (LCM) of two positive integers."""

def gcf(a,b):
    if a != 0 or b != 0:
        # calculate the reminder
        r = a%b
        #print("This is r ", r)
        if r != 0:
            return gcf(b,r)
        else:
            return b
    else:
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            return 1

print(gcf(14,22))

#The formula of LCM is LCM(a,b) = ( a × b) / GCF(a,b).
def lcm(a,b):
    new_gcf = gcf(a,b)
    new_lcm = a * b / new_gcf
    return new_lcm

print(lcm(22,130))
