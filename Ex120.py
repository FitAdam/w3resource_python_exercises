"""120. Write a Python program to format a specified string to limit the number of characters to 6."""



str_num = "1234567890"

def format(word):
    c = ''
    y = 0
    while y < 1:
        for x in word:
            if (y == 6):
                break
            else:
                c = c+x
            y+=1    
    return c
    

print(format('pancake'))
print(format(str_num))
        