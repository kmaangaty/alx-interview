#!/usr/bin/python3
"""
Solves the N Queens problem.
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(size):
    """
    Solves the N Queens problem recursively.

    Args:
        board_size (int): The size of the chessboard.

    Returns:
        list: List of solutions,
         where each solution is a list of queen positions.
    """
    if size == 0:
        return [[]]
    inner_solution = solve_nqueens(size - 1)
    return [solution + [(size, col + 1)]
            for col in range(n)
            for solution in inner_solution
            if is_safe((size, col + 1), solution)]


def attack_queen(square, queen):
    """
    Checks if two queens attack each other.

    Args:
        square (tuple): Position of the new queen.
        queen (tuple): Position of an existing queen.

    Returns:
        bool: True if the queens attack each other, False otherwise.
    """
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or \
        abs(row1 - row2) == abs(col1 - col2)


def is_safe(sqr, qns):
    """
    Checks if placing a queen at a square is safe.

    Args:
        square (tuple): Position of the new queen.
        queens (list): List of existing queen positions.

    Returns:
        bool: True if the square is safe, False otherwise.
    """
    for q in qns:
        if attack_queen(sqr, q):
            return False
    return True


for answer in reversed(solve_nqueens(n)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
