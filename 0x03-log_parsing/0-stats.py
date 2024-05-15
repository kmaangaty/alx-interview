#!/usr/bin/python3
"""parsing HTTP request logs and computing metrics.

This script reads lines from standard input, extracts information from HTTP request logs,
and computes metrics based on the extracted data.
"""

import re


def extract_input(input_line):
    """
    extract_input() of a line of an HTTP request log.

    Args:
        input_line (str): A line from an HTTP request log.

    Returns:
        dict: A dictionary containing extracted information from the input line.
    """
    # Regular expression patterns for extracting components from the log line
    log_pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(*log_pattern)
    match = re.fullmatch(log_format, input_line)
    if match:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, status_codes_stats):
    """Prints accumulated statistics.

    Args:
        total_file_size (int): The total file
         size accumulated so far.
        status_codes_stats (dict): A dictionary
        containing counts of different status codes.
    """
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which
        to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): A dictionary containing
         counts of different status codes.

    Returns:
        int: The new total file size after updating metrics.
    """
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    """Start parser."""
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
