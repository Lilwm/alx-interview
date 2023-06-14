#!/usr/bin/python3
""" 0. Change comes from within """


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet a given amount.
    Args:
    coins: A list of the values of the coins in your possession.
    total: The amount of change you need to make.
    Returns:
    The fewest number of coins needed to meet total.
    If total is 0 or less, returns 0.
    If total cannot be met by any number of coins you have, returns -1.
    """
    if total <= 0:
        return 0
    # Initialize the number of coins to 0.
    num_coins = 0

    # Iterate over the coins in descending order.
    for coin in sorted(coins, reverse=True):
        while coin <= total:
            num_coins += 1
            total -= coin
    # If the target amount is not 0, then the number of coins needed is -1.
    if total > 0:
        return -1

    # Return the number of coins.
    return num_coins
