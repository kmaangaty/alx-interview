#!/usr/bin/python3
"""
Script to compute metrics from stdin.

This script reads input from stdin, parses the data, and computes
metrics based on the input data. It tracks the total file size and
counts occurrences of different HTTP status codes. It also handles
keyboard interrupts (CTRL + C) gracefully and prints statistics when
interrupted or after every 10 lines.
"""
import sys
import signal

# Initialize variables
line_count = 0
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_statistics():
    """Prints statistics."""
    print("File size:", total_size)
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        if count > 0:
            print("{}: {}".format(code, count))


def handle_interrupt(sig, frame):
    """Handles keyboard interrupt."""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

for line in sys.stdin:
    line_count += 1
    try:
        _, _, _, status_code_str, size_str = line.split()
        status_code = int(status_code_str)
        size = int(size_str)
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += size
    except ValueError:
        # Skip line if format is not as expected
        continue

    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_statistics()
