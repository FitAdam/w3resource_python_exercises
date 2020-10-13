"""
3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
"""

def foo(lst):
    """
    removes and prints every third number from a list of numbers until the list becomes empty.
    """
    position = 2 
    idx = 0
    len_lst = len(lst)
    while len_lst > 0:
        idx = (position+idx) % len_lst
        num = lst.pop(idx)
        len_lst-=1
        print(num)

    print(f"The list is {lst}.")
   
foo([10,20,30,40,50,60,70,80,90])


