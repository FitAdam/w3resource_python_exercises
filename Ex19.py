"""19. Write a Python program to get a new string from a given string where
 "Is" has been added to the front. 
 If the given string already begins with "Is" then return the string unchanged."""

new_str = 'blablalogy a science?'
def add_if_to_front(new_str):
    if len(new_str) >= 2 and new_str[:2] == 'Is':
        return new_str
    else:
        return 'Is ' + new_str

print(add_if_to_front(new_str))
