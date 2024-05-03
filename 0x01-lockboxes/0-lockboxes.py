#!/usr/bin/python3
"""
Script to determine if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be unlocked.

    Args:
        boxes (list of int): A list of lists representing
        the boxes and their keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    keys = [0]

    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)

    if len(keys) == len(boxes):
        return True
    else:
        return False
