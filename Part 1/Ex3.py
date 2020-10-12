"""3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14"""

from datetime import date
from datetime import datetime
today = date.today()
current_time = datetime.now()
print("Today's date:", today)
print("Current's time", current_time)

# To get the current date and time, 
# you can use datetime class of the datetime module.
# dd/mm/YY H:M:S
dt_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(dt_string)	
