#!/usr/bin/python3
"""
Script to determine if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be unlocked.

    Args:
        boxes (list of int): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # Initialize the list of keys with the keys in the first box
    keys = [0]

    # Traverse through the keys and explore other boxes
    for key in keys:
        # Check keys in the current box
        for box_key in boxes[key]:
            # If the key is new and within the range of boxes, add it to the list of keys
            if box_key not in keys and box_key < len(boxes):
                keys.append(box_key)

    # If the number of keys equals the number of boxes, all boxes can be unlocked
    if len(keys) == len(boxes):
        return True
    else:
        return False
