#!/usr/bin/python3
"""
This script reads from stdin line by line and computes metrics.
After every 10 lines and/or a keyboard interruption. keyboard prints
    - Total file size:i.e sum of all previous <file size>
    - Number of lines by status code(asc)
"""

import sys
from collections import defaultdict


def compute_metrics():
    """
    reads from stdin and prints metrics every 10 lines or on Ctrl+C.
    """
    # initialize variables
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        # loop over input lines
        for line in sys.stdin:
            line = line.strip()

            # parse input line
            try:
                _, _, _, status_code, file_size = line.split()
                status_code = int(status_code)
                file_size = int(file_size)
            except ValueError:
                # skip line if it doesn't match expected format
                continue

            # update metrics
            total_size += file_size
            status_counts[status_code] += 1
            line_count += 1

            # print metrics every 10 lines or on keyboard interrupt
            if line_count % 10 == 0:
                print(f'Total file size: {total_size}')

                for status_code in sorted(status_counts):
                    print(f'{status_code}: {status_counts[status_code]}')

            # handle keyboard interrupt
            try:
                sys.stdin.flush()
            except KeyboardInterrupt:
                print(f'Total file size: {total_size}')

                for status_code in sorted(status_counts):
                    print(f'{status_code}: {status_counts[status_code]}')

                sys.exit(0)

    except KeyboardInterrupt:
        # handle keyboard interrupt
        print(f'Total file size: {total_size}')

        for status_code in sorted(status_counts):
            print(f'{status_code}: {status_counts[status_code]}')

        sys.exit(0)


if __name__ == '__main__':
    compute_metrics()
