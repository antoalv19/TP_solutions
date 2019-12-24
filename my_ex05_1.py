"""
Exercise 5.1. The time module provides a function, also named time, that returns the current
Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On
UNIX systems, the epoch is 1 January 1970.
# >>> import time
# >>> time.time()
1437746094.5735958
Write a script that reads the current time and converts it to a time of day in hours, minutes, and
seconds, plus the number of days since the epoch.

"""

import time

day_in_sec = 60 ** 2 * 24

now = time.time()


def hours(t):
    return int((t % day_in_sec) // 60 ** 2)


def mins(t):
    return int((t % day_in_sec) % 60 ** 2) // 60


def seconds(t):
    return int((t % day_in_sec) % 60 ** 2) % 60


def days_since(t):
    return int(t // day_in_sec)


print(days_since(now))
