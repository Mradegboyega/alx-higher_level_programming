#!/usr/bin/python3
"""
Module Name: 2-matrix_divided
Description: This module provides a function for dividing all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Function Name: matrix_divided
    Description: Divides all elements of a matrix.

    Parameters:
    - matrix: A list of lists of integers or floats.
    - div: A number (integer or float) that is not equal to 0.

    Returns:
    A new matrix where all elements are divided by div and rounded to 2 decimal places.
    
    Raises:
    - TypeError: If matrix is not a list of lists of integers or floats,
                or if each row of the matrix does not have the same size,
                or if div is not a number.
    - ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    
    return new_matrix
