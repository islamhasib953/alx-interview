#!/usr/bin/python3

import signal
import sys

count_status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

total_file_size = 0
line_processed = 0


# def interrupt_handeler(signum, frame):
#     print_status()
#     sys.exit(0)


# signal.signal(signal.SIGINT, interrupt_handeler)


def print_status():
    """
    Method to print
    Args:
        count_status: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """
    print(f"File size: {total_file_size}")
    for status in sorted(count_status.keys()):
        if count_status[status] > 0:
            print(f"{status}: {count_status[status]}")


def process_line(line):
    global line_processed
    global total_file_size
    parsed_line = line.split()
    parsed_line = parsed_line[::-1]
    if len(parsed_line) > 2:
        total_file_size += int(parsed_line[0])
        status_code = int(parsed_line[1])
        if status_code in count_status.keys():
            count_status[status_code] += 1
        line_processed += 1
        if line_processed % 10 == 0:
            print_status()


try:
    for line in sys.stdin:
        process_line(line)
finally:
    print_status()
