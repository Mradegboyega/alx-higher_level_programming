#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass  # Handle the case when the index is out of bounds

    print()  # Print a new line after the elements
    return count
