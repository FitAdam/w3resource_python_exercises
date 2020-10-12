"""14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days"""

import calendar
from datetime import date

y = int(input("Input the year : "))
m = int(input("Input the month : "))
d = int(input("Input the day : "))
#print(calendar.month(y, m, d))

y1 = int(input("Input the year : "))
m1 = int(input("Input the month : "))
d1 = int(input("Input the day : "))
#print(calendar.month(y1, m1, d1))

y2 = y - y1
m2 = m - m1
d2 = d - d1
print(f"The number of days between these two dates is {abs(d2)}.")


#Better solution
first_date = date(2014, 7, 12)
last_date = date(2014, 7, 11)
num = last_date - first_date
# abs() returns absolute value
print(abs(num.days))
