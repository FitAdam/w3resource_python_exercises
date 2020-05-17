"""20. Write a Python program to get a string which is n (non-negative integer) copies of a given string."""

def larger_string(new_str, n):
   result = ""
   # range(from 0 to n)
   for i in range(n):
      result = result + new_str
   return result


print(larger_string('abc', 1))
print(larger_string('.py', 3))


"""The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

Syntax
range(start, stop, step)

Parameter	Description
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to stop (not included).
step	Optional. An integer number specifying the incrementation. Default is 1 """