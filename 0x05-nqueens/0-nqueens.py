#!/usr/bin/python3
"""
N queens
"""

import sys


def is_safe(b, r, c):
    """
    Checks if it's safe to place a queen at board[row][col].
    """
    # Check the row on the left side
    for i in range(c):
        if b[i] == r or b[i] == r - c + i or b[i] == r + c - i:
            return False
    return True


def solve_nqueens_util(n, col, board, result):
    """
    Utility function to solve N Queens problem recursively.
    """
    if col == n:
        result.append(board[:])
        return
    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            solve_nqueens_util(n, col + 1, board, result)


def solve_nqueens(n):
    """
    Solves the N Queens problem for a given board size.
    """
    result = []
    solve_nqueens_util(n, 0, [0] * n, result)
    for board in result:
        print([[i, board[i]] for i in range(n)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    solve_nqueens(N)
