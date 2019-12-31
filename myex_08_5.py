"""
Write a function called rotate_word that takes a string and an integer as parameters,
and returns a new string that contains the letters from the original string rotated by the given amount.
"""


def rotate_word(word, num):
    return "".join([chr(ord(letter) + num) for letter in word])


print(rotate_word("IBM", -1))
