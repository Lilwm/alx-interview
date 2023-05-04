#!/usr/bin/python3
""" Minimum operations function"""


def minOperations(n):
    """
    calculates the min number of operations to get given H's.
    Args:
    function takes an integer n as input

    Returns: no of minimum operations required or 0
    """
    min_op = 1
    start = 0
    counter = 0
    while min_op < n:
        remainder = n - min_op
        if (remainder % min_op == 0):
            start = min_op
            min_op += start
            counter += 2
        else:
            min_op += start
            counter += 1
    return counter
