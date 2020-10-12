"""145. Write a Python program to test if a variable is a list or tuple or a set. """

def check(x):
	if isinstance(x, tuple):
		print(f'{x} is a tuple')
	elif isinstance(x, list):
		print(f'{x} is a list')
	elif isinstance(x, set):
		print(f'{x} is a set')
	else:
		print('wrong input')


check([1,2,3,4,5])
check((1,2)) 
check({'python', 'javascript', 'c++'})
