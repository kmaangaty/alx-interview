#!/usr/bin/python3
"""
Solves the N Queens problem.
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    board_size = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if board_size < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(board_size):
    """
    Solves the N Queens problem recursively.

    Args:
        board_size (int): The size of the chessboard.

    Returns:
        list: List of solutions, where each solution is a list of queen positions.
    """
    if board_size == 0:
        return [[]]

    inner_solutions = solve_nqueens(board_size - 1)
    return [solution + [(board_size, col + 1)]
            for col in range(board_size)
            for solution in inner_solutions
            if is_safe((board_size, col + 1), solution)]


def is_attacked(square, queen):
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
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def is_safe(square, queens):
    """
    Checks if placing a queen at a square is safe.

    Args:
        square (tuple): Position of the new queen.
        queens (list): List of existing queen positions.

    Returns:
        bool: True if the square is safe, False otherwise.
    """
    for queen in queens:
        if is_attacked(square, queen):
            return False
    return True


for solution in reversed(solve_nqueens(board_size)):
    formatted_solution = []
    for position in [list(pos) for pos in solution]:
        formatted_solution.append([i - 1 for i in position])
    print(formatted_solution)
