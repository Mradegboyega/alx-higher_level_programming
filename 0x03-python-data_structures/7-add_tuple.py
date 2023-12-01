#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuples have at least 2 elements by padding with zeros if necessary
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Add corresponding elements of the two tuples
    result_tuple = (a[0] + b[0], a[1] + b[1])
    return result_tuple
