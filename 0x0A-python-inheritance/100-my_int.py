#!/usr/bin/python3

class MyInt(int):
    """
    A class representing an integer with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverted equality operator (==).

        Args:
        - other: The value to compare against.

        Returns:
        - True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted inequality operator (!=).

        Args:
        - other: The value to compare against.

        Returns:
        - True if equal, False if not equal.
        """
        return super().__eq__(other)

