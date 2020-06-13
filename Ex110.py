"""110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function."""
my_list = [1, 5, 4, 30, 8, 15, 3, 45, 55, 60, 37, 100, 105, 220]

new_list = list(filter(lambda x: (x%15 == 0) , my_list))

print(new_list)