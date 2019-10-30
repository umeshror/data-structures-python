def find_fibo(n):
    # base case
    if n == 0:
        return 1

    # recusrsive case
    return n * find_fibo(n - 1)


print(find_fibo(5))


def find_sum(n):
    # Base Case
    if n == 0:
        return 0

    return n + find_sum(n - 1)


print(find_sum(5))

"""
Given an integer, create a function which returns the sum of all the individual
 digits in that integer. For example: if n = 4321, return 4+3+2+1

"""


def sum_func(n):
    # Base case
    if len(str(n)) == 1:
        return n

    # Recursion
    else:
        return n % 10 + sum_func(n / 10)


print(sum_func(4321))
