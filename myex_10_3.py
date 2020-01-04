"""Write a function called middle that takes a list and returns a new list that contains all but the
first and last elements"""


def middle(t):
    return t[1:-1]


test = [1, 1, 2, 3]
print(middle(test))
