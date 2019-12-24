def is_palindrome(x):
    return True if list(x) == list(x)[::-1] else False


print(is_palindrome("anna"))
