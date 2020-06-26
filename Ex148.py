"""148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers."""


def find_max_and_mim(lst):
	lst.sort()
	print(f'{lst[0]} is the minimum number')
	print(f'{lst[-1]} is the maximum number')


find_max_and_mim([3,2,9,10,1, 22, 41])