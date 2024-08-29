#!/usr/bin/python3

import signal
import sys
import re

count_status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

total_file_size = 0
line_processed = 0
# pattern = r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
# pattern = r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'


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


def interrupt_handeler(signum, frame):
    print_status()
    sys.exit(0)


signal.signal(signal.SIGINT, interrupt_handeler)


def process_line(line):
    global line_processed
    global total_file_size
    parsed_line = line.split()
    parsed_line = parsed_line[::-1]
    # match = re.match(pattern, line)
    try:
        if len(parsed_line) > 2:
            # parts = match.groups()
            total_file_size += int(parsed_line[0])
            status_code = int(parsed_line[1])
            # file_size = int(parts[4])
            # check_status_code = count_status.get(status_code)
            # if check_status_code is not None:
            if status_code in count_status.keys():
                count_status[status_code] += 1
            # total_file_size+=file_size
            line_processed += 1
        if line_processed % 10 == 0:
            print_status()
    finally:
        print_status()


for line in sys.stdin:
    process_line(line)
