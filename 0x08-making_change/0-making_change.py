#!/usr/bin/python3
"""
Module to solve the coin change problem using dynamic programming.
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): List of coin denominations available.
        total (int): The target total amount to make up with the fewest coins.

    Returns:
        int: Minimum number of coins needed to meet the total amount.
             Returns -1 if the total cannot be met with the given coins.
    """
    if total < 0:
        return -1
    if total == 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, total + 1):
            if dp[j - coin] != float('inf'):
                dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
