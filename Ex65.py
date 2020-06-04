"""65. Write a Python program to convert seconds to day, hour, minutes and seconds."""

def convert(seconds):
    days = seconds // 86400
    rest = seconds % 86400
    hours = rest // 3600
    rest = rest % 3600
    minutes = rest // 60
    rest = rest % 60
    seconds = rest
    
    return f"days: {days}, hours {hours}, minutes {minutes}, seconds {seconds}"


x = 86400 + 3600 + 60 + 7
print(convert(1234565))
    
