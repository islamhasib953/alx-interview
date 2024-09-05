#!/usr/bin/python3
"""valid UTF8"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    cnt = 0
    for byte in data:
        binary = bin(byte).replace("0b", "").rjust(8, "0")[-8:]
        if cnt == 0:
            if binary.startswith("110"):
                cnt = 1
            elif binary.startswith("1110"):
                cnt = 2
            elif binary.startswith("11110"):
                cnt = 3
            elif binary.startswith("10"):
                return False
        else:
            if not binary.startswith("10"):
                return False
            cnt -= 1
    return cnt == 0
