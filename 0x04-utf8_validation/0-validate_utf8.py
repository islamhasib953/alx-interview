#!/usr/bin/python3
"""valid UTF8"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    for i in range(len(data)):
        cnt_ones = 0
        byte = bin(data[i])[2:]
        if len(byte) == 8:
            find_zero = byte.find("0")
            cnt_ones = len(byte[:find_zero])
            cnt = 1
            for j in range(1, cnt_ones):
                i += 1
                cnt += 1
                byte_new_data = bin(data[i])[2:]
                zero = byte_new_data.find("0")
                ones = len(byte_new_data[:zero])
                if ones > 1:
                    return False
            if cnt < cnt_ones or cnt > cnt_ones:
                return False
    return True
