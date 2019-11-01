"""
Implement a Fibonnaci Sequence in three different ways:

Recursively
Dynamically (Using Memoization to store results)
Iteratively

1, 1, 2, 3, 5, 8, 13, 21, 34

"""


def fib_iterative(n):
    # starting point
    a = 0
    b = 1

    # Follow algorithm
    for i in range(n):
        a, b = b, a + b

    return a


print(fib_iterative(3))


def fib_recursion(n):
    """

    fib_rec(n)  = fib_rec(n - 1) + fib_rec(n - 2)
    fib_rec(2)  = fib_rec(1) + fib_rec(0)
    fib_rec(3)  = fib_rec(2) + fib_rec(1)
    fib_rec(5)  = fib_rec(4) + fib_rec(3)
                = fib_rec(3) + fib_rec(2) + fib_rec(2) + fib_rec(1)
                = fib_rec(2) + fib_rec(1) + fib_rec(2) + fib_rec(2) + fib_rec(1)

    2 =  1 + 1
    3 =  2 + 1
    """
    # Base Case
    if n == 0 or n == 1:
        return n

    return fib_recursion(n - 1) + fib_recursion(n - 2)


print(fib_recursion(8))

cache = {}


def fib_dynamic(n):
    """
    fib_rec(n)  = fib_rec(n - 1) + fib_rec(n - 2)
    cache = {}
    fib_rec(2)  = fib_rec(1) + fib_rec(0)
    fib_rec(3)  = fib_rec(2) + cache(1)
    fib_rec(5)  = fib_rec(4) + fib_rec(3)
                = cache(3) + cache(2) + cache(2) + cache(1)

    2 =  1 + 1
    3 =  2 + 1
    """
    # Base Case
    if n == 0 or n == 1:
        return n
    if cache.get(n):
        return cache[n]
    cache[n] = fib_dynamic(n - 1) + fib_dynamic(n - 2)
    return cache[n]


print(fib_dynamic(11))
