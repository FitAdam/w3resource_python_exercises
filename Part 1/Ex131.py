"""131. Write a Python program to split a variable length string into variables."""

new_list = ['a', 'b', 'c']
abc = ''
for x in new_list:
    abc+=x

print(abc)

a = abc[0]
b = abc[1]
c = abc[2]

print(a,b,c)