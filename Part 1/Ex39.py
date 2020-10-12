"""39. Write a Python program to compute the future value of 
a specified principal amount, rate of interest, and a number of years. Go to the editor
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79"""

def future_value(amt, intr, years):
    return round(amt*((1+(0.01*intr)) ** years),2)

print(future_value(10000,3.5,7))
# how to calcualte %
print(100*((0.01*3.5)))