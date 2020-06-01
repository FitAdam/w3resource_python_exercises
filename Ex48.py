"""48. Write a Python program
 to parse a string to Float or Integer."""

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

    

print(num('12'))
print(num('34.3'))
#print(num('abc'))    