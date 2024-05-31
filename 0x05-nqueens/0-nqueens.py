#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placin
g N non-attacking queens on an N×N chessboard.
"""

import sys


def is_safe(b, r, c):
    """
    Checks if it's safe to place a queen at board[row][col].

    Args:
        b (list): List representing the current board state.
        r (int): Row index to place the queen.
        c (int): Column index to place the queen.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    # Check the row on the left side
    for i in range(c):
        if b[i] == r or b[i] == r - c + i or b[i] == r + c - i:
            return False
    return True


def solve_nqueens_util(board_size, column, current_board, result):
    """
    Utility function to solve N Queens problem recursively.

    Args:
        board_size (int): Size of the board.
        column (int): Current column index.
        current_board (list): List representing the current board state.
        result (list): List to store the solutions.
    """
    if column == board_size:
        result.append(current_board[:])
        return
    for row in range(board_size):
        if is_safe(current_board, row, column):
            current_board[column] = row
            solve_nqueens_util(board_size, column + 1, current_board, result)


def solve_nqueens(board_size):
    """
    Solves the N Queens problem for a given board size.

    Args:
        board_size (int): Size of the board.
    """
    result = []
    solve_nqueens_util(board_size, 0, [0] * board_size, result)
    for board in result:
        print([[i, board[i]] for i in range(board_size)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if board_size < 4:
        print('N must be at least 4')
        sys.exit(1)

    solve_nqueens(board_size)
