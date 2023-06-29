#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """
    Determines the winner of the game given x rounds
    and the array of numbers for each round.

    Args:
      x: The number of rounds.
      nums: The array of numbers for each round.

    Returns:
      The name of the player that won the most rounds.
      If the winner cannot be determined, returns None.
    """
    maria_wins = 0
    ben_wins = 0

    # Generate prime numbers up to the maximum value in nums
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Count wins for each round
    for n in nums:
        prime_count = sum(primes[:n+1])

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
