#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            value = my_list[i]
            if type(value) is int:
                print("{:d}".format(value), end="")
                count += 1
    except (IndexError, ValueError, TypeError):
        pass  # Handle exceptions and continue silently

    print()  # Print a new line after the integers
    return count
