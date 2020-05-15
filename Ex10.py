"""10. Write a Python program that accepts an integer (n) 
and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615"""

def compute(n):
    result = n + (n*10+n) +(n*100+n*10+n)
    return result

#print(compute(5))

def compute2(n):
    n1 = int( "%s" % n )
    n2 = int( "%s%s" % (n,n) )
    n3 = int( "%s%s%s" % (n,n,n) )
    return n1 + n2 + n3
    
print(compute2(5))


"""Python uses C-style string formatting to create new, 
formatted strings. The "%" operator is used 
to format a set of variables enclosed in
 a "tuple" (a fixed size list), together with a format string, 
 which contains normal text together with "argument specifiers", 
special symbols like "%s" and "%d"."""

data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string + " %s %s your balance is %d" %("John", "Doe", 53.44))