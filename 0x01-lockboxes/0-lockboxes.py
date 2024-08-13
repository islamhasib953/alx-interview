#!/usr/bin/python3

'''
this problem is You have n number of locked boxes in front of you. Each box is
numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
        There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
# def realCanUnlockAll(boxes):
#     unlocked = [0] * len(boxes)
#     stack = []
#     unlocked[0] = 1
#     stack.append(boxes[0])
#     while len(stack):
#         box = stack.pop()
#         for key in box:
#             if  key < len(boxes) and not unlocked[key]:
#                 stack.insert(0, boxes[key])
#                 unlocked[key] = 1
#     return True if sum(unlocked) == len(boxes) else False

'''
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
            should_visit.extend(key for key in boxes[i] if key not in visited)

    return len(visited) == len(boxes)
