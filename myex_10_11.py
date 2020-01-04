"""
Two words are a “reverse pair” if each is the reverse of the other.
Write a program that finds all the reverse pairs in the word list.
"""


def make_word_list():
    word_list = []
    fin = open("/Users/antonioalvino/Downloads/words.txt")
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def reverse_pair():
    rev_list = make_word_list()
    rev_ret = []
    for word in rev_list:
        if word[::-1] in rev_list:
            rev_ret.append(word + " e " + word[::-1])
    return rev_ret


print(reverse_pair())
