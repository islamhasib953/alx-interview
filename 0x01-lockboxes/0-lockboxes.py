#!/usr/bin/python3
"""
lock boxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
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
