"""
Given a target amount n and a list (array) of distinct coin values, \what's
the fewest coins needed to make the change amount.

For example:

If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:

1+1+1+1+1+1+1+1+1+1

5 + 1+1+1+1+1

5+5

10

With 1 coin being the minimum amount.
"""
import sys


def coin_change(target, coins, cache=None):
    """
    INPUT: Target change amount and list of coin values
    OUTPUT: Minimum coins needed to make change
    """
    if not cache:
        cache = {}

    if cache.get(target):
        return cache[target]
    # Default to target value
    min_coins = sys.maxsize

    # Check to see if we have a single coin match (BASE CASE)
    if target in coins:
        cache[target] = 1
        return 1

    else:

        # for every coin value that is <= than target
        valid_coins = [c for c in coins if c <= target]
        for coin in valid_coins:
            # Recursive Call (add a count coin and subtract from the target)
            updated_target = target - coin
            num_coins = 1 + coin_change(updated_target, valid_coins, cache)

            # Reset Minimum if we have a new minimum
            min_coins = min(num_coins, min_coins)
            cache[target] = min_coins
    return min_coins


print coin_change(63,[1,5,10,25])
