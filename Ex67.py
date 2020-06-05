"""67. Write a Python program 
to convert pressure in kilopascals 
to pounds per square inch, a millimeter of mercury (mmHg) 
and atmosphere pressure."""

def convert_pressure(kilopascals):
    pound_per_square_inch = kilopascals/ 6.895
    millimeter_of_mercury = kilopascals * 7.501
    atmosphhere_pressure = kilopascals / 101
    return print(f'{pound_per_square_inch} pound per squure inch, {millimeter_of_mercury} milimiter of mercury, {atmosphhere_pressure} atmosphere pressure')


print(convert_pressure(12.35))
