#!/usr/bin/python3
"""valid UTF8"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    count = 0

    for bit in data:
        binary = bin(bit).replace("0b", "").rjust(8, "0")[-8:]
        if count == 0:
            if binary.startswith("110"):
                count = 1
            elif binary.startswith("1110"):
                count = 2
            elif binary.startswith("11110"):
                count = 3
            elif binary.startswith("10"):
                return False
        else:
            if not binary.startswith("10"):
                return False
            count -= 1

    return count == 0
