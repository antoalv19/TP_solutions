"""
Read the documentation of this method and write an invocation that counts the number of a’s in 'banana'.
"""


def count_as():
    word = str(input("Inserisci la parola da analizzare:\n"))
    letter = str(input("Inserisci la lettera da contare:\n"))
    return "Ho trovato ben {} lettere {}, nella parola {}.".format(word.count(letter), letter, word)


print(count_as())
