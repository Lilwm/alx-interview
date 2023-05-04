#!/usr/bin/python3
""" Minimum operations function"""


def minOperations(n):
    """
    calculates the min number of operations to get given H's.
    Args:
    function takes an integer n as input

    Returns: no of minimum operations required or 0
    """
    # Base case: if n is already equal to 1
    if n == 1:
        return 0
    # Initialize the dynamic programming array with max values
    dp = [float('inf')] * (n+1)
    # For n = 1, the number of operations needed is 0
    dp[1] = 0
    # Calculate minimum operations for each i from 2 to n
    for i in range(2, n+1):
    # Try all possible factors of i
        for j in range(1, i):
            # Check all possible factors of i and update dp[i]
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i//j))
    # Return the minimum operations needed to obtain n H characters
    return dp[n] if dp[n] != float('inf') else 0