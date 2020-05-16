""" 12. Write a Python program to print the calendar
 of a given month and year.
Note : Use 'calendar' module."""

import calendar

year = 2020
print(calendar.calendar(year, w=2, l=1, c=6, m=3))


y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

