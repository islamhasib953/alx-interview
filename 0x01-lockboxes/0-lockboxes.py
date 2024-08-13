#!/usr/bin/python3
"""
lock boxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
        There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """

    vistited = set()
    should_visit = [0]
    while should_visit:
        i = should_visit.pop()
        if i not in vistited:
            vistited.add(i)
        for j in boxes[i]:
            if j not in vistited:
                should_visit.append(j)

    return len(vistited) == len(boxes)
