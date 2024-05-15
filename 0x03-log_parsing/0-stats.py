#!/usr/bin/python3
"""
Log parsing script that computes metrics from stdin.

This script reads input from stdin, parses the data, and computes
metrics based on the input data. It tracks the total file size and
counts occurrences of different HTTP status codes. It also handles
keyboard interrupts (CTRL + C) gracefully and prints statistics when
interrupted or after every 10 lines.
"""
import sys
import signal

# Initialize variables
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_statistics():
    """Prints statistics."""
    print("Total file size:", total_file_size)
    sorted_status_codes = sorted(status_code_counts.items())
    for code, count in sorted_status_codes:
        if count > 0:
            print("{}: {}".format(code, count))


def handle_interrupt(sig, frame):
    """Handles keyboard interrupt."""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

# Process input
for line_count, line in enumerate(sys.stdin, start=1):
    if line_count % 10 == 0:
        print_statistics()

    try:
        # Split the line into components
        _, _, _, status_code_str, file_size_str = line.split()

        # Convert status code and file size to integers
        status_code = int(status_code_str)
        file_size = int(file_size_str)

        # Update total file size
        total_file_size += file_size

        # Update status code count
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

    except ValueError:
        # Skip line if format is not as expected
        continue
