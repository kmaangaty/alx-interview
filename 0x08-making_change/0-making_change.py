#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet
a given amount total.
"""
import sys


def makeChange(coins, total_amount):
    """
    Calculate the fewest number of coins needed to meet
     the given total amount.

    Args:
        coins (list of int): List of coin denominations available.
        total_amount (int): Target total amount to achieve using the coins.

    Returns:
        int: Fewest number of coins needed to meet the total amount.
             If total_amount is 0 or less, returns 0.
             If total_amount cannot be met by any combination of coins,
              returns -1.
    """
    if total_amount <= 0:
        return 0

    min_coins = [sys.maxsize for _ in range(total_amount + 1)]
    min_coins[0] = 0

    num_coins = len(coins)

    for amount in range(1, total_amount + 1):
        for coin_index in range(num_coins):
            if coins[coin_index] <= amount:
                srt = min_coins[amount - coins[coin_index]]
                if srt != sys.maxsize and srt + 1 < min_coins[amount]:
                    min_coins[amount] = srt + 1

    if min_coins[total_amount] == sys.maxsize:
        return -1
    return min_coins[total_amount]
