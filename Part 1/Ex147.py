"""147. Write a Python function to check whether a number is divisible by another number. 
Accept two integers values form the user."""


def check_div(x,y):
	if x % y == 0:
		print(f'{x} is divisible by {y}.')
	else:
		print(f'{x} is NOT divisible by {y}.')

check_div(25, 4)
check_div(25, 5)

