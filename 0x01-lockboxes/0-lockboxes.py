#!/usr/bin/python3
"""lockbox implementation"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes in the list of lists 'boxes' can be opened.
    Args:
    - boxes: a list of n sublists,where the i-th sublist contains the keys in box i.
    The first box, boxes[0], is unlocked.
    Returns:
    - unlocked (bool): True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked_boxes = set([0])
    new_keys = set(boxes[0])
    
    while new_keys:
        next_box = new_keys.pop()
        unlocked_boxes.add(next_box)
        new_keys |= set(boxes[next_box]) - unlocked_boxes
    
    return len(unlocked_boxes) == n
