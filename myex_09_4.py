"""
Write a function named uses_only that takes a word and a string of letters, 
and that returns True if the word contains only letters in the list.
Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa”?
"""


def uses_only(word, letters):
    for c in word:
        if c not in letters:
            return False
    return True


print(uses_only("cane", "ance"))
