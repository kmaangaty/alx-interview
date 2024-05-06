#!/usr/bin/python3

"""
Minimum Operations

This module contains a function that calculates
the fewest number of operations needed
to result in exactly n H characters in a file,
using only "Copy All" and "Paste" operations.
"""


def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations
    needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
