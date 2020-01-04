"""Exercise 10.2. Write a function called cumsum that takes a list of numbers and returns the cumulative sum; that
is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For example: t =
[1, 2, 3] cumsum(t) [1, 3, 6] """


def cumsum(t):
    cum_arr = []
    for i in range(len(t)):
        cum_arr.append(sum(t[:i+1]))
    return cum_arr


test = [1, 2, 3]

print(cumsum(test))
