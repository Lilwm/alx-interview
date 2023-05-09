#!/usr/bin/python3
"""
This script reads from stdin line by line and computes metrics.
After every 10 lines and/or a keyboard interruption. keyboard prints
    - Total file size:i.e sum of all previous <file size>
    - Number of lines by status code(asc)
"""
import sys


def print_stats():
    """log parsing script
    Args:
    Returns: total size, status code lines
    """
    try:
        # Initialize variables
        file_size = 0
        status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                        '403': 0, '404': 0, '405': 0, '500': 0}
        count = 0
        # Read from standard input
        for line in sys.stdin:
            count += 1
            tokens = line.split()
            try:
                file_size += int(tokens[8])
            except FileNotFoundError:
                pass
            # Check if line has all expected fields
            try:
                status_codes[tokens[7]] += 1
            except FileNotFoundError:
                pass
            if count % 10 == 0:
                print("File size: {:d}".format(file_size))
                for key, value in sorted(status_codes.items()):
                    if value != 0:
                        print("{:s}: {:d}".format(key, value))
        print("File size: {:d}".format(file_size))
        for key, value in sorted(status_codes.items()):
            if value != 0:
                print("{:s}: {:d}".format(key, value))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    print_stats()
