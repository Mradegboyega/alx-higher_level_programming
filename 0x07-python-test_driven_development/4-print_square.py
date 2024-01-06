#!/usr/bin/python3
"""
Module Name: 4-print_square
Description: This module provides a function for printing a square with the character #.
"""

def print_square(size):
    """
    Function Name: print_square
    Description: Prints a square with the character #.

    Parameters:
    - size: The size length of the square.

    Raises:
    - TypeError: If size is not an integer or if size is a float and is less than 0.
    - ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
