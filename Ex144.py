"""144. Write a Python program to check whether variable is of integer or string. """

def check(x):
	if isinstance(x, int):
		print(f'{x} is an integer')
	elif isinstance(x, str):
		print(f'{x} is a string')



check(123)
check('clock')