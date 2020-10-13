"""7. Write a Python program to count the number of each character of a given text of a text file. """


def analyse(name):
    with open(name, 'r') as file:
        text = file.read().replace('\n', '')
    lst_char = list(text)
    lst_char_2 = []
    #print(lst_words)
    # this gives me a list without duplicates, useful for looping over the words
    for x in lst_char:
        if x not in lst_char_2:
            lst_char_2.append(x)

    for i in lst_char_2:
        word_counter = lst_char.count(i)
        print(f"The element: '{i}', exists  {word_counter} times. ")


analyse(r'Part 2\workfile.txt')

