"""
 1   2   3
 4   5   6
 7   8   9
     0
Chess knight on any numbered key of a phone pad (indicated above), and the
knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Input: 1
Output: 10

Input: 2
Output: 20

f(1, n) = f(6, n-1) + f(8, n-1)

dp[start] = f(start, n)

f(0, N) + f(1, N) + ... + f(9, N) = sum(dp)
"""


def knight_dialer(N):
    # from 1 we can go to [4, 6]
    # from 2 we can go to [6, 8] and so on...
    moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
             [1, 7, 0], [2, 6], [1, 3], [2, 4]]

    total_hops_from = [1] * 10

    for hops in range(N - 1):
        hops_taken = [0] * 10
        for _from, count in enumerate(total_hops_from):
            for _to in moves[_from]:
                hops_taken[_to] += count
        total_hops_from = hops_taken

    return sum(total_hops_from)


print knight_dialer(4)
