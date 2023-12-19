#!/usr/bin/python3
"""This module defines a class Square with size validation and area calculation."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class with optional size.

        Args:
            size (number): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            number: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (number): The size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            number: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Equality comparison based on square areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison based on square areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater-than comparison based on square areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater-than-or-equal comparison based on square areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less-than comparison based on square areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Less-than-or-equal comparison based on square areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if area is less or equal, False otherwise.
        """
        return self.area() <= other.area()
