"""116. Write a Python program to print Unicode characters. """

def unicode_print(word):
    return word.encode(encoding="utf-8", errors="strict")
    

print(unicode_print('Łódż'))

print(b'\xc5\x81\xc3\xb3d\xc5\xbc'.decode("utf-8", errors="strict"))
