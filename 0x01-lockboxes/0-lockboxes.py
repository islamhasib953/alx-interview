#!/usr/bin/python3
"""
Lock Boxes Module

This module contains the function `canUnlockAll` which determines
if all boxes can be unlocked given a list of boxes where each box
contains keys to other boxes.

The first box (boxes[0]) is unlocked. The function returns True if
all boxes can be opened, otherwise returns False.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list of lists where each list contains
                               the keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    visited = set()
    should_visit = [0]

    while should_visit:
        i = should_visit.pop()
        if i not in visited:
            visited.add(i)
        for j in boxes[i]:
            if j not in visited:
                should_visit.append(j)
    return len(visited) == len(boxes)
