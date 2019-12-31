"""
Exercise 9.1. Write a program that reads words.txt and prints
only the words with more than 20 characters (not counting whitespace)
"""


def read_file(filename, num):
    fin = open(filename)
    for x in fin:
        if len(x) > num:
            print(x)


print(read_file("/Users/antonioalvino/Downloads/words.txt", 20))
