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
    possible_moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                      [1, 7, 0], [2, 6], [1, 3], [2, 4]]
    # if N is 1, knight can dial only one number in 10 ways
    total_numbers_dialed = [1] * 10

    for hop in range(N - 1):
        # hops to take in this jump
        moves = [0] * 10
        for dial_from, dial_count in enumerate(total_numbers_dialed):
            # possible numbers to dial from given dial number
            moves_to_take = possible_moves[dial_from]

            for dial_to in moves_to_take:
                moves[dial_to] += dial_count

        total_numbers_dialed = moves

    return sum(total_numbers_dialed)

print(knight_dialer(4))
