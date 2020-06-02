"""62. Write a Python program to convert all units of time into seconds"""
from time import time, ctime

t = time()

print(ctime(t))

def hours_to_sec(h):
    return h * 3600

def minutes_to_sec(m):
    return m * 60

def days_to_sec(d):
    return hours_to_sec(d * 24)


print(days_to_sec(30))