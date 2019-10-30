def find_fibo(n):
    # base case
    if n == 0:
        return 1

    # recusrsive case
    return n * find_fibo(n - 1)


print(find_fibo(5))

