"""Write a function called has_duplicates that takes a list and returns True if there is any element that appears
more than once. It should not modify the original list. """


def has_duplicates(t):
    for x in t:
        if t.count(x) > 1:
            return True
    return False


print(has_duplicates([1, 2, 3, 3]))
