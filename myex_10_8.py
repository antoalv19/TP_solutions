"""If there are 23 students in your class, what are the chances that two of you have the same birthday? You can
estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can
generate random birthdays with the randint function in the random module. """


from random import randint


def has_duplicates(t):
    for x in t:
        if t.count(x) > 1:
            return True
    return False


def collision_check(num):
    global collision, tot
    for n in range(num):
        rand_list = [randint(1, 31) for i in range(23)]
        collision = 0
        tot = 0
        if has_duplicates(rand_list):
            collision += 1
            tot += 1
        else:
            tot += 1
    return (collision / tot) * 100


print(collision_check(2))
