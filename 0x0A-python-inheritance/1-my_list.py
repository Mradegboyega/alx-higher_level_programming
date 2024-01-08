#!/usr/bin/python3

class MyList(list):
    """
    A class that inherits from list and includes additional methods.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
