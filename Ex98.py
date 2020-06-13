"""98. Write a Python program to get the system time."""


from datetime import datetime

now = datetime.now()
#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)