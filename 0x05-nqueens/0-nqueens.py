#!/usr/bin/python3
"""
Solves the N Queens problem.
"""

import sys


def print_board(board):
    """
    Prints the board.
    """
    for row in board:
        print(row)


def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at board[row][col].
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col):
    """
    Utility function to solve N Queens problem recursively.
    """
    n = len(board)
    # If all queens are placed, print the solution
    if col >= n:
        print_board(board)
        print()
        return True

    # Initialize result
    res = False

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        # Check if the queen can be placed on board[i][col]
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Make the next column safe recursively
            res = solve_nqueens_util(board, col + 1) or res

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0

    # If the queen can't be placed in any row in this column, then return False
    return res


def solve_nqueens(n):
    """
    Solves the N Queens problem for a given board size.
    """
    # Create an empty board
    board = [[0] * n for _ in range(n)]

    # Start from the first column
    if not solve_nqueens_util(board, 0):
        print("No solution exists")


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
