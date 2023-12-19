#!/usr/bin/python3
"""This module defines a class Square with a private attribute size."""


class Square:
    """This class represents a square."""

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Note:
            This method does not perform type or value verification.
        """
        self.__size = size
