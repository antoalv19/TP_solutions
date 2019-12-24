"""
1. Write a function named is_triangle that takes three integers as arguments, and that prints
either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks
with the given lengths.
"""


def is_triangle(a, b, c):
    if a > b+c or b > a+c or c > a+b:
        print("No")
    else:
        print("Yes")


"""
2. Write a function that prompts the user to input three stick lengths, converts them to integers,
and uses is_triangle to check whether sticks with the given lengths can form a triangle.
"""


def can_form_tri():
    a = int(input("Inserire valore di A\n"))
    b = int(input("Inserire valore di B\n"))
    c = int(input("Inserire valore di C\n"))
    is_triangle(a, b, c)


can_form_tri()