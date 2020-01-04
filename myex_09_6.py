"""
Write a function called is_abecedarian that returns
True if the letters in a word appear in alphabetical order (double letters are ok).
How many abecedarian words are there?
"""


def is_abecedarian(word):
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if ord(word[i]) > ord(word[j]):
                return False
    return True


def count_abecedarian():
    fin = open("/Users/antonioalvino/Downloads/words.txt")
    abcount = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            abcount += 1
    return abcount


print(count_abecedarian())
