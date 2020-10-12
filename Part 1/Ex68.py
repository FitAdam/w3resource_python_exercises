"""68. Write a Python program 
to calculate the sum of the digits in an integer."""

def calculate(num):
    #Return an iterator that applies function to every item of iterable,
    #  yielding the results. If additional iterable arguments are passed, function must take that many arguments 
    # and is applied to the items from all iterables in parallel.
    lst = map(int, str(num))
    y  = 0
    for x in lst:
        y = y + x
    return y

print(calculate(5245))
