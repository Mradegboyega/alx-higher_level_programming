#!/usr/bin/python3
"""
Module Name: 0-add_integer
Description: This module provides a function for adding two integers.
"""

def add_integer(a, b=98):
    """
    Function Name: add_integer
    Description: Adds two integers.

    Parameters:
    - a: The first integer or float.
    - b: The second integer or float (default is 98 if not provided).

    Returns:
    An integer: the addition of a and b.
    
    Raises:
    - TypeError: If both a and b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    # Casting to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
