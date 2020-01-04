"""
Write a function named uses_all that takes a word and a string of required letters, 
and that returns True if the word uses all the required letters at least once. 
How many words are there that use all the vowels aeiou? How about aeiouy?
"""


def uses_all(word, reqletters):
    for c in reqletters:
        if c not in word:
            return False
    return True


def conta_parole(letters):
    fin = open("/Users/antonioalvino/Downloads/words.txt")
    wordcount = 0
    for word in fin:
        if uses_all(word, letters):
            wordcount += 1
    return wordcount


print(conta_parole("aeiouy"))
