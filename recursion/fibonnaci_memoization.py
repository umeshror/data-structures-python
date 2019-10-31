"""
Implement a Fibonnaci Sequence in three different ways:

Recursively
Dynamically (Using Memoization to store results)
Iteratively

1, 1, 2, 3, 5, 8, 13, 21, 34

"""


def fib_rec(n):
    # Base Case
    if n == 0 or n == 1:
        return n

    return fib_rec(n - 1) + fib_rec(n - 2)


print(fib_rec(3))
