"""
6. Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies. 
"""

def analyse(text):
    lst_words = text.split()
    lst_words_2 = []
    #print(lst_words)
    # this gives me a list without duplicates, useful for looping over the words
    for x in lst_words:
        if x not in lst_words_2:
            lst_words_2.append(x)

    for i in lst_words_2:
        word_counter = lst_words.count(i)
        print(f"The element: '{i}', exists  {word_counter} times. ")
        
    
                

    #print(f"This is a list {lst_words}")


text = 'C# (pronounced "C sharp") is a simple, modern, object-oriented, and type-safe programming language. Its roots in the C family of languages makes C# immediately familiar to C, C++, Java, and JavaScript programmers.'
analyse(text)