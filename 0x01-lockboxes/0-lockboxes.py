#!/usr/bin/env python3
"""
Determines if all the boxes can be opened.

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

A key with the same number as a box opens that box. You can assume all keys will be positive integers.
There can be keys that do not have boxes. The first box boxes[0] is unlocked.

Returns:
    bool: True if all boxes can be opened, False otherwise.
"""


def canUnlockAll(boxes):
    """
    Args:
        boxes (list of int): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or len(boxes) == 1:
        return True

    keys = set(boxes[0])
    opened = {0}

    while opened:
        box = opened.pop()
        for key in boxes[box]:
            if key < len(boxes) and key not in keys:
                opened.add(key)
                keys.add(key)

    return len(keys) == len(boxes)
