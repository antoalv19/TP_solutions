"""
Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters
and then prints the number of words that don’t contain any of them.
Can you find a combination of 5 forbidden letters that excludes the smallest number of words?
"""


def avoids(word, forbidden):
    for c in forbidden:
        if c not in word:
            continue
        else:
            return False
    return True


def forbidden_words(filename):
    forbidden = str(input("Inserisci lettere proibite:\n"))
    fin = open(filename)
    lista_parole = []
    for word in fin:
        if avoids(word, forbidden):
            print(word)
            lista_parole.append(word)
    return len(lista_parole)


print(forbidden_words("/Users/antonioalvino/Downloads/words.txt"))
