#!/usr/bin/python3
"""LockBoxes Challenge"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened or not.

    Args:
        boxes (list of int): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    opened_boxes = set()
    keys = set()
    current_box = 0

    while current_box < num_boxes:
        opened_boxes.add(current_box)
        keys.update(boxes[current_box])
        next_box = None
        for key in keys:
            if key != current_box and key < num_boxes and key not in opened_boxes:
                next_box = key
                break
        if next_box is not None:
            current_box = next_box
        else:
            break

    for box in range(num_boxes):
        if box not in opened_boxes and box != 0:
            return False
    return True
