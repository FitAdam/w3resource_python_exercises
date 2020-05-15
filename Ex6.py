"""6. Write a Python program which accepts 
a sequence of comma-separated numbers from user 
and generate a list and a tuple with those numbers."""

#Sample data : 3, 5, 7, 23
#Output :
#List : ['3', ' 5', ' 7', ' 23']
#Tuple : ('3', ' 5', ' 7', ' 23')

a = input("enter some numbers: ")

new_list = a.split(",")
new_tuple = tuple(new_list)

print("Sample data: ", a)
print("List: ", new_list)
print("Tuple: ", new_tuple)