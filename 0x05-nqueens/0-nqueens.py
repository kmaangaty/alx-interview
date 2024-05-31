#!/usr/bin/python3
"""
Solves the N Queens problem.
"""

import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    # Convert the argument to an integer
    board_size = int(sys.argv[1])
except ValueError:
    # Handle the case where the argument is not an integer
    print('N must be a number')
    exit(1)

# Check if the board size is valid
if board_size < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(board_size):
    """
    Solves the N Queens problem using recursion and backtracking.
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
    """
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or \
        abs(row1 - row2) == abs(col1 - col2)


def is_safe(square, queens):
    """
    Checks if placing a queen at a square is safe.
    """
    for queen in queens:
        if is_attacked(square, queen):
            return False
    return True


# Reverse the solutions for printing them in the correct order
for solution in reversed(solve_nqueens(board_size)):
    formatted_solution = []
    for position in [list(pos) for pos in solution]:
        formatted_solution.append([i - 1 for i in position])
    print(formatted_solution)
