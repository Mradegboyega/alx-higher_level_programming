#!/usr/bin/python3
"""
This module provides a function to generate Pascal's triangle.

Author: Your Name
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle of n.

    Args:
    n (int): Number of rows to generate in Pascal's triangle.

    Returns:
    list: List of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            row.extend([prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)])
            row.append(1)
        triangle.append(row)

    return triangle
