#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to row n.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle up to row n.
              Each inner list represents a row of the triangle, with the
              elements representing the values in that row.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
