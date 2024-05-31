#!/usr/bin/env python3
"""
This script solves the N Queens puzzle.
Usage: nqueens N
"""

import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed on board[row][col].
    This function is called when "col" queens are already placed
    in columns from 0 to col - 1. So we need to check only left
    side for attacking queens.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col):
    """
    Solve the N Queens problem using backtracking
    """
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        return [solution]

    solutions = []
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            for sol in solve_nqueens(board, col + 1):
                solutions.append(sol)
            board[i][col] = 0
    return solutions


def print_solutions(solutions):
    """
    Print all the solutions
    """
    for solution in solutions:
        print(solution)


def main():
    """
    Main entry point for the script.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = solve_nqueens(board, 0)
    print_solutions(solutions)
