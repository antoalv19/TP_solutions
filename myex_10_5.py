"""
Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise.
"""


def is_sorted(t):
    return t == sorted(t)


print(is_sorted(["b", "a"]))
