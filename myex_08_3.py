"""
A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
Use this idiom to write a one-line version of is_palindrome from Exercise 6.3.
"""


def is_palindrome(x):
    return True if list(x) == list(x)[::-1] else False


print(is_palindrome("anna"))
