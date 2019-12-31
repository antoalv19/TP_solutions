"""
Exercise 9.1. Write a program that reads words.txt and prints
only the words with more than 20 characters (not counting whitespace)
"""


def read_file(filename, num):
    fin = open(filename)
    for x in fin:
        if len(x) > num:
            print(x)


# print(read_file("/Users/antonioalvino/Downloads/words.txt", 20))

"""
Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.
Write a program that reads words.txt and prints only the words that have no “e”.
Compute the percentage of words in the list that have no “e”.
"""


def has_no_e(word):
    return True if word.count("e") == 0 else False


def read_file_no_e(filename):
    fin = open(filename)
    for x in fin:
        if has_no_e(x):
            print(x)


print(read_file_no_e("/Users/antonioalvino/Downloads/words.txt"))
