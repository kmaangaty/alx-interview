#!/usr/bin/python3
"""
This script solves the N-Queens problem for a given board size N.
"""

import sys


def solve_nqueens(board_size):
    """
    solve the N-Queens problem for a given board size.
    Parameters:
        board_size (int): The size of the chessboard (N).
    Returns:
        List[List[int]]: A list of solutions, where each solution is a list.
    """

    def is_safe(col, queens_positions):
        """
        check if a position is safe for placing a queen.
        Parameters:
            col (int): The column position to check.
            queens_positions (List[int]): list of column positions of queens.

        Returns:
            bool: True if the position is safe, False otherwise.
        """
        row = len(queens_positions)
        for r in range(row):
            if (
                queens_positions[r] == col or
                queens_positions[r] - r == col - row or
                queens_positions[r] + r == col + row
            ):
                return False
        return True

    def place_queens(n, row, queens_positions, solutions):
        """
        recursively attempts to place queens on the board.
        Parameters:
            n (int): The size of the chessboard (N).
            row (int): The current row index where a queen is to be placed.
            queens_positions (List[int]): list of column positions of queens.
            solutions (List[List[int]]): The list to store valid solutions.
        """
        if row == n:
            solutions.append(queens_positions[:])
            return

        for col in range(n):
            if is_safe(col, queens_positions):
                queens_positions.append(col)
                place_queens(n, row + 1, queens_positions, solutions)
                queens_positions.pop()

    solutions = []
    place_queens(board_size, 0, [], solutions)
    return solutions


def main():
    """
    main function to handle user input and solve the N-Queens problem.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(board_size)
    for solution in solutions:
        print([[row, solution[row]] for row in range(len(solution))])


if __name__ == "__main__":
    main()
