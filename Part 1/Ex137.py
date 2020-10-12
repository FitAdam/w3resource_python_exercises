"""137. Write a Python program to extract 
single key-value pair of a dictionary in variables."""

dict_os = {'coffee':'cookies'}

(a1, a2), = dict_os.items()

print(a2)
print(a1)