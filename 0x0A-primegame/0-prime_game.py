#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """
    gets the winner given x rounds and the array of numbers for each round.

    Args:
        x: The number of rounds.
        nums: The array of numbers for each round.

    Returns:
        The name of the player that won the most rounds.
        If the winner cannot be determined, returns None.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        if primes.count(True) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
