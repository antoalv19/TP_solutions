"""
Give me a word with three consecutive double letters. I’ll give you a couple of words that almost qualify,
but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in
there. Or Mississippi: M-i-s-s-i-s-s-i- p-p-i. If you could take out those i’s it would work. But there is a word
that has three consecutive pairs of letters and to the best of my knowledge this may be the only word. Of course
there are probably 500 more but I can only think of one.
"""


def find_double(word):
    i = 0
    ctr = 0  # double counter
    while i < len(word) - 2:
        if word[i + 1] == word[i]:
            ctr += 1
            i += 2
            if ctr == 3:
                return word
        else:
            ctr = 0
            i += 1
    return None


print(find_double("bookkeeper"))
