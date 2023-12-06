#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Create a new set to store common elements
    common_set = set()

    # Iterate through each element in the first set
    for element in set_1:
        # If the element is also present in the second set, add it to the common set
        if element in set_2:
            common_set.add(element)

    return common_set
