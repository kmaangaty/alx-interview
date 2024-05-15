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
x = 0
y = 0
z = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def a():
    """Prints statistics."""
    print("File size:", y)
    s = sorted(z.items())
    for c, n in s:
        if n > 0:
            print("{}: {}".format(c, n))


def b(s, f):
    """Handles keyboard interrupt."""
    a()
    sys.exit(0)


signal.signal(signal.SIGINT, b)

for lb in sys.stdin:
    x += 1
    try:
        _, _, _, c, s = lb.split()
        c = int(c)
        s = int(s)
        if c in z:
            z[c] += 1
        y += s
    except ValueError:
        continue

    # Print stats every 10 lines
    if x % 10 == 0:
        a()
