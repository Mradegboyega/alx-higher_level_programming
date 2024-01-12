#!/usr/bin/python3
"""
Square module
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class, inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class

        Args:
            size (int): Size of the square.
            x (int): X coordinate of the square (default is 0).
            y (int): Y coordinate of the square (default is 0).
            id (int): ID of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.

        Returns:
            dict: Dictionary representation of the Square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

