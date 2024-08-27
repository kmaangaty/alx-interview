#!/usr/bin/python3
"""
0-island_perimeter.py
"""


def island_perimeter(grid):
    """
    Function to calculate the perimeter of the island described in the grid.

    Args:
    - grid (list of int): The 2D grid of 0s and 1s representing the island.

    Returns:
    - int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four possible directions
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
