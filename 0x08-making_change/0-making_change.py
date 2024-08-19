#!/usr/bin/python3
"""
Coin Change Problem
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make up a given total

    Args:
        coins (list of ints): a list of coin denominations
        total (int): the target total to be met

    Returns:
        int: The minimum number of coins needed to meet the target total
             or -1 if it's not possible to meet the target total
    """
    if total <= 0:
        return 0
    if not coins:
        return -1
    try:
        index = coins.index(total)
        return 1
    except ValueError:
        pass
    coins.sort(reverse=True)
    cct = 0
    for cc in coins:
        if total % cc == 0:
            cct += total // cc
            return cct
        if total >= cc:
            cct += total // cc
            total = total % cc
        if total == 0:
            break
    if total > 0:
        return -1
    return cct
